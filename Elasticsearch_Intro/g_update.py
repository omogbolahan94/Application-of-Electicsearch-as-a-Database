from a_create_index import es
from b_insert_doc import document_ids

# the title of the first document
#
response = es.update(
    index="my_index",
    id=document_ids[0],
    script={
        "source": "ctx._source.title = params.title", # change the title attribute of the context source
        "params": {
            "title": "New Title"
        }
    },
)
print(response.body)

# if a field does not exists, it will update it
response = es.update(
    index="my_index",
    id=document_ids[0],
    script={
        "source": "ctx._source.new_field = 'dummy_value'",
    },
)
print(response.body)

# remove a field
response = es.update(
    index="my_index",
    id=document_ids[0],
    script={
        "source": "ctx._source.remove('new_field')",
    },
)
print(response.body)

# if document does not exists, use the upseart to tell elasticsearch to insert it as a new document
response = es.update(
    index="my_index",
    id="1",
    doc={
        "book_id": 1234,
        "book_name": "A book",
    },
    doc_as_upsert=True,
)
print(response.body)