from flask import Flask, render_template
from apiReq import get_Char, get_Loc, get_episode  # Importa las funciones de apireq.py

app = Flask(__name__, template_folder='templates')

# Rutas para obtener datos de la API y pasarlos a home.html
@app.route('/')
def home():
    characters = get_Char()  # Llama a la función para obtener personajes de la API
    locations = get_Loc()    # Llama a la función para obtener ubicaciones de la API
    episodes = get_episode()  # Llama a la función para obtener episodios de la API
    return render_template('home.html', characters=characters, locations=locations, episodes=episodes)

if __name__ == '__main__':
    app.run(debug=True)
