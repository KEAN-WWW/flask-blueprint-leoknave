from flask import Flask
from application.bp.homepage.homepage import homepage  # Correct import

app = Flask(__name__)

# Register the Blueprint
app.register_blueprint(homepage, url_prefix="/")

if __name__ == '__main__':
    app.run(debug=True)
