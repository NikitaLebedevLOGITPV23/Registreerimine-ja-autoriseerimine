from MyMoodle import *
salasõnad=["Parool.1"]
kasutajanimed=["Kasutaja"]
while True:
    print("1-registreerimine\n2-autoriseerimine\n3-nime või parooli muutmine\n4-unustanud parooli taastamine\n5-lõpetamine")
    vastus=int(input("Sissestage arv "))
    if vastus==1:
        print("Registreerimine")
        kasutajanimed,salasõnad=registreerimine(kasutajanimed,salasõnad)
    elif vastus==2:
        print("Autoriseerimine")
        autoriseerimine(kasutajanimed,salasõnad)
    elif vastus==3:
        print("Nime või parooli muutmine")
    elif vastus==4:
        print("Unustanud parooli taastamine")
    elif vastus==5:
        print("Lõpetamine")
        break
    else:
        print("Tunmatu valik")