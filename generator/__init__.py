from flask import Flask

app = Flask(__name__)
app.config.update(
    {
        "TEMPLATES_AUTO_RELOAD": True
    }
)

from generator import views