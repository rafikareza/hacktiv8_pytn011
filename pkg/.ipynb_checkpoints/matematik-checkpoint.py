pi = 3.14
golden_ratio = 1.618

def nambah(a,b):
    return a+b

def cekGenap(num):
    return num % 2 == 0

# kalau script, keluarin hasil print ini
if (__name__ == '__main__'):
    print("halo, ini modul matematik.py")
    print("lokasi modul ini ada di Dekstop > mods folder")
    print("...")
    import sys
    print(sys.argv) # sebuah list
    if (sys.argv[1] == 'nambah'):
        num1 = int(sys.argv[2])
        num2 = int(sys.argv[3])
        print(nambah(num1, num2))