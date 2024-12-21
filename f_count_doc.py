from a_create_index import es
from b_insert_doc import document_ids

# count the number of document in an index
response = es.count(index='my_index')
print(response.body)

# using an optional query parameter to count the number of document that matches the query argument
# for instance: find document whose created_on columns is less than and greater a specific date
query = {
    "range": {
        "created_on": {
            "gte": "2024-09-24", # greater than
            "lte": "2024-09-24", # less than
            "format": "yyyy-MM-dd"
        }
    }
}

response = es.count(index='my_index', query=query)
count = response["count"]
