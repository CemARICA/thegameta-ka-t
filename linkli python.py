import PySimpleGUI as psg      
import random
psg.theme("LightBlue7")
thegame=["Taş","Kağıt","Makas"]
tas=thegame[0]; kagit=thegame[1]; makas=thegame[2]
print("Taş, Kağıt, Makas oyununa hoş geldiniz.. \n")
def button1():
    bilgisayar = random.choice(thegame)
    if bilgisayar==tas:
            print("Bilgisyar taş seçti: Berabere Kaldın Buda benden Olsun : https://www.youtube.com/watch?v=OaohP-rJMS4")
    elif bilgisayar==kagit:
            print("Bilgisyar kağıt seçti: Kaybettin Cezasını Çek: https://www.youtube.com/watch?v=GDNAzQGzqZc")
    else:
            print("Bilgisyar makas seçti: Tebrikler Kazandın: https://www.youtube.com/watch?v=rdDiWh40QT0")
def button2():
    bilgisayar = random.choice(thegame)
    if bilgisayar==kagit:
            print("Bilgisayar kağıt seçti: Berabere, Nasıl kazanamayız yaa: https://www.youtube.com/watch?v=HB_GnnhNz-8")
    elif bilgisayar==makas:
            print("Bilgisayar makas seçti: Kaybettin: https://www.youtube.com/watch?v=PIwQX7mdGEU")
    else:
            print("Bilgisayar taş seçti: Kazandın: https://www.youtube.com/watch?v=Zuq8w8j235I&list")
def button3():
    bilgisayar = random.choice(thegame)
    if bilgisayar==makas:
            print("Bilgisayar makas seçti: Berabere: https://www.youtube.com/watch?v=KI6AwO7bhJ8")
    elif bilgisayar==tas:
            print("Bilgisayar taş seçti: Kaybettin: https://www.youtube.com/watch?v=ZZIriG4iSX0")
    else:
            print("Bilgisayar kağıt seçti: Kazandın: https://www.youtube.com/watch?v=jPCJIB1f7jk")
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