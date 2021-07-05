import xmlrpc.client

class ClaseCliente():
    def __init__(self, url, db, username, password):
        self.url = url
        self.db = db
        self.username = username
        self.password = password
    
    def verifUrl (self, url):
        try:
            common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
            version = common.version()
            return (version)
        except:
            return ("No se pudo conectar")
        

    
    