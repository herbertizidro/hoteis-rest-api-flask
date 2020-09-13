from flask import Flask
from flask_restful import Api
from resources.hotel import Hoteis, Hotel

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hoteis.db' #setando o banco pro app flask
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)

@app.before_first_request  #cria o banco antes da primeira requisição, se já não existir
def dbCreate():
    db.create_all()

#adicionando os recursos(classes) criados e suas urls ao objeto api
api.add_resource(Hoteis, '/hoteis')
api.add_resource(Hotel, '/hoteis/<string:hotel_id>') #espera receber um parâmetro string

if __name__ == '__main__': #se executar ESTE arquivo...
    from sql_alchemy import db
    db.init_app(app)
    #app.run(host="0.0.0.0", port = 2000, debug = False) em produção: debug = False
    app.run(debug = True) #inicia o app
