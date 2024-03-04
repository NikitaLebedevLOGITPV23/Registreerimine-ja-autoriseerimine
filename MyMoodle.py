from string import *
from time import sleep
def registreerimine(kasutajad:list,paroolid:list)->any:
    """Funktsioon tagastab 2 listid
    :param list kasutaja: Kasutaja nimede kirjeldus
    :param list paroolid: Kasutaja nimed paroolid
    :rtype: list,list
    """
    while True:
        nimi=input("Mis on sinu nimi on? ")
        if nimi not in kasutajad:
            while True:
                parool=input("Mis on sinu parool? ")
                flag_p=False
                flag_l=False 
                flag_u=False 
                flag_d=False 
                if len(parool)>8:
                    parool_list=list(parool)
                    for p in parool_list:
                        if p in punctuation:
                            flag_p=True 
                        elif p in ascii_lowercase:
                            flag_l=True 
                        elif p in ascii_uppercase:
                            flag_u=True
                        elif p in digits:
                            flag_d=True
                    if flag_p and flag_u and flag_l and flag_d:
                        kasutajad.append(nimi)
                        paroolid.append(parool)
                        break
                    else:
                        print("Nõrk salasõna!")
                break
            else:
                print("Selline kasutaja on juba olemasi! ")
        return kasutajad, paroolid
def autoriseerimine(kasutajad:list,paroolid:list):
    """Funktsioon kuvab ekraanile "Tere tulemas! kui kasutaja on olemas nimekirjas
    Niki on järjendis kasutajad
    Salasõna on paroolide järjendis
    Nimi ja salasõna indeksid on võrdsed
    :param list kasutajad: Kasutaja nimede kirjeldus
    :param list paroolid: Kasutaja nimed paroolid
    """
    p=0
    while True:
        nimi=input("Sisesta kasutajanimi: ")
        parool=input("Sesesta salasõna: ")
        p+=1
        if nimi in kasutajad and parool in paroolid:
            if kasutajad.index(nimi)==paroolid.index(parool):
                print(f"Tere tulemast! {nimi}")
                break
            else:
                print("Vale nimi või salassõna!")
                if p==5:
                    print("Proovi uuesti 10 sek pärast")
                    for i in range(10):
                        sleep(1)
                        print(f"On jäänud {10-i} sek")
        else:
            print("Kasutajat poke")