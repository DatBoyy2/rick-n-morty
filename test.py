import requests
import random
from flask import Flask, render_template, jsonify, request
from flask_apscheduler import APScheduler
import json

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
        origin = str(page['origin']['name'])
        origin_url = str(page['origin']['url'])
        location = str(page['location']['name'])
        location_url = str(page['location']['url'])
    

        character_info = {
            "name": name,
            "status": status,
            "species": species,
            "gender": gender,
            "image": image,
            "origin": origin,
            "location": location,
            "location_url": location_url,
            "origin_url": origin_url
        }

    except Exception as e:
        print(f"Error: {e}")
        character_info = None  # Maneja el error apropiadamente

    return render_template('character.html', character=character_info)


@app.route('/location/<path:location_url>')
def get_location_chars(location_url):
    try:
        page = requests.get(location_url).json()
        origin_name = page['name']  # Obtenemos el nombre de la ubicación
        residents_urls = page['residents']

        residents = []
        for resident_url in residents_urls:
            resident_data = requests.get(resident_url).json()
            # Agregamos el nombre de la ubicación a los datos de cada residente
            resident_data['origin_name'] = origin_name
            residents.append(resident_data)

    except Exception as e:
        print(f"Error: {e}")
        residents = []  # En caso de error, devuelve una lista vacía

    return render_template('location.html', location_url=location_url, characters=residents)



def get_all_characters_from_origin(usr_origin_url):
    page = requests.get("https://rickandmortyapi.com/api/location/{}".format(str(usr_origin_url))).json()
    originslist = []
    url_format_characters = "https://rickandmortyapi.com/api/character/"
    for __ in range(0, 60000):
        try:
            residents_value = str(page['residents'][__])
            originslist.append(residents_value)
        except:
            break

    for _ in originslist:
        match = re.search(r'/(\d+)$', str(_))

        if match:
            character_number = int(match.group(1))
            url_format_characters += str(character_number) + ","

    characterlist = []
    page = requests.get(url_format_characters).json()
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
            characterlist.append(character)

            while_count += 1
        except:break
    return characterlist





@app.route('/origin/<int:location_id>')
def get_origin_chars(location_id):
    print(location_id)
    characters_list_from_some_origen = get_all_characters_from_origin(location_id)

    return render_template('location.html', location_url=location_id, characters=characters_list_from_some_origen)



if __name__ == '__main__':
    app.run(debug=True)