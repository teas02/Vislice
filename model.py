STEVILO_DOVOLJENIH_NAPAK = 10

PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = 'o'
NAPACNA_CRKA= '-'

ZMAGA= 'W'
PORAZ ='X'
ZACETEK = 'S'

DATOTEKA_Z_BESEDAMI = 'besede.txt'
DATOTEKA_S_STANJEM = 'stanje.json'

class Igra:
    def __init__(self, geslo, crke=None):
        self.geslo = geslo.upper()
        if crke is not None:
            self.crke = crke
        else:
            self.crke = []

    def napacne_crke(self):
        return [crka for crka in self.crke if crka not in self.geslo]

    def pravilne_crke(self):
        return [crka for crka in self.crke if crka in self.geslo]

    def stevilo_napak(self):
        return len(self.napacne_crke())

    def zmaga(self):
        return all([crka in self.crke for crka in self.geslo])

    def poraz(self):
        return self.stevilo_napak() >= STEVILO_DOVOLJENIH_NAPAK

    def pravilni_del_gesla(self):
        niz = ''
        for crka in self.geslo:
            if crka in self.crke:
                niz += crka + ' '
            else:
                niz += '_ '
        return niz

        #''.join([(crka if crka in self.crke else '_') for crka in self.geslo])

    def nepravilni_ugibi(self):
        return ' '.join(self.napacne_crke())

    def ugibaj(self, crka):
        crka = crka.upper()
        if crka in self.crke:
            return PONOVLJENA_CRKA
        else:
            self.crke.append(crka)
            if self.zmaga():
                return ZMAGA
            elif self.poraz():
                return PORAZ
            elif crka in self.geslo:
                return PRAVILNA_CRKA
            else:
                return NAPACNA_CRKA

with open(DATOTEKA_Z_BESEDAMI, encoding='utf8') as d:
    bazen_besed = d.read().split('\n')

bazen_besed = []
with open(DATOTEKA_Z_BESEDAMI, encoding='utf8') as d:
    for beseda in d:
        bazen_besed.append(beseda.strip())

import random
import json

def nova_igra():
    geslo = random.choice(bazen_besed)
    return Igra(geslo)

class Vislice:
    def __init__(self):
        self.igre = {}
        self.datoteka_s_stanjem = DATOTEKA_S_STANJEM
    
    def prost_id_igre(self):
        if len(self.igre) == 0:
            return 0
        else:
            return max(self.igre.keys()) + 1
    
    def nova_igra(self):
        self.nalozi_igre_iz_datoteke()
        id_igre = self.prost_id_igre()
        igra = nova_igra()
        self.igre[id_igre] = (igra, ZACETEK)
        self.zapisi_igre_v_datoteko()
        return id_igre

    def ugibaj(self, id_igre, crka):
        self.nalozi_igre_iz_datoteke()
        igra, _ = self.igre[id_igre]    # ali igra = self.igre[id_igre][0]
        stanje = igra.ugibaj(crka)
        self.igre[id_igre] = (igra, stanje)
        self.zapisi_igre_v_datoteko()

    def zapisi_igre_v_datoteko(self):
        with open(self.datoteka_s_stanjem, 'w', encoding='utf-8') as f:
            igre = {id_igre: (igra.geslo, igra.crke, stanje)                # to je IZPELJAN SEZNAM
                for id_igre, (igra, stanje) in self.igre.items()}           #
            json.dump(igre, f)         # seznam igre zapisujemo v f

    def nalozi_igre_iz_datoteke(self):
        with open(self.datoteka_s_stanjem, 'r', encoding='utf-8') as f:
            igre = json.load(f)   # prebere vse iz datoteke f in shrani v igre
            self.igre = {int(id_igre): (Igra(geslo, crke), stanje)
                    for id_igre, (geslo, crke, stanje) in igre.items()}

    
