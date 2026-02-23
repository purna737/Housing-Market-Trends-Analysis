from flask import Flask, render_template

app = Flask(__name__)

# -------------------------------
# Home Page
# -------------------------------
@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")


# -------------------------------
# Dashboard Page (Tableau Embed)
# -------------------------------
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


# -------------------------------
# Story Page (Tableau Story)
# -------------------------------
@app.route("/story")
def story():
    return render_template("story.html")


# -------------------------------
# About Page
# -------------------------------
@app.route("/about")
def about():
    return render_template("about.html")


# -------------------------------
# Run Application
# -------------------------------
if __name__ == "__main__":
    app.run(debug=True)