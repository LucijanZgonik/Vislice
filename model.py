STEVILO_DOVOLJENIH_NAPAK = 10
PRAVILNA_CRKA = '+'
NAPACNA_CRKA = '-'
PONOVLJENA_CRKA = 'o'
ZMAGA = 'W'
PORAZ = 'L'

class Igra:
    def __init__(self,geslo,crke):
        self.geslo = geslo
        self.crke = crke

    def napacne_crke(self):
        nap = ''
        for x in self.crke:
            if x in self.geslo:
                nap = nap
            else:
                nap = nap + x
        self.nap = nap
    
    def pravilne_crke(self):
        prav = ''
        for x in self.crke:
            if x in self.geslo:
                prav = prav + x
            else:
                prav = prav
        self.prav = prav

    def stevilo_napak(self):
        self.st_nap = len(self.nap)

    def zmaga(self):
        if self.prav == self.geslo:
            'W'
        
    def poraz(self):
        if self.st_nap > 9:
            'L'
        
    def pravilni_del_gesla(self):
        pr = ''
        for x in self.geslo:
            if x in self.prav:
                pr = pr + x
            else:
                pr = pr + '_'

    def nepravilni_ugibi(self):
        ne = ''
        for x in self.nap:
            ne = ne + ' '



    

                





