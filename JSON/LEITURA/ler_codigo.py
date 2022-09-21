import urllib.request, json 
with open("arquivo.txt") as file:
	for linha in file:
		print(f'https://proxyapp.correios.com.br/v1/sro-rastro/{linha}')
		
		with urllib.request.urlopen(f'https://proxyapp.correios.com.br/v1/sro-rastro/{linha}') as url:
			data = json.loads(url.read().decode())
			formatado = json.dumps(data, indent=4)
			#print(data)
			print(formatado)

