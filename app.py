
#librerias a utilizar
import requests
from flask import Flask, render_template,request


#funcion que se utiliza para ir a buscar al Itunes API
def apple_API_search(inp):

    #lista de resultados
    results_appleAPI = []
    #request al Itunes API
    URL = "https://itunes.apple.com/search?term={}".format(inp.replace(" ","+"))
    page = requests.get(URL)

    #iteracion sobre listado de resultados y se saca la informacion relevante (nombre del artista, nombre de la cancion o show, y el tipo)
    for i in page.json()['results']:
        
        var = {'track_name': i['trackName'], 'artistName': i['artistName'],'kind': i['kind']}

        results_appleAPI.append(var)



    
    return results_appleAPI




#funcion que se utiliza para ir a buscar al API de TVmaze
def TVmaze_API_search(inp):
    #results dictionary
    results_TVmazeAPI = []
    


    #request to Itunes API
    URL = "https://api.tvmaze.com/search/people?q={}".format(inp.replace(' ','+')) + "&embed=castcredits"
    page = requests.get(URL)
    #resultado se retorna en forma de lista con un elemento aqui se convierte a json y se agarra ese unico elemento en la lista
    page = page.json()[0]
    #se encuentra el id unico que esa persona tiene dentro del API de TVmaze
    id_artista = page['person']['id']
    
    
    #request para encontrar todos los shows donde ese artista ha aparecido

    URL1 = "https://api.tvmaze.com/people/{}?embed=castcredits".format(id_artista)


    page1 = requests.get(URL1)

    raw_data = page1.json()['_embedded']['castcredits']




    #iteracion sobre resultados para extraer la informacion relevante de cada item (nombre del show, artista)
    for i in raw_data:
    
        link_var = i['_links']['show']['href']
        page2 = requests.get(link_var)


        name = page2.json()['name']
        var = {'show_name': page2.json()['name'],'artist_name':inp,'kind':"tv show"}

        results_TVmazeAPI.append(var)


    return results_TVmazeAPI


#declaracion de la creacion del API 
app = Flask(__name__)

#ruta principal
@app.route('/home', methods =['GET', 'POST'])
def home():
    if request.method=='POST':
        #se recibe el nombre del artista desde el form en html
        artist_name = request.form['artist_search']   
        TVmaze_results = []
        apple_results = []
        #se intenta hacer un call a la funcion de TVmaze con el nombre que se recibio como query 
        try:
            TVmaze_results = TVmaze_API_search(artist_name) 
        except:
            pass
        #se intenta hacer un call a la funcion de Itunes API con el nombre que se recibio como query 
        try:
            apple_results = apple_API_search(artist_name)  
        except:
            pass
         
        
        return render_template('search.html',links = TVmaze_results,links1 = apple_results)

    else:
        return render_template('search.html')
    
if __name__ == "__main__":
    #se levanta el API para poder ser utilizado
    app.run(debug=True)
