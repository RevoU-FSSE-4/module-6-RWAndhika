from flask import Flask
from flasgger import Swagger
from employee_view import employees_blueprint
from animal_view import animals_blueprint

app = Flask(__name__)
swagger = Swagger(app)

app.register_blueprint(employees_blueprint)
app.register_blueprint(animals_blueprint)

if __name__ == "__main__":
    app.run(debug=True)