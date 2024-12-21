from a_create_index import es
from b_insert_doc import document_ids

# delete the document with the id at index 0 of the documents_ids variable
# trying to delete an document with an id that does not exists will throw out an error
response = es.delete(index='my_index', id=document_ids[0])

print(response.body)