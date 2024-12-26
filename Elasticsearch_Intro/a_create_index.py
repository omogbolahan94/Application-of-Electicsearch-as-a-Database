# from pprint import pprint
from elasticsearch import Elasticsearch

# ensure the elasticsearch container is running the image before tryin to connect to it:
es = Elasticsearch('http://localhost:9200')
client_info = es.info()
# print('Connected to Elasticsearch!')
# print(client_info.body)


if __name__ == "__main__":
    # create an index and configure it with number of shards and replicas: my_index
    # for the sake of practicing and to avoid creating multiple index,
    # we will delete an exisiting index before creating a new one
    es.indices.delete(index='my_index', ignore_unavailable=True)
    es.indices.create(
        index="my_index",
        settings={
            "index": {
                "number_of_shards": 3,  # how many pieces the data is split into
                "number_of_replicas": 2  # how many copies of the data
            }
        },
    )
    