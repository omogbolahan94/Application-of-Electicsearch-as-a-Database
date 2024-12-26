from a_create_index import es
from b_insert_doc import document_ids


############################### Simple Search ################################
# find all in a single index: code below finds documents that matches the query: "match_all": {} means all documents
# for multiple indices, seperate them with comma or 
# use wildcards e.g 'index*' for index that starts with index or 
# use '_all'
response = es.search(
    index='my_index', # multile: index1, index2; 
    body={
        "query": {"match_all": {}}
    }
)

n_hits = response['hits']['total']['value']
print(f"Found {n_hits} documents in my_index")



############################# Using Query DSL ########################
# Leaf search (term search): value that matches the exact search
response = es.search(
    index='my_index',
    body={
        "query": {
            "term": {
                "created_on": "2024-09-22"
            }
        }
    }
)

n_hits = response['hits']['total']['value']
print(f"\nFound {n_hits} documents in my_index")

# Leaf search (match): search any document that contains the word 'document' in its text field with text data type
response = es.search(
    index='my_index',
    body={
        "query": {
            "match": {
                "text": "document"
            }
        }
    }
)

n_hits = response['hits']['total']['value']
print(f"\nFound {n_hits} documents in my_index")

# Leaf search (range): find the documents with date less than "2024-09-23"
response = es.search(
    index='my_index',
    body={
        "query": {
            "range": {
                "created_on": {
                    "lte": "2024-09-23"
                }
            }
        }
    }
)

n_hits = response['hits']['total']['value']
print(f"\nFound {n_hits} documents in my_index")


# Copound search: documents that was Created on 2024-09-24 and have the word "third" in the text field.
# using multiple leaf query as list of values in the must key
response = es.search(
    index='my_index',
    body={
        "query": {
            "bool": {
                "must": [
                    {
                        "match": {
                            "text": "third"
                        }
                    },
                    {
                        "range": {
                            "created_on": {
                                "gte": "2024-09-24",
                                "lte": "2024-09-24"
                            }
                        }
                    }
                ]
            }
        }
    }
)


n_hits = response['hits']['total']['value']
print(f"\nFound {n_hits} documents in my_index")