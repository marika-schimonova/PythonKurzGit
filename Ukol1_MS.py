# Tato třída bude obsahovat atributy `jmeno:str`, `druh:str` a `vaha:int`. Všechny parametry jsou povinné a budou se nastavovat v metodě `__init__()`
# Dále přidej třídě `Zvire`:
# * metodu `__str__()`, formát výpisu je na tobě
# * metodu `export_to_dict()`, která vratí reprezentaci zvířete jako slovník, například takto:

class Zvire:
    def __init__(self, jmeno: str, druh: str, vaha: int):
        self.jmeno = jmeno
        self.druh = druh
        self.vaha = vaha
    
    def __str__(self):
        return f'Tohle zvire se jmenuje {self.jmeno}, je to {self.druh} a vazi {self.vaha} kg'

    def export_to_dict(self):
        return(self.__dict__) 

# objekt pavouk 
pavouk = Zvire('Adolf', 'Tarantule Velká', 0.1)
print(pavouk)
pavouk_export = pavouk.export_to_dict()
print(pavouk_export)

# kontrola pavouka
assert pavouk_export['jmeno'] == 'Adolf'
assert pavouk_export['druh'] == 'Tarantule Velká'
assert pavouk_export['vaha'] == 0.1

# objekt zvire
zvire = Zvire('Láďa', 'Koala', 15)
print(zvire)
zvire_export = zvire.export_to_dict()
print(zvire_export) 

assert hasattr(zvire, 'jmeno')
assert hasattr(zvire, 'druh')
assert hasattr(zvire, 'vaha')
assert isinstance(zvire.jmeno, str)
assert isinstance(zvire.druh, str)
assert isinstance(zvire.vaha, int)
assert zvire.export_to_dict() == {'jmeno': 'Láďa', 'druh': 'Koala', 'vaha': 15}


# Vytvoř objekty typu `Zvire` z následujícího seznamu slovníků. Použij for cyklus, můžeš (ale nemusíš) to napsat jako funkci. 
#Výsledkem bude list obsahující 4 objekty typu `Zvire`.
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

# Tato třída bude obsahovat atributy `cele_jmeno:str`, `rocni_plat:int` a `pozice:str`. Všechny parametry jsou povinné a budou se nastavovat v metodě `__init__()`
# Zaměstnanci dále přidej:
# * metodu `__str__()`, formát výpisu je na tobě
# * metodu `ziskej_inicialy()`, která bude vracet výstup ve formátu `A.W.`, uvažuj pouze změstnance se dvěma jmény.
# Vytvoř objekty typu `Zamestnanec` z následujícího seznamu slovníků. Použij for cyklus, můžeš (ale nemusíš) to napsat jako funkci. 
# Výsledkem bude list obsahující 3 objekty typu `Zamestnanec`.

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

# kontrola zamestnanec 
zamestnanec = Zamestnanec('Petr Novak', 50000, 'Programator')
assert hasattr(zamestnanec, 'cele_jmeno')
assert hasattr(zamestnanec, 'rocni_plat')
assert hasattr(zamestnanec, 'pozice')
assert isinstance(zamestnanec.cele_jmeno, str)
assert isinstance(zamestnanec.rocni_plat, int)
assert isinstance(zamestnanec.pozice, str)
assert zamestnanec.ziskej_inicialy() == 'P.N.'

###################################################
# Tato třída bude dědit od třídy `Zamestnanec`, jediné co bude mít navíc je parametr `oblibene_zvire: Zvire`, 
# parametr bude typu `Zvire` (třída kterou jsi už vytvořil/a). Parametr `pozice` rovnou nastav na `'Reditel'`.

class Reditel(Zamestnanec): 
    def __init__(self, cele_jmeno, rocni_plat, zvire, pozice = 'Reditel'):
        super().__init__(cele_jmeno, rocni_plat, pozice)
        self.oblibene_zvire = zvire

# Priklad vytvoreni objektu (klidne zkopiruj)
reditel = Reditel(cele_jmeno= 'Karel', rocni_plat=800_000 , zvire=pavouk)
assert reditel.pozice == 'Reditel'
assert isinstance(reditel.oblibene_zvire, Zvire)
print(reditel)

# kontrola reditel
zvire = Zvire('Lev', 'Lvice', 150)
reditel = Reditel('Jan Novotny', 80000, zvire)
assert isinstance(reditel.oblibene_zvire, Zvire)

class Zoo():
    def __init__(self, nazev: str, adresa: str , reditel: Reditel, zamestnanci: Zamestnanec, zvirata: Zvire ):
          self.nazev = nazev
          self.adresa = adresa
          self.reditel = reditel      
          self.zamestnanci = zamestnanci
          self.zvirata  = zvirata

    def  __str__(self): 
        return f'{self.nazev} je na adrese  {self.adresa} jeji reditel je  {self.reditel.cele_jmeno}, dale tam pracuji {self.zamestnanci} a maji tam napriklad {self.zvirata}'

    vaha_celkem = 0
  # tohle nejde :(  
    def vaha_vsech_zvirat_v_zoo():
        for one in [zvire]: 
            vaha_celkem += one.vaha
            return vaha_celkem
        
# zvire_list = [zvire01, zvire02, zvire03]
# zamestnanec_list = [zamestnanec01, zamestnanec02, zamestnanec03]

zoo = Zoo('Zoo Praha', 'Praha', reditel, [zamestnanec], [zvire])
print(zoo)   
print(zoo.reditel)


# print(zoo.vaha_vsech_zvirat_v_zoo())
# print('Celková váha zvířat v ZOO:', zoo.vaha_vsech_zvirat_v_zoo())
# print('Měsíční náklady na zaměstnance:', zoo.mesicni_naklady_na_zamestnance())

              
# kontrola Zoo class
zoo = Zoo('Zoo Praha', 'Praha', reditel, [zamestnanec], [zvire])
assert hasattr(zoo, 'nazev')
assert hasattr(zoo, 'adresa')
assert hasattr(zoo, 'reditel')
assert hasattr(zoo, 'zamestnanci')
assert hasattr(zoo, 'zvirata')
assert isinstance(zoo.nazev, str)
assert isinstance(zoo.adresa, str)
assert isinstance(zoo.reditel, Reditel)
assert isinstance(zoo.zamestnanci, list)
assert isinstance(zoo.zvirata, list)
# assert zoo.vaha_vsech_zvirat_v_zoo() == 150
# assert zoo.mesicni_naklady_na_zamestnance() == (zamestnanec.rocni_plat + reditel.rocni_plat) / 12




