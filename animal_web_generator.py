from data_fetcher import load_animals_data_from_api, load_animals_template, serialize_animal


#print("DEBUG CWD =", os.getcwd())

def build_html(animals_data, template, search_term):

    if template == "":
        print("Failed to generate (no template).")
        return

    if not animals_data:
        error_msg = f"<h2>The animal '{search_term}' doesn't exist.</h2>"
        html = template.replace("__REPLACE_ANIMALS_INFO__", error_msg)
        write_html_file(html)
        print("HTML file generated (error message shown).")
        return


    output = ""
    for animal in animals_data:
        output += serialize_animal(animal)

    html = template.replace("__REPLACE_ANIMALS_INFO__", output)
    write_html_file(html)
    print("HTML file generated successfully with animal information.")




def write_html_file(content):
    with open("animals.html", "w") as file:
        file.write(content)



def main():
    template = load_animals_template()

    search_term = input("please enter a animal:").strip().lower()
    animals_data = load_animals_data_from_api(search_term)

    build_html(animals_data, template, search_term)






if __name__ == "__main__":
    main()

