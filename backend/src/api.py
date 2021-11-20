from flask import Flask, request, Response, render_template, redirect, url_for, make_response, jsonify
from flask_cors import CORS
import json
from db import Especialidade

# Porta do servidor
PORT = 3001

# Instância do Flask
app = Flask(__name__)
CORS(app)

es = Especialidade()

@app.route('/')
def index():
    especialidades = es.get_all()
    
    return jsonify(especialidades)


if __name__ == '__main__':
    app.run(debug=True, port=PORT)