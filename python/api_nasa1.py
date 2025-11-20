'''
    Api:Aplication Programming Interface
    Nasa API: https://api.nasa.gov/
    developer: Jose E. Colimba
    Date:09112025
    Scripts description: Get snd read data from about comets and others
    https://api.nasa.gov/neo/rest/v1/neo/3726709?api_key={api_key}

    
'''
'''
Api: Application Programming Interface
Nasa API: https://api.nasa.gov/
developer: Jose E. Colimba
Date: 09-11-2025
Script description: Get and read data about comets and others
'''

import requests
import os

os.system('cls')

def get_nasa_data(api_key):
    print("::: COMETS DATA FROM NASA API :::")
    url = f"https://api.nasa.gov/neo/rest/v1/neo/3726710?api_key={api_key}"

    # Realizar la solicitud GET
    response = requests.get(url)
    response.raise_for_status()  
    data = response.json()

    print(data)


# Ejecutar función
API_KEY_NASA = "HTYIT4thL2YMDbnaARTOrenKaxcsDIjg1g8bFe1F"
get_nasa_data(API_KEY_NASA)
