from flask import Flask
from controller.customer_controller import cc


if __name__ == '__main__':
    app = Flask(__name__)

    app.register_blueprint(cc)

    app.run(port=8080, debug=True)
