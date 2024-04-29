from flask import Flask, request, render_template, redirect, url_for
from dotenv import load_dotenv
from pymongo import MongoClient

from modules.validate_password import validate_password
from modules.hash_password import hash_password

load_dotenv()

try:
    # MongoClient Connection
    client = MongoClient('localhost', 27017)
    # Database Creation
    db = client.recipedb
    # Collection Creation
    users = db.users
    recipes = db.recipes

    print("DB Connection Successful!")
except:
    print("DB Connection Failed!")

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home/index.html")

# Recipe routes

@app.route("/recipes")
def list_recipe():
    try:
        recipes_data = recipes.find()
        return render_template("recipes/list_recipe.html", recipes=recipes_data)
    except:
        return "<div>No Recipe Found</div>"
@app.route("/recipes/add", methods=["GET","POST"])
def create_recipe():
    if request.method == "GET":
        return render_template("recipes/create_recipe.html")
    elif request.method == "POST":
        title = request.form.get("title")
        description = request.form.get("description")
        ingredients = request.form.get("ingredients")
        preparation_time = request.form.get("preparation_time")
        cooking_time = request.form.get("cooking_time")
        total_time = int(preparation_time) + int(cooking_time)
        servings = request.form.get("servings")

        # Insert Data in the database
        recipes.insert_one({
            "title": title, 
            "description": description,
            "ingredients": ingredients, 
            "preparation_time": preparation_time, 
            "cooking_time": cooking_time, 
            "total_time": total_time, 
            "servings": servings
        })

        return redirect("/")

@app.route("/recipes/update", methods=["GET","PATCH"])
def update_recipe():
    if request.method == "GET":
        return render_template("recipes/update_recipe.html")
    elif request.method == "POST":
        title = request.form.get("title")
        description = request.form.get("description")
        ingredients = request.form.get("ingredients")
        preparation_time = request.form.get("preparation_time")
        cooking_time = request.form.get("cooking_time")
        total_time = int(preparation_time) + int(cooking_time)
        servings = request.form.get("servings")

        # Update Data in the database
        recipes.update_one({
            "title": title, 
            "description": description,
            "ingredients": ingredients, 
            "preparation_time": preparation_time, 
            "cooking_time": cooking_time, 
            "total_time": total_time, 
            "servings": servings
        })

        return redirect("/")

# User routes
@app.route("/signup", methods=["GET","POST"])
def signup():
    if request.method == "GET":
        return render_template("user/signup.html")
    else:
        first_name = request.form.get("first_name")
        middle_name = request.form.get("middle_name")
        last_name = request.form.get("last_name")
        email = request.form.get("email")
        password = request.form.get("password")

        if validate_password(password):
            password = hash_password(password)
            user = users.insert_one({
                "first_name": first_name,
                "middle_name": middle_name,
                "last_name": last_name,
                "email": email,
                "password": password
            })
            return user
        else:
            return "<div>Password must have 1 uppercase, 1 lowercase, 1 digit, 1 special symbol</div>"


if __name__ == "__main__":
    app.run()