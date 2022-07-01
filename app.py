from flask import Flask

# importing the pets dictionary - contains some data that we can use to populate the webpages
from helper import pets

# creation an instance of the Flask class
app = Flask(__name__)


# creation first index route with route decorator
# introduction with offered animals with links that links to each individual animal page
@app.route("/")
def index():
    return """
  <h1>Adopt a Pet</h1>
  <p>Browse through the links below to find your new furry friend:</p>
  <ul>
    <li><a href="animals/dogs">Dogs</a></li>
    <li><a href="animals/cats">Cats</a></li>
    <li><a href="animals/rabbits">Rabbits</a></li>
  </ul>
  """


# creation animals route - individual pages for each animal type
@app.route("/animals/<pet_type>")
def animals(pet_type):
    html = f"<h1>List of {pet_type}</h1>"
    html += "<ul>"
    # for loop iterates over each element in the list of pets
    # enumerate => to simultaneously loop over item and create index
    for count, pet in enumerate(pets[pet_type]):
        html += f"""
    <li><a href="/animals/{pet_type}/{count}">{pet['name']}</li>"""
    html += "</ul>"
    return html


# creation the pet route
# creation and linking to individual profile pages for each pet
@app.route("/animals/<pet_type>/<int:pet_id>")
def pet(pet_type, pet_id):
    # variable pet stores the profile information of the pet who is of pet_type and has index position pet_id in its list of pets
    pet = pets[pet_type][pet_id]
    # following elements display the profile info stored in the pet dictionary
    return f"""
  <h1>{pet["name"]}</h1>
  <img src={pet['url']} />
  <p>{pet['description']}</p>
  <ul>
    <li>Breed: {pet['breed']}</li>
    <li>Age: {pet['age']}</li>
  </ul>
  """
