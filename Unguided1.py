def kalkulator():
    print("Ketik Q jika sudah selesai.")

    n = input("Masukkan perhitungan : ")

    if n == "Q":
        global status
        status = False
        return

    n = n.split()

    if n[1] == "+":
        return int(n[0])+int(n[2])
    elif n[1] == "-":
        return int(n[0])-int(n[2])
    elif n[1] == "*":
        return int(n[0])*int(n[2])
    elif n[1] == "/":
        return int(n[0])/int(n[2])
    else:
        return "Invalid input"


status = True
while status == True:
    print()
    x = kalkulator()

    if x != None:
        print("Hasilnya : {}".format(x))



