from elasticsearch import Elasticsearch
import csv
import time

def pagetodata(page,nrows,need_field):
    data = []
    
    #print "page.len:",len(page['hits']['hits'])
    for i in range(nrows):
        tuple_field=()
        for k,v in enumerate(need_field):
            #deperacated!!if  use this one ,please  commnet writer.writerow(need_field) or add field manully in csvfile!!
            if v in ('str_transfercount','str_trdcount'):              
                cont = page['hits']['hits'][i]['_source'].get(v,'0')
                if cont != '0':
                    cont_v = cont.split('|')
                    tuple_field =tuple_field + (cont_v[0],cont_v[1],)
                else:
                    tuple_field =tuple_field + (0,0,)
            else:
                tuple_field =tuple_field + (page['hits']['hits'][i]['_source'].get(v,'0'),)
                
#         data.append((page['hits']['hits'][i]['_source']['long_fundid'],
#                      page['hits']['hits'][i]['_source']['double_gainaby'],
#                      page['hits']['hits'][i]['_source']['double_riskaby'],
#                      
#                      ))
        data.append(tuple_field)

    return data


if __name__ == "__main__":
    start =time.clock()
    destip = '10.237.2.69'
    index = 'my_review'
    mapping = 'cust_mapping'
    
    csvfile = file('custview.csv','wb')
    
    need_field=['long_fundid','double_totpa','long_applycount','long_busicount','long_firfollow',
                'long_hitcount','long_logoncount','long_stockcount',
                'str_transfercount','str_trdcount']
    need_field_head=['fundid','totpa','applycount','busicount','firfollow',
                'hitcount','logoncount','stockcount',
                'transfercount','transferamount','trdcount','trdamount']
    
    es = Elasticsearch([{'host':destip,'port':9200}])
    
    nrows=100
   
    #s=es.search(index='cust_my_review', doc_type="cust_mapping",body=allbody,params=para)
    page=es.search(index=index, 
                doc_type=mapping,
                scroll = '2m',
                size=nrows,
                filter_path=['hits.total','_scroll_id','hits.hits._source'])
    
    sid = page['_scroll_id']
    scroll_size = page['hits']['total']
    
    #print page['hits']['hits'][0]['_source']['long_fundid'],page['hits']['hits'][0]['_source']['long_days']
    
    writer = csv.writer(csvfile)
    writer.writerow(need_field_head)                       ##write head

    transed = 0
    needrows=199   
    while(scroll_size >0 and transed < needrows):
        print "Scrolling..."
        page = es.scroll(scroll_id = sid, scroll ='2m')
        
        scroll_size = len(page['hits']['hits'])
        print "scroll size: "+ str(scroll_size)
        
        transrow = (needrows-transed) if needrows-transed < scroll_size else scroll_size

        data=pagetodata(page, transrow,need_field)
            
        print "start to write csv..."
        writer.writerows(data)
        print "write over. "
        # Update the scroll ID
        sid = page['_scroll_id']
        # Get the number of results that we returned in the last scroll

        
        transed = transed + transrow
        print "transed size: "+ str(transed)
        
     
    print "GetDataElapsedTime:%f s"%(time.clock()-start)   
#print s['hits']['hits'][0]['_source']['long_fundid'],s['hits']['hits'][0]['_source']['long_days']
