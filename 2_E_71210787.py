nama= input("Nama : ")
ttl=input("Tempat tanggal lahir : ")

pisah_nama=nama.rsplit(" ",1)
pisah_ttl=ttl.split(" ",1)

print("Haloo!",pisah_nama[1]+",",pisah_nama[0]) 
print("Anda lahir di",pisah_ttl[0],"pada tanggal",pisah_ttl[1])