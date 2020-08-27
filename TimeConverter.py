
waktu = -60 #dalam satuan detik
print (f"Masukan detik : {waktu}") # cetak string masukan detik bersama dengan waktu yang ingin di konversi
if waktu <0 :
    print("Invalid input!") 
elif type(waktu) == str: # jika type data dari waktu itu adalah string, maka akan muncul keterangan 'Invalid input!'
    print("Invalid input!") 
elif type(waktu) == float:#jika type data dari waktu itu adalah float, maka akan muncul keterangan 'Invalid input!' 
    print("Invalid input!")
elif waktu > 359999 : #jika value waktu itu bertipe int tapi nilainya diatas 359999, maka akan muncul keterangan 'Invalid input!
    print("Invalid input!")
elif waktu >0: # jika semua kondisi diatas tidak memenuhi, maka akan memproses function timeConverter
    def timeConverter(seconds): #function ini bernama timeConverter dengan parameter seconds
        jam = seconds//3600 # variabelnya jam ini merupakan hasil dari pembagian seconds sebagai parameter dengan jam, karena 1 jam = 3600 detik
        menit = (seconds-jam*3600)//60 #variabel menit ini merupakan pengurangan antara second dengan  variabel jam yang dikali 3600 yang lalu akan dibagi 60 . alasannya karena jika tidak dilakukan pengurangan dan pembagian hasilnya bisa melebihi 60
        detik = seconds%60 # variabel detik ini di set jika nilai seconds = 60, akan mulai lagi dari 0
        return f'Konversi: {jam}:{menit}:{detik}' # setelah variabel sudah di set, maka value yang ada didalam jam, menit, dan detik akan di return
    print(timeConverter(waktu))  # ketika function timeConverter dicetak dengan value dari parameter seconds, maka value yang ada di return akan dicetak

