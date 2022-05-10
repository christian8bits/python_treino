import json

python_obj = {
  "nome": "David",
  "class": "A",
  "idade": 10
}
print(type(python_obj))
j_data = json.dumps(python_obj)

print(j_data)
