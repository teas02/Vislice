import bottle
import model

SKRIVNOST = 'moja skrivnost'
vislice = model.Vislice()

@bottle.get('/')
def index():
    return bottle.template('index.tpl')

@bottle.post('/nova_igra/')
def nova_igra():
    id_igre = vislice.nova_igra()
    bottle.response.set_cookie("idigre", str(id_igre), path='/', secret=SKRIVNOST)
    bottle.redirect('/igra/')

@bottle.get('/igra/')
def pokazi_igro():
    id_igre = int(bottle.request.get_cookie("idigre", secret= SKRIVNOST))
    igra, stanje = vislice.igre[id_igre]
    return bottle.template('igra.tpl', igra=igra, stanje=stanje)

@bottle.post('/igra/')
def ugibaj():
    id_igre = int(bottle.request.get_cookie("idigre", secret=SKRIVNOST))           #pazi! secret mora biti v get_cookie, ne pa v int!   To zakodira piskotek, da se ne vidi, koliko jih je?
    crka = bottle.request.forms.getunicode('crka')  #tako pogledamo v obrazec v neko polje
    vislice.ugibaj(id_igre, crka)
    bottle.redirect('/igra/')

@bottle.get('/img/<picture>')
def serve_picture(picture):
    return bottle.static_file(picture, root='img')

bottle.run(reloader=True, debug=True)

