import random
import time

print("""**************************

SAYI TAHMİN OYUNU

1 ile 100 arasında sayıyı tahmin edin.

**************************""")


rastgeleSayı = random.randint(1,100)

tahminHakkı = 7

while True :

    tahmin = int(input("Tahmininiz: "))

    if (tahmin < rastgeleSayı):
        print("Bilgiler sorgulanıyor...")
        time.sleep(1)

        print("Daha yüksek bir sayı giriniz..")

        tahminHakkı -= 1

    elif (tahmin > rastgeleSayı ):
        print("Bilgiler sorgulanıyor..")
        time.sleep(1)

        print("Daha düşük bir sayı giriniz...")
        tahminHakkı -= 1

    else:
        print("Bilgiler sorgulanıyor..")
        time.sleep(1)

        print("Tebrikler sayınız doğru:",rastgeleSayı)
        break

    if tahminHakkı == 0 :
        print("Tahmin Hakkınız Bitmiştir...")
        print("Random Sayı:",rastgeleSayı )
        break



