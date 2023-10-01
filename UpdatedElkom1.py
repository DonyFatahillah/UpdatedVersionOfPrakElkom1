import math
#importing function from math library
import time

#while true for repeating the process if necessary
while True:
    
    #three options and which one to calculate
    print("""
a) hitung sisi a >
b) hitung sisi b >
c) hitung sisi c >
""")

    #the options input (you must use either 3 of these letter a, b, or c)
    opsi = input("pilih opsi (a/b/c) : ")

    #this is the condition if the option was a
    if opsi == "a":

        #the input of b & c numbers
        b = float(input("Masukan sisi B : "))
        c = float(input("Masukan sisi C : "))

        #this is the condition if c were less than b
        if c < b:
            print("angka C harus lebih besar dari B")        
            continue 
        #it will continue the process till you got the right number
        #it must be c > b


        #this is the variable to count the a side
        hitungA = math.sqrt(c**2 - b**2)

        #this is the result
        print(f"Jika sisi b adalah {b}, dan sisi c adalah {c}, maka sisi a nya adalah {hitungA}")
        
    #this is the condition if the option was b
    elif opsi == "b":

        #the input of a & c numbers
        a = float(input("Masukan sisi A : "))
        c = float(input("Masukan sisi C : "))

        #this is the condition if c were less than a
        if c < a:
            print("angka C harus lebih besar dari A")        
            continue
        #it will continue the process till you got the right number
        #it must be c > a

        #this is the variable to count the B side
        hitungB = math.sqrt(c**2 - a**2)

        #this is the result
        print(f"Jika sisi a adalah {a}, dan sisi c adalah {c}, maka sisi a nya adalah {hitungB}")
        
    #this is the condition if the option was c
    elif opsi == "c":

        #input for the a & b numbers
        a = float(input("Masukan sisi A : "))
        b = float(input("Masukan sisi B : "))
        
        #this is the variable to count the C side
        hitungC = math.sqrt(a**2 + b**2)

        #this is the result
        print(f"Jika sisi a adalah {a}, dan sisi b adalah {b}, maka sisi a nya adalah {hitungC}")
        
    #this is the condition if the option was neither of them
    else:
        print("masukan opsi yang valid!")
        
  
    #an option whether if you want to repeat the process or no
    ulangi = input("Ulangi Proses? (y/n) : ")

    #if it was the letter "n" it will stop
    if ulangi.lower() == "n":
        print("\nThank you for using my program <3\n")
        break
    
    #if it was the letter "y" it will repeat the process
    elif ulangi.lower() == "y":
        continue

    #if it was neither y or n it will break automatically
    else:
        break
