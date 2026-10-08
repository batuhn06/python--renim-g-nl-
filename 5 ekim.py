import random 

print("Merhabalarr benimle sayı tahmin oyununu oynamaya var mısın bakalım haha ?!")
print("Senin için 47 ile 470 arasında bir sayı tuttum, bilebileceğini hiç sanmıyorum ama buraya kadar geldiysen bir dene bakalım!\n")

# 47 ve 470 arasında rastgele bir sayı seçiyoruz.
# Değişken ismini İngilizce karakterlerle (gizli_sayi) sabitledik.
gizli_sayi = random.randint(47, 470)
deneme_sayisi = 0

# Süreç, kullanıcı doğru sayıyı tahmin edene kadar sürecektir.
while True:
    try:
        tahmin = int(input("Tahmininiz:  "))
        deneme_sayisi += 1 
        
        # Tahmini kontrol aşaması (if, elif ve else aynı hizada)
        if tahmin < gizli_sayi:
            print("Hahahahaha olmadı, biraz daha yüksekten uçmalısın!\n")
        elif tahmin > gizli_sayi: 
            print("Biraz alçalmaya ne dersin?\n")	
        else:
            print(f"OLAMAZ, BENİ NASIL DA HAKLADIN ÖYLE!! TEBRİK EDERİM {gizli_sayi} sayısını {deneme_sayisi}. deneme sonunda buldun!")
            break
            
    # except bloğu, yukarıdaki try bloğu ile tam aynı hizada
    except ValueError:
        print("Geçersiz karakter girişi yapıldı! LÜTFEN SADECE SAYI GİRİNİZ!!\n")
   		