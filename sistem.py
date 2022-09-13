import re
import os
import time

tablo = open("Donemodevi2/Hizmetler.txt", "r")
tl_adet = re.split('[,]', tablo.readline())
kopukleme_hizmeti = re.split('[,TL]', tablo.readline())
yikama_hizmeti = re.split('[,TL]', tablo.readline())
kurulama_hizmeti = re.split('[,TL]', tablo.readline())
cilalama_hizmeti = re.split('[,TL]', tablo.readline())

tl_adet = {"beslira_adet" : int(tl_adet[0]),
           "onlira_adet" : int(tl_adet[1]),
           "yirmilira_adet" : int(tl_adet[2]),
           "ellilira_adet" : int(tl_adet[3]),
           "yuzlira_adet" : int(tl_adet[4])}

kopukleme_hizmeti = {"HizmetID" : int(kopukleme_hizmeti[0]),
                     "HizmetAd" : kopukleme_hizmeti[1],
                     "HizmetAdet" : int(kopukleme_hizmeti[2]),
                     "HizmetFiyat" : int(kopukleme_hizmeti[3])} 

yikama_hizmeti = {"HizmetID" : int(yikama_hizmeti[0]),
                     "HizmetAd" : yikama_hizmeti[1],
                     "HizmetAdet" : int(yikama_hizmeti[2]),
                     "HizmetFiyat" : int(yikama_hizmeti[3])}

kurulama_hizmeti = {"HizmetID" : int(kurulama_hizmeti[0]),
                     "HizmetAd" : kurulama_hizmeti[1],
                     "HizmetAdet" : int(kurulama_hizmeti[2]),
                     "HizmetFiyat" : int(kurulama_hizmeti[3])}

cilalama_hizmeti = {"HizmetID" : int(cilalama_hizmeti[0]),
                     "HizmetAd" : cilalama_hizmeti[1],
                     "HizmetAdet" : int(cilalama_hizmeti[2]),
                     "HizmetFiyat" : int(cilalama_hizmeti[3])}

kasa = tl_adet["yuzlira_adet"]*100 + tl_adet["ellilira_adet"]*50 + tl_adet["yirmilira_adet"]*20 + tl_adet["onlira_adet"]*10 + tl_adet["beslira_adet"]*5
girilen_para = 0
hizmet_bedeli = 0
para_ustu = 0

def para_girisi():
    global girilen_para
    while True:
        print(kopukleme_hizmeti["HizmetID"], ")", kopukleme_hizmeti["HizmetAd"], "-", kopukleme_hizmeti["HizmetFiyat"],"TL")
        print(yikama_hizmeti["HizmetID"], ")", yikama_hizmeti["HizmetAd"], "-", yikama_hizmeti["HizmetFiyat"],"TL")
        print(kurulama_hizmeti["HizmetID"], ")", kurulama_hizmeti["HizmetAd"], "-", kurulama_hizmeti["HizmetFiyat"],"TL")
        print(cilalama_hizmeti["HizmetID"], ")", cilalama_hizmeti["HizmetAd"], "-", cilalama_hizmeti["HizmetFiyat"],"TL\n")
        print("0) Bitis\n")
        print("Girilen para miktari: ", girilen_para, "TL\n")
        islem_secim = int(input("Para girisi yapacaginiz islemleri seciniz: "))

        if(islem_secim == 1):
            girilen_para += kopukleme_hizmeti["HizmetFiyat"]
        elif(islem_secim == 2):
            girilen_para += yikama_hizmeti["HizmetFiyat"]
        elif(islem_secim == 3):
            girilen_para += kurulama_hizmeti["HizmetFiyat"]
        elif(islem_secim == 4):
            girilen_para += cilalama_hizmeti["HizmetFiyat"]
        elif(islem_secim == 0):
            print("Toplam", girilen_para, " TL para attiniz.\n")
            break
        else:
            print("Hatali islem yaptiniz! Lutfen islem numarasina göre secim yapiniz.")   
            time.sleep(5)

        os.system('cls')

def menu():
    global hizmet_bedeli
    global para_ustu

    while True:
        print(kopukleme_hizmeti["HizmetID"], ")", kopukleme_hizmeti["HizmetAd"], "-", kopukleme_hizmeti["HizmetAdet"], "adet hizmet kaldi -", kopukleme_hizmeti["HizmetFiyat"],"TL")
        print(yikama_hizmeti["HizmetID"], ")", yikama_hizmeti["HizmetAd"], "-", yikama_hizmeti["HizmetAdet"], "adet hizmet kaldi -", yikama_hizmeti["HizmetFiyat"],"TL")
        print(kurulama_hizmeti["HizmetID"], ")", kurulama_hizmeti["HizmetAd"], "-", kurulama_hizmeti["HizmetAdet"], "adet hizmet kaldi -", kurulama_hizmeti["HizmetFiyat"],"TL")
        print(cilalama_hizmeti["HizmetID"], ")", cilalama_hizmeti["HizmetAd"], "-", cilalama_hizmeti["HizmetAdet"], "adet hizmet kaldi -", cilalama_hizmeti["HizmetFiyat"],"TL\n")
        print("0) Bitis\n")
        print("Secilen hizmetlerin toplam islem tutari: ", hizmet_bedeli, "TL\n")
        islem_secim = int(input("Yapmak istediğiniz hizmeti/hizmetleri seçiniz: "))

        if(islem_secim == 1 and kopukleme_hizmeti["HizmetAdet"] >= 1):
            hizmet_bedeli += kopukleme_hizmeti["HizmetFiyat"]
            kopukleme_hizmeti["HizmetAdet"] -= 1
        elif(islem_secim == 1 and kopukleme_hizmeti["HizmetAdet"] == 0):
            print("Hizmet bitmistir baska bir hizmet secebilirsiniz")
            time.sleep(5)
            os.system('cls')    
        if(islem_secim == 2 and yikama_hizmeti["HizmetAdet"] >= 1):
            hizmet_bedeli += yikama_hizmeti["HizmetFiyat"]
            yikama_hizmeti["HizmetAdet"] -= 1
        elif(islem_secim == 2 and yikama_hizmeti["HizmetAdet"] == 0):
            print("Hizmet bitmistir baska bir hizmet secebilirsiniz")
            time.sleep(5)
            os.system('cls')
        if(islem_secim == 3 and kurulama_hizmeti["HizmetAdet"] >= 1):
            hizmet_bedeli += kurulama_hizmeti["HizmetFiyat"]
            kurulama_hizmeti["HizmetAdet"] -= 1
        elif(islem_secim == 3 and kurulama_hizmeti["HizmetAdet"] == 0):
            print("Hizmet bitmistir baska bir hizmet secebilirsiniz")
            time.sleep(5)
            os.system('cls')
        if(islem_secim == 4 and cilalama_hizmeti["HizmetAdet"] >= 1):
            hizmet_bedeli += cilalama_hizmeti["HizmetFiyat"]
            cilalama_hizmeti["HizmetAdet"] -= 1
        elif(islem_secim == 4 and cilalama_hizmeti["HizmetAdet"] == 0):
            print("Hizmet bitmistir baska bir hizmet secebilirsiniz")
            time.sleep(5)
            os.system('cls')
        if(islem_secim == 0):
            para_ustu = girilen_para - hizmet_bedeli
            para_hesap()
            break

        if(girilen_para < hizmet_bedeli):
            print("İsleminiz secildi fakat girilen para miktari hizmet bedelini karsilamiyor! Lutfen para ekleyiniz!\n")
            time.sleep(5)
            os.system('cls')
            return system()

        os.system('cls')

def para_hesap():
        global hizmet_bedeli
        global girilen_para
        global para_ustu
        global kasa

        print("\nGirilen para miktari ", girilen_para, "TL")
        print("Toplam", hizmet_bedeli, "TL'lik islem yapildi\n")
        print("Para üstünüz toplam ", para_ustu, "TL")

        if (para_ustu>=100):
            banknot = (int(para_ustu//100))
            if(banknot <= tl_adet["yuzlira_adet"]):
                tl_adet["yuzlira_adet"] -= banknot 
                para_ustu = (int(para_ustu%100)) 
                print("{} adet 100 TL".format(banknot))
            elif(banknot >= tl_adet["yuzlira_adet"] and tl_adet["yuzlira_adet"] > 0):
                para_ustu -= tl_adet["yuzlira_adet"]*100
                print("{} adet 100 TL".format(tl_adet["yuzlira_adet"]))
                tl_adet["yuzlira_adet"] = 0

        if (para_ustu>=50):
            banknot = (int(para_ustu//50))
            if(banknot <= tl_adet["ellilira_adet"]):
                tl_adet["ellilira_adet"] -= banknot 
                para_ustu = (int(para_ustu%50)) 
                print("{} adet 50 TL".format(banknot))
            elif(banknot >= tl_adet["ellilira_adet"] and tl_adet["ellilira_adet"] > 0):
                para_ustu -= tl_adet["ellilira_adet"]*50
                print("{} adet 50 TL".format(tl_adet["ellilira_adet"]))
                tl_adet["ellilira_adet"] = 0

        if (para_ustu>=20):
            banknot = (int(para_ustu//20))
            if(banknot <= tl_adet["yirmilira_adet"]):
                tl_adet["yirmilira_adet"] -= banknot 
                para_ustu = (int(para_ustu%20)) 
                print("{} adet 20 TL".format(banknot))
            elif(banknot >= tl_adet["yirmilira_adet"] and tl_adet["yirmilira_adet"] > 0):
                para_ustu -= tl_adet["yirmilira_adet"]*20
                print("{} adet 20 TL".format(tl_adet["yirmilira_adet"]))
                tl_adet["yirmilira_adet"] = 0

        if (para_ustu>=10):
            banknot = (int(para_ustu//10))
            if(banknot <= tl_adet["onlira_adet"]):
                tl_adet["onlira_adet"] -= banknot 
                para_ustu = (int(para_ustu%10)) 
                print("{} adet 10 TL".format(banknot))
            elif(banknot >= tl_adet["onlira_adet"] and tl_adet["onlira_adet"] > 0):
                para_ustu -= tl_adet["onlira_adet"]*10
                print("{} adet 10 TL".format(tl_adet["onlira_adet"]))
                tl_adet["onlira_adet"] = 0
            
        if (para_ustu>=5):
            banknot = (int(para_ustu//5))
            if(banknot <= tl_adet["beslira_adet"]):
                tl_adet["beslira_adet"] -= banknot 
                para_ustu = (int(para_ustu%5)) 
                print("{} adet 5 TL".format(banknot))
            elif(banknot >= tl_adet["beslira_adet"] and tl_adet["beslira_adet"] > 0):
                para_ustu -= tl_adet["beslira_adet"]*5
                print("{} adet 5 TL".format(tl_adet["beslira_adet"]))
                tl_adet["beslira_adet"] = 0
        
        if(para_ustu < kasa):
            kasa = 0
            print("\nKasadaki para miktari ", kasa, "TL")
            print("Kasada yeterli miktarda para bulunmamaktadir. Kalan {} TL para ustunuz icin su anda isleminizi gerceklestiremiyoruz!".format(para_ustu))

def system():
    para_girisi()
    menu()

system()