import xmlrpc.client

class ClaseCliente():
    def __init__(self, url, db, username, password):
        self.url = url
        self.db = db
        self.username = username
        self.password = password
    
    def verifUrl (self):
        try:
            common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(self.url))
            version = common.version()
            return (version)
        except:
            return ("No se pudo conectar")

    def AutenticarCliente (self):
        try:
            common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(self.url))
            uid = common.authenticate(self.db, self.username, self.password, {})
            
            return (uid)
        except:
            return ("No se pudo obtener el uid del usuario")    

    
    