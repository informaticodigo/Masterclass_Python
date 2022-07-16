import urllib.request as request
from urllib.request import urlopen
import re
from bs4 import BeautifulSoup
import warnings
warnings.filterwarnings("ignore")

# Todo va entre excepciones por si falla algo, dado que al
# analizar el html, no solo depende de nuestro código
try:
    # Se solicita una url al usuario
    pagina = input('Inserta la url de la página que quieres analizar sin el https:// ni el www. Ejemplo: python.org ')
    req = request.Request('http://{}'.format(pagina))
    resultado = request.urlopen(req)
    print('Esta es la url de la página, puedes verificar si tiene o no tiene https y www', resultado.geturl())  # Mostramos la url real
    try:
        print('\n')
        url = 'http://{}'.format(pagina)
        site = request.urlopen(url)
        meta = site.info()  # Obtenemos las cabeceras de la página
        if site.headers['content-length'] != None:  # Comprobamos que no estén vacías
            print(" Content-Length:", site.headers['content-length'])
        else:
            print("Peso de la página: información no disponible")
    except:
        print('Peso de la página: información no disponible')

    try:
        print('\n')
        soup = BeautifulSoup(site)
        description = soup.find('meta', attrs={'name': 'description'})  # Buscamos la etiqueta meta-description
        b = len(description.get('content'))
        if (b > 0):  # Comprobamos que no esté vacía
            print('la descripción es:', description)
            print('El tamaño de descripción es:', len(description.get('content')))
        else:
            print('No tiene descripción')
    except:
        print('Meta Description: se ha producido un error')
    try:
        print('\n')
        html = urlopen('http://{}'.format(pagina))
        soup = BeautifulSoup(html.read())
        print('El título es:', soup.html.head.title.string)  # Obtenemos el título
        print('El tamaño del título es:', len(soup.html.head.title.string), 'caracteres')
    except:
        print('Título SEO de la página: información no disponible')

    try:
        print('\n')
        site = request.urlopen('http://{}'.format(pagina))
        soup = BeautifulSoup(site)
        keywords1 = soup.find('meta', attrs={'name': 'keywords'})  # Buscamos la etiqueta meta-keywords
        keywords = keywords1.get('content').split()
        print('Lista de palabras clave, y al lado, las veces que aparecen en el sitio web')
        for word in keywords:
            print(word, len(soup.findAll(text=re.compile(word))))
    except:
        print('Palabras clave de la página: información no disponible')

    try:
        print('\n')
        site = request.urlopen('http://{}'.format(pagina))
        soup = BeautifulSoup(site)
        print('Aquí vienen las palabras que el creador de la página ha querido resaltar con negrita y con significado SEO, para leerlos fíjate en lo que pone dentro de la etiqueta strong')
        for strong in soup.find_all('strong'):  # Encontramos todas las etiquetas strong
            print(strong)
        print("En total son:", len(soup.find_all('strong')))
    except:
        print('No ha querido resaltar ninguna palabra con negrita con significado SEO')

    try:
        print('\n')
        site = request.urlopen('http://{}'.format(pagina))
        soup = BeautifulSoup(site)
        print('Aquí vienen las palabras que el creador de la página ha querido resaltar con itálica (cursiva) y con significado SEO, para leerlos fíjate en lo que pone dentro de la etiqueta em')
        for em in soup.find_all('em'):
            print(em)
        print("En total son:", len(soup.find_all('em')))
    except:
        print('No ha querido resaltar ninguna palabra con itálica (cursiva) con significado SEO')

    try:
        print('\n')
        site = request.urlopen('http://{}'.format(pagina))
        soup = BeautifulSoup(site)
        count = 1
        for image in soup.findAll('img'):
            print('Imagen #', count, ':', image["src"])  # Mostramos el atributo src de cada imagen
            print('Alt de imagen #', count, ":", image.get('alt', 'None'))  # Mostramos el atributo alt de cada imagen
    except:
        print('Alts de imágenes de la página: información no disponible')

    try:
        print('\n')
        site = request.urlopen('http://{}'.format(pagina))
        soup = BeautifulSoup(site)
        print('Aquí vienen los títulos h1 de la página, para leerlos fíjate en lo que pone dentro de la etiqueta h1')
        for h1 in soup.find_all('h1'):
            print(h1)
        print("En total son:", len(soup.find_all('h1')))
    except:
        print('H1 de la página (títulos): Información no disponible')

    try:
        print('\n')
        site = request.urlopen('http://{}'.format(pagina))
        soup = BeautifulSoup(site)
        print('Aquí vienen los títulos h2 de la página, para leerlos fíjate en lo que pone dentro de la etiqueta h2')
        for h2 in soup.find_all('h2'):
            print(h2)
        print("En total son:", len(soup.find_all('h2')))
    except:
        print('H2 de la página (títulos): Información no disponible')

    try:
        print('\n')
        site = request.urlopen('http://{}'.format(pagina))
        soup = BeautifulSoup(site)
        print('Aquí vienen los títulos h3 de la página, para leerlos fíjate en lo que pone dentro de la etiqueta h3')
        for h3 in soup.find_all('h3'):
            print(h3)
        print("En total son:", len(soup.find_all('h3')))
    except:
        print('H3 de la página (títulos): Información no disponible')

    try:
        print('\n')
        site = request.urlopen('http://{}'.format(pagina))
        soup = BeautifulSoup(site)
        print('Aquí vienen los títulos h4 de la página, para leerlos fíjate en lo que pone dentro de la etiqueta h4')
        for h4 in soup.find_all('h4'):
            print(h4)
        print("En total son:", len(soup.find_all('h4')))
    except:
        print('H4 de la página (títulos): Información no disponible')

    try:
        print('\n')
        site = request.urlopen('http://{}'.format(pagina))
        soup = BeautifulSoup(site)
        print('Aquí vienen los títulos h5 de la página, para leerlos fíjate en lo que pone dentro de la etiqueta h5')
        for h5 in soup.find_all('h5'):
            print(h5)
        print("En total son:", len(soup.find_all('h5')))
    except:
        print('H5 de la página (títulos): Información no disponible')

    try:
        print('\n')
        site = request.urlopen('http://{}'.format(pagina))
        soup = BeautifulSoup(site)
        print('Aquí vienen los títulos h6 de la página, para leerlos fíjate en lo que pone dentro de la etiqueta h6')
        for h6 in soup.find_all('h6'):
            print(h6)
        print("En total son:", len(soup.find_all('h6')))
    except:
        print('H6 de la página (títulos): Información no disponible')

    try:
        print('\n')
        site = request.urlopen('http://{}'.format(pagina))
        soup = BeautifulSoup(site)
        links = []
        elements = soup.select('a')
        for element in elements:
            link = element.get('href')
            if link.startswith('http'):
                links.append(link)
        print('Lista de enlaces')
        print(links)
        print('Si la respuesta es 200 está bien el enlace, si es 404, está roto')
        for link in links[:10]:  # Seleccionamos solo los primeros 10 links para evitar que el sitio nos bloquee como método anti-bots
            petition = urlopen(link)
            print("Enlace: ", link, "Respuesta: ", petition.code)  # Mostamos el código de la petición
    except:
        print('Enlaces rotos de la página: Información no disponible')

    try:
        print('\n')
        url = 'http://{}'.format(pagina)
        page = request.urlopen(url)
        soup = BeautifulSoup(page)
        icon_link = soup.find('link', rel="icon")
        icon = request.urlopen(url + icon_link['href'])
        with open("test.ico", "wb") as f:  # Abrir un archivo para descargar el icono
            try:
                f.write(icon.read())
                print("Hay icono, lo tienes descargado en el mismo sitio que este documento como test.ico!")
            except:
                print("No hay Icono")
    except:
        print('Icono de la página: Información no disponible')

    try:
        print('\n')
        site = request.urlopen('http://{}'.format(pagina))
        soup = BeautifulSoup(site)
        if (soup.findAll(text=re.compile(".google-analytics"))):  # Buscamos la etiqueta de analytics
            print("Tiene Anaylitics")
        else:
            print("No tiene Analytics")
    except:
        print('Analytics de la página: Información no disponible')

    try:
        print('\n')
        site = request.urlopen('http://{}'.format(pagina))
        soup = BeautifulSoup(site, 'html.parser')
        lang = soup.find('html')['lang']  # Tomamos el atributo lang de la etiqueta html
        print('El idioma del sitio web es:', lang)
    except:
        print('Lenguaje de la página: Esta página no especifica lenguaje')

    try:
        print('\n')
        site = 'http://{}'.format(pagina)
        print("página:", site)
        petition = request.urlopen(site)
        meta = petition.info()
        print('Meta información de la página:')
        print(meta)
    except:
        print('Meta información de la página: Información no disponible')

    try:
        print('\n')
        site = request.urlopen('http://{}'.format(pagina))
        soup = BeautifulSoup(site)
        print('Meta Viewport de la página:')
        print(soup.find('meta', attrs={'name': 'viewport'}))
    except:
        print('Meta Viewport de la página: Información no disponible')

except:
    print('Lo Siento, ha habido un gran error')
