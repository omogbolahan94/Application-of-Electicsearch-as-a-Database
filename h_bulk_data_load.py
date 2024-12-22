from a_create_index import es


# we can insert document individually but it is not efficient because in every insert, we will be making a new API call
# Bulk operation helps us to load the documents in bulk in a single API call.
# it only require an operation key (list of action and source dictionary for each document)
# action: specify index name and the unique id of the document
# source: the document to insert

es.indices.delete(index='my_index', ignore_unavailable=True)
es.indices.create(index='my_index')

response = es.bulk(
    operations=[
        # Action 1: add a document to the index "my_index" with id equal to 1
        {
            "index": {
                "_index": "my_index",
                "_id": "1"
            }
        },
        # Source 1
        {
            "title": "Sample Title 1",
            "text": "This is the first sample document text.",
            "created_on": "2024-09-22"
        },
        # Action 2
        {
            "index": {
                "_index": "my_index",
                "_id": "2"
            }
        },
        # Source 2
        {
            "title": "Sample Title 2",
            "text": "Here is another example of a document.",
            "created_on": "2024-09-24"
        },
        # Action 3
        {
            "index": {
                "_index": "my_index",
                "_id": "3"
            }
        },
        # Source 3
        {
            "title": "Sample Title 3",
            "text": "The content of the third document goes here.",
            "created_on": "2024-09-24"
        },
        # Action 4: update the title field of document with id=1 in the my_index index 
        {
            "update": {
                "_id": "1",
                "_index": "my_index"
            }
        },
        # Source 4
        {
            "doc": {
                "title": "New Title"
            }
        },
        # Action 5
        {
            "update": {
                "_id": "2",
                "_index": "my_index"
            }
        },
        # Source 5
        {
            "doc": {
                "new_field": "dummy_value"
            }
        },
        # Action 6: delete does not require source. It will delete the document with id 3 in my_index
        {
            "delete": {
                "_index": "my_index",
                "_id": "3"
            }
        },
    ],
)

print(response.body)
