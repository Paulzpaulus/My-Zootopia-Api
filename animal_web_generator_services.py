import json
import requests

def load_animals_data():
    try:
        with open("animals_data.json", "r") as file:
            animals_data = json.load(file)
            return animals_data
    except FileNotFoundError:
        print("Error: animals_data.json not found.")
        return []
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in animals_data.json.")
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
