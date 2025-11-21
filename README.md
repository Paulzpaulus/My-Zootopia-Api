# Animal Web Generator
The Animal Web Generator is a Python application that fetches animal information from the API Ninjas
Animals API and generates a static HTML page displaying the results.
The project demonstrates API usage, environment-based secret handling, HTML templating, and clean
project architecture.
## Features
- Fetches animal data from a public REST API
- Clean separation of concerns
- data_fetcher.py handles API requests
- animal_web_generator.py handles HTML generation
- Generates a static animals.html file
- Template-based rendering
- Accepts any animal name as user input
## Project Structure
My-Zootopia-Api/
■■■ animal_web_generator.py
■■■ data_fetcher.py
■■■ animal_web_generator_services.py
■■■ animals_template.html
■■■ requirements.txt
■■■ .env
■■■ .gitignore
■■■ README.md
## Installation
Clone the repository:
git clone
cd My-Zootopia-Api
Install dependencies:
pip install -r requirements.txt
Create a .env file in the project root:
API_KEY=your_api_ninjas_key_here
## Usage
Run the program:
python3 animal_web_generator.py
Enter an animal name when prompted:
Please enter an animal: fox
The program will:
1. Fetch matching animal data
2. Insert the data into the HTML template
3. Generate animals.html
4. You can open the file in any browser
If the animal does not exist, an error message will appear inside the generated page.
## Configuration
The application requires an API key from API Ninjas.
Store it in the .env file:
API_KEY=
## Contributing
Contributions are welcome.
Please follow the current architecture and use clear commit messages.
## License
This project is intended for educational use and does not include a specific license.
