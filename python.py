def okunus(sayi):
    birler = ["Sıfır", "Bir", "İki", "Üç", "Dört", "Beş", "Altı", "Yedi", "Sekiz", "Dokuz"]
    onlar = ["", "On", "Yirmi", "Otuz", "Kırk", "Elli", "Altmış", "Yetmiş", "Seksen", "Doksan"]
    
    birinci = sayi % 10
    ikinci = sayi // 10
    
    return onlar[ikinci] + " " + birler[birinci]

while True:
    sayi = input("Sayı (Çıkmak için 'q' girin): ")
    
    if sayi.lower() == 'q':
        print("Programdan çıkılıyor...")
        break
    elif sayi.isdigit() and len(sayi) <= 2:
        sayi = int(sayi)
        print(okunus(sayi))
    else:
        print("Geçersiz giriş. Lütfen iki haneli bir sayı girin veya 'q' tuşlayarak çıkın.")