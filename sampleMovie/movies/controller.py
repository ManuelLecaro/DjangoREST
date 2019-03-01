from zeep import Client
from zeep import xsd

class TipoPlan:
    #id = 1
    nombre =''
    costo = 0.0
    def __init__(self, nombre, costo):
        #self.id = id
        self.nombre = nombre
        self.costo = costo
    def comoArreglo(self):
        return {
            #'id':str(self.id),
            'nombre':self.nombre,
            'costo':self.costo,
            }
    def __str__(self):
        return  "nombre: "+self.nombre+", costo:"+ self.costo


'''class Controller:
    wsdl = 'http://127.0.0.1:8000/soap_service/?WSDL'
    client = Client(wsdl)
    #value = zeep.xsd.AnyObject(zeep.xsd.String(), "my string value")

    def listar(self):  
        listaPlanes = []  
        lista = self.client.service.tomarplanes()
        lista = lista.split(",")
        for i in lista:
            valores = i.split(":")
            persona = TipoPlan(valores[0],int(valores[1]))
            listaPlanes.append(persona)
        return listaPlanes'''