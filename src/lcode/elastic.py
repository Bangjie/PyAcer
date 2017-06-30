from elasticsearch import Elasticsearch
import csv



def pagetodata(page,nrows,need_field):
    data = []

    
 
    
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
    destip = '10.17.24.64'
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
    needrows=100000
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
    writer.writerow(need_field_head)
    data=pagetodata(page, nrows,need_field)
    writer.writerows(data)
    
    
    
    transed = 100
    while(scroll_size >0 and transed < needrows):
        print "Scrolling..."
        page = es.scroll(scroll_id = sid, scroll ='2m')
        
        data=pagetodata(page, nrows,need_field)
        print "start to write csv..."
        writer.writerows(data)
        print "write over. "
        # Update the scroll ID
        sid = page['_scroll_id']
        # Get the number of results that we returned in the last scroll
        scroll_size = len(page['hits']['hits'])
        print "scroll size: "+ str(scroll_size)
        
        transed = transed + scroll_size
        print "transed size: "+ str(transed)
        
        
#print s['hits']['hits'][0]['_source']['long_fundid'],s['hits']['hits'][0]['_source']['long_days']
