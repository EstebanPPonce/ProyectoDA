import requests
import pandas as pd
from bs4 import BeautifulSoup
pd.set_option('display.max_columns', 8)
pd.set_option('display.max_rows', 80) 

def ams(dataArr):
    id = 0
    datar = {}
    for atm in dataArr: 
        id += 1

        if 'FichaInmueble_dormitorios' not in dataArr:
            datar['dorm'] = 'sin datos'
        if 'FichaInmueble_bano' not in dataArr:
            datar['ban'] = 'sin datos'
        if 'FichaInmueble_superficie' not in dataArr:
            datar['sup'] = 'sin datos'
      
        if atm == 'FichaInmueble_dormitorios':
            datar['dorm'] = dataArr[id] 
        if atm == 'FichaInmueble_bano':
            datar['ban'] = dataArr[id]
        if atm == 'FichaInmueble_superficie':
            datar['sup'] = dataArr[id]
        
    return datar

links ='https://clasificados.lavoz.com.ar/inmuebles/departamentos?list=true&provincia=cordoba&ciudad=cordoba&apto-credito=no&operacion=venta&precio-desde=10000&moneda=dolares&tipo-de-unidad=departamento&page='
data_list = []
for link in range(1,3):


    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0','encode': 'utf-8'}

    url = links +  str(link)

    r = requests.get(url, headers=headers)

    soup = BeautifulSoup(r.text, 'html.parser')

    publicaciones = soup.find_all('div', {'class': 'flex col col-12 my2'})

    
    data_item = {}
    
    for item in publicaciones:
        
      #  titulo   = item.find('div', {'class': 'bold mx0 mt0 pt1 col-12 title-2lines-list h2'}).text
      
        precio   = item.find('span', {'class': 'price'}).text
        link     = item.find('a', {'class': 'text-decoration-none'})['href']
        dataDpto = item.find('div', {'class': 'items-center'}).text.split(" ")
        
        try:
            ubicacion = item.find('span', {'class': 'h4'}).text
        except:
            ubicacion = 'sin ubicacion'
        extradata = ams(dataDpto)
      #  data_item['titulo'] = titulo.encode('utf8').strip()[:15]
        data_item['precio'] = precio.strip()
        data_item['ubicacion'] = ubicacion
        if 'dorm' in extradata : data_item['dorm']  = extradata['dorm'] 
        if 'ban' in extradata : data_item['ban']   = extradata['ban'] 
        if 'sup' in extradata : data_item['sup']   = extradata['sup']
        #
        item = pd.DataFrame([data_item])

        data_list.append(item)


    df_final = pd.concat(data_list)

print(df_final)