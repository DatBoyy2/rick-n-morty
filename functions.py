import requests
import random
from flask import Flask, render_template, jsonify, request
from flask_apscheduler import APScheduler
import json
import re

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


#Character related functions

def FristTwentyCharactersUpdatedInformation():
    
    print("Obteniendo datos actualizados")
    characterlist = [] 
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

            character = {"id": id, "name": name, "status": status, "species": species, "gender": gender, "image": image}
            characterlist.append(character)  

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
characterlist = FristTwentyCharactersUpdatedInformation()
scheduler.add_job(id='Get Updated Info', func=FristTwentyCharactersUpdatedInformation, trigger="interval", seconds=55)
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

        pattern = r'/(\d+)$'

        match = re.search(pattern, origin_url)
        
        origen_number = None  

        match = re.search(pattern, origin_url)

        if match:
            origen_number = match.group(1)

        match = re.search(pattern, location_url)

        if match:
            location_number = match.group(1)

        character_info = {
            "name": name,
            "status": status,
            "species": species,
            "gender": gender,
            "image": image,
            "origin": origin,
            "location": location,
            "location_url": location_url,
            "origin_url": origin_url,
            "origen_id" : origen_number,
            "location_id": location_number,
        }

    except Exception as e:
        print(f"Error: {e}")
        character_info = None  # Maneja el error apropiadamente

    return render_template('character.html', character=character_info)



#origin/Location functions

def get_all_characters_from_origin(usr_location_url):
    page = requests.get("https://rickandmortyapi.com/api/location/{}".format(str(usr_location_url))).json()
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

            character = {"id": id, "name": name, "status": status, "species": species, "gender": gender, "image": image}
            characterlist.append(character)

            while_count += 1
        except:break
    return characterlist


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

            character = {"id": id, "name": name, "status": status, "species": species, "gender": gender, "image": image}
            characterlist.append(character)

            while_count += 1
        except:break
    return characterlist


@app.route('/location/<int:location_id>')
def get_location_chars(location_id):
    characters_list_from_some_origen = get_all_characters_from_origin(location_id)

    return render_template('location.html', location_url=location_id, characters=characters_list_from_some_origen)


@app.route('/origin/<int:location_id>')
def get_origin_chars(location_id):
    print(location_id)
    characters_list_from_some_origen = get_all_characters_from_origin(location_id)

    return render_template('location.html', location_url=location_id, characters=characters_list_from_some_origen)


@app.route('/all-locations')
def get_all_locations():
    locations = requests.get(location_url).json()['results']
    return render_template('locations-list.html', locations=locations)


#Episodes related functions

@app.route('/all-episodes')
def get_all_episodes():
    episodes = requests.get(episode_url).json()['results']
    return render_template('episodes-list.html', episodes=episodes)


def get_characters_from_episode(episode_url):
    episode_data = requests.get(episode_url).json()
    characters_urls = episode_data['characters']
    character_list = []

    for character_url in characters_urls:
        character_data = requests.get(character_url).json()
        character_info = {
            "id": character_data['id'],
            "name": character_data['name'],
            "status": character_data['status'],
            "species": character_data['species'],
            "gender": character_data['gender'],
            "image": character_data['image']
        }
        character_list.append(character_info)

    return character_list


@app.route('/episode/<int:episode_id>')
def get_episode_characters(episode_id):
    episode_url = f"https://rickandmortyapi.com/api/episode/{episode_id}"
    characters_list = get_characters_from_episode(episode_url)
    return render_template('episode-char.html', characters=characters_list)



if __name__ == '__main__':
    app.run(debug=True)