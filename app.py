from flask import Flask, request, render_template

app = Flask(__name__)

app.debug=True

recipes = [
    {
        "title": "Spaghetti Carbonara",
        "description": "Classic Italian pasta dish with bacon, eggs, and cheese.",
        "ingredients": ["Spaghetti", "Eggs", "Bacon", "Parmesan Cheese"],
        "preparation_time": 20,
        "cooking_time": 15,
        "servings": 4
    },
    {
        "title": "Chicken Alfredo",
        "description": "Creamy pasta dish with chicken and Alfredo sauce.",
        "ingredients": ["Fettuccine", "Chicken Breast", "Heavy Cream", "Parmesan Cheese"],
        "preparation_time": 15,
        "cooking_time": 20,
        "servings": 4
    },
    {
        "title": "Margherita Pizza",
        "description": "Traditional Italian pizza topped with tomatoes, mozzarella, and basil.",
        "ingredients": ["Pizza Dough", "Tomatoes", "Fresh Mozzarella", "Basil"],
        "preparation_time": 10,
        "cooking_time": 15,
        "servings": 2
    }
]

@app.route("/")
def index():
    return render_template("layouts.html")

@app.route("/recipes")
def list_recipe():
    return render_template("recipes/list_recipe.html", recipes=recipes)

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
        servings = request.form.get("servings")

        # Print or process the received data as needed
        print(f"Received data: {title}, {description}, {ingredients}, {preparation_time}, {cooking_time}, {servings}")

        # Here you can add the received recipe data to your recipes list or database

        return "<div>Data Successfully Entered</div>"

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
        servings = request.form.get("servings")

        # Print or process the received data as needed
        print(f"Received Updated data: {title}, {description}, {ingredients}, {preparation_time}, {cooking_time}, {servings}")

        # Here you can add the received recipe data to your recipes list or database

        return "<div>Data Successfully Updated</div>"

if __name__ == "__main__":
    app.run()