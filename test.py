import requests
import random
from flask import Flask, render_template, jsonify, request
from flask_apscheduler import APScheduler

app = Flask(__name__, template_folder='templates', static_folder='static')
scheduler = APScheduler()

#URL
url="https://rickandmortyapi.com/api/"
character_url=url+"character/"
location_url=url+"location/"
episode_url=url+"episode/"


#home

@app.route('/')
def home():
    return render_template('home.html')

#Generar id random
charIDlist = []
cont1 = 0
while cont1 < 20:
    id = random.randint(1, 826)
    if id not in charIDlist:
        charIDlist.append(id)
        cont1 += 1

def FrontPageFristTwentyCharactersUpdatedInformation():
    #Get Updated Data From Api
    print("Obteniendo datos actualizados")
    characterlist = []  # Inicializar characterlist dentro de la función get_Char()
    url_format_api_request = ""
    for i in charIDlist:
        url_format_api_request += str(i) + ","
    page = requests.get(character_url + "{}".format(url_format_api_request)).json()

    while_count = 0
    while True:
        try:
            name = str(page[while_count]['name'])
            status = str(page[while_count]['status'])
            species = str(page[while_count]['species'])
            gender = str(page[while_count]['gender'])
            image = str(page[while_count]['image'])
            id = str(page[while_count]['id'])

            character = {"id": id, "name": name, "status": status, "species": species,
                             "gender": gender, "image": image}
            characterlist.append(character)  # Agregar el character al characterlist

            while_count+= 1
        except:
            break
    return characterlist



def RequestApiCharacterInformation(CharactersLoadInt):
    characters = []
    url_api_request = ""
    number_of_api_request = []
    for _ in range(CharactersLoadInt):
        while True:
            id = random.randint(1, 826)
            if id not in charIDlist:
                charIDlist.append(id)
                number_of_api_request.append(number_of_api_request)
                url_api_request += str(id) + ","
                break

    page = requests.get(character_url + "{}".format(url_api_request)).json()

    while_count_api = 0
    while True:
        try:
            character = {
                        "name": page[while_count_api]['name'],
                        "status": page[while_count_api]['status'],
                        "species": page[while_count_api]['species'],
                        "gender": page[while_count_api]['gender'],
                        "image": page[while_count_api]['image'],
                        "id": page[while_count_api]['id']
            }
            characters.append(character)
            while_count_api += 1
        except:
            break

    return characters


#Crontab Update Data Every 5 Seconds
characterlist = FrontPageFristTwentyCharactersUpdatedInformation()
scheduler.add_job(id='Get Updated Info', func=FrontPageFristTwentyCharactersUpdatedInformation, trigger="interval", seconds=55)
scheduler.start()

@app.route('/all-characters')
def get_Char():
    return(render_template('charlist.html', characterlist=characterlist))

@app.route('/load-more-characters')
def load_more_characters():
    new_characters = RequestApiCharacterInformation(12)
    return jsonify(new_characters)
        
@app.route('/character/<int:character_id>')
def show_character(character_id):
    page = requests.get(character_url + str(character_id)).json()
    
    try:
        name = str(page['name'])
        status = str(page['status'])
        species = str(page['species'])
        gender = str(page['gender'])
        image = str(page['image'])
        
        origin_url = page['origin']['url']
        origin_data = requests.get(origin_url).json()
        origin_name = origin_data['name']

        location_url = page['location']['url']
        location_data = requests.get(location_url).json()
        location_name = location_data['name']
        
        residents_urls = location_data['residents'][:5]  # Obtén las URLs de los primeros 5 residentes
        residents = []

        for resident_url in residents_urls:
            resident_data = requests.get(resident_url).json()
            residents.append({
                "name": resident_data['name'],
                "image": resident_data['image']
            })

        character_info = {
            "name": name,
            "status": status,
            "species": species,
            "gender": gender,
            "image": image,
            "origin": origin_name,
            "location": location_name,
            "residents": residents
        }

    except Exception as e:
        print(f"Error: {e}")
        character_info = None  # Maneja el error apropiadamente

    return render_template('character.html', character=character_info)

if __name__ == '__main__':
    app.run(debug=True)