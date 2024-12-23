import json
from a_create_index import es


es.indices.delete(index='my_index', ignore_unavailable=True)
es.indices.create(index='my_index')


dummy_data = json.load(open("data/dummy_data_2.json"))
# duplicate the document so that we have more then 3 documents
for _ in range(10):
    dummy_data += dummy_data

print(len(dummy_data))

# list of source and action
operations = []
for document in dummy_data:
    # append source
    operations.append({'index': {'_index': 'my_index'}})
    # append the above source action
    operations.append(document)

es.bulk(operations=operations)

################### Search - size + from ###############################
# search that retrieves 10 documents, starting from the 11th document
# This demonstrates pagination using the size and from parameters.
response = es.search(
    index="my_index",
    body={
        "query": {
            "match_all": {}
        },
        "size": 10,
        "from": 10
    },
)

for hit in response['hits']['hits']:
    print(hit['_source'])

################# Timeout ##################
# If the query takes longer than the specified timeout (10s), it will be aborted.
response = es.search(
    index="my_index",
    body={
        "query": {
            "match": {
                "message": "search keyword"
            }
        },
        "timeout": "10s"
    },
)

print('\n', response.body)

################# Aggregate #################
# calculate the average value of the age field across all documents that match the query. 
# The result of the aggregation is stored in the avg_age key.
response = es.search(
    index="my_index",
    body={
        "query": {
            "match_all": {}
        },
        "aggs": {
            "avg_age": {
                "avg": {
                    "field": "age"
                }
            }
        }
    }
)

average_age = response['aggregations']['avg_age']['value']
print(f"\nAverage Age: {average_age}")


############### combining them together #####################
response = es.search(
    index="my_index",
    body={
        "query": {
            "match": {
                "message": "important keyword"
            }
        },
        "aggs": {
            "max_price": {
                "max": {
                    "field": "price"
                }
            }
        },
        "size": 5,
        "from": 20,
        "timeout": "5s"
    },
)

# for hit in response['hits']['hits']:
#     print(hit['_source'])

max_price = response['aggregations']['max_price']['value']
print(f"Max Price: {max_price}")

