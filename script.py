from types import MethodDescriptorType
from sympy.logic import *
from sympy import symbols
from flask import *
from flask_cors import CORS

api = Flask(__name__)
CORS(api)

@api.route("/")
def index():
    return 'server works'

@api.route("/api/simplify", methods=['GET', 'POST'])
def simplify():
    json_data = request.get_json()
    vars = json_data['vars']
    sym = [symbols(l) for l in vars]
    minterms = [int(i) for i in json_data['minterms']]
    print(minterms) 
    simp = SOPform(sym, minterms, [])
    return jsonify({"simplified": str(simp) if simp else 0})

if __name__ == '__main__':
    api.run(debug=True)