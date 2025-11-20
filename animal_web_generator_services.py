import json
import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")

def load_animals_data_from_api(search_term):
    """
   get animal info of API.
    search_term: e.g "Fox"
    return: JSON
    """
    url = f"https://api.api-ninjas.com/v1/animals?name={search_term}"

    try:
        response = requests.get(url, headers={"X-Api-Key": API_KEY})
    except Exception as e:
        print(f"Error contacting API: {e}")
        return []

    if response.status_code != 200:
        print("API returned non-200 status")
        return []

    try:
        return response.json()
    except json.JSONDecodeError:
        print("API returned non-JSON response")
        return []



def load_animals_template():
    try:
        with open("animals_template.html", "r") as template_file:
            template = template_file.read()
            return template
    except FileNotFoundError:
        print("Error: animals_template.html not found.")
        return ""
    except Exception as e:
        print(f"Error: {e}")
        return ""



def serialize_animal(animal):
    name = animal.get('name')
    diet = (animal.get('characteristics') or {}).get('diet', 'Unknown')
    type_ = (animal.get('characteristics') or {}).get('type', 'Unknown')
    locs = animal.get('locations') or []
    location = locs[0] if locs else 'Unknown'

    output = ""
    output += "<li class='cards__item'>\n"
    output += f"  <div class='card__title'>{name}</div>\n"
    output += "  <p class='card__text'>\n"
    output += f"    <strong>Diet:</strong> {diet}<br/>\n"
    output += f"    <strong>Location:</strong> {location}<br/>\n"
    output += f"    <strong>Type:</strong> {type_}<br/>\n"
    output += "  </p>\n"
    output += "</li>\n"
    return output
