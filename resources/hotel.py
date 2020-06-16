from flask_restful import Resource, reqparse
from models.hotel import HotelModel

'''
exemplo hotel

{
  'hotel_id': 'orlando',
  'nome': 'Orlando',
  'avaliacao': 4.3,
  'diaria': 420,
  'cidade': 'Rio de Janeiro'
}
'''

#exibe todos os hotéis do banco de dados
class Hoteis(Resource):
    def get(self):
        # o mesmo que SELECT * FROM hoteis
        return {'hoteis': [hotel.json() for hotel in HotelModel.query.all()]}


#CRUD   
class Hotel(Resource):

    #para os métodos post e put: analisa as solicitações - define o tipo de dado esperado, se pode ou não ser omitido(required), fornece uma
    #mensagem de ajuda pro caso de um dado obrigatório não ser informado na requisição
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome', type=str, required=True, help="Field 'nome' required.") #campo obrigatório
    argumentos.add_argument('avaliacao')
    argumentos.add_argument('diaria')
    argumentos.add_argument('cidade')

    #métodos GET, POST, PUT e DELETE
    def get(self, hotel_id): #visualizar hotel
        hotel = HotelModel.findHotel(hotel_id)
        if hotel:
            return hotel.json()
        return {'message': 'Hotel not found.'}, 404 #not found

    
    def post(self, hotel_id): #adicionar hotel
        if HotelModel.findHotel(hotel_id):
            return {'message': 'Hotel id <' + hotel_id + '> already exists.'}, 400 #bad request        
        dados = Hotel.argumentos.parse_args() #dados da solicitação
        hotel = HotelModel(hotel_id, **dados) #passa esses dados por meio de ** kwargs para o modelo que representa a tabela no banco de dados
        
        try:
            hotel.saveHotel()
        except:
            return {'message': 'An internal error ocurred trying to save hotel.'}, 500 #internal server error
        
        return hotel.json(), 200 #success
    
    def put(self, hotel_id): #atualizar hotel
        dados = Hotel.argumentos.parse_args()
        hotel = HotelModel.findHotel(hotel_id)
        if hotel:
            hotel.updateHotel(**dados)
            try:
                hotel.saveHotel()
            except:
                return {'message': 'An internal error ocurred trying to save hotel.'}, 500 #internal server error
            return hotel.json(), 200
        return {'message': 'Hotel not found.'}, 404 #not found
    
    def delete(self, hotel_id):
        hotel = HotelModel.findHotel(hotel_id)
        if hotel:
            try:
                hotel.deleteHotel()
            except:
                return {'message': 'An internal error ocurred trying to delete hotel.'}, 500 #internal server error
            return {'message': 'Hotel deleted.'}
        return {'message': 'Hotel not found.'}, 404
