from flask import Flask
from blog.routes.employees_routes import employees_blueprint
from blog.routes.animals_routes import animals_blueprint
from flasgger import Swagger

app = Flask(__name__)
app.register_blueprint(employees_blueprint)
app.register_blueprint(animals_blueprint)
swagger = Swagger(app)

if __name__ == "__main__":
    app.run(debug=True)