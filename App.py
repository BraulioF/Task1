from flask import Flask,jsonify
import Components.AutCliente 
import Components.Partner

url = "http://52.142.63.20:1269"
db = 'fraccion_test'
username = 'WSadnet@adnetworks.cl'
password = 'WSadnet@adnetworks.cl'

cliente = Components.AutCliente.ClaseCliente(url, db, username, password)
version = cliente.verifUrl()
uid = cliente.AutenticarCliente()


partner = Components.Partner.ClasePartner()
partners_id = partner.ObtenerPartnerID(cliente.url, cliente.db, uid, cliente.password)
partners_details = partner.ObtenerPartnerDetalles(cliente.url, cliente.db, uid, cliente.password,partners_id)



app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    return jsonify({'detalles...': partners_details})

if __name__ == "__main__":
    app.run(debug=True) 