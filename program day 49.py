def paket():
    print(" kode 1 : paket hemat  Rp. 7.500")
    print("kode 2 : paket nasi harga Rp.10.000")
    print("kode 3 : paket spesial harga Rp.15.000")
paket()
taif_Ppn=10/100
nama_kasir=input("masukkan nama kasir:")
jumlah_pembelian=int(input("masukkan jumlah pembelian:"))
total_pembayaran=[]
for i in range(jumlah_pembelian):
    kode_kasir=int(input("masukkan kode paket yang di pilih:"))
    if kode_kasir == 1:
        tarif_kena_Ppn=7500*10/100
        harga_pembayaran=(7500-tarif_kena_Ppn)
        print(harga_pembayaran)
    elif kode_kasir == 2:
        tarif_kena_Ppn=10000*10/100
        harga_pembayaran=(10000-tarif_kena_Ppn)
        print(harga_pembayaran)
    elif kode_kasir == 3:
        tarif_kena_Ppn=15000*10/100
        total_pembayaran=(15000-tarif_kena_Ppn)
        harga_pembayaran.append(total_pembayaran)
        print(harga_pembayaran)
    else:
        print("kode kasir yang di masukkan tidak terdapat dalam paket atau menu")
