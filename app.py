from flask import Flask, request
from controller.client_controller import cc

app = Flask(__name__)

app.register_blueprint(cc)

users = {
    "bachy21": {
        "mobile_phone": "512-826-0002",
        "todos": [
            {
                "description": "Do laundry",
                "completed": False
            },
            {
                "description": "Go to the doctor's office",
                "completed": False
            },
            {
                "description": "Call Fred",
                "completed": False
            }
            ,
            {
                "description": "Take out trash",
                "completed": True
            },
            {
                "description": "Wash dishes",
                "completed": True
            }
        ]
    },
    "jane12345": {
        "mobile_phone": "512-826-0001",
        "todos": []
    }
}

# Decorator
# Decorators are a concept from Python
# The @app.route decorator is coming from Flask
# and it is essentially treating a function
# as the initial execution point
# whenever an HTTP request is received
# to that particular endpoint
@app.route('/test')
def hello():
    print("Hi, the hello() function is being executed")
    return "Hello World"



app.run(port=8080, debug=True)




  # Start up the web server on port 8080