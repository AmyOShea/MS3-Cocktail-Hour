import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from flask_paginate import Pagination, get_page_args
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.context_processor
def context_processor():
    categories = list(mongo.db.categories.find())
    return dict(categories=categories)


@app.route("/")
@app.route("/home")
def home():
    categories = mongo.db.categories.find()
    return render_template("index.html", categories=categories)


@app.route("/collection/<category_id>")
def collection(category_id):
    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("collection.html", category=category)


@app.route("/get_recipes")
def get_recipes():
    # https://gist.github.com/mozillazg/69fb40067ae6d80386e10e105e6803c9
    # https://stackoverflow.com/questions/27992413/how-do-i-calculate-the-offsets-for-pagination/27992616
    # pylint: disable=unbalanced-tuple-unpacking
    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page',
        offset_parameter='offset')
    per_page = 12
    offset = (page - 1) * per_page
    total = mongo.db.recipes.find().count()
    recipes = mongo.db.recipes.find()
    recipes_paginated = recipes[offset: offset + per_page]
    pagination = Pagination(page=page, per_page=per_page,
                            total=total, css_framework='materializecss')
    return render_template("recipes.html", recipes=recipes_paginated,
                           page=page,
                           per_page=per_page,
                           pagination=pagination)


@app.route("/full_recipe/<recipe_id>")
def full_recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("full_recipe.html", recipe=recipe)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    # pylint: disable=unbalanced-tuple-unpacking
    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page',
        offset_parameter='offset')
    per_page = 12
    offset = (page - 1) * per_page
    total = mongo.db.recipes.find({"$text": {"$search": query}}).count()
    recipes = mongo.db.recipes.find({"$text": {"$search": query}})
    recipes_paginated = recipes[offset: offset + per_page]
    pagination = Pagination(
        page=page, per_page=per_page,
        total=total, css_framework='materializecss')
    return render_template("recipes.html", recipes=recipes_paginated,
                           page=page, per_page=per_page, pagination=pagination)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username is already in use
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already in use")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put user into session
        session["user"] = request.form.get("username").lower()
        flash("Registration Complete!")
        return redirect(url_for("account", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check for username in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # check for matching password
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                return redirect(url_for("account", username=session["user"]))
            else:
                # invalid password
                flash("Username or password is incorrect")
                return redirect(url_for("login"))

        else:
            # cannot find username
            flash("Username or password is incorrect")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/account/<username>", methods=["GET", "POST"])
def account(username):
    username = mongo.db.users.find_one(
        # pylint: disable=unbalanced-tuple-unpacking
        {"username": session["user"]})["username"]
    # pylint: disable=unbalanced-tuple-unpacking
    page, per_page, offset = get_page_args(
        page_sparameter='page', per_page_parameter='per_page',
        offset_parameter='offset')
    per_page = 12
    offset = (page - 1) * per_page
    user = mongo.db.users.find_one({"username": session["user"]})
    recipes = list(mongo.db.recipes.find(
        {"created_by": ObjectId(user["_id"])}))
    total = len(recipes)
    recipes_paginated = recipes[offset: offset + per_page]
    pagination = Pagination(
        page=page, per_page=per_page, total=total,
        css_framework='materializecss')
    if session["user"]:
        for recipe in recipes:
            try:
                recipe["created_by"] = mongo.db.users.find_one(
                    {"_id": recipe["created_by"]})["username"]
            except Exception:
                pass
        return render_template("account.html", username=username,
                               recipes=recipes_paginated, page=page,
                               per_page=per_page, pagination=pagination)
    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        user = mongo.db.users.find_one({"username": session["user"]})
        recipe = {
            "category_name": request.form.getlist("category_name"),
            "cocktail_name": request.form.get("cocktail_name"),
            "main_ingredient": request.form.get("main_ingredient"),
            "ingredients": request.form.getlist("ingredients"),
            "method": request.form.getlist("method"),
            "image_url": request.form.get("image_url"),
            "created_by": ObjectId(user["_id"])
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Uploaded!")
        return redirect(url_for("account", username=session["user"]))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_recipe.html", categories=categories)


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        user = mongo.db.users.find_one({"username": session["user"]})
        update = {
            "category_name": request.form.getlist("category_name"),
            "cocktail_name": request.form.get("cocktail_name"),
            "main_ingredient": request.form.get("main_ingredient"),
            "ingredients": request.form.getlist("ingredients"),
            "method": request.form.getlist("method"),
            "image_url": request.form.get("image_url"),
            "created_by": ObjectId(user["_id"])
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, update)
        flash("Recipe Edited!")
        return redirect(url_for("account", username=session["user"]))

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_recipe.html", recipe=recipe,
                           categories=categories)


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe has been deleted successfully")
    return redirect(url_for("account", username=session["user"]))

"""
@app.route("/mocktails")
def mocktails():
    # https://gist.github.com/mozillazg/69fb40067ae6d80386e10e105e6803c9
    # https://stackoverflow.com/questions/27992413/how-do-i-calculate-the-offsets-for-pagination/27992616
    # pylint: disable=unbalanced-tuple-unpacking
    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page',
        offset_parameter='offset')
    per_page = 12
    offset = (page - 1) * per_page
    total = mongo.db.recipes.find({"category_name": 'Mocktails'}).count()
    recipes = mongo.db.recipes.find({"category_name": 'Mocktails'})
    recipes_paginated = recipes[offset: offset + per_page]
    pagination = Pagination(page=page, per_page=per_page,
                            total=total, css_framework='materializecss')
    return render_template("mocktails.html", recipes=recipes_paginated,
                           page=page,
                           per_page=per_page,
                           pagination=pagination)


@app.route("/classics")
def classics():
    # https://gist.github.com/mozillazg/69fb40067ae6d80386e10e105e6803c9
    # https://stackoverflow.com/questions/27992413/how-do-i-calculate-the-offsets-for-pagination/27992616
    # pylint: disable=unbalanced-tuple-unpacking
    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page',
        offset_parameter='offset')
    per_page = 12
    offset = (page - 1) * per_page
    total = mongo.db.recipes.find({"category_name": 'Classics'}).count()
    recipes = mongo.db.recipes.find({"category_name": 'Classics'})
    recipes_paginated = recipes[offset: offset + per_page]
    pagination = Pagination(page=page, per_page=per_page,
                            total=total, css_framework='materializecss')
    return render_template("classics.html", recipes=recipes_paginated,
                           page=page,
                           per_page=per_page,
                           pagination=pagination)


@app.route("/elegance")
def elegance():
    # https://gist.github.com/mozillazg/69fb40067ae6d80386e10e105e6803c9
    # https://stackoverflow.com/questions/27992413/how-do-i-calculate-the-offsets-for-pagination/27992616
    # pylint: disable=unbalanced-tuple-unpacking
    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page',
        offset_parameter='offset')
    per_page = 12
    offset = (page - 1) * per_page
    total = mongo.db.recipes.find({"category_name": 'Elegance'}).count()
    recipes = mongo.db.recipes.find({"category_name": 'Elegance'})
    recipes_paginated = recipes[offset: offset + per_page]
    pagination = Pagination(page=page, per_page=per_page,
                            total=total, css_framework='materializecss')
    return render_template("elegance.html", recipes=recipes_paginated,
                           page=page,
                           per_page=per_page,
                           pagination=pagination)


@app.route("/fruity")
def fruity():
    # https://gist.github.com/mozillazg/69fb40067ae6d80386e10e105e6803c9
    # https://stackoverflow.com/questions/27992413/how-do-i-calculate-the-offsets-for-pagination/27992616
    # pylint: disable=unbalanced-tuple-unpacking
    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page',
        offset_parameter='offset')
    per_page = 12
    offset = (page - 1) * per_page
    total = mongo.db.recipes.find({"category_name": 'Fruity'}).count()
    recipes = mongo.db.recipes.find({"category_name": 'Fruity'})
    recipes_paginated = recipes[offset: offset + per_page]
    pagination = Pagination(page=page, per_page=per_page,
                            total=total, css_framework='materializecss')
    return render_template("fruity.html", recipes=recipes_paginated,
                           page=page,
                           per_page=per_page,
                           pagination=pagination)


@app.route("/hot_drinks")
def hot_drinks():
    # https://gist.github.com/mozillazg/69fb40067ae6d80386e10e105e6803c9
    # https://stackoverflow.com/questions/27992413/how-do-i-calculate-the-offsets-for-pagination/27992616
    # pylint: disable=unbalanced-tuple-unpacking
    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page',
        offset_parameter='offset')
    per_page = 12
    offset = (page - 1) * per_page
    total = mongo.db.recipes.find({"category_name": 'Hot Drinks'}).count()
    recipes = mongo.db.recipes.find({"category_name": 'Hot Drinks'})
    recipes_paginated = recipes[offset: offset + per_page]
    pagination = Pagination(page=page, per_page=per_page,
                            total=total, css_framework='materializecss')
    return render_template("hot_drinks.html", recipes=recipes_paginated,
                           page=page,
                           per_page=per_page,
                           pagination=pagination)


@app.route("/pitchers")
def pitchers():
    # https://gist.github.com/mozillazg/69fb40067ae6d80386e10e105e6803c9
    # https://stackoverflow.com/questions/27992413/how-do-i-calculate-the-offsets-for-pagination/27992616
    # pylint: disable=unbalanced-tuple-unpacking
    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page',
        offset_parameter='offset')
    per_page = 12
    offset = (page - 1) * per_page
    total = mongo.db.recipes.find({"category_name": 'Pitchers'}).count()
    recipes = mongo.db.recipes.find({"category_name": 'Pitchers'})
    recipes_paginated = recipes[offset: offset + per_page]
    pagination = Pagination(page=page, per_page=per_page,
                            total=total, css_framework='materializecss')
    return render_template("pitchers.html", recipes=recipes_paginated,
                           page=page,
                           per_page=per_page,
                           pagination=pagination)


@app.route("/shots")
def shots():
    # https://gist.github.com/mozillazg/69fb40067ae6d80386e10e105e6803c9
    # https://stackoverflow.com/questions/27992413/how-do-i-calculate-the-offsets-for-pagination/27992616
    # pylint: disable=unbalanced-tuple-unpacking
    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page',
        offset_parameter='offset')
    per_page = 12
    offset = (page - 1) * per_page
    total = mongo.db.recipes.find({"category_name": 'Shots'}).count()
    recipes = mongo.db.recipes.find({"category_name": 'Shots'})
    recipes_paginated = recipes[offset: offset + per_page]
    pagination = Pagination(page=page, per_page=per_page,
                            total=total, css_framework='materializecss')
    return render_template("shots.html", recipes=recipes_paginated,
                           page=page,
                           per_page=per_page,
                           pagination=pagination)
"""

# https://flask.palletsprojects.com/en/2.0.x/errorhandling/
@app.errorhandler(403)
def forbidden(e):
    return render_template('403.html'), 403


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
