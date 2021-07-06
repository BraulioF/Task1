from flask import Flask,jsonify
import Components.AutCliente 
import Components.Partner
import xmlrpc.client

url = "http://52.142.63.20:1269"
db = 'fraccion_test'
username = 'WSadnet@adnetworks.cl'
#username = 'Wwww'
password = 'WSadnet@adnetworks.cl'
#password = 'asdasd'

cliente = Components.AutCliente.ClaseCliente(url, db, username, password)
version = cliente.verifUrl()
uid = cliente.AutenticarCliente()

partner = Components.Partner.ClasePartner()
partners_id = partner.ObtenerPartnerID(cliente.url, cliente.db, uid, cliente.password)

if(partners_id == xmlrpc.client.Error):
    error = True
else:
    partners_details = partner.ObtenerPartnerDetalles(cliente.url, cliente.db, uid, cliente.password,partners_id)
    error = False

app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    if(error):
        return ("Usuario o Contraseña Incorrectos")
    else:
        return jsonify({'detalles...': partners_details})

if __name__ == "__main__":
    app.run(debug=True) 