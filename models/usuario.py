from sql_alchemy import db


class UserModel(db.Model):
    #mapeando a classe para o SQLAlchemy(classe representa tabela)
    #nome da tabela
    __tablename__ = 'usuarios'
    #colunas
    user_id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(40))
    senha = db.Column(db.String(40))

    #colunas --> atributos
    def __init__(self, login, senha):
        self.login = login
        self.senha = senha

    def json(self):
        return {
            'user_id': self.user_id,
            'login': self.login
        }

    #semelhantemente ao @staticmethod, cria métodos que pertencem à classe e não ao objeto
    #mas com a diferença que, nesse caso, desejo referenciar a classe no método --> cls
    @classmethod
    def findUser(cls, user_id):
        # SELECT * FROM usuarios WHERE user_id = $user_id ...
        user = cls.query.filter_by(user_id=user_id).first() #query.filter_by - recurso do sql alchemy. 
        if user:
            return user
        return None

    @classmethod
    def find_by_login(cls, login):
        # SELECT * FROM usuarios WHERE user_id = $user_id ...
        user = cls.query.filter_by(login=login).first() #query.filter_by - recurso do sql alchemy. 
        if user:
            return user
        return None

    def saveUser(self):
        db.session.add(self)
        db.session.commit()

    def deleteUser(self):
        db.session.delete(self)
        db.session.commit()
        
