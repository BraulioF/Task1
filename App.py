from flask import Flask,jsonify
import Components.AutCliente 

cliente = Components.AutCliente.ClaseCliente("http://52.142.63.20:1269", 'fraccion_test', 'WSadnet@adnetworks.cl', 'WSadnet@adnetworks.cl')
version = cliente.verifUrl("http://52.142.63.20:1269")
##url = "http://52.142.63.20:1269"
##db = 'fraccion_test'
##username = 'WSadnet@adnetworks.cl'
##password = 'WSadnet@adnetworks.cl'

#import xmlrpc.client

#common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
#version = common.version()

print("aaaaaaaaaaaaaaaaa", version)
##uid = common.authenticate(db, username, password, {})
##models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

#partners_id = models.execute_kw(db, uid, password,
#    'res.partner', 'search',
#    [[['is_company', '=', True],['customer','=',True]]])


#parners_details = models.execute_kw(db, uid, password,
#    'res.partner', 'read', [partners_id])
# count the number of fields fetched by default
#len(parners_details)


app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    return jsonify({'detalles...': version})

if __name__ == "__main__":
    app.run(debug=True) 