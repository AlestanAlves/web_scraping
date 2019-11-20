import urllib.request 

content = urllib.request.urlopen("https://www.melhorcambio.com/dolar-hoje")
content = str(content)
find = '<input type= "hidden" valeu="'
posicao = int(content.index(find) + len(find))
dolar = content [posicao : posicao + 4]
print(dolar)