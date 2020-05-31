# Ujian Fundamental Batch 7

# Soal 1 himpunan

'''
Diketahui:

A = himpunan (set) bilangan genap antara 1 dan 20.
B = himpunan (set) bilangan ganjil antara 1 dan 20.
C = himpunan (set) bilangan negatif lebih dari -10.
D = himpunan (set) bilangan prima antara 1 dan 20.
E = himpunan (set) bilangan komposit antara 1 dan 20.
Definisi & kategori bilangan dapat Anda simak di laman Wikipedia. Buatlah sebuah file python (.py) yang dapat menyelesaikan permasalahan himpunan berikut:

a. A ∪ B ∪ C ∪ D ∪ E

b. (A ∩ B) ∪ (D ∩ E)

c. (A ∪ B) ∩ (D ∪ E)

d. (A ∪ B) - (D ∪ E)

e. (A ∪ B ∪ C) - (A ∩ E)
'''

A = {2, 4, 6, 8, 10, 12, 14, 16, 18}
B = {3, 5 ,7, 9, 11, 13, 15, 17, 19}
C = {-9,-8,-7,-6,-5,-4,-3,-2,-1}
D = {2,3,5,7,11,13,17,19}
E = {4,6,8,9,10,12,14,15,16,18}

# soal a
print( A | B | C | D | E )
print(A.union(B).union(C).union(D).union(E))

# soal b
print((A & B) | (D & E))
print((A.intersection(B)).union(D.intersection(E)))

# soal c
print((A | B) & (D | E))
print((A.union(B)).intersection((D.union(E))))

# soal d
print ((A | B) - (D | E))
print ((A.union(B)).difference((D.union(E))))

# soal E
print ((A | B | C) - (A & E))
print ((A.union(B).union(C)).difference(A.intersection(E)))


# Soal 2 Segitiga kata

def segitigaKata(x):
    syarat = [1]
    awal = 1
    hasil = ''
    inisiasi = 0
    x = x.replace(' ', '')
    for i in range(2, len(x)):
        awal = awal + i
        syarat.append(awal)
    # print (syarat)
    # print (len(x))
    if len(x) in syarat :
        for i in range(syarat.index(len(x))+2):
            for j in range(i) :
                hasil += x[inisiasi] + ' '
                inisiasi += 1
            hasil += '\n'
        inisiasi = 0
        for i in range(syarat.index(len(x))+1,0,-1):
            for j in range(i) :
                hasil += x[inisiasi] + ' '
                inisiasi += 1
            hasil += '\n'
        print(hasil)
    else :
        print("Mohon maaf, jumlah karakter tidak memenuhi syarat membentuk pola.")

segitigaKata("Purwhadika")
segitigaKata('Purwadhika Startup and Coding School @BSD')
segitigaKata('kode')
segitigaKata('kode python')
segitigaKata('lintang')

# soal 3 - nomor kartu kredit

import json
with open('ccNasabah.json', 'r') as jsonku:
    data = json.load(jsonku)

valid = []
invalid = []
syarat3 = ['0','1','2','3','4','5','6','7','8','9']
syarat5 = ['0000', '1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888', '9999']
for i in data :
    if i['noCreditCard'][0] == '4' or i['noCreditCard'][0] == '5' or i['noCreditCard'][0] == '6':
        if len(i['noCreditCard'].replace(' ','').replace('-','').replace('.','')) == 16:
            for j in syarat5:
                if j in i['noCreditCard'].replace(' ','').replace('-','').replace('.',''):
                    invalid.append(i)
            for k in i['noCreditCard'].replace(' ','').replace('-','').replace('.','') :
                if k not in syarat3 :
                    invalid.append(i)
            if i not in invalid :
                if i['noCreditCard'][4] == '-' and i['noCreditCard'][9] == '-' and i['noCreditCard'][14] == '-' :
                    valid.append(i)
                elif len(i['noCreditCard']) != 16:
                    invalid.append(i)
                else:
                    valid.append(i)
        else :
            invalid.append(i)
    else :
        invalid.append(i)        

with open('ccValid.json', 'w') as validjson:
    json.dump(valid, validjson)
with open('ccInvalid.json', 'w') as invalidjson:
    json.dump(invalid, invalidjson)


# Ujian Fundamental Batch 4

# Soal 1 fungsi pangkat

def pangkat(x, y):
    hasil = 1
    for i in range(0, y) :
        hasil *= x
    return hasil

print(pangkat(2, 2))
print(pangkat(3, 3))
print(pangkat(10, 5))

# Soal 2 membalik posisi elemen list

def balikPosisi(x) :
    tempx = []
    for i in x :
        tempx.insert(0, i)
    return tempx

print(balikPosisi([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(balikPosisi(['A', 'B', 'C', 'D', 'E', 'F', 'G']))
print(balikPosisi(['Messi', 'Suarez', 'Coutinho', 'Dembele', 'Rakitic']))

# Ujian  Fundamental batch 3

#  Soal 1 FPB & KPK

angka1 = int(input('Ketik angka pertama : '))
angka2 = int(input('Ketik angka kedua : '))
maks = max(angka1,angka2)
min = min(angka1,angka2)
for i in range(1,min+1) :
    if angka1 % i == 0 and angka2 % i == 0 :
        FPB = i
for j in range(maks,(angka1*angka2)+1) :
    if j % angka1 == 0 and j % angka2 == 0 :
        KPK = j
        break
print(f'FPB dari {angka1} dan {angka2} adalah = {FPB}') 
print(f'KPK dari {angka1} dan {angka2} adalah = {KPK}')

# soal 2- kategori bilangan

angka = int(input('Ketik angka : '))
def lisbilangan(x) :
    kategori = []
    kategori.append("Bulat")
    if x >= 0 :
        kategori.append("Cacah")
        if x > 0:
            kategori.append("Asli")
            if x % 2 == 0:
                kategori.append("Genap")
            else :
                kategori.append("Ganjil")
            if x == 2 :
                kategori.append('Prima')
            else :
                for i in range(2, x) :
                    if x % i == 0:
                        kategori.append('Komposit')
                        break
                if 'Komposit' not in kategori :
                    kategori.append('Prima')
        else :
            kategori.append("Nol")        
    else:
        kategori.append("Negatif")
    return kategori

print(lisbilangan(angka))

# soal 3 Top 5 news API

import requests
x = 0
while x != 1 :
    print(
    '''
    Selamat datang, mau tahu berita apa hari ini?
    [1] Berita seputar teknologi
    [2] Berita seputar bisnis
    [3] Berita seputar olahraga
    [4] Berita seputar kesehatan
    [5] Berita seputar science
    '''
    )
    pilihan = input(" Ketik pilihan Anda [1/2/3/4/5] : ")
    if pilihan == '1' :
        kategori = 'technology'
        break
    elif pilihan == '2' :
        kategori = 'business'
        break
    elif pilihan == '3' :
        kategori = 'sports'
        break
    elif pilihan == '4' :
        kategori = 'health'
        break
    elif pilihan == '5' :
        kategori = 'science'
        break
    else :
        print('Mohon maaf anda salah memasukkan pilihan, silahkan coba lagi ! ')

apikey= '06e2e6386e48479db9f5457ffe32f50e'
url = f'https://newsapi.org/v2/top-headlines?country=id&category={kategori}&apiKey={apikey}'
data = requests.get(url)
news = data.json()

print(f'Berikut adalah top 5 berita Indonesia bidang {kategori}')
for i in range(0, 5):
    judul = news['articles'][i]['title']
    print(f'{i+1} - {judul}')

# SOAL REMEDIAL

# soal 2 Alamat Email

huruf = []
for i in range(ord('a'),ord('z')+1) :
    huruf.append(chr(i))

angka = []
for i in range (10) :
    angka.append(str(i))

Hasil = 'EMAIL VALID'
email = input('Input email : ').lower()
if '@' in email and '.' in email:
    for i in email[:email.index('@')] :
        if i in huruf or i in angka or i == "-" or i == '_':
            Hasil = 'EMAIL VALID'
        else :
            Hasil = 'EMAIL TIDAK VALID'
            break
    for i in email[email.index('@')+1:email.index('.')] :
        if i in huruf or i in angka :
            Hasil = 'EMAIL VALID'
        else :
            Hasil = 'EMAIL TIDAK VALID'
            break
    if len(email[email.index('.')+1:]) > 5:
        Hasil = 'EMAIL TIDAK VALID'
    else : 
        for i in email[email.index('.')+1:] :
            if i not in huruf : 
                Hasil = 'EMAIL TIDAK VALID'
                break
else:
    Hasil = 'EMAIL TIDAK VALID'

print(f'Hasil : {Hasil}')

# Soal Ujian Purwhadika Jakarta

# Soal 1

def Hashtag (string):
    if len(string) <= 140 and len(string) >0 :
        Hasil = "#"
        string = list(string.split())
        for i in string :
            Hasil += str(i.capitalize())
        return print(Hasil)
    else :
        return print(False)

Hashtag(" Hello there how are you doing")
Hashtag(" Hello World " )
Hashtag("")

# Soal 2

def create_phone_number(number):
    bagian1 = ''
    bagian2 = ''
    bagian3 = ''
    for i in range(3) :
        bagian1 += str(number[i])
    for i in range(3,6) :
        bagian2 += str(number[i])
    for i in range(6, len(number)) :
        bagian3 += str(number[i])
    return print(f"({bagian1}) {bagian2}-{bagian3}")
    
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])

# Soal 3

def sort_odd_even(num) :
    indexganjil=[]
    indexgenap=[]
    listganjil=[]
    listgenap=[]
    x=0
    y=0
    for i in num :
        if i % 2 == 0 :
            listgenap.append(i)
            indexgenap.append(num.index(i))
        else :
            listganjil.append(i)
            indexganjil.append(num.index(i))
    listganjil.sort()
    listgenap.sort(reverse=True)
    for i in listganjil :
        num[indexganjil[x]] = i
        x += 1
    for i in listgenap:
        num[indexgenap[y]] = i
        y += 1
    print(num)
    

sort_odd_even([5, 3, 2, 8, 1, 4])

# Soal 4

def hollowTriangle(height) :
    Hasil = ''
    x = height-1
    for i in range(height-1):
        for j in range(x, 0, -1):
            Hasil += '_'
        Hasil += '#'
        if i+1 >= 2 :
            for j in range (0, (1 + 2 * (i-1))):
                Hasil += '_' 
            Hasil += '#'
        for j in range(x, 0, -1):
            Hasil += '_'
        x -= 1
        Hasil += '\n'
    for i in range (0, (1 + 2 * (height-1))):
        Hasil += '#'
        
    print(Hasil)

hollowTriangle(6)