target = "test"
queries = [ {'target': "yeet"}, {'target':"test"}, {'target':"bruh"} ]
new_queries = filter(lambda query: query['target'] != target, queries)

print(list(new_queries))