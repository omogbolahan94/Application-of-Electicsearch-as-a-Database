# stored dense vector of numeric type
# only application when there is few or no zero element
# does not support aggregation or sorting
# cannot store multiple values in one dense vector field
# use KNN to retrieve the nearest vector
# max size of a dense vector is 4096
# there is need to manually do the mapping unlike the other data type
from a_create_index import es


es.indices.delete(index='my_index', ignore_unavailable=True)
es.indices.create(
    index="my_index",
    mappings={
        "properties": {
            "sides_length": {
                "type": "dense_vector",
                "dims": 4  # length of the vector
            },
            "shape": {
                "type": "keyword"
            }
        }
    },
)

response = es.index(
    index='my_index',
    id=1,
    document={
        "shape": "square",
        "sides_length": [5, 5, 5, 5],
    }
)

print(response.body)