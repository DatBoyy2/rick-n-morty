import requests
import random
from flask import Flask, render_template, jsonify

app = Flask(__name__, template_folder='templates', static_folder='static/styles')

#URLs

url="https://rickandmortyapi.com/api/"
character_url=url+"character/"
location_url=url+"location/"
episode_url=url+"episode/"


#Lists

charIDlist = []

#generar id random

cont1 = 0

while cont1 < 20:
    
    id = random.randint(1, 826)
    
    if id not in charIDlist:
        
        charIDlist.append(id)
        cont1 += 1
        
    else:
        
        continue
    

#Characters related functions

@app.route('/')
def get_Char():
    
    characterlist = [] # Inicializar characterlist dentro de la función get_Char()

    for i in charIDlist:   

        
        try:
            
            page = requests.get(character_url+"{}".format(i)).json()
            name = str(page['name'])
            status = str(page['status'])
            species = str(page['species'])
            gender = str(page['gender'])
            image = str(page['image'])
                  
                
            character = {"name" : page['name'], "status" : page['status'], "species" : page['species'], "gender" : page['gender'], "image" : page['image']}
            characterlist.append(character) # Agregar el character al characterlist
                
                


        except:
            print(
                "No result found for the id : {} \nYou can be IP limited check the Website"+character_url+"{}".format(
                i, i))

            break

    return(render_template('home.html', characterlist=characterlist))

@app.route('/load-more-characters')
def load_more_characters():
    new_characters = generate_random_characters(12)  # Generar 12 nuevos personajes aleatorios
    return jsonify(new_characters)

def generate_random_characters(count):
    characters = []
    for _ in range(count):
        id = random.randint(1, 826)
        try:
            page = requests.get(character_url + "{}".format(id)).json()
            character = {
                "name": page['name'],
                "status": page['status'],
                "species": page['species'],
                "gender": page['gender'],
                "image": page['image']
            }
            characters.append(character)
        except:
            print("No se encontraron resultados para el ID: {}".format(id))
    return characters
        
        
if __name__ == '__main__':
    app.run(debug=True)