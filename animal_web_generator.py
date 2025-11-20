from animal_web_generator_services import load_animals_data_from_api, load_animals_template, serialize_animal



def build_html(animals_data, template):
    output = ""

    for animal in animals_data:
        output += serialize_animal(animal)

    new_html = template.replace("__REPLACE_ANIMALS_INFO__", output)

    write_html_file(new_html)
    print("HTML file generated successfully with animal information.")


def write_html_file(content):
    with open("animals.html", "w") as file:
        file.write(content)



def main():
    template = load_animals_template()
    search_term = "Fox"
    animals_data = load_animals_data_from_api(search_term)
    build_html(animals_data, template)






if __name__ == "__main__":
    main()

