##Author : Mohin Paramasivam
##Examination : Sijil Pelajaran Malaysia

kertas1 = float(input("Sila Masukkan markah kertas 1  anda : "))
kertas2 = float(input("Sila Masukkan markah kertas 2  anda : "))
kertas3 = float(input("Sila Masukkan markah kertas 3 anda  : "))

peratuskertas1 = 30
peratuskertas2 = 50
peratuskertas3 = 20

markahkertas1 = (kertas1/40)*peratuskertas1
markahkertas2 = (kertas2/100)*peratuskertas2
markahkertas3 = (kertas3/100)*peratuskertas3

Jumlahmarkah = (markahkertas1 + markahkertas2 + markahkertas3)

if (Jumlahmarkah >= 90 and Jumlahmarkah <= 100):

	Gred = "A+"

elif (Jumlahmarkah >= 80 and Jumlahmarkah <= 89 ):
	Gred = "A"
	
elif (Jumlahmarkah >= 70 and Jumlahmarkah <= 79 ):
	Gred = "A-"

elif (Jumlahmarkah >= 65 and Jumlahmarkah <= 69 ):
	Gred = "B+"

elif (Jumlahmarkah >= 60 and Jumlahmarkah <= 64 ):
	Gred = "B"

elif (Jumlahmarkah >= 55 and Jumlahmarkah <= 59 ):
	Gred = "C+"

elif (Jumlahmarkah >= 50 and Jumlahmarkah <= 54 ):
	Gred = "C"

elif (Jumlahmarkah >= 45 and Jumlahmarkah <= 49 ):
	Gred = "D"

elif (Jumlahmarkah >= 40 and Jumlahmarkah <= 44 ):
	Gred = "E"

else:
	Gred = "G"


print("  ")


print("Peratus Kertas 1 : " + str(markahkertas1))
print("Peratus Kertas 2 : " + str(markahkertas2))
print("Peratus Kertas 3 : " + str(markahkertas3))

print("  ")

print("Markah Sejarah 	:  " + str(round(Jumlahmarkah)) + " " + "%")
print("				")
print("Gred           	:   " +    Gred)

