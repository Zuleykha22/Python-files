# file_one = open('test.txt')
# content = file_one.read()
file_one = open('test.txt', 'w')

greeting = 'Hi, dear'
addition = file_one.write(greeting)
# print(content)
# print()

source = open('photo.jpeg', mode='rb').read()
source += b'simarenin shekli'
print(source)

