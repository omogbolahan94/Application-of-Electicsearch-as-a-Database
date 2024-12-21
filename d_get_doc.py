from a_create_index import es
from b_insert_doc import document_ids

# get document at index 0
# trying to get a document with an id that does not exists will throw out an error
response = es.get(index='my_index', id=document_ids[0])

print(response.body)