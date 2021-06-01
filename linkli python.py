import PySimpleGUI as psg      
import random
psg.theme("LightBlue7")
thegame=["Taş","Kağıt","Makas"]
tas=thegame[0]; kagit=thegame[1]; makas=thegame[2]
print("Taş, Kağıt, Makas oyununa hoş geldiniz.. \n")
def button1():
    bilgisayar = random.choice(thegame)
    if bilgisayar==tas:
            print("Bilgisyar taş seçti: Berabere")
    elif bilgisayar==kagit:
            print("Bilgisyar kağıt seçti: Kaybettin")
    else:
            print("Bilgisyar makas seçti: Kazandın")
def button2():
    bilgisayar = random.choice(thegame)
    if bilgisayar==kagit:
            print("Bilgisayar kağıt seçti: Berabere")
    elif bilgisayar==makas:
            print("Bilgisayar makas seçti: Kaybettin")
    else:
            print("Bilgisayar taş seçti: Kazandın")
def button3():
    bilgisayar = random.choice(thegame)
    if bilgisayar==makas:
            print("Bilgisayar makas seçti: Berabere")
    elif bilgisayar==tas:
            print("Bilgisayar taş seçti: Kaybettin")
    else:
            print("Bilgisayar kağıt seçti: Kazandın")
dispatch_dictioanary = { "Taş": button1, "Kağıt": button2, "Makas": button3 }
layout = [ [psg.Button("Taş"), psg.Button("Kağıt"), psg.Button("Makas"), psg.Quit()] ]
window = psg.Window("forTeam", layout, size=(250,150))
while True:
    event, values = window.read()
    if event in (None, "Quit"):
        break        
    if event in dispatch_dictioanary:
        func_to_call = dispatch_dictioanary[event]
        func_to_call()        
    else:
        print("Hata! \n-----".format(event))
window.close()
