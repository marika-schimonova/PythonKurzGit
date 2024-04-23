class Zvire:
    def __init__(self, jmeno: str, druh: str, vaha: int):
        self.jmeno = jmeno
        self.druh = druh
        self.vaha = vaha
    
    def __str__(self):
        return f'Tohle zvire se jmenuje {self.jmeno}, je to {self.druh} a vazi {self.vaha} kg'

    def export_to_dict(self):
            x = []
            x.append(self.jmeno)
            x.append(self.druh)
            x.append(self.vaha)
            return x
    
pavouk = Zvire('Adolf', 'Tarantule Velká', 0.1)


print(pavouk)
print(pavouk.export_to_dict())

pavouk_export = pavouk.export_to_dict()

# kontrola 
assert pavouk_export[0] == 'Adolf'
assert pavouk_export[1] == 'Tarantule Velká'
assert pavouk_export[2] == 0.1

zvirata_dict = [
    {'jmeno': 'Růženka', 'druh': 'Panda Velká', 'vaha': 150},
    {'jmeno': 'Vilda', 'druh': 'Vydra Mořská', 'vaha': 20},
    {'jmeno': 'Matýsek', 'druh': 'Tygr Sumaterský', 'vaha': 300},
    {'jmeno': 'Karlík', 'druh': 'Lední medvěd', 'vaha': 700},
]

zvire01 = Zvire(zvirata_dict[0].get('jmeno'), zvirata_dict[0].get('druh'), zvirata_dict[0].get('vaha'))
zvire02 = Zvire(zvirata_dict[1].get('jmeno'), zvirata_dict[1].get('druh'), zvirata_dict[1].get('vaha'))
zvire03 = Zvire(zvirata_dict[2].get('jmeno'), zvirata_dict[2].get('druh'), zvirata_dict[2].get('vaha'))
zvire04 = Zvire(zvirata_dict[3].get('jmeno'), zvirata_dict[3].get('druh'), zvirata_dict[3].get('vaha'))

print(zvire01)
print(zvire02)
print(zvire03)
print(zvire04)

###########################################################



class Zamestnanec: 
    def __init__(self, cele_jmeno: str, rocni_plat: int, pozice: str):
          self.cele_jmeno   = cele_jmeno
          self.rocni_plat   = rocni_plat
          self.pozice       = pozice

    def __str__(self): 
        return f'Tohle je {self.cele_jmeno}, pracuje na pozici {self.pozice} a rocne vydelava {self.rocni_plat} Kc.'
    
    def ziskej_inicialy(self):
        split_cele_jmeno = self.cele_jmeno.split(' ')
        initialy = split_cele_jmeno[0][0] + '.' +split_cele_jmeno[1][0] + '.'
        # z = split_name[1][0]
        return initialy


zamestnanci_dict = [
    {'cele_jmeno': 'Tereza Vysoka', 'rocni_plat': 700_000, 'pozice': 'Cvičitelka tygrů'},
    {'cele_jmeno': 'Anet Krasna', 'rocni_plat': 600_000, 'pozice': 'Cvičitelka vyder'},
    {'cele_jmeno': 'Martin Veliky', 'rocni_plat': 650_000, 'pozice': 'Cvičitel ledních medvědů'},
]

zamestnanec01 = Zamestnanec(zamestnanci_dict[0].get('cele_jmeno'), zamestnanci_dict[0].get('rocni_plat'), zamestnanci_dict[0].get('pozice'))
zamestnanec02 = Zamestnanec(zamestnanci_dict[1].get('cele_jmeno'), zamestnanci_dict[1].get('rocni_plat'), zamestnanci_dict[1].get('pozice'))
zamestnanec03 = Zamestnanec(zamestnanci_dict[2].get('cele_jmeno'), zamestnanci_dict[2].get('rocni_plat'), zamestnanci_dict[2].get('pozice'))

print(zamestnanec01)
print(zamestnanec02)
print(zamestnanec03)

print(zamestnanec01.ziskej_inicialy())

###################################################


class Reditel(Zamestnanec): 
    def __init__(self, cele_jmeno: str, rocni_plat: int, pozice: str , oblibene_zvire: str ):
        super().__init__(cele_jmeno, rocni_plat, pozice)
        self.pozice = 'reditel'
        self.oblibene_zvire = oblibene_zvire

# Priklad vytvoreni objektu (klidne zkopiruj)
zvire = Zvire()
reditel = Reditel(jmeno='Karel', rocni_plat=800_000, oblibene_zvire=zvire)
assert reditel.pozice == 'Reditel'
assert isinstance(reditel.oblibene_zvire, Zvire)
