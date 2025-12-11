from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)

"""
---------------------------------------------------------------
How Routing Works in Flask
---------------------------------------------------------------
Routing in Flask means connecting a URL to a specific function
in your Python code. Each route is created using the 
@app.route() decorator. When a user visits a URL (such as "/about"),
Flask finds the matching route and runs the function below it.

That function usually returns an HTML template using 
render_template(), which tells Flask which webpage to display.

Example:
@app.route("/about")
def about():
    return render_template("about.html")

In this example:
- The user visits /about
- Flask runs the about() function
- The function returns the about.html page to the browser

This is how Flask handles different pages in a web application.
---------------------------------------------------------------
"""

