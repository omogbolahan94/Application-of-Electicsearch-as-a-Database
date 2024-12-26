from a_create_index import es
from b_insert_doc import document_ids

# confirm if an index exists: my_index
# output i boolean: True or False
response = es.indices.exists(index='my_index')
print(response.body)

# check if a documents at index 0 of document_ids exists
# output i boolean: True or False
response = es.exists(index='my_index', id=document_ids[0])
print(response.body)