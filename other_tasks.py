baliqlar = {
    'qelseme teneffusu', '2 kamerali urek', 'uzgec', 'korteks yoxdur',
    'yumurtlama', 'dis yoxdur', '4 ayaq'
}

cuculer = {
    'toraks teneffusu', 'urek yoxdur', '6 ayaq',
    'korteks vardir', 'beyin yoxdur', 'yumurtlama', 'metamorfoz', 
    'dis yoxdur'
}

amfibialar = {
    'qelseme teneffusu', 'agciyer teneffusu', 'uzgec', '4 ayaq', 
    '2 kamerali urek', '3 kamerali urek', 'metamorfoz', 'koteks vardir',
    'yumurtlama', 'dis yoxdur'
}

surunenler = {
    'agciyer teneffusu', '3 kamerali urek', '4 ayaq', 'korteks vardir', 'yumurtlama',
    'dis var'
}

quslar = {
    'agciyer teneffusu', '4 kamerali urek', 'korteks vardir',
    'yumurtlama', 'dis yoxdur'
}

memeliler = {
    'agciyer teneffusu', '4 kamerali urek', '4 ayaq', 'korteks vardir',
    'dogma', 'dis vardir'
}
hi = {'yes', 'no', 'maybe'}

sinifler = {
    'baliqlar': baliqlar,
    'cuculer': cuculer,
    'amfibialar': amfibialar,
    'surunenler': surunenler,
    'quslar': quslar,
    'memeliler': memeliler,
}
'''
1. Quşların xüsusiyyətlərinə `"2 ayaq"` əlavə edin.
2. Balıqların xüsusiyyətlərindən `"4 ayaq"` məlumatını çıxarın
3. Amfibialar ilə cücülərin ortaq cəhətlərini göstərən kod yazın
4. Balıqlar ilə amfibiaların fərqli cəhətlərini göstərən kod yazın
5. Balıqlar ilə heç bir ortaq cəhətə sahib olmayan sinifi tapan kod yazın
6. Quşlar ilə ən çox ortaq cəhətə sahib olan sinifi tapın
7. İstifadəçi input ilə sizə bəzi özəlliklər girəcək. Siz həmin özəlliklərə əsasən heyvanın 
   hansı sinifə aid ola biləcəyini təxmin edən kod yazın. Örnək

`input: dis yoxdur, agciyer teneffusu, korteks vardir` 
`output: Bu heyvan quslar sinifine aid ola biler`
'''

# quslar.add('2 ayaq')
# baliqlar.discard('4 ayaq')
# print(amfibialar.intersection(cuculer))
# print(amfibialar.difference(baliqlar))

# no_intersection = True
# for ad, sinif in sinifler.items():
#     if baliqlar.isdisjoint(sinif):
#         print(baliqlar, 'sinfi baliqlar ile hec bir ortaq xususiyyete malik deyil')
#         no_intersection = False
# if no_intersection:
#     print('baliqlar sinfi ile ortaq xususiyyeti olmayan sinif yoxdur')

# max_count = -1
# max_name = ''
# for ad, sinif in sinifler.items():
#     count = len(sinif.intersection(quslar))
#     if count > max_count and sinif != quslar:
#         max_name = ad
#         max_count = count
# print(f'Quslar ile en cox ozelliye sahib sinif {max_name} sinfidir')

# text = input('ozellikleri daxil edin:'  )
# spes = text.split(', ')
# spes = set(spes)

# for ad,sinif in sinifler.items():
#     if spes.issubset(sinif):
#         print(f'bu canli {ad} sinifine aid ola biler')   

# Error handling 

# bolunen = input('Bolunen: ')
# bolen = input('Bolen: ')

# def bolme(a, b):
#     if int(a) < 0:
#         # raise ValueError('bolunen menfi ola bilmez!')
#         raise Exception('bolunen menfi ola bilmez!')
#     result = int(a) / int(b)
#     print('Netice:', result)

# bolme(bolunen, bolen)

# try:
#     bolme(bolunen, bolen)
# except ValueError as error_message:
#     print(f'Ancaq eded daxil etmek olar! Xeta mesaji: {error_message}')
# except ZeroDivisionError:
#     print('Hec bir eded 0-a bolune bilmez!')
# except Exception as error_message2:
#     print(f'Bilinmeyen bir error bas verdi! Xeta mesaji: {error_message2}')
# finally:
#     print('Program bitdi!')


# try:
#     animals = input('Heyvanlari girin: ').split(', ')
#     if not 3 < len(animals) < 10:
#         raise ValueError('Say 3le 10 arasinda olmalidir.')
#     prices = { 'inek': 500, 'toyuq': 50, 'qoyun': 120, 'at': 900, 'keci': 210 }
#     print('Umumi qiymet:', sum(map(lambda animal: prices[animal], animals))) 
# except KeyError:
#     print('You may have made following mistakes: \n\
# You eneterd a type other than string \n\
# You entered animal names out of the list you have given \n\
# You entered the names not splitted by comas')
# except Exception as error_message:
#     print(f'bilinmeyen error bas verdi: {error_message}')


'''
DIVIDER
'''

# file = open(r'D:\Users\Ujer\Desktop\Tools\text.txt', encoding='UTF-8')
# file = open('text.txt', encoding='UTF-8')
# content = file.read()

# print(content.splitlines())

# print('content:', file.read(10))
# file.read(10)
# print('content:', file.read(10))

# file = open('test.txt', encoding="UTF-8")
# cont = file.read()

# file_two = open(r'C:\Users\zuley\Desktop\gallery\far_one.txt', encoding="UTF-8", mode='w')
# # content = file_two.read()
# file_two.write('More')
# file_two.close()
# # print(content)

# # file_three = open('writing.txt', encoding="UTF-8", mode='w')
# # file_three.write('Writing test')
# # file_three.close()

# # file_f = open('writings.txt', encoding="UTF-8", mode='x')
# # file_f.write('Writings test')
# # file_f.close()

# # file_f = open('writing.txt', encoding="UTF-8", mode='a')
# # file_f.write('Adding some text')
# # file_f.close()

# file_f = open('writing.txt', encoding="UTF-8", mode='a')
# # first_ten = file_f.read(10)
# # file_f.seek(0)
# # t = file_f.read()
# # file_f.write('Trying again')
# # file_f.close()
# # file_f.close()
# # print(t)
# txt = 'Hello World!'
# file_f.write(txt)
# file_f.close()

"""
Modlar:
r - oxuma (default)
w - yazma
x - yazma (errorla)
a - yazma (elave)
r+ - oxuma + yazma
w+ - yazma + oxuma
x+
a+
"""

# text = 'salam ' * 100

# file = open('text.txt', mode='w', encoding='UTF-8')
# file.write(text)
# file.close()

# file = open('text.txt', mode='r', encoding='UTF-8')
# first_ten = file.read(10)
# file.seek(0)
# text = file.read()

# print(repr(first_ten), repr(text))
# file.write('salam\n')
# file.write('necesen!')

# file = open('text.txt', mode='a', encoding='UTF-8')
# file.write('\nYaxsiyam, sen necesen?')

# file = open('text2.txt', mode='x', encoding='UTF-8')
# file.write('Men de yaxsiyam')

# file = open('text.txt', mode='r+', encoding='UTF-8')
# text = file.read()
# text = text.replace('e', 'ə')
# file.seek(0)
# file.write(text)
# file.seek(20)
# file.truncate()
# file.close()

# file = open('text.txt', mode='w+', encoding='UTF-8')
# file.write('Men her gun\n Python ve Javascript oyrenirem')
# file.seek(0)
# print(file.read())
# file.close()

# import math
# from math import factorial, pi

# val = math.factorial(5)
# val = math.pi
# val = factorial(5) * pi

# print(val)

# nums = ''
# i = 1000
# while i >= 1:
#     nums += str(i).zfill(4) + '.' + '\n'
#     nums += str(i).zfill(4) + '.' + '\n'
#     i -= 1

# fl = open('task.txt', mode='w+', encoding='UTF-8')
# fl.write(nums)
# fl.close()

# file = open('nline.txt', mode='r+')
# rd = file.read()
# rd = rd.replace('\n', 'S')
# file.seek(0)
# file.write(rd)
# file.close()

# file = open('task_file.txt', mode='r+')
# info = file.read()
# info_splt = info.split('\n')
# new_l = sorted(info_splt, key=lambda x: x.split( )[2], reverse=True)
# res = '\n'.join(new_l)
# file.seek(0)
# file.write(res)
# file.close()

# file = open('IMG-1.jpg', mode='r+')
# source = file.read()
# source += b'hidden message'
# file.close()

# file = open('IMG-1.jpg', mode='rb+')
# source = file.read()
# source += b'hidden message'
# file.close()
# print(source)

# c = b'\xff\xfef\x00e\x00r\x00m\x00a\x00'

# print(c.decode('UTF-16'))

# file = open('hide-image.png', mode='rb+')
# b_codes = file.read()
# print(b_codes)
# b_codes = b_codes[::-1]
# file.seek(0)
# file.truncate()
# file.write(b_codes)
# # file.close()
# cont = file.read()
# file.close()
# print(cont)

file = open('hide-image.png', mode='rb+')
b_codes = file.read()
# print(b_codes)
b_codes = b_codes[::-1]
file.seek(0)
file.truncate()
file.write(b_codes)
# file.close()
cont = file.read()
print(cont)