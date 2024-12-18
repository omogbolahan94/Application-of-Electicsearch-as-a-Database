import json
from create_index_1 import es

dummy_data = json.load(open("data/dummy_data.json"))
# print the data
# print(dummy_data)


def insert_document(document):
    response = es.index(index='my_index', body=document)
    return response


def print_info(response):
    print(f"""Document ID: {response['_id']} is '{
          response["result"]}' and is split into {response['_shards']['total']} shards.""")


for document in dummy_data:
    response = insert_document(document)
    print_info(response)

# print the mapping of the data inserred into my_index to see their data types:
# index_mapping = es.indices.get_mapping(index='my_index')
# pprint(index_mapping["my_index"]["mappings"]["properties"])

# to add a mapping, it must be done before the data is inserted
# es.indices.delete(index='my_index', ignore_unavailable=True)
# es.indices.create(index='my_index')

# mapping = {
#     'properties': {
#         'created_on': {'type': 'date'},
#         'text': {
#             'type': 'text',
#             'fields': {
#                 'keyword': {
#                     'type': 'keyword',
#                     'ignore_above': 256
#                 }
#             }
#         },
#         'title': {
#             'type': 'text',
#             'fields': {
#                 'keyword': {
#                     'type': 'keyword',
#                     'ignore_above': 256
#                 }
#             }
#         }
#     }
# }

# es.indices.put_mapping(index='my_index', body=mapping)