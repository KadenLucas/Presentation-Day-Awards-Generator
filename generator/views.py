from flask import render_template, request, send_file
from generator.presentation import generate
from generator import app


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("index.html")
    
    elif request.method == "POST":
        presentation = generate(
            "assets/template.pptx",
            request.form.get("year"),
            request.files.get("awards").stream,
        )
        
        return send_file(
            presentation,
            "application/zip",
            True,
            "awards.zip",
            False,
            False
        )