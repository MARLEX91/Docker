from flask import Flask
from flask_pymongo import PyMongo
from bson import ObjectId

app = Flask(__name__)

# Configuración de MongoDB
app.config["MONGO_URI"] = "mongodb://alex:password@mongo:27017/miapp?authSource=admin"
mongo = PyMongo(app)

# Definimos el esquema para los datos
@app.route('/crear')
def crear():
    print('creando...')
    mongo.db.animales.insert_one({'tipo': 'Chanchito', 'estado': 'Feliz'})
    return 'ok'

@app.route('/')
def listar():
    print('listando... chanchitos...')
    animales = mongo.db.animales.find()
    return '<br>'.join([f'{animal["tipo"]} - {animal["estado"]}' for animal in animales])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
