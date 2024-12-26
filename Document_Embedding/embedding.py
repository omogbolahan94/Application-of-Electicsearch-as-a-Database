# hugging face package for its LLM models
import sys
import os
import json
from sentence_transformers import SentenceTransformer

# Add the parent directory to sys.path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)


from Elasticsearch_Intro import a_create_index 


# embedding is the transformation of text into numerical vector.
#  all-MiniLM-L6-v2 model fhas speed, compact size, and versatility as a general-purpose model. More information on huggingface
# model = SentenceTransformer('all-MiniLM-L6-v2')

# es.indices.delete(index='my_index', ignore_unavailable=True)
# es.indices.create(
#     index="my_index",
#     mappings={
#         "properties": {
#             "embedding": {
#                 "type": "dense_vector",
#             }
#         }
#     },
# )

# # load the documents
# documents = json.load(open("../data/dummy_data.json"))

# def get_embedding(text):
#     return model.encode(text)


# operations = []
# for document in tqdm(documents, total=len(documents)):
#     operations.append({'index': {'_index': 'my_index'}})
#     operations.append({
#         **document,
#         'embedding': get_embedding(document['text']),
#     })

# response = es.bulk(operations=operations)
# print(response.body)