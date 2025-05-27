import os
import sys
import io



while True:
    print("1-TXT\n2-PNG\n3-Çıkış")
    msg = str(input("İşeminizi giriniz: "))
    
    string_io = io.StringIO()
    sys.stdout = string_io
    if msg == "1":
        dosya = str(input("dosyanın adını giriniz: "))
        os.system(f"python txt.py {dosya}")
        print(string_io.getvalue())
    elif msg == "2":
        dosya2 = str(input("dosyanın adını giriniz: "))
        os.system(f"python png.py {dosya2}")
        print(stringIO.getvalue())
    elif msg == "3":
        print("Çıkış Yapılıyor...")
        break
    else:
        print("Lütfen geçerli bir işlem giriniz!")