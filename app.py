import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


class Task:
    def __init__(self, task_id, title, description, due_date, category, is_urgent):
        self._id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.category = category
        self.is_urgent = is_urgent

    def to_dict(self):
        return {
            "_id": self._id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "category": self.category,
            "is_urgent": self.is_urgent
        }

    @staticmethod
    def from_dict(dict_):
        return Task(
            dict_["_id"],
            dict_["title"],
            dict_["description"],
            dict_["due_date"],
            dict_["category"],
            dict_["is_urgent"]
        )


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = 'mongodb+srv://veronicapreda55:Roberto11Busi@myfirstcluster.rqruklq.mongodb.net/my_task_manager'
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

# code added for welcome template
@app.route('/')
def welcome():
    return render_template('welcome.html')


@app.route("/")
@app.route("/get_tasks")
def get_tasks():
    tasks = list(mongo.db.tasks.find())
    return render_template("tasks.html", tasks=tasks)


@app.route("/my_tasks", methods=["GET", "POST"])
def my_tasks():
    """
    Display tasks for current user, and search tasks by task name
    """
    query = request.form.get("query")
    tasks = list(mongo.db.tasks.find({"created_by": session["user"]}))
    if query:
        tasks = list(mongo.db.tasks.find(
            {"$text": {"$search": query}, "created_by": session["user"]}))
    return render_template("my_tasks.html", tasks=tasks)



@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    tasks = list(mongo.db.tasks.find({"$text": {"$search": query}}))
    return render_template("tasks.html", tasks=tasks)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format
                        (request.form.get("username")))
                    return redirect(url_for(
                        "my_tasks", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


# code added
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # Check if user is logged in
    if "user" not in session:
        return redirect(url_for("login"))

    # Get the user's document from the database
    user = mongo.db.users.find_one({"username": username})

    if request.method == "POST":
        # Extract the form data
        full_name = request.form.get("full_name")
        bio = request.form.get("bio")
        email = request.form.get("email")
        location = request.form.get("location")

        # Update the user's document in the database
        mongo.db.users.update_one(
            {"username": username},
            {"$set": {"full_name": full_name, "bio": bio, "email": email, "location": location}}
        )

        # Display a success message to the user
        flash("Your profile has been updated successfully.")

        # Redirect to the my_tasks page
        return redirect(url_for("my_tasks"))

    # Render the profile page with the user's information
    return render_template("profile.html", username=username, user=user)



@app.route("/logout")
def logout():
    #remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_task", methods=["GET", "POST"])
def add_task():
    if request.method == "POST":
        is_urgent = "on" if request.form.get("is_urgent") else "off"
        task = {
            "category_name": request.form.get("category_name"),
            "task_name": request.form.get("task_name"),
            "task_description": request.form.get("task_description"),
            "is_urgent": is_urgent,
            "due_date": request.form.get("due_date"),
            "created_by": session["user"]
        }
        mongo.db.tasks.insert_one(task) 
        flash("Task Succesfully Added")
        return redirect(url_for("get_tasks"))

    categories =mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_task.html", categories=categories)

# code modified to add conpletion date
@app.route("/edit_task/<task_id>", methods=["GET", "POST"])
def edit_task(task_id):
    if request.method == "POST":
        is_urgent = "on" if request.form.get("is_urgent") else "off"
        is_complete = "on" if request.form.get("is_complete") else "off"  # added line
        is_in_progress = "on" if request.form.get("is_in_progress") else "off"  # added line
        submit = {
            "category_name": request.form.get("category_name"),
            "task_name": request.form.get("task_name"),
            "task_description": request.form.get("task_description"),
            "is_urgent": is_urgent,
            "due_date": request.form.get("due_date"),
            "created_by": session["user"],
            "is_complete": is_complete,
            "is_in_progress": is_in_progress
        }
        mongo.db.tasks.update_one({"_id": ObjectId(task_id)}, {"$set": submit}) 
        flash("Task Successfully Updated")
        return redirect(url_for("get_tasks"))

    task = mongo.db.tasks.find_one({"_id": ObjectId(task_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_task.html", task=task, categories=categories)


@app.route("/update_all_tasks", methods=["POST"])
def update_all_tasks():
    mongo.db.tasks.update_many({}, {"$set": {"is_complete": "off", "is_in_progress": "off"}})
    flash("All tasks updated successfully")
    return redirect(url_for("get_tasks"))



# updating the delete task route
@app.route('/delete_task/<task_id>')
def delete_task(task_id):
    task = mongo.db.tasks.find_one({'_id': ObjectId(task_id)})
    if 'user' not in session:
        flash('Please log in first', 'error')
        return redirect(url_for('login'))

    if session['user'].lower() == task['created_by'].lower():
        mongo.db.tasks.delete_one({'_id': ObjectId(task_id)})
        flash('Task Deleted', 'success')
        return redirect(url_for('get_tasks'))

    flash('You are not authorized to delete this task', 'error')
    return redirect(url_for('get_tasks'))



@app.route("/get_categories")
def get_categories():
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("categories.html", categories=categories)


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.insert_one(category)
        flash("New Category Added")
        return redirect(url_for("get_categories"))

    return render_template("add_category.html")


@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.update_one({"_id": ObjectId(category_id)}, {"$set": submit})
        flash("Category Successfully Updated")
        return redirect(url_for("get_categories"))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=category)



@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    mongo.db.categories.delete_one({"_id": ObjectId(category_id)})
    flash("Category Successfully Deleted")
    return redirect(url_for("get_categories"))

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)