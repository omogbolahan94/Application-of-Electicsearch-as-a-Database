# from pprint import pprint
from elasticsearch import Elasticsearch

# ensure the elasticsearch container is running the image before tryin to connect to it:
es = Elasticsearch('http://localhost:9200')
client_info = es.info()
# print('Connected to Elasticsearch!')
# print(client_info.body)

# create an index and configure it with number of shards and replicas: my_index
es.indices.create(
    index="my_index",
    settings={
        "index": {
            "number_of_shards": 3,  # how many pieces the data is split into
            "number_of_replicas": 2  # how many copies of the data
        }
    },
)