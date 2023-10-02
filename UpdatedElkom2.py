import math

while True:

    print("""
          
Kalkulator Pytagoras
          
a.) hitung sisi A <>
b.) hitung sisi B <>
c.) hitung sisi C <>
""")

    opsi = input("Masukan opsi : ")

    if opsi in ("a", "A"):

        b = input("masukan angka b : ")
        c = input("masukan angka c : ")

        if not b.isdigit() or not c.isdigit():
            print("\nmasukan angka, bukan huruf.")
            continue
        angkaB = float(b)
        angkaC = float(c)
        if angkaC < angkaB:
            print("c harus lebih besar dari b")
            continue
        hitungA = math.sqrt(angkaC**2 - angkaB**2)

        print(f"hasilnya, sisi a adalah {hitungA}")
        

    elif opsi in ("b", "B"):

        a = input("masukan angka a : ")
        c = input("masukan angka c : ")

        if not a.isdigit() or not c.isdigit():
            print("\nmasukan angka, bukan huruf.")
            continue
        angkaA = float(a)
        angkaC = float(c)
        if angkaC < angkaA:
            print("c harus lebih besar dari a")
            continue
        hitungB = math.sqrt(angkaC**2 - angkaA**2)
        print(f"hasilnya, sisi b adalah {hitungB}")

    elif opsi in ("c", "C"):

        a = input("masukan angka a : ")
        b = input("masukan angka b : ")

        if not a.isdigit() or not b.isdigit():
            print("\nmasukan angka, bukan huruf.")
        angkaA = float(a)
        angkaB = float(b)

        hitungC = math.sqrt(angkaA**2 + angkaB**2)
        print(f"hasilnya, sisi c adalah {hitungC}")
    else:
        print("opsi tidak valid!")

    ulangi = input("ulangi proses? (y/n) : ")
    if ulangi in ("n", "N", "No", "NO", "no"):
        break

    if ulangi in ("y", "Y", "Yes", "YES", "yes", "yEs", "YEs", "yES"):
        continue

    else:
        break
