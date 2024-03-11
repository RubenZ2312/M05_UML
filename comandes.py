class Client:
    def __init__(self, id, nom, adreca, telefon, email):
        self.id = id
        self.nom = nom
        self.adreca = adreca
        self.telefon = telefon
        self.email = email
        self.usuaris_web = []
        self.comptes_pagament = []

    def add_usuari_web(self, login, password):
        usuari_web = UsuariWeb(login, password)
        self.usuaris_web.append(usuari_web)

    def add_compte_pagament(self):
        compte_pagament = ComptePagament()
        self.comptes_pagament.append(compte_pagament)


class UsuariWeb:
    def __init__(self, login, password):
        self.id = None
        self.login = login
        self.password = password
        self.estat = "nou"
        self.carros = []

    def nou(self):
        self.estat = "nou"

    def actiu(self):
        self.estat = "actiu"

    def bloquejat(self):
        self.estat = "bloquejat"

    def bannejat(self):
        self.estat = "bannejat"

    def afegir_carro(self, carro):
        self.carros.append(carro)


class Carro:
    def __init__(self):
        self.id = None
        self.linies = []
        self.factura = None

    def afegir_linia_comanda(self, linia_comanda):
        self.linies.append(linia_comanda)


class LiniaComanda:
    def __init__(self, producte, quantitat, preu):
        self.id = None
        self.producte = producte
        self.quantitat = quantitat
        self.preu = preu


class Producte:
    def __init__(self, codi, nom, proveidor):
        self.id = None
        self.codi = codi
        self.nom = nom
        self.proveidor = proveidor


class Factura:
    def __init__(self, codi, adreca_facturacio, data_emisio, data_tancament, pagament):
        self.codi = codi
        self.adreca_facturacio = adreca_facturacio
        self.data_emisio = data_emisio
        self.data_tancament = data_tancament
        self.pagament = pagament


class Pagament:
    def __init__(self, tipus, importe):
        self.tipus = tipus
        self.importe = importe


class OrdreEnviament:
    def __init__(self, data_comanda, data_enviament, destinacio, importe, estat):
        self.data_comanda = data_comanda
        self.data_enviament = data_enviament
        self.destinacio = destinacio
        self.importe = importe
        self.estat = estat


# Exemple d'ús:
client1 = Client(1, "John Doe", "123 Main Street", "555-1234", "john@example.com")
client1.add_usuari_web("john_doe", "password123")
client1.add_compte_pagament()

usuari1 = client1.usuaris_web[0]
carro1 = Carro()
usuari1.afegir_carro(carro1)

producte1 = Producte("P001", "Camisa", "Fashion Supplier")
linia_comanda1 = LiniaComanda(producte1, 2, 25.99)
carro1.afegir_linia_comanda(linia_comanda1)

# I així successivament...
