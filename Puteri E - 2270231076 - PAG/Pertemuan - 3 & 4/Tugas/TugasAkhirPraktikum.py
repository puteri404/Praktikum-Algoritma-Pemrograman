# Tugas Akhir Praktikum Algoritma Pemrograman
# Nama: Puteri Elisabeth P
# NIM : 2270231076
# Program : Kasir Minimarket


print("=============== Kode Kelabu Minimart =============== ")
print("    ============ Selamat Berbelanja ============")
print("=== Jl. Kita Masih Panjang, Blok CG No. 06, Jakarta Pusat ===")
print("== Email: ask_kobuminimmart@gmail.com, Phone: 0891-2345-678 ==")
print("================================================================")


pembeli= str(input("Nama Pembeli: "))
alamat= str(input("Alamat Pembeli: "))
no_telp= int(input("No. Telp: +62"))
tanggal= str(input("Masukkan Tanggal Pembelian: "))

print("\n----------- Daftar Barang -----------")
print("1. Sabun Mandi Batang - Rp. 5000")
print("2. Shampoo 500 ml - Rp. 27000")
print("3. Kopi Susu Bubuk 10 Saset - Rp. 18500")
print("4. Minyak Goreng 2L - Rp. 35700")
print("5. Gula Pasir 1 Kg - Rp. 20000")
print("--------------------------------------")

nmr_brng=int(input("Nomor Barang: "))
total=int(input("Total pembelian: "))

if nmr_brng == 1:
    harga1=5000
    harga=harga1
    totalpembelian=total*5000
    print (total," Sabun Mandi Batang = Rp", totalpembelian)
    pembelian=("Sabun Mandi Batang")

elif nmr_brng == 2:
    harga2=27000
    harga=harga2
    totalpembelian=total*27000
    print (total," Shampoo 500 ml = Rp", totalpembelian)
    pembelian=("Shampoo 500 ml")

elif nmr_brng == 3:
    harga3=18500
    harga=harga3
    totalpembelian=total*18500
    print (total, " Kopi Susu Bubuk 10 Saset = Rp", totalpembelian)
    pembelian=("Kopi Susu Bubuk 10 Saset")

elif nmr_brng == 4:
    harga4=35700
    harga=harga4
    totalpembelian=total*35700
    print (total, " Minyak Goreng 2L = Rp", totalpembelian)
    pembelian=("Minyak goreng 2L")

elif nmr_brng == 5:
    harga5=20000
    harga=harga5
    totalpembelian=total*20000
    print (total, " Gula Pasir 1 Kg = Rp", totalpembelian)
    pembelian=("Gula Pasir 1 Kg")

else:
    print("Maaf, pilihan belum ada/tidak tersedia. Silahkan masukkan kembali!")

totalsemua=totalpembelian

print("Total Pembayaran: Rp ",totalsemua)
tunai = int(input("Uang Tunai: Rp"))
kembalian = int(tunai-totalsemua)
print("Kembalian: ",kembalian)

print("\n-------------- Struk Belanja ----------------")
print("Nama Pembeli: ", pembeli)
print("Alamat Pembeli: ", alamat)
print("No. Telp: +62", no_telp)
print("Tanggal: ", tanggal)
print("Nomor Barang: ", total,pembelian,"(Rp", harga, ")")
print("Total Pembayaran: Rp", totalsemua)
print("Tunai: Rp", tunai)
print("Kembalian: Rp", kembalian)
print("----------- Terima Kasih Telah Berbelanja ------------")
