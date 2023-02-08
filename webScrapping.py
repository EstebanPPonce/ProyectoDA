import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0'}

url = 'https://clasificados.lavoz.com.ar/inmuebles/departamentos?list=true&provincia=cordoba&ciudad=cordoba&apto-credito=no&operacion=venta&precio-desde=10000&moneda=dolares&tipo-de-unidad=departamento'

r = requests.get(url, headers=headers)

soup = BeautifulSoup(r.text, 'html.parser')

publicaciones = soup.find_all('div', {'class': 'flex col col-12 my2'})

publicacionIndividual = soup.find('div', {'class': 'flex col col-12 my2'})


spanTag1dormitorios = publicacionIndividual.find('span', {'class': 'pr1'}).next_sibling.strip()
spanTag2banos = publicacionIndividual.find('span', {'class': 'px1'}).next_sibling.strip()

spans2y3 = publicacionIndividual.find_all('span', {'class': 'px1'}, limit=2)




#print('dormitorios:',spanTag1dormitorios)
#print('banos:',spanTag2banos)


#for item in publicaciones:
#	titulo = item.find('div', {'class': 'bold mx0 mt0 pt1 col-12 title-2lines-list h2'}).text
#	precio = int(item.find('span', {'class': 'price'}).text)
#	link = item.find('a', {'class': 'text-decoration-none'})['href']
#	print(link)
#	try:
#		ubicacion = item.find('span', {'class': 'h4'}).text
#	except:
#		ubicacion = 'sin ubicacion'
	