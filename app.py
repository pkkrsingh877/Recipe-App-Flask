from flask import Flask, request, render_template, redirect, url_for
from dotenv import load_dotenv
from pymongo import MongoClient

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

if __name__ == "__main__":
    app.run()