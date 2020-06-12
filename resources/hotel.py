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

#exibe todos os hotéis disponíveis
class Hoteis(Resource):
    def get(self):
        # SELECT * FROM hoteis
        return {'hoteis': [hotel.json() for hotel in HotelModel.query.all()]}


#CRUD   
class Hotel(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome', type=str, required=True, help="Field 'nome' required.") #campo obrigatório
    argumentos.add_argument('avaliacao')
    argumentos.add_argument('diaria')
    argumentos.add_argument('cidade')
    
    def get(self, hotel_id): #visualizar hotel
        hotel = HotelModel.findHotel(hotel_id)
        if hotel:
            return hotel.json()
        return {'message': 'Hotel not found.'}, 404 #not found

    
    def post(self, hotel_id): #adicionar hotel
        if HotelModel.findHotel(hotel_id):
            return {'message': 'Hotel id <' + hotel_id + '> already exists.'}, 400 #bad request        
        dados = Hotel.argumentos.parse_args()
        hotel = HotelModel(hotel_id, **dados) #** kwargs
        
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
