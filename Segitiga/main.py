def segitiga():
    
    sisi_a = float(input("Masukkan sisi a: "))
    sisi_b = float(input("Masukkan sisi b: "))
    sisi_c = float(input("Masukkan sisi c: ")) 
    
    if sisi_a == sisi_b == sisi_c:
        print("Segitiga sama sisi")
        keliling = 3 * sisi_a
        print("Keliling segitiga adalah: ", keliling)
        luas = 0,5 * sisi_c * sisi_a
        print("Luas segitiga adalah: ", luas)
    elif sisi_a == sisi_b and sisi_b != sisi_c:
        print("Segitiga sama kaki") 
        keliling = 2 * sisi_a + sisi_b
        print("Keliling segitiga adalah: ", keliling)
        luas = 0,5 * sisi_c * sisi_a
        print("Luas segitiga adalah: ", luas)
    elif sisi_a != sisi_b != sisi_c:
        print("Segitiga sembarang")
        keliling = sisi_b + sisi_a + sisi_c
        print("Keliling segitiga adalah: ", keliling)
        luas = 0,5 * sisi_c * sisi_a
        print("Luas segitiga adalah: ", luas)
        
        

segitiga()