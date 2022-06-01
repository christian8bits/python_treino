import json 
with open('JN644074710BR.json', 'r') as openfile: 
	json_object = json.load(openfile) 
  
formatado = json.dumps(json_object, indent=4)
#print(data)



print(json_object) 
print(type(json_object)) 
print('')
print(formatado)
