''' text = "Upon its release on 25 December 2009, 3 Idiots received 
widespread critical acclaim and commercial success and is considered to 
be among the greatest Bollywood films ever made;[15] it was also the 
highest-grossing film in its opening weekend in India, had the highest 
opening day collections for an Indian film up until that point and also
 held the record for the highest net collections in the first week for 
 a Hindi film. Eventually, it became one of the few Indian films at the 
 time to become successful in East Asian markets such as China[16] and 
 Japan,[17] eventually bringing its worldwide gross to ₹392 crore
 ($90 million)[a][18][19] — it was the highest-grossing Indian film 
 ever at the time and the highest grossing Indian film of the 2000s. 
 It is also the 16th highest grossing Indian film of all time.[20] The 
 film also had a social impact on attitudes to education in India,[21] 
 as well as education in other Asian countries such as China.[7]" '''

# print(text.count(".") + text.count(','))

# cumle = 'Mən hər gün pythonda programlar düzəldirəm'

# print(cumle.replace('ə', 'e').replace('ü', 'u'))

# kod = '455#654543f5dg#yes'
# firstTag = kod.index('#') + 1
# secondTag = kod.rindex('#')
# print(kod[firstTag:secondTag])

# numb = 21.3942534
# print(round(numb, 7))

# ad = input('Adinizi daxil edin: ')
# print('Salam hormetli', ad, 'bey/xanim')

# print(dir('string'))

###

# card = "5382-1739-9201-9017"
# print(card.replace(card[0:9], "*"*len(card[0:9])))

# ##
# print((15%4)**3)
# ##
# print(round(256.91872, 2))
# print(round(256.91872, -2))
# ##
# print("000{}".format(34))
# print(str(34).zfill(4))
# ##


# numbInt = input("")
# print(numbInt, 'ededinin tam hissesi: ', int(float(numbInt)))

# Girilən websaytın əvvəlindəki https:// və 
# sonundakı .com hissələrini silən və istifadəçiyə göstərən program hazırlayın. (input və print ilə)

# website = 'https://compar.com'
# print((website.lstrip("htsp:/")).rstrip('.com'))

# website = input("")
# print('url protocol is: ',website[0:8],"\n","the domain is: ", website[14:])

##

# İstifadəçi yazacağınız inputlar vasitəsilə dəyişmək istədiyi sözü, 
# nəyə dəyişmək istədiyini və mətni daxil edəcək, qurduğunuz program 
# isə mətndə həmin sözləri dəyişib istifadəçiyə print edəcək

# text = "There's always democracy and happiness in Azerbaijan"

# cumle = input('Cumleni girmeyin, daxil edin: ')
# deyisilecek = input('Deyisilecek sozu girin: ')
# hedef = input('Hedef sozu girin: ')

# print(cumle.replace(deyisilecek, hedef))

''' +994 ile baslamali, 13 ededden ibaret olmali, ancaq ededlerden ibaret olmalidir '''

# number = input('Nomreni daxil edin: ')
# number = '+994506661845'
# and (number[1:]).isnumeric() and number.startswith('+994'):
# if len(number) == 13:
#     if number.startswith('+994'):
#         if number[1:].isnumeric():
#             print('nomre duzgundur')
#         else:
#             print('nomre yalniz reqemlerden ibaret olmalidir')
#     else:
#         print('nomrenin basligi duzgun deyil')
# else:
#     print('nomrenin uzunlugu duzgun deyil')


# l = [1, 2, 3, 4, [1, 2, 3, [1, 2, 3, [1, 2, 3]]]]

# print(l[-1][1:-1] + l[-1][-1][:-1][::-1])

'''Istifadəçi sizə "5 salam" şəklində solda ədəd, ortada, boşluq, 
sağda isə bir input verəcək. Buna əsasən sağdakı yazını istifadəçinin 
qeyd etdiyi ədəd qədər yazıb, istifadəçiyə qatarın. Örnək yuxaridakı 
inputun outputu salam salam salam salam salam'''

# greeting = '5 salam'
# greetingList = greeting.split(' ')
# print(greetingList)
# word = greetingList[1]
# count = int(greetingList[0])

# print((word + ' ') * count)

'''İstifadəçinin daxil etdiyi cümlədəki sözləri tərsinə çevirilmiş şəkildə istifadəçiyə qaytarın. 
Örnək: Input: This is an example! Output: sihT si na !elpmaxe'''

sentence = 'This is an example!'
words = sentence.split(' ')
reversed_words = [word[::-1] for word in words]
print((' ').join(reversed_words))

'''
Fermada keçinin sırasını tapın
Fermadan bir at çıxarıb, ən sağdan bir toyuq əlavə edin  soldan bir keci əlavə edin
Fermanın yarısını dinamik bir şəkildə silin
Yeni gələn ['at', 'qoyun', 'inek', 'inek', 'qoyun'] heyvanları fermaya əlavə edin
Fermadakı heyvanları tərsinə sıralayın
Fermadaki ineklerin sayinin umumki fermanin nece faiz oldugunu tapin
Oxsar fermadan isteyen basqa bir fermere fermamizin kopyasini verin
Fermani temizleyin'''

# ferma = ['at', 'qoyun', 'inek', 'at', 'inek', 'qoyun', 'at', 'at', 'keci'] 

# ferma.remove('at').insert(0, 'keci').append('toyuq')
# print(ferma.index('keci'))
# ferma.clear()
# newFarm = ferma.copy()
# newF = ferma[:(len(ferma)//2)]
# ferma.reverse()
# ferma.extend(['at', 'qoyun', 'inek', 'inek', 'qoyun'])
# bigFarm = ferma * 3
# print(bigFarm)
# print(ferma.count('inek')*100/len(ferma))

''' '''

# ID = 'AZE1599511'

# if len(ID) == 10:
#     if ID[0:3].isalpha():
#         if ID[0:3].isupper():
#             if ID[3:].isnumeric():
#                 print('Seriya nomresi duzgun daxil edilmisdir')
#             else:
#                 print('3-cu xarakterden sonra yalniz reqemler olmalidir')
#         else:
#             print('Seriya nomresinin evveli boyuk herflerle yazilmalidir')
#     else:
#         print('Seriya nomresinin ilk uc xarakteri herflerden ibaret olmalidir')
# else:
#     print('Seriya nomresinin uzunlugu 10 xarakterden ibaret olmalidir')

'''
1. 2000 AZN altına kredit verilmir
2. 2000 - 10000 AZN arası 5 faiz
3. 10000 - 50000 AZN arası 4 faiz
4. 50000 - 200000 AZN arası 3 faiz
5. 200000 - 500000 AZN arası 2 faiz
6. 500000 AZN yuxarısında kredit verilmir
'''

# credit = 600000

# if credit < 2000:
#     print('Size kredit dusmur')
# if credit < 10_000:
#     print('Sizin yekun borcunuz', credit*1.05, " AZN olacaqdir")
# if credit < 50_000:
#     print('Sizin yekun borcunuz ', credit*1.04, " AZN olacaqdir")
# if credit < 200_000:
#     print('Sizin yekun borcunuz ', credit*1.03, " AZN olacaqdir")
# if credit < 500_000:
#     print('Sizin yekun borcunuz ', credit*1.02, " AZN olacaqdir")
# if credit > 500_000:
#     print('Qeyd olunan meblegde kredit verilmir')

'''
1. Ən az 8 ən çox 40 characterdən ibarət olmalıdır
2. Ancaq ingilis sriflərindən ibarət olmalıdır
3. Ancaq hərf və rəqəmlərdən ibarət olmalıdır
4. Mütləq şəkildə ən az bir böyük və bir kiçik hərf olmalıdır
5. Mütləq şəkildə ən az 1 hərf və ən az 1 rəqəm olmalıdır
'''

# password = input('Sifreni daxil edin: ')

# if len(password) <8 or len(password) > 40:
#     print('sifrenin uzunlugu en az 8 en cox 40 olmalidir')
# elif not password.isascii():
#     print('sifre yalniz ingilis herflerinden ibaret olmalidir')
# elif not password.isalnum():
#     print('sifre herf ve reqemlerden ibaret olmalidir')
# elif password.isupper() or password.islower():
#     print('sifrede en az bir b[ywk ve bir kicik herf olamlidir')
# elif password.isalpha() or password.isnumeric():
#     print('sifrede en az bir herf ve bir reqem olmalidir')
# else:
#     print('sifre qebul olundu')

'''A task'''

# text = 'Salyut 1 kosmosa göndərilən ilk kosmik stansiya idi. \
# O, 1971-ci ilin aprelində Sovet İttifaqı tərəfindən orbitə \
# və 1971-ci ilin oktyabr ayına qədər kosmosda qaldı. \
# müddətdə onu ekipajlarla birlikdə iki kosmik gəmi \
# ziyarət etdi. Salyut 1-in məqsədi kosmik stansiyanın necə \
# işlədiyini öyrənmək və sınaqdan keçirmək idi. İkinci məqsəd \
# kosmosda uzun müddət qalmağın insan orqanizminə necə təsir \
# etdiyini öyrənmək idi. Onun bir sıra problemləri var idi, lakin ondan gələcək stansiyalara kömək edən çox şey öyrənildi.'

# print('kömək' in text and 'həyat' in text and 'sınaq' in text)

# print(text.index('kosmos'), text.rindex('kosmos'))

# print(text.startswith('Salyut') and text.endswith('ildi.'))

'''1-dən 100-ə kimi olan bütün ədədlərin toplamını tapın '''

# i = 1
# result = 0

# while i < 100:
#     result += i
#     i += 1
# print(result)

# for i in range(0, 100):
#     result += i
#     i+=1
# print(result)

''' 100000-dən aşağı doğru gedərək 9999-a bölünən ilk ədədi konsolda göstərin. '''

# i = 100_000

# while i > 0:
#     if i%9999 == 0:
#         print(i)
#         break
#     i -= 1

# for i in range(100000, 0):
#     if i%9999 == 0:
#         print(i)
#         break
#     i -= 1

''''Men her gun Python oyrenirem’ bu stringin saitlər çıxarılmış vəziyyətini konsolda göstərin. '''

# txt = 'Men her gun Python oyrenirem'
# vowels = 'aioue'
# i = 0
# res = ''

# for i in txt:
#     if i not in vowels:
#         res += i
# print(res)

# while i < len(txt):
#     if txt[i] not in vowels:
#         res += txt[i]
#     i+=1
# print(res)

'''(Orta) İstifadəçinin girdiyi cümlədə neçə heca olduğunu deyən program hazırlayın. 
Hecaların sayını tapmaq üçün saitlərdən istifadə edin.'''

# sentence = input('Cumleni daxil edin: ')
# vowels = 'aioue'
# res = ''

# for i in sentence:
#     if i in vowels:
#         res += i
# print('Daxil etdiyiniz cumlede heca sayi: ', len(res))

'''Aşağıdakı result listinin 0-cı 
indexinə numbers listi daxilindəki müsbət ədədlərin cəmini, 
1-ci indexə isə mənfi ədədlərin cəmini yerləşdirin. '''

# result = [0, 0]
# numbers = [10.2, -32, -5.45, 32, 7, 43, -24.06, -4, -6.33, 62]

# for i in numbers:
#     if i > 0:
#         result[0] = result[0] + i
#     else:
#         result[1] = result[1] + i
# print(result)

''' İstifadəçinin girdiyi ədədi tək ədədlərdən ibarət 
tərsinə çevirilmiş list şəklinə salın. Listin bütün 
elementlərinin integer olmasına diqqət edin.: '''

# num = input('Ededi daxil edin: ')
# res = []

# for i in num:
#     res.append(int(i))
# res.reverse()
# print(res)

'''list içərisindəki ən böyük və ən kiçik ədədi dinamik şəkildə tapın.'''

# numbers = [10.2, -32, -5.45, 32, 7, 43, -24.06, -4, -6.33, 62]
# numbers.sort()
# print(numbers[0], numbers[-1])

# # maxNum = max(numbers)
# # minNum = min(numbers)
# # print(maxNum, minNum)

'''
5. Aşağıda tələbələrin semestr nəticələri qeyd edilmişdir. Buna əsasən qeyd olunmuş 
statistik məlumatları eyni anda print edin.
    1. Tələbə sayı
    2. Ümumi ortalama.
    3. Kəsilən tələbələrin ümumi faizi (51- qiymət alanlar)
    4. Yüksək nəticə göstərən tələbələrin ümumu faizi (80+ qiytət alanlar)
'''
# r = [31, 38, 69, 83, 83, 56, 38, 41, 96, 48, 43, 60, 49, 47, 73, 60, 69, 96, 50, 74]
# res = 0
# failed = []
# successful = []
# for i in r:
#     res += i
#     if i < 51:
#         failed.append(i)
#         failedPercent = len(failed)*100//len(r)
#     elif i > 80:
#         successful.append(i)
#         succededPercent = len(successful)*100//len(r)

# print('Telebe sayi:', len(r),'\n', 'Umumi ortalama: ', res//len(r), '\n',\
# 'Kesilen telebelerin faizi:', failedPercent, '\n' \
# 'Ugurlu telebelerin faizi:', succededPercent )

'''
Aşağıdakı fake databazanı istifadə edərək login sistemi qurun.
1. istifadəçi username səhv girərsə belə bir istifadəçi yoxdur deyin
2. şifrəni səhv girərsə şifrəniz yanlışdır deyin
3. əgər blok olunubsa siz daxil ola bilməzsiniz deyin
4. əgər hər şey qaydasındadırsa “filankes giriş etdiniz” deyin
'''

users = [
    {'name': 'Akif', 'username': 'a456', 'password': '1234', 'blocked': False},
    {'name': 'Senan', 'username': 'sm_ov', 'password': '5423s', 'blocked': False},
    {'name': 'Kamal', 'username': 'km123', 'password': '34-kk-325', 'blocked': True}
]

# username = input('Istifadeci adinizi daxil edin: ')
# user_found = None
# for i in users:
#     if username == i['username']:
#         user_found = i

# if not user_found:
#     print('Bele bir istifadeci yoxdur')
#     exit()

# password = input('Sifrenizi daxil edin: ')
# if password == user_found['password']:
#     if user_found['blocked'] == False:
#         print(user_found['name'], ', giris etdiniz')
#     else:
#         print('Siz daxil ola bilmezsiniz')
# else:
#     print('Sifre yalnisdir')

'''
2. Bunları terminalda göstərin
    1. İstifadəçinin boyunu artırın
    2. Telefonun markasını dəyişərək Samsung edin
    3. İstifadəçinin adını silin
    4. İstifadəçinin ilk sifarişini silin
    5. İstifadəçinin sifarişlərinin başına ball əlavə edin
    6. Sonuna headphones əlavə edin
'''
# user = {
#     'name': 'Elnur',
#     'height': 179,
#     'phone': {
#         'model': 'Iphone',
#     },
#     'orders': ['book', 'mouse', 'mousepad']
# }

# user['height'] += 10
# user['phone']['model'] = 'Samsung'
# del user['name']
# del user['orders'][0]
# user['orders'].insert(0, 'ball')
# user['orders'].append('headphones')
# orders = user['orders']
# orders.append('headphones')
# print(user)

'''
Listi dinamik olaraq ["Resul Serifov", 25] vəziyyətinə gətirin
'''
# info = ["Resul", "Serifov", 35]

# info[0] = info[0] + " " + info[1]
# info[2] -= 10
# info.pop(1)
# print(info)

''' 
5. Dictionary əsasən istifadəçi sizə məhsul adı girəcək. Bu məhsulun 
mağazada olan qiymətini göstərən proqram hazırlayın. Girilən 
məhsul mağaza da olmadığı halda "None" qaytarın.
6. Mağazaya yeni məhsullar və qiymətlərini əlavə edin.
7. Mağazada nə qədər məhsul olduğunu göstərin
8. Məhsulların qiymətini 30% artırıb yeni qiymətləri mağazaya əlavə edin.
'''

# shop = {
# 	"t-shirt" : 59.00,
# 	"jeans" : 75.00,
# 	"sweatshirt" : 60.00, 
# 	"shoe" : 124.99, 
# 	"jacket" : 154.90
# }

# product = input('Axtardiginiz mehsulun adini daxil edin: ')
# # product_existence = None

# print(shop.get(product))

# newProducts = {
#     "bra" : 54.0,
#     "sock" : 12.50
# }

# shop.update(newProducts)
# print(len(shop))


# for i in shop:
#     shop[i] *= 1.3
# print(shop)

''' İstifadəçinin girdiyi cümlədəki sözləri tərsinə çevirilmiş şəkildə istifadəçiyə qaytarın. '''

# sentence = "This is an example!"
# sent =  sentence.split(' ')

'''
[2384, 12385, 13226, 653, 12362423] list içərisindəki ədədlərin 
key olduğu və value-ların həmin ədədlərin rəqəm sayı olduğu bir dictionary hazırlayın
'''

# nums = [2384, 12385, 13226, 653, 12362423]
# numAndLens = {}
# for i in nums:
#     num = i
#     numLen = len(str(i))
#     numAndLens[i] = numLen

# numAndLens = {num: len(str(num)) for num in nums}
# print(numAndLens)

''' '''

# n = [1, 2, 3, 4, 5, 6, 7]

# result = [num**3 for num in n if num%2]

# print(result)

# products = [
#     {'title': 'a', 'price': 2800},
#     {'title': 'b', 'price': 2500},
#     {'title': 'c', 'price': 3800},
#     {'title': 'd', 'price': 3400},
#     {'title': 'e', 'price': 1500}
# ]

# filteredProducts = [pr['title'] for pr in products if 2000 < pr['price'] < 3500]

# print(filteredProducts)

# words = ['qələm', 'əmanət', 'gözəllik', 'insan']

# changedWords = [w.replace('ə', 'e') for w in words if 'ə' in w]

# changedWordsDict = {w: w.replace('ə', 'e') for w in words if 'ə' in w}

# print(changedWordsDict)

'''
-100-dən müsbət 100-ə qədər ədədlər arasında 7-yə 
bölünən ədədlərin 3-ə vurulmasından ibarət bir list qurun. 
Bunun üçün range və list comprehensions istifadə edin.
'''

# dividedBySeven = [i*3 for i in range(-100, 101) if i%7 == 0]

# print(dividedBySeven)

'''
Istifadəçi sizə bir input vasitəsilə bunun kimi bir məlumat girəcək:
input: firstname Elcin, username elchina, birthday 18-08-2000
Bu inputa əsasən yuxarıdakı dictionary-ni update edin ve istifadəçiye gosterin. 
Misal yuxarıdakı inputa əsasən dictionary son halı aşağıdakı kimi olacaq.

user_info = {
    'firstname': 'Elcin',
    'lastname': 'Huseynov',
    'username': 'elchina',
    'password': '12345',
    'birthday': '18-08-2000'
}
'''
# user_info = {
#     'firstname': 'Elvin',
#     'lastname': 'Huseynov',
#     'username': 'elivin_h_ov',
#     'password': '12345',
#     'birthday': '19-08-1997'
# }

# newData = input('Enter new info: ')

# newDataList = newData.split(' ')

# firstname = newDataList[newDataList.index('firstname')+1]
# username = newDataList[newDataList.index('username')+1]
# birthday = newDataList[newDataList.index('birthday')+1]

# user_info['firstname'] = firstname
# user_info['username'] = username
# user_info['birthday'] = birthday

# print(user_info)

'''
Aşağıdakı kodda sual işarələrinin yerini doldurun. 
Örnək outputa nəzər yetirərək nəticənin həmin formada alınmasına diqqət edin.
'''

# animal = input('Ferma admin paneline xos geldiniz. Axtardiginiz heyvani daxil edin: ')
# farm = ('inek', 'keci', 'at', 'at', 'at', 'keci', 'at', 'qoyun', 'at', 'keci', \
# 'at', 'toyuq', 'inek', 'keci', 'at', 'toyuq', 'inek', 'toyuq', 'inek', 'toyuq', \
# 'keci', 'toyuq', 'qoyun', 'keci', 'keci', 'qoyun', 'at', 'qoyun', 'inek', 'at', \
# 'keci', 'qoyun', 'inek', 'keci', 'qoyun', 'inek', 'toyuq', 'at', 'toyuq', 'keci', \
# 'inek', 'toyuq', 'at', 'toyuq', 'at', 'keci', 'qoyun', 'keci', 'keci', 'inek')
# qiymetler = {'at': 1200, 'inek': 900, 'toyuq': 50, 'keci': 300, 'qoyun': 150}

# text = f"""
# Axtarilan Heyvan: {animal}
# Fermadaki {animal} sayi:  {farm.count(animal)} 
# Diger heyvanlara olan faizi: {farm.count(animal) * 100 // len(farm)} %
# {animal}in umumi qiymeti: {qiymetler[animal] * farm.count(animal)} AZN
# """
# print(text)

'''
listdən yeni bir dictionary hazırlayın. Həmin dictionarynin keyləri ədədlər, 
valueləri isə mübət və ya mənfi yazılı stringlər olacaq.
Ornək: {10: 'musbet', -21: 'menfi', ...}
'''
# nums = [1, 32, 42, -41, -5, 3, 31, 7, -8, 14, 6, -79 ]

# negAndPos = {n: ('musbet' if n > 0 else 'menfi') for n in nums}

# print(negAndPos)

'''Aşağıdakı listdən istifadə edərək qrammatik səhvi düzəldib print edin'''

# cumle = "sehvelerden en yaxsi sehife bu sehvedir"
# l = ["sehve", "sehife"]

# duzgunCumle = cumle.replace(*l)

# print(duzgunCumle)

'''Verilən məlumatlara əsasən hansı qardaş hansına nə qədər pul verməli olduğunu göstərən kod yazın. 
Örnək outputlar: Boyuk qardas kiciye 2700 manat vermelidir və ya Kicik qardas boyuye 3700 manat vermelidir'''

# ferma = ('at', 'inek', 'inek', 'keci', 'qoyun', 'qoyun', 'qoyun', 'inek', 'at', 'toyuq', \
# 'inek', 'inek', 'keci', 'at', 'keci', 'qoyun', 'inek', 'at', 'toyuq', 'inek', 'keci', \
# 'keci', 'inek', 'toyuq', 'inek', 'toyuq', 'keci', 'toyuq', 'at', 'keci', 'at', 'keci', 'inek', \
# 'qoyun', 'keci', 'at', 'qoyun', 'inek', 'inek', 'toyuq', 'at', 'at', 'toyuq', 'at', 'inek', 'toyuq', 'inek', 'toyuq', 'toyuq', 'qoyun')
# qiymetler = {'at': 1200, 'inek': 900, 'toyuq': 50, 'keci': 300, 'qoyun': 150}

# totalPriceOne = 0
# totalPriceTwo = 0

# for i in ferma[:len(ferma)//2]:
#     totalPriceOne += qiymetler[i] 

# for j in ferma[len(ferma)//2:]:
#     totalPriceTwo += qiymetler[j]

# if totalPriceOne > totalPriceTwo:
#     print('Boyuk qardas kicik qardasa', (totalPriceOne - totalPriceTwo) // 2, 'manat vermelidir')
# else:
#     print('Kicik qardas boyuk qardasa', (totalPriceTwo - totalPriceOne) // 2, 'manat vermelidir')

''' '''

# ededler = [1, 2, -3, 4, -5, -6]
# n = []

# for i in ededler:
#     if i%2==0:
#         n.append('cut')
#     else:
#         n.append('tek')

# pos_or_neg = ['tek' if i%2 else 'cut' for i in ededler]

# print(pos_or_neg)

# pos_or_neg = {i: ('menfi' if i<0 else 'musbet') for i in ededler}

# print(pos_or_neg)

''' '''

# b = bin(344)
# print(b)

# print(bin(ord('N')))
# print(chr(78))

# dec = 344
# print(bin(dec), "in binary.")
# print(oct(dec), "in octal.")
# print(hex(dec), "in hexadecimal.")

'''Istifadəçinin girdiyi stringi binary şəklində göstərin. Örnək:'''

# sentence = input('Bir cumle daxil edin: ')
# binary_number = ''

# for i in sentence:
#     binary_number += (bin(ord(i))).lstrip('0b') + ' '

# print(binary_number)

'''İstifadəçinin girdiyi mətn daxilindəki hərflərin ingilis əlifbasındakı 
sırasına qarşılıq gələn ədədlərlə dəyişdirilmiş şəkildə göstərin.'''

# letter = input('Herfler daxil edin')
# letter_alphabet = ''

# for letter in letters.lower():
#     if letter.isalpha():
#         letter = str(ord(letter)-96)
#         letter_alphabet += letter + ', '
#     else:
#         letter_alphabet += letter
# print(letter_alphabet)

'''FORMAT''' 

# lang = 'Python'
# thought = '{} is the best programming language ever'.format(lang)

# format_test = 'Kart sahibi: {:*<8}'.format('Zuleykha'[:4])
# format_test = 'Kart sahibi: {:*<8.3}'.format('Zuleykha')
# format_test = 'Kart sahibleri: {1:*<8.3}, {0:*<8.3}'.format('Zuleykha', 'Javad') - indexlerin yerini qarisiq yazmaq
# Adli arqumentler 
# format_test = 'Kart sahibinin melumatlari: {ad:*<8.3} {soyad:*<8.3}'.format(ad='Zuleykha', soyad='Hasanova')
# format_test = '{:*^40}'.format('Zuleykha')
# format_test = '{0} ve {1} komandalari yarisdilar ve {0} komandasi qalib geldi'.format('python', 'c#')
# format_test = '{lang1} ve {lang2} komandalari yarisdilar ve {lang1} komandasi qalib geldi'.format(lang1='python', lang2='c#')

# format_test = 'Musterinin borcu: {}'.format(140/3)
# format_test = 'Musterinin borcu: {:.3}'.format(14/3) outputu - 4.67
# format_test = 'Musterinin borcu: {:.3f}'.format(14/3) outputu - 4.667
# format_test = 'Musterinin borcu: {:,}'.format(1488*1389) 
# format_test = 'Musterinin borcu: {:.2%}'.format(3/4) 2 - sifirlarin sayi 
# print(format_test)

'''2 input alacaqsiniz. Birinde reqemler ve digerinde reqemlerin uygun geleceyi nomre yazilisi olacaq. 
Hemin nomre yazilisi icerisindeki diesleri verilen reqemlerle evezlemelsiniz''' 

# number = '79052479075'
# sequence = "+# ### ### ## ##"
# final_number = ''
# l = [1, 2, 'sdf', 545]

# for i in sequence:
#     if i == "#":
#         for j in number:
#             final_number = final_number + j
#     else:
#         final_number = final_number + i

# print(final_number)

# print('+# ### ### ## ##'.replace('#', "{}").format(*number))

'''
n1 = 15 və n2 = 13. Başqa bir variable yaratmadan aşağıdakı sual işarələrini doludurun.
print('%s + %s = %s' ??????????) 
Output bu şəkildə olmalıdır: 15 + 13 = 28
'''
# n1 = 15 
# n2 = 13
# result = ('%s + %s = %s' % (n1, n2, n1+n2))

'''userData variablendan istifadə edərək aşağıdakı outputu çıxarın
Hormetli A. E. Serifov, sizin 5326-6644********** nomreli
kredit kartiniza 341.35AZN odenis edildi.
Umumi 12,543AZN teskil eden borcunuzdan 2.72% borc silinmisdir!
'''

# userData = [
#     {
#         'debt': 12543,
#         'payed': 341.346742,
#         'payed_percent': 0.027214122777644904,
#         'card_number': '5326-6644-1234-6432',
#         'first_name': 'Akif',
#         'last_name': 'Serifov',
#         'father_name': 'Elekber',
#     }
# ]

# print(userData[0]['first_name'][0], userData[0]['father_name'][0], userData[0]['last_name'])

'''Stringlərin ilk hərfini böyüdüb, birləşdirən bir funksiya hazırlayın. '''

# def upunion(*args):
#     return ''.join([name[0].upper() for name in args])

# unions = [
#     ['musteqil', 'dovletler', 'birliyi'],
#     ['milli', 'meclis']
# ]

# union_names = [upunion(*union) for union in unions]
# print(union_names)

'''Kitabi sehve-sehve oxumalisan ki, orgenesen, sehve='sehife', orgen='oyren')-Kitabi sehife-sehife oxumalisan ki, oyrenesen''' 

# def correction(text, *kwargs):
#     for key, value in kwargs.items():
#         text = text.replace(key, value)
#     return text

# print(correction('Kitabi sehve-sehve oxumalisan ki, orgenesen', sehve='sehife', orgen='oyren'))
 
# print(correction('Kitabi sehve-sehve oxumalisan ki, orgenesen'))

'''Birinci argument ilk qiyməti, ikinci argument isə yeni qiyməti göstərir. 
Yeni qiymətin ilkindən neçə faiz fərqləndiyini print edən funksiya düzəldin.
find_percent(200, 60) # output: qiymet 70% azalmisdir 
find_percent(100, 150) # output: qiymet 50% artmisdir '''

# def find_percent(price_one, price_two):
#     if price_one > price_two:
#         print('Qiymet', int(100-(price_two*100/price_one)), '%', 'azalmisdir')
#     else:
#         print('Qiymet', int(price_two*100/price_one - 100), '%', 'artmisdir' )

# find_percent(200, 60)

'''Girilən listin ən böyük ədədindən ən kiçiyini çıxarıb, nəticə verən bir funksiya hazırlayın.
big_dif_sml([6, 3, 8, 9, 2]) => 7 # en  boyuk 9, en kicik 2'''

# def find_biggest (numbers):
#     numbers.sort()
#     diff = numbers[-1] - numbers[0]
#     return diff

'''üç rəqəmli ədədləri sözə çevirən bir funksiya hazırlayın. Örnək output:
eded_cevir(658) => altı yüz əlli səkkiz'''


# hundreds = ['yuz', 'iki yuz', 'uc yuz', 'dord yuz', 'bes yuz', 'alti yuz', 'yeddi yuz', 'sekkiz yuz', 'doqquz yuz']
# decs = ['on', 'iyirmi', 'otuz', 'qirx', 'elli', 'altmis', 'yetmis', 'seksen', 'doxsan']
# single_nums = ['bir', 'iki', 'uc', 'dord', 'bes', 'alti', 'yeddi', 'sekkiz', 'doqquz']

# def def_numb (number):
#     result = ''
#     for i in range(1, 10):
#         if str(number)[0] == str(i):
#             result = result + hundreds[i-1]
#     for i in range(1, 10):
#         if str(number)[1] == str(i):
#             result = result + ' ' + decs[i-1]
#     for i in range(1, 10):
#         if str(number)[2] == str(i):
#             result = result + ' ' + single_nums[i-1]
#     return result

# print(def_numb(568))        

''' '''
# def rev_num (number):
#     res = []
#     for i in str(number):
#         res += i
#     res.reverse()
#     result = int("".join(res))
#     return result


# def rev_num (number):
#     number = str(number)[::-1]
#     number = int(number)
#     return number

# def sum_of_nums(*args):
#     summed = 0
#     for num in args:
#         summed += rev_num(num)
#     return summed

# print(sum_of_nums(14, 123, 512, 12, 78, 41, 457))

# Lambda
# rev_num = lambda num: int(str(num)[::-1])
# print(rev_num(2548))

''' '''
# formula = lambda num: int(str(num)[::-1])
# print(formula(4545))
# F = m * a

'''Mətnlər üzərində işləmək üçün böyük bir program hazırlamsınız ancaq sonradan öyrənirsiniz ki, 
programı çalışdıracaq müştərinin komputeri azərbaycan şriftlərini dəstəkləmir. Bütün funksiyaları 
yenidən yazmaq yerinə elə bir dekorator yazın ki, həmin funksiyaların return etdiyi stringlərdəki 
aze hərfləri ingilis qarşılığıyla dəyişdirilmiş olsun. Örnək:
@ing_cevir
def salam_ver(ad, soyad):
	return 'Salam hörmətli {} {}, necəsiniz?'.format(ad, soyad)

print(salam_ver('Arif', 'Həsənov'))
# output: Salam hormetli Arif Hesenov, necesiniz?
''' 

# sentence = 'Özümü təqdim edim. Mənim adım Züleyxa, soyadım Həsənovadır.'

# def convert_to_ascii_letters (text):
#     letters_dictionary = {
#     'ə': 'e',
#     'ı': 'i',
#     'ö': 'o',
#     'ü': 'u',
#     'ğ': 'g',
#     'Ö': 'O',
#     'Ü': 'U',
#     'Ğ': 'G'  
#     }
#     for item in letters_dictionary:
#         for letter in text:
#             if letter == item:
#                 text = text.replace(item, letters_dictionary[item])
#     return text

# print(convert_to_ascii_letters(sentence))

# OR

# def convert_to_ascii_letters (text):
#     letters_dictionary = {
#     'ə': 'e',
#     'ı': 'i',
#     'ö': 'o',
#     'ü': 'u',
#     'ğ': 'g',
#     'Ö': 'O',
#     'Ü': 'U',
#     'Ğ': 'G'  
#     }
#     result = ''
#     for l in text:
#         result += letters_dictionary.get(l, l)
#     return result

# def convert_ascii(f):
#     def wrapper(*args, **kwargs):
#         result = f(*args, **kwargs)
#         result = convert_to_ascii_letters(result)
#         return result
#     return wrapper

# @convert_ascii
# def introduction():
#     return 'Zəhmət olmasa, özünüzü təqdim edin'


''' '''

# numbers = [2, 4, 6, 8, 10]
# def square(number):
#     return number * number

# squared_numbers_iterator = map(square, numbers)
# squared_numbers = list(squared_numbers_iterator)
# print(squared_numbers)

# def add(x, y):
#     return x + y

# def calculate(func, x, y):
#     return 20 + func(x, y)

# result = calculate(add, 4, 6)
# print(result)  

'''Lambda ilə factorial hesablayan recursive function hazırlayın.'''

# factorial = lambda n: 1 if n == 0 else n * factorial(n-1)

''' Aşağıdakı ədədlər arasında rəqəmlərinin cəmi ən yüksək olanı çıxarın. '''

# numbers = [85856, 73930, 95298, 57870, 99688, 92907, 13075, 12905, 52948, 97687, 10832,\
# 78757, 99502, 65889, 34618, 59109, 83419, 31486, 94522, 34400]

# def find_digits_sum (number):
#     sum = 0
#     for i in str(number):
#         sum += int(i)
#     return sum

# def my_max (iterable):
#     biggest_iter = iterable[0]
#     for i in iterable:
#         if i > biggest_iter:
#             biggest_iter = i
#     return biggest_iter

# def my_max (iterable, key=None):
#     biggest_iter = iterable[0]
#     biggest_iter_value = key(biggest_iter) if key else biggest_iter
#     for i in iterable:
#         i_value = key(i) if key else i 
#         if i_value > biggest_iter_value:
#             biggest_iter_value = i_value
#             biggest_iter = i
#     return biggest_iter

# print(my_max(numbers, find_digits_sum))

# find_digits_sum_list = map(find_digits_sum, numbers)
# print(list(find_digits_sum_list))

'''Outputdan bir hissə:
Babək 1100 manat dəyərində Iphone götürüb'''

# children = ['Arif', 'Babek', 'Hesen', 'Rufet', 'Sahin', 'Eldeniz', 'Turan', 'Sahmar', 'Kamal', 'Ruslan']
# gifts = ['Ball', 'Iphone', 'Bicycle', 'Ball', 'Piano', 'Bicycle', 'Socks', 'Play Station', 'Ball', 'Socks']
# prices = {'Ball': 10, 'Iphone': 1100, 'Bicycle': 500, 'Piano': 1500, 'Sock': 10, 'Play Station': 1200}  

# for i in range(len(children)):
#     result = ''
#     result += children[i] + 

'''Aşağıdakı dataları tiplərinə görə sıralamaq lazımdır. Sıra bu şəkildə olacaq: 
Listlər, Dictonarylər, Booleanlar, İntegerlər, Floatlar, Stringlər.'''

# types_list = [{'a': 1, 'b': 2}, 5, 7.8, 'asdf', 23, ['a', 'b'], True,  False] 

# for typ in types_list:
#     types_list_by_sequence = []
#     if type(i) == list:
#         types_list_by_sequence += i


# adlar = ['Aslan', 'Husniyye', 'Behram', 'Cavad']
# telefonlar = ['Xiaomi', 'iPhone', 'iPhone', 'Samsung']
# address = ['Xirdalan', 'Xirdalan', 'Sebail', 'Masazir']

# res = list(filter(lambda x: x%2 == 0, range(0, 10)))
# res = list(map(lambda x: x%2 == 0, range(0, 10)))
# print(res)

