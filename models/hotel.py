from sql_alchemy import db


class HotelModel(db.Model):
    #mapeando a classe para o SQLAlchemy(classe vira tabela)
    #nome da tabela
    __tablename__ = 'hoteis'
    #colunas
    hotel_id = db.Column(db.String, primary_key=True)
    nome = db.Column(db.String(80))
    avaliacao = db.Column(db.Float(precision=1)) #precision determina quantas casas após o ponto
    diaria = db.Column(db.Float(precision=2))
    cidade = db.Column(db.String(40))

    
    def __init__(self, hotel_id, nome, avaliacao, diaria, cidade):
        self.hotel_id = hotel_id
        self.nome = nome
        self.avaliacao = avaliacao
        self.diaria = diaria
        self.cidade = cidade

    def json(self):
        return {
            'hotel_id': self.hotel_id,
            'nome': self.nome,
            'avaliacao': self.avaliacao,
            'diaria': self.diaria,
            'cidade': self.cidade
        }

    @classmethod
    def findHotel(cls, hotel_id):
        # SELECT * FROM hoteis WHERE hotel_id = $hotel_id ...
        hotel = cls.query.filter_by(hotel_id=hotel_id).first() #query - recurso do sql alchemy. 
        if hotel:
            return hotel
        return None

    def saveHotel(self):
        db.session.add(self)
        db.session.commit()

    def updateHotel(self, nome, avaliacao, diaria, cidade):
        self.nome = nome
        self.avaliacao = avaliacao
        self.diaria = diaria
        self.cidade = cidade

    def deleteHotel(self):
        db.session.delete(self)
        db.session.commit()
        
