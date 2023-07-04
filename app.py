from flask import Flask
from flask_cors import CORS
from services import Table

app = Flask(__name__)
CORS(app)

@app.route('/Init', methods=['GET'])
def hello():
    return "Hola mundo"

@app.route('/tabla1', methods=['GET'])
def get_data_table_1():
    return Table.table_1()

@app.route('/tabla2', methods=['GET'])
def get_data_table_2():
    return Table.table_2()

if __name__=='__main__':
    app.run()