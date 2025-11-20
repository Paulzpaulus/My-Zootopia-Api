from animal_web_generator_services import load_animals_data, load_animals_template, serialize_animal

def load_data():
    animals_data = load_animals_data()
    template = load_animals_template()
    return animals_data, template

def build_html(animals_data, template):
    output = ""
    for animal in animals_data:
        output += serialize_animal(animal)

        new_html = template.replace("__REPLACE_ANIMALS_INFO__", output)

        write_html_file(new_html)
    else:
        print("Failed to generate HTML file due to missing data or template.")

def write_html_file(content):
    with open("animals.html", "w") as file:
        file.write(content)



def main():
    animals_data, template = load_data()
    build_html(animals_data, template)
    print("HTML file generated successfully with animal information.")





if __name__ == "__main__":
    main()

