gaji_pokok = float(input("Masukkan gaji pokok karyawan: Rp "))
jumlah_anak = int(input("Masukkan jumlah anak: "))
masuk_kerja_hari = int(input("Masukkan jumlah hari masuk kerja dalam sebulan: "))

tunjangan_istri_suami = 0.10  # 10% dari gaji_pokok
tunjangan_anak = 0.05  # 5% dari gaji_pokok per anak
pajak = 0.15  # 15% dari gaji_pokok, tunjangan istri & anak
bantuan_transport_per_hari = 20000
bpjs = 75000

total_tunjangan_istri_suami = gaji_pokok * tunjangan_istri_suami
total_tunjangan_anak = gaji_pokok * tunjangan_anak * jumlah_anak
total_pajak = (gaji_pokok + total_tunjangan_istri_suami + total_tunjangan_anak) * pajak
total_bantuan_transport = bantuan_transport_per_hari * masuk_kerja_hari

take_home_pay = gaji_pokok + total_tunjangan_istri_suami + total_tunjangan_anak -
total_pajak + total_bantuan_transport - bpjs

print("\n===== RINCIAN PENDAPATAN BULANAN =====")
print(f"Gaji Pokok          : Rp {gaji_pokok:.2f}")
print(f"Tunjangan Istri/Suami : Rp {total_tunjangan_istri_suami:.2f}")
print(f"Tunjangan Anak      : Rp {total_tunjangan_anak:.2f}")
print(f"Pajak               : Rp {total_pajak:.2f}")
print(f"Bantuan Transport   : Rp {total_bantuan_transport:.2f}")
print(f"Potongan BPJS       : Rp {bpjs:.2f}")
print("-------------------------------------")
print(f"Take Home Pay       : Rp {take_home_pay:.2f}")
