from flask import Flask,jsonify
import Components.AutCliente 
import Components.Partner

url = "http://52.142.63.20:1269"
db = 'fraccion_test'
username = 'WSadnet@adnetworks.cl'
#username = 'Wwww'
password = 'WSadnet@adnetworks.cl'
#password = 'asdasd'

cliente = Components.AutCliente.ClaseCliente(url, db, username, password)
version = cliente.verifUrl()
uid = cliente.AutenticarCliente()

if(uid!= False):
    partner = Components.Partner.ClasePartner()
    partners_id = partner.ObtenerPartnerID(cliente.url, cliente.db, uid, cliente.password)
    partner_details = partner.ObtenerPartnerDetalles(cliente.url, cliente.db, uid, cliente.password,partners_id)
    error = False
else:
    print("Usuario o contraseña errados")
    error = True

app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
        if(error):
            return "Error Usuario o contraseña incorrectos"
        else:
            return jsonify({'detalles...': partner_details})

if __name__ == "__main__":
    app.run(debug=True) 