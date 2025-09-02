from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Team, We are learning Devops and getting hands-on experience on Docker. Today we are learning how to deploy a simple Flask application using Docker.app!'

@app.route('/health')
def health():
    return 'Server is up and running'
