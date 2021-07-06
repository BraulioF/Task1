import xmlrpc.client
class ClasePartner():

    def ObtenerPartnerID (self, url, db, uid, password):
        models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
        partners_id = models.execute_kw(db, uid, password,
                    'res.partner', 'search',
                    [[['is_company', '=', True],['customer','=',True]]])
        return partners_id

    def ObtenerPartnerDetalles (self, url, db, uid, password,partners_id):
        models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
        parners_details = models.execute_kw(db, uid, password,
                        'res.partner', 'read', [partners_id])
        return parners_details 
