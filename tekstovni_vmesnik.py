import model

def izpis_igre(igra):
    niz = f"""{igra.pravilni_del_gesla()}
Nepravilni ugibi: {igra.nepravilni_ugibi()}
Napačno lahko ugibaš še {model.STEVILO_DOVOLJENIH_NAPAK - igra.stevilo_napak()}-krat."""
    return niz

def izpis_zmage(igra):
    niz = f"čestitke! Pravilno ste uganili geslo {igra.geslo}!"
    return niz

def izpis_poraza(igra):
    niz = f"Več sreče prihodnjič! Pravilno geslo je bilo {igra.geslo}!"
    return niz

def zahtevaj_vnos():
    return input("Ugibaj črko: ")

def pozeni_vmesnik():
    igra = model.nova_igra()
    while not igra.zmaga() and not igra.poraz():
        print(izpis_igre(igra))
        crka = zahtevaj_vnos()
        while len(crka) != 1 or not crka.isalpha():
            crka = zahtevaj_vnos()
        stanje = igra.ugibaj(crka)
    if igra.zmaga():
        print(izpis_zmage(igra))

    else:
        print(izpis_poraza(igra))
    
    odlocitev = input("Bi želeli igrati ponovno? (D/N): ")
    if odlocitev == "D":
        pozeni_vmesnik()


pozeni_vmesnik()