STEVILO_DOVOLJENIH_NAPAK = 10
PRAVILNA_CRKA = '+'
NAPACNA_CRKA = '-'
PONOVLJENA_CRKA = 'o'
ZMAGA = 'W'
PORAZ = 'L'

class Igra:
    def __init__(self,geslo,crke=None):
        self.geslo = geslo
        if crke is None:
            self.crke = []
        else:
            self.crke = [c.lower() for c in crke]
        

    def napacne_crke(self):
        nap = ''
        for x in self.crke:
            if x in self.geslo:
                nap = nap
            else:
                nap = nap + x
        return nap
    
    def pravilne_crke(self):
        prav = ''
        for x in self.crke:
            if x in self.geslo:
                prav = prav + x
            else:
                prav = prav
        return prav

    def stevilo_napak(self):
        return len(self.napacne_crke())


    def zmaga(self):
        for c in self.geslo:
            if c not in self.crke:
                return False
            else:
                return True
    
    def poraz(self):
        return self.stevilo_napak() > STEVILO_DOVOLJENIH_NAPAK
        
    def pravilni_del_gesla(self):
        pr = ''
        for x in self.geslo:
            if x in self.crke:
                pr = pr + x
            else:
                pr = pr + '_'
        return pr

    def nepravilni_ugibi(self):
        return " ".join(self.napacne_crke())
        
    def ugibaj(self,crka):
        crka = crka.lower()
        if crka in self.crke:
            return PONOVLJENA_CRKA

        self.crke.append(crka)
        
        if crka in self.geslo:
            if self.zmaga():
                return ZMAGA
            else:
                return PRAVILNA_CRKA
        else:
            if self.poraz():
                return PORAZ
            else:
                return NAPACNA_CRKA
                

bazen_besed = []
with open ("Vislice/besede.txt") as datoteka_bazena:
    for beseda in datoteka_bazena:
        bazen_besed.append(beseda.strip().lower())

import random

def nova_igra():
    nakljucna_beseda = random.choice(bazen_besed)
    return Igra(nakljucna_beseda)






    

                





