import urllib.request, json 
with urllib.request.urlopen("https://proxyapp.correios.com.br/v1/sro-rastro/JN644074710BR") as url:
    data = json.loads(url.read().decode())
    formatado = json.dumps(data, indent=4)
    #print(data)
    print(formatado)

