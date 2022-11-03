#Bagian pembukaan
#UTS V.1.0.0
print ("==========program inputan nilai============")
print ("")
#Bagian perkenalan
print("NAMA : CAHYA SULAIMAN")
print("NIM  : B22067")
print("PRODI: S I C")
print ("")
#Bagian penginputan data
inputan = input('masukan nilai: ')
#Bagian pengubahan type data
cvt = int(inputan)

#Bagian eksekusi data
if cvt >= 90 and cvt <= 100 :       #eksekusi nilai A 90-100
    print ("Nilai A")
elif cvt >= 75 and cvt <= 89 :      #eksekusi nilai B 75-89
    print("Nilai B")
elif cvt >= 60 and cvt <= 74 :      #eksekusi nilai C 60-74
    print("Nilai C")
elif cvt >= 50 and cvt <= 59 :      #eksekusi nilai D 50-59
    print("Nilai D")
elif cvt >= 0 and cvt  <= 49 :      #eksekusi nilai E 0-49
    print("Nilai E")
else:                               #eksekusi nilai yang tidak masuk akal atau negatif
    print("mohon ditulis dengan Angka yang benar")

#Bagian penutup
print ("Selesai")
