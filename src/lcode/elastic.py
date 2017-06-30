from elasticsearch import Elasticsearch
import csv



def pagetodata(page,nrows,need_field):
    data = []

    
 
    
    for i in range(nrows):
        tuple_field=()
        for k,v in enumerate(need_field):
            
            tuple_field =tuple_field + (page['hits']['hits'][i]['_source'].get(v,'Null'),)
        
        
#         data.append((page['hits']['hits'][i]['_source']['long_fundid'],
#                      page['hits']['hits'][i]['_source']['double_gainaby'],
#                      page['hits']['hits'][i]['_source']['double_riskaby'],
#                      
#                      ))
        data.append(tuple_field)

    return data


if __name__ == "__main__":
    csvfile = file('custview.csv','wb')
    
    need_field=['long_fundid','double_gainaby','double_riskaby','long_hitcount']
    
    es = Elasticsearch([{'host':'10.237.2.69','port':9200}])
    
    nrows=100
    needrows=100000
    #s=es.search(index='cust_my_review', doc_type="cust_mapping",body=allbody,params=para)
    page=es.search(index='cust_my_review', 
                doc_type="cust_mapping",
                scroll = '2m',
                size=nrows,
                filter_path=['hits.total','_scroll_id','hits.hits._source'])
    
    sid = page['_scroll_id']
    scroll_size = page['hits']['total']
    
    #print page['hits']['hits'][0]['_source']['long_fundid'],page['hits']['hits'][0]['_source']['long_days']
    
    writer = csv.writer(csvfile)
    writer.writerow(need_field)
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
        
        print 
#print s['hits']['hits'][0]['_source']['long_fundid'],s['hits']['hits'][0]['_source']['long_days']
