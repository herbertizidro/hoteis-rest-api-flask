from flask_restful import Resource, reqparse
from models.usuario import UserModel
from flask_jwt_extended import create_access_token, jwt_required
from werkzeug.security import safe_str_cmp


atributos = reqparse.RequestParser()
atributos.add_argument("login", type=str, required=True, help="Field 'login' required.")
atributos.add_argument("senha", type=str, required=True, help="Field 'senha' required.")

#/usuarios/{user_id}  
class User(Resource):

    #métodos GET, POST, PUT e DELETE
    def get(self, user_id): #visualizar hotel
        user = UserModel.findUser(user_id)
        if user:
            return user.json()
        return {'message': 'User not found.'}, 404 #not found

    @jwt_required
    def delete(self, user_id):
        user = UserModel.findUser(user_id)
        if user:
            try:
                user.deleteUser()
            except:
                return {'message': 'An internal error ocurred trying to delete user.'}, 500 #internal server error
            return {'message': 'User deleted.'}
        return {'message': 'User not found.'}, 404

#/cadastro
class UserRegister(Resource):

    def post(self):
        dados = atributos.parse_args()
        if UserModel.find_by_login(dados["login"]):
            return {"message":"The login '{}' already exists.".format(dados["login"])}
        user = UserModel(**dados)
        user.saveUser()
        return {"message":"User created successfully!"}, 201 #usuário criado
        
        
class UserLogin(Resource):
    
    @classmethod
    def post(cls):
        dados = atributos.parse_args()
        user = UserModel.find_by_login(dados["login"])
        if user and safe_str_cmp(user.senha, dados["senha"]):
            token_acesso = create_access_token(identity=user.user_id)
            return {"access token": token_acesso}, 200
        return {"message": "The username or password is incorrect."}, 401
    
        
