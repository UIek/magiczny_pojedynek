from time import sleep
from random import randint
print("MAGICZNY POJEDYNEK")
print(50*"-")
#-----------------------------------BOHATER
sleep(1.5)
imie = input("Podaj imię: ").capitalize()
print(f"WITAJ {imie}")
sleep(2)
print(50* " ")
print("Wybierz postać:")
sleep(1)
print("a - WRÓŻKA (+20 HP)")
print("b - CZARODZIEJ (+20 MOCY)")
print("c - RYCERZ (+20 ATAK)")
sleep(2)
print(50* " ")
wybor = input("Podaj wybór: ").lower()
if wybor == "a":
    bohater ={
        'hp':120,
        'atak':50,
        'moc':100}
elif wybor == "b":
    bohater ={
        'hp':100,
        'atak':50,
        'moc':120}
elif wybor == "c":
    bohater ={
        'hp':100,
        'atak':70,
        'moc':100}
else:
    print("ZŁY WYBÓR")
    print('Jesteś zwykłym człowiekiem szukającym przygód.')
    bohater = {
        'hp':100,
        'atak':50,
        'moc':100
    }
for k,v in bohater.items():
    print(f"{k} --- {v}")
    print(50*'-')
#-----------------------------------PRZECIWNIK
wielka_stopa = {
    "nazwa":"wielka stopa",
    "hp":50,
    "atak":15,
    "występowanie":"mroczny las"
}
syrena = {
    "nazwa":"syrena",
    "hp":20,
    "atak":41,
    "występoanie":"brzeg morza"}
smok = {
    "nazwa":"smok",
    "hp":100,
    "atak":50,
    "występowanie":"jaskinia smoka"}
chochlik = {
    "nazwa":"chochlik",
    "hp":10,
    "atak":15,
    "występowanie":"twoja droga"}
cyklop = {
    "nazwa":"cyklop",
    "hp":7,
    "atak":31,
    "występowanie":"bezludna wyspa"}
nimfa_wodna = {
    "nazwa":"nimfa_wodna",
    "hp":3,
    "atak":59,
    "występowanie":"Jezioro Smutku"}
wampir = { 
    "nazwa":"wampir",
    "hp":50,
    "atak":69,
    "występowanie":"Opuszczony Zamek"}
wilkolak = {
    "nazwa":"wilkołak",
    "hp":32,
    "atak":74,
    "występowanie":"Mroczny las"}
#----------------------------------------DROGI
def pustynia():
    print("Wchodzisz na pustynie.")
    print("Napotkałeś drogę pełną kaktusów,")
    print("przeprawiwając się przez nią tracisz 20 Hp.")
    bohater['hp'] -= 20
    print(f"Zostało Ci {bohater['hp']} Hp")

def mroczny_las():
    print("Wchodzisz do morocznego lasu,")
    print("na swojej drodze spotykasz wielką stopę.")

def mroczny_las_2():
    print("Wchodzisz do morocznego lasu,")
    print("na swojej drodze spotykasz wilkołaka.")

def brzeg_morza():
    print("Dochodisz do brzegu morza,")
    print("spostrzegasz pięką syrene.")
    print("Atakuje Cię niespodziewanie zabierając 41 Hp.")
    bohater['hp'] -= 41
    print(f"Zostaje Ci {bohater['hp']} Hp.")

def jaskinia_smoka():
    print("Wchodzisz do ogromniej, ciemnej jaskini.")
    print("Spostrzegasz potężnego smoka.")

def jezioro_smutku():
    print("Zatrzymujesz się przy jeziorze i nagle spod wody wypływa nimfa wodna.")

def opuszczony_zamek():
    print("Widzisz opuszczony zamek i postanawiasz poszukać w nim skarbów.")
    print("Gdy wchodzisz, nagle zaczyna grać upiorna muzyka,") 
    print("a nietoperz wiszący na suficie zmienia się w żądnego krwii wampira.")
    print("W ten sposób zaczyna się walka o twoje życie...")

def bezludna_wyspa():
    print("Postanawiasz wypłynąć w poszukiwaniu przygód, nagle dostrzegasz bezludnom wyspe.")
    print("Gdy dopływasz do brzegu atakuje Cię cyklop.")
#-----------------------------------------------------------------CHOCHLIK, JEDNOROŻEC, ELIKSIR, SFINKS
def chochlik():
    print('Złośliwy chochlik wyskoczył Ci na droge, aby uprzykrzyć Ci życie')
    print('Osłabił twój atak o 15.')
    print('Na szczęście okazał się dobrym chochlikiem i podarował Ci 5 hp.')
    bohater['atak'] -= 15
    bohater['hp'] += 5
    print(f"masz teraz {bohater['atak']} ataku i {bohater['hp']} hp")
def jednorozec():
    print('Na twojej drodze pojawił się jednorożec.')
    print('Postanowił Ci oddać połowe swojego życia, abyś mógł dalej walczyć ze złem.')
    bohater['hp'] += 45
    print(f"Teraz masz {bohater['hp']} hp.")
def eliksir():
    print("W posiadłości wampira znalazłeś magiczny eliksir.")
    bohater['atak'] += 18
    print("Po wypiciiu zyskałeś 18 ataku.")
    print(f"Teraz masz {bohater['atak']} ataku.")
def sfinks():
    zmienna = randint(0, 10)
    print("Spotykasz Sfinksa i zadaje Ci pytanie")
    print(pytania[zmienna])
    odp1 = input("Podaj odpowiedź: ")
    if  odp1 == odpowiedzi[zmienna]:
        print("WYGRAŁEŚ !!!")
        print("Opowiedziałeś poprawnie i tym sposobem pokonałeś Sfinksa. ")
        print("On w ramach rozpaczy skoczył w przepać")
    elif odp1 != odpowiedzi[zmienna]:
        print ("Sfinks zrzuca Cię w przepaść!!!")
        print ("GAME OVER !!!")

#--------------------------------------------RUNDA 1
i = 0 
if bohater['hp'] > 0:
    print('Dochodzisz do rozstaju dróg, co wybierasz?')
    print('a - brzeg morza')
    print('b - Mroczny Las')
    droga = input("Gdzie idziesz? ")
    if droga == "a":
        brzeg_morza()
        while syrena['hp'] > 0:
            print("Co robisz? ")
            print('a - normaly atak')
            print('b - super atak')
            atak = input()
            if atak == 'a':
                syrena['hp'] -= bohater['atak']
            elif atak == 'b':
                if bohater['moc'] >= 10:
                    syrena['hp'] -= bohater['atak']*2
                    bohater['moc'] -= 10
                else:
                    print('Nie masz już sił, aby wykonać super atak.')
            bohater['hp'] -= syrena['atak']
            if bohater['hp'] > 0:
                print(f"Zostało ci {bohater['hp']} hp i {bohater['moc']} mocy")
                print('POKONAŁEŚ SYRENE!!!!!!!!')
            else:
                print('ZOSTAŁEŚ POKONANY PRZEZ SYRENE!!!!')
    if droga == "b":
        mroczny_las_2()
        while wilkolak['hp'] > 0:
            print("Co robisz? ")
            print('a - normaly atak')
            print('b - super atak')
            atak = input()
            if atak == 'a':
                wilkolak['hp'] -= bohater['atak']
            elif atak == 'b':
                if bohater['moc'] >= 10:
                    wilkolak['hp'] -= bohater['atak']*2
                    bohater['moc'] -= 10
                else:
                    print('Nie masz już sił, aby wykonać super atak.')
            bohater['hp'] -= wilkolak['atak']
            if bohater['hp'] > 0:
                print(f"Zostało ci {bohater['hp']} hp i {bohater['moc']} mocy.")
                print('POKONAŁEŚ WILKOŁAKA!!!!!!!!')
            else:
                print('ZOSTAŁEŚ POKONANY PRZEZ WILOŁAKA!!!!')
if bohater['hp'] >= 10 and i == 0:
    jednorozec()
    i += 1
#----------------------------------------------------------RUNDA 2
if bohater['hp'] > 0:
    print('Dochodzisz do rozstaju dróg, co wybierasz?')
    print('a - Mroczny Las')
    print('b - Jezioro Smutku')
    droga = input("Gdzie idziesz? ")
    if droga == "a":
        mroczny_las()
        while wielka_stopa['hp'] > 0:
            print("Co robisz? ")
            print('a - normaly atak')
            print('b - super atak')
            atak = input()
            if atak == 'a':
                wielka_stopa['hp'] -= bohater['atak']
            elif atak == 'b':
                if bohater['moc'] >= 10:
                    wielka_stopa['hp'] -= bohater['atak']*2
                    bohater['moc'] -= 10
                else:
                    print('Nie masz już sił, aby wykonać super atak.')
            bohater['hp'] -= wielka_stopa['atak']
            if bohater['hp'] > 0:
                print(f"Zostało ci {bohater['hp']} hp i {bohater['moc']} mocy.")
                print('POKONAŁEŚ WIELKĄ STOPĘ!!!!!!!!')
            else:
                print('ZOSTAŁEŚ POKONANY PRZEZ WIELKĄ STOPĘ!!!!')
    if droga == "b":
        jezioro_smutku()
        while nimfa_wodna['hp'] > 0:
            print("Co robisz? ")
            print('a - normaly atak')
            print('b - super atak')
            atak = input()
            if atak == 'a':
                nimfa_wodna['hp'] -= bohater['atak']
            elif atak == 'b':
                if bohater['moc'] >= 10:
                    nimfa_wodna['hp'] -= bohater['atak']*2
                    bohater['moc'] -= 10
                else:
                    print('Nie masz już sił, aby wykonać super atak.')
            bohater['hp'] -= nimfa_wodna['atak']
            if bohater['hp'] > 0:
                print(f"zostało ci {bohater['hp']} hp i {bohater['moc']} mocy")
                print('POKONAŁEŚ NIMFE WODNĄ!!!!!!!!')
            else:
                print('ZOSTAŁEŚ POKONANY PRZEZ NIMFE WODNĄ!!!')
if bohater['hp'] >= 10 and i == 0:
    jednorozec()
    i += 1
#-----------------------------------------------------------------RUNDA 3
if bohater['hp'] > 0:
    chochlik()
if bohater['hp'] > 0:
    print('Dochodzisz do rozstaju dróg, co wybierasz?')
    print('a - Opuszcony Zamek')
    print('b - Bezludna Wyspa')
    droga = input("Gdzie idziesz? ")
    if droga == "a":
        opuszczony_zamek()
        while wampir['hp'] > 0:
            print("Co robisz? ")
            print('a - normaly atak')
            print('b - super atak')
            atak = input()
            if atak == 'a':
                wampir['hp'] -= bohater['atak']
            elif atak == 'b':
                if bohater['moc'] >= 10:
                    wampir['hp'] -= bohater['atak']*2
                    bohater['moc'] -= 10
                else:
                    print('Nie masz już sił, aby wykonać super atak.')
            bohater['hp'] -= wampir['atak']
            if bohater['hp'] > 0:
                print(f"Zostało ci {bohater['hp']} hp i {bohater['moc']} mocy.")
                print('POKONAŁEŚ WAMPIRA!!!!!!!!')
                eliksir()
            else:
                print('ZOSTAŁEŚ POKONANY PRZEZ WAMPIRA!!!!')
    if droga == "b":
        bezludna_wyspa()
        while cyklop['hp'] > 0:
            print("Co robisz? ")
            print('a - normaly atak')
            print('b - super atak')
            atak = input()
            if atak == 'a':
                cyklop['hp'] -= bohater['atak']
            elif atak == 'b':
                if bohater['moc'] >= 10:
                    cyklop['hp'] -= bohater['atak']*2
                    bohater['moc'] -= 10
                else:
                    print('Nie masz już sił, aby wykonać super atak.')
            bohater['hp'] -= cyklop['atak']
            if bohater['hp'] > 0:
                print(f"Zostało ci {bohater['hp']} hp i {bohater['moc']} mocy.")
                print('POKONAŁEŚ CYKLOPA!!!!!!!!')
            else:
                print('ZOSTAŁEŚ POKONANY PRZEZ CYKLOPA!!!!')
if bohater['hp'] >= 10 and i == 0:
    jednorozec()
    i += 1
#--------------------------------------------------------------RUNDA 4
if bohater['hp'] > 0: 
    print('Dochodzisz do rozstaju dróg, co wybierasz?')
    print('a - pustynia')
    print('b - jaskinia smoka')
    droga = input("Gdzie idziesz? ")
    if droga == "a":
        pustynia()
    if droga == "b":
        jaskinia_smoka()
        while smok['hp'] > 0:
            print("Co robisz? ")
            print('a - normaly atak')
            print('b - super atak')
            atak = input()
            if atak == 'a':
                smok['hp'] -= bohater['atak']
            elif atak == 'b':
                if bohater['moc'] >= 10:
                    smok['hp'] -= bohater['atak']*2
                    bohater['moc'] -= 10
                else:
                    print('Nie masz już sił, aby wykonać super atak.')
            bohater['hp'] -= smok['atak']
            if bohater['hp'] > 0:
                print(f"Zostało Ci {bohater['hp']} hp i {bohater['moc']} mocy.")
                print('POKONAŁEŚ SMOKA!!!!!!!!')
            else:
                print('ZOSTAŁEŚ POKONANY PRZEZ SMOKA!!!!')
if bohater['hp'] >= 10 and i == 0:
    jednorozec()
    i += 1
if bohater['hp'] > 0:
    print('YOU LOST!!!!!!')
#-----------------------------------------------------------------ZAGADKI 
pytania = [
    "Choć jest duże to nigdy nie rośnie, ma korzenie...",
    "Gniazdo moje szarobure siecią jest spowite...",
    "Jedni oszukują, inni się chowają, lecz zawsze w końcu mnie spotykają",
    "Jestem lekki, jak wiatr, niewiększy od kciuka",
    "Jestem żywy, ale nie oddycham...",
    "Co zawsze jest stare, czasami nowe, nigdy smutne, czasem błękitne...",
    "Po zmroku przychodzą, choć się ich nie wzywa...",
    "Nigdy nie odpoczywa, nigdy nie stoi, porusza się chicho od wzgórza do wzgórza...",
    "Co może przywołać zmarłych, wywołać łzy....",
    "Co może biec, ale nigdy nie chodzi...",
    "Wchodzisz jednym wyjsciem, wychodzisz dwoma, ale dopiero, kiedy wyjdziesz jesteś naprawde w środku..."
]
odpowiedzi = [
    "góra",
    "pająk",
    "śmierć",
    "koliber",
    "ryba",
    "księżyc",
    "gwiazdy",
    "słońce",
    "wspomnienia",
    "rzeka",
    "spodnie"]

if bohater['hp'] > 0:
    sfinks()

    


            





