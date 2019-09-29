from flask import Flask, jsonify, request, render_template
import random, time
import subprocess

PORT=4444
a = input("Do you have Flask installed? y/n\n")
app = Flask(__name__)

if(a == 'n'):
    try:
        subprocess.run(["pip", "install", "flask"], check=True)
        print("Download successfull")
    except:
        print("Download failed!")
        print("Try downloading Flask (http://www.devfuria.com.br/python/flask/)")



@app.route('/', methods=['GET', 'POST'])
def hello():

    # POST request
    if request.method == 'POST':
        print('Incoming..')
        print(request.get_json())  # parse as JSON
        return 'OK', 200

    # GET request
    elif request.method == "GET":
        message = {'greeting':'Hello from Flask!'}
        return jsonify(message)  # serialize and use JSON headers
    return render_template('index.html')



app.run(port=4996)
