from flask import Flask, render_template, request

app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route("/")
def home():
    return render_template("home.html", title="Home")

@app.route("/about")
def about():
    return render_template("about.html", title="About")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    submitted = False
    name = ""
    email = ""

    if request.method == "POST":
        submitted = True
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()

    return render_template(
        "contact.html",
        title="Contact",
        submitted=submitted,
        name=name,
        email=email
    )

if __name__ == "__main__":
    app.run(debug=True)
