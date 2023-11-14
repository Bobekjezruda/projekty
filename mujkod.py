import random 
from abc import ABC, abstractmethod

class Cokoliv(ABC):
    @abstractmethod
    def rekni_neco(self):
        pass

class Zruda(Cokoliv):
    def __init__(self,jmeno,ATK):
        self.jmeno = jmeno
        self.ATK = ATK
    def rekni_neco(self):
        print(f"{self.jmeno} rika: ziju navdy")
    def __str__(self):
        return f"Jmeno: {self.jmeno}"
class Clovek(Cokoliv):
    
    def __init__(self,jmeno, HP, ATK):
        self.jmeno = jmeno
        self.HP = HP
        self.ATK = ATK   
    def rekni_neco(self):
        print(f"{self.jmeno} rika: umru")
    
    def __str__(self):
        return f"Jmeno: {self.jmeno}"

    
class Rytejr(Clovek):
    
    def __init__(self, jmeno, HP,ATK):
        super().__init__(jmeno, HP, ATK)
    
    def rekni_neco(self):
        super().rekni_neco()
    

class Turnaj():
    def __init__(self):
        self.seznam_rytiru = []
    
    def registrace(self, seznamnabidky):
        self.seznam_rytiru.append(random.choice(seznamnabidky))
        self.seznam_rytiru.append(random.choice(seznamnabidky))

    
    def duel(self):
        rytejr1 = random.choice(self.seznam_rytiru)
        rytejr2 = random.choice(self.seznam_rytiru)
        if rytejr1 == bobek:
            self.seznam_rytiru.remove(rytejr2)
        if rytejr2 == bobek:
            self.seznam_rytiru.remove(rytejr1)
        while rytejr1.HP >= 0 and rytejr2.HP >= 0 and rytejr1 != bobek and rytejr2 != bobek:
            rytejr2.HP -= rytejr1.ATK
            rytejr1.HP -= rytejr2.ATK
            self.seznam_rytiru.remove(rytejr1)
        else:
            self.seznam_rytiru.remove(rytejr2)

turnaj = Turnaj()
guts = Rytejr("Guts",50000000000000000,50000000000000000)
griffith = Rytejr("Griffith",5,5)
Random = Rytejr("random",random.randint(0,50000000000000000),random.randint(0,50000000000000000))
pepa = Clovek("Pepa", 45000,0)
pepa.rekni_neco()
bobek = Zruda("Bobek",3500)
bobek.rekni_neco()
guts.rekni_neco()
griffith.rekni_neco()
turnaj.duel()
print(turnaj.seznam_rytiru[0])

seznamnabidky = [guts,griffith,bobek,pepa]
