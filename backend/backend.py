#!/usr/bin/python
import sqlalchemy
from flask import Flask
from flask_jsonpify import jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
# Utility function for the connection to the db
def connect(user, password, db, host='dbpostgres', port=5432):

    url = 'postgresql://{}:{}@{}:{}/{}'
    url = url.format(user, password, host, port, db)

    # The return value of create_engine() is our connection object
    con = sqlalchemy.create_engine(url, client_encoding='utf8')

    # We then bind the connection to MetaData()
    meta = sqlalchemy.MetaData(bind=con, reflect=True)

    return con, meta

# Connect to the db

# While could not connect (because of host not found - which means docker image might not be running yet, sleep 1 second, retry)
connection, metadata = connect('postgres','admin', 'postgres', host='dbpostgres',port=5432)



class User_Name(Resource):
    def get(self, email):
        query = connection.execute("select username from users where email =  \'" + email + "\'")  # This line performs query and returns json result
        return {'username for user with given email': [i[0] for i in query.cursor.fetchall()]}  # Fetches the username for the given email if it exists


class User_Mail(Resource):
    def get(self, user_name):
        query = connection.execute("select email from users where username = \'" + user_name + "\'")
        result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
        return jsonify(result)


class Answer(Resource):
    def get(self):
        return jsonify("nimic inca")



api.add_resource(User_Name, '/users/email/<email>')  # Get the username for a given email address
api.add_resource(User_Mail, '/users/username/<user_name>')  # Get the email address for a given existing user
api.add_resource(Answer, '/answer')  # Get the email address for a given existing user


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')