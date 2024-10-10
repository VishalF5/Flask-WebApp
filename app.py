from flask import Flask

from api.admins import admin_blueprint
from api.assignments import assignment_blueprint
from api.users import user_blueprint

app = Flask(__name__)

# Register routes
app.register_blueprint(admin_blueprint)
app.register_blueprint(user_blueprint)
app.register_blueprint(assignment_blueprint)

if __name__ == "__main__":
    app.run(debug=True)
