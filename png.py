from getpass import getpass
import pyAesCrypt
from sys import argv

def sifrele(dir):
    password = getpass("Password girin: ")
    bufferSize = 512*1024
    pyAesCrypt.encryptFile(str(dir), str(dir)+".aes", password, bufferSize)
    print(f"Dosyanız şifrelendi: {str(dir)}.aes")
    
def sifreCoz(dir):
    password = getpass("Password girin: ")
    bufferSize = 521*1024
    # Dosya adından .aes uzantısını çıkarıyoruz
    output_file = str(dir).replace('.aes', '')
    pyAesCrypt.decryptFile(str(dir), output_file, password, bufferSize)
    print(f"Dosyanız açıldı: {output_file}")
    
dir = argv[1]

islem = str(input("1-Şifrele\n2-Şifre Çöz\n3-Çıkış\nİşleminizi giriniz: "))
if islem == "1":
    sifrele(dir)
elif islem == "2":
    sifreCoz(dir)
elif islem == "3":
    print("Program sonlandırlıyor...")
    sys.exit()
else:
    print("Lütfen geçerli bir işlem giriniz:")