class Zvire:
    """Vytvori zvire s danymi vlastnostmi."""

    def __init__(self, jmeno, zvuk):
        self.jmeno = jmeno
        self.zvuk = zvuk
        sel.pozice = None

    
    def slysi_na(self, jmeno):
        """Slysi zvire na dane jmeno?"""
        if self.pozice!= "doma":
            return False
        return self.jmeno == jmeno or \
                jmeno == "Potvurka"

    def ozvi_se(self):
        """Vyda zvuk daneho zvirete."""
        print(self.jmeno, "rika:", self.zvuk)

    def __str__(self):
        return self.jmeno

    def __repr__(self):
        return f"Zvire({self.jmeno}, {self.zvuk})"

    def __eq__(self, other):
        return self.jmeno == other.jmeno and \
               self.zvuk == other.zvuk
     
    

class Kocka(Zvire):
    """Vytvori kocku s danymi vlastnostmi."""

    def __init__(self, jmeno, zvuk):
        Zvire.__init__(self, jmeno, zvuk)
        self.pocet_zivotu = 9

    def slysi_na(self, jmeno):
        # Copak kocka slysi na jmeno?
        return False
class Pes(Zvire)
    def __init__ (self, jmeno):
        Zvire:__init__(self, jmeno, "Haf")
        self. zavrcel = False
    def ozvi_se(self):
        if self.zavrcel:
            print ("Haf")
            self.zavrcel = False
        else:
            print("Vrrr")
            self.zavrcel = True
    
          
