import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0'}

linksPublicaciones = []

#for x in range(1,3):
#	r = requests.get(f'https://clasificados.lavoz.com.ar/inmuebles/departamentos?list=true&provincia=cordoba&ciudad=cordoba&apto-credito=no&operacion=venta&precio-desde=10000&moneda=dolares&tipo-de-unidad=departamento&page={x}', headers=headers)
#	soup = BeautifulSoup(r.text, 'html.parser')
#
#	listaPublicaciones = soup.find_all('div', {'class': 'flex col col-12 my2'})


#	for item in listaPublicaciones:
#		titulo = item.find('div', {'class': 'bold mx0 mt0 pt1 col-12 title-2lines-list h2'}).text
#		link = item.find('a', {'class': 'text-decoration-none'})['href']
#		linksPublicaciones.append(link)


testlink = 'https://clasificados.lavoz.com.ar/avisos/departamentos/4321702/milenica-univ-2-dorm-2-banos-cochera-cubierta-balcon-oportunidad'

r = requests.get(testlink, headers=headers)
soup = BeautifulSoup(r.text, 'html.parser')

#nombre = soup.find('h1', {'class': 'h2 m0 mb0 bold line-height-1'}).text
#precio = soup.find('div', {'class': 'h2 mt0 main bolder'}).text.strip()

#superficie = soup.find_all('div', {'class': 'inline-flex align-baseline2 col-10'})

listaFeatures = soup.find_all('div',{'class': 'inline-flex align-baseline2 col-10'})



for i in listaFeatures:
	print(i.text.strip())


asd = 2


