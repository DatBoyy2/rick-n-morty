import requests
import random
from flask import Flask, render_template


#URLs

url="https://rickandmortyapi.com/api/"
character_url=url+"character/"
location_url=url+"location/"
episode_url=url+"episode/"


#Lists

charIDlist = []
episodeIDlist = []
locationIDlist = []


#Characters related functions

def get_Char():
    
    count = 0
    
    while count < 20:
        
        id = random.randint(1,826)  
        
        if id not in charIDlist:
        
            try:
            
                page = requests.get(character_url+"{}".format(id)).json()
                name = str(page['name'])
                status = str(page['status'])
                species = str(page['species'])
                gender = str(page['gender'])
                print("|{}| Name : {}// {}// {}// {} ".format(id,name,status,species,gender))
                count += 1
                charIDlist.append(id)

            except:
                print(
                    "No result found for the id : {} \nYou can be IP limited check the Website"+character_url+"{}".format(
                    id, id))

                break
        
        else:
            
            continue
        
        
def get_more_characters():
        
    count = 0
    
    while count < 10:
        
        id = random.randint(1,826)  
        
        if id not in charIDlist:
        
            try:
            
                page = requests.get(character_url+"{}".format(id)).json()
                name = page['name']
                status = page['status']
                species = page['species']
                gender = page['gender']
                print("|{}| Name : {}// {}// {}// {} ".format(id,name,status,species,gender))
                count += 1
                charIDlist.append(id)

            except:
                print(
                    "No result found for the id : {} \nYou can be IP limited check the Website"+character_url+"{}".format(
                    id, id))

                break
        
        else:
            
            continue
        
        
        
#Locations related functions
        
def get_Loc():
    
    count = 0
    
    while count < 20:
        
        id = random.randint(1,126)  
        
        if id not in locationIDlist:
        
            try:
            
                page = requests.get(location_url+"{}".format(id)).json()
                name = str(page['name'])
                type = str(page['type'])
                dimension = str(page['dimension'])
                print("|{}| Name : {}// {}// {}".format(id,name, type, dimension))
                count += 1
                locationIDlist.append(id)

            except:
                print(
                    "No result found for the id : {} \nYou can be IP limited check the Website"+location_url+"{}".format(
                    id, id))

                break
        
        else:
            
            continue
        

def get_more_locations():
    
    count = 0
    
    while count < 10:
        
        id = random.randint(1,126)  
        
        if id not in locationIDlist:
        
            try:
            
                page = requests.get(location_url+"{}".format(id)).json()
                name = page['name']
                type = page['type']
                dimension = page['dimension']
                print("|{}| Name : {}// {}// {}".format(id,name, type, dimension))
                count += 1
                locationIDlist.append(id)

            except:
                print(
                    "No result found for the id : {} \nYou can be IP limited check the Website"+location_url+"{}".format(
                    id, id))

                break
        
        else:
            
            continue




#episode related functions

def get_episode():
    
    count = 0
    
    while count < 20:
        
        id = random.randint(1,51)  
        
        if id not in episodeIDlist:
        
            try:
            
                page = requests.get(episode_url+"{}".format(id)).json()
                name = str(page['name'])
                date = str(page['air_date'])
                episode = str(page['episode'])
                print("|{}| Name : {}// {}// {}".format(id,name, date, episode))
                count += 1
                episodeIDlist.append(id)

            except:
                print(
                    "No result found for the id : {} \nYou can be IP limited check the Website"+episode_url+"{}".format(
                    id, id))

                break
        
        else:
            
            continue
        
        
def get_more_episodes():
    
    count = 0
    
    while count < 10:
        
        id = random.randint(1,51)  
        
        if id not in episodeIDlist:
        
            try:
            
                page = requests.get(episode_url+"{}".format(id)).json()
                name = page['name']
                date = page['air_date']
                episode = page['episode']
                print("|{}| Name : {}// {}// {}".format(id,name, date, episode))
                count += 1
                episodeIDlist.append(id)

            except:
                print(
                    "No result found for the id : {} \nYou can be IP limited check the Website"+episode_url+"{}".format(
                    id, id))

                break
        
        else:
            
            continue
        
        
