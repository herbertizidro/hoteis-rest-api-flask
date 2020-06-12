from flask import Flask
from flask_restful import Api
from resources.hotel import Hoteis, Hotel

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hoteis.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

@app.before_first_request  #antes da primeira requisição cria o banco se não existir
def dbCreate():
    db.create_all()

api.add_resource(Hoteis, '/hoteis')
api.add_resource(Hotel, '/hoteis/<string:hotel_id>')

if __name__ == '__main__':
    from sql_alchemy import db
    db.init_app(app)
    #app.run(host="0.0.0.0", port = 2000, debug = False)
    app.run(debug = True)
