'''CODEWARS'''

# def square_digits(num):
#     res = ''
#     for digit in str(num):
#         res += str(int(digit)**2)
#     return int(res)

# print(square_digits(254))

''' Check to see if a string has the same amount of 'x's and 'o's. 
The method must return a boolean and be case insensitive. The string can contain any char.
Examples input/output:
XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false '''

# def define_letter_amount(word):
#     return word.lower().count('o') == word.lower().count('x')

# print(define_letter_amount('zpzp'))

# def get_sum(a,b):
#     ordered_numbers = [a, b]
#     if a > b:
#         ordered_numbers = [b, a]
#     elif a == b:
#         return a
#     result = 0
#     for i in range(ordered_numbers[0], ordered_numbers[1]+1):
#         result += i
#     return result

# print(get_sum(4, 2))

# passengers = [[10,0], [3,5], [5,8]]

# def flat(l):
#     result = []
#     for i in l:
#         if type(i) != list:
#             result.append(i)
#         else:
#             result.extend(flat(i))
#     return result

# def passenger_counter(bus_stops):
#     result = 0
#     bus_stops = flat(bus_stops)
#     for i in range(0, len(bus_stops)):
#         if tuple(enumerate(bus_stops))[i][0]%2 == 0:
#             result += tuple(enumerate(bus_stops))[i][1]
#         else:
#             result -= tuple(enumerate(bus_stops))[i][1]
#     return result

# def passenger_counter(bus_stops):
#     result = 0
#     for i in bus_stops:
#         result += i[0] - i[1]
#     return result

# print(passenger_counter(passengers))

'''"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
"indivisibility" -> 1 # 'i' occurs six times
"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
"aA11" -> 2 # 'a' and '1'
"ABBA" -> 2 # 'A' and 'B' each occur twice'''


# def duplicate_count(text):
#     text = text.lower()
#     result = []
#     for i in text:
#         if text.count(i) > 1:
#            if i not in result:
#             result.append(i)
#     return len(result) 

# print(duplicate_count('ABBA'))

''' '''
# s = [160, 3, 1719, 19, 11, 13, -21]

# def even_or_odd (l):
#     res_even = [i for i in l if i%2 == 0]
#     res_odd = [i for i in l if i%2]
#     if len(res_odd) < len(res_even):
#         return int(res_odd[0])
#     else:
#         return int(res_even[0])

# print(even_or_odd(s))

''' Find shortest word in a string'''

s = "Lets all go on holiday somewhere very cold"

# def find_short(s):
#     len_of_words = []
#     for i in s.split():
#         len_of_words.append(len(i))
#     return min(len_of_words)

# def find_short(s):
#     return min([len(x) for x in s.split()])

'''The Hashtag Generator'''

# def generate_hashtag (word, to_upper = lambda x: x.capitalize()):
#     if word == '':
#         return False
#     else:
#         words_list = word.strip(' ').split(' ')
#         hash_tag = '#'
#         for i in words_list:
#             hash_tag += to_upper(i)
#             if len(hash_tag) > 140:
#                 return False
#         return hash_tag

# qwerty = " Hello there thanks for trying my Kata"  # "#HelloThereThanksForTryingMyKata"
# print(generate_hashtag(qwerty))

# OTHER WAYS:
# def generate_hashtag(s): return '#' +s.strip().title().replace(' ','') if 0<len(s)<=140 else False

#def generate_hashtag(s):
    # ans = '#'+ str(s.title().replace(' ',''))
    # return s and not len(ans)>140 and ans or False

'''LIKE STATUS'''

# names = ['Zuleykha', 'Javad', 'Safura', 'Sanan', 'Ahmad']

# def likes(names):
#     if len(names) == 0:
#         return 'No one likes this'
#     elif len(names) == 1:
#         status = f'{names[0]} likes this'
#         return status
#     elif len(names) == 2:
#         status = f'{names[0]} and {names[1]} like this'
#         return status
#     elif len(names) == 3:
#         status = f'{names[0]}, {names[1]} and {names[2]} like this'
#         return status
#     elif len(names) > 3:
#         status = f'{names[0]}, {names[1]} and {len(names)-2} others like this'
#         return status

# ANOTHER WAY:

# def likes(names):
#     n = len(names)
#     return {
#         0: 'no one likes this',
#         1: '{} likes this', 
#         2: '{} and {} like this', 
#         3: '{}, {} and {} like this', 
#         4: '{}, {} and {others} others like this'
#     }[min(4, n)].format(*names[:3], others=n-2)

''' '''

# https://www.codewars.com/kata/52774a314c2333f0a7000688/train/python

''' '''
# def narcissistic(number):
#     res = 0
#     for i in str(number):
#         res += int(i) **len(str(number))
#     if res == number:
#         return True
#     else:
#         return False

# Another way:
# def narcissistic(value):
#     return bool(value==sum([int(a) ** len(str(value)) for a in str(value)]))

'''''' 
# recipeq = {"flour": 500, "sugar": 200, "eggs": 1}
# availableq = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}

# recipeq = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
# availableq = {"sugar": 500, "flour": 2000, "milk": 2000}

# def cakes (recipe, available):
#     res = []
#     for food, amount in recipe.items():
#         for av_food, av_amount in available.items():
#             if av_food == food:
#                 res.append(av_amount/amount)
#                 return int(min(res))
#             else:
#                 return 0

# print(cakes(recipeq, availableq))

# {'cream': 200, 'flour': 300, 'sugar': 150, 'milk': 100, 'oil': 100} 
# {'sugar': 1700, 'flour': 20000, 'milk': 20000, 'oil': 30000, 'cream': 5000}

# https://www.codewars.com/kata/525c65e51bf619685c000059/train/python - FAILED
#RIGHT WAY:
# def cakes (recipe, available):
#     res = set()
#     for ing, amount in recipe.items():
#         if ing in available:
#             current_amount = available[ing]
#             ratio = current_amount // amount
#             res.add(ratio)
#         else:
#             return 0
    
#     return min(res)

''' ''' 
# original_string = 'Hey fellow warriors'

# def spin_words(sentence):
#     result = []
#     for i in sentence.split(' '):
#         if len(i) >= 5:
#             result.append(i[::-1])
#         else:
#             result.append(i)
#     reversed_result = ' '.join(result)
#     return reversed_result

# print(spin_words(original_string))

# ANOTHER WAY:
# def spin_words(sentence):
#     return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])

'''DIRECTION QUESTION'''

# opposites = {'NORTH': 'SOUTH', 'SOUTH': 'NORTH', 'WEST': 'EAST', 'EAST': 'WEST'}
# def dirReduc(arr):
#     counter = 0
#     while counter < len(arr)-1:
#         curr = arr[counter]
#         next = arr[counter+1]
        
#         if opposites[curr] == next:
#             arr.pop(counter)
#             arr.pop(counter)
#             if counter > 0:
#                 counter -= 1
#             continue
        
#         counter += 1
        
#     return arr

''' ''' 
# new_url = url.strip('htps:/')
# new_url_two = url_two.strip('whtps:/.')

# url_zombie = "http://www.zombie-bites.com"  
# def domain_name(url):
#     stripped_url = url.strip('whtps:/.')
#     for i in stripped_url:
#         if i == '.':
#             result = stripped_url[0:stripped_url.index(i)]
#     return result

# print(domain_name(url_zombie))

''' ''' 
# list_one = [ 1, True, 1 ]
# list_two = [ 2, 2, 2 ]
# print(all(list_one))
# for i in list_one:
#     first_index = list_one[0]
#     if type(first_index) == type(i):
#         print(True)

# def find_type (lst):
#     c = 0
#     first_index = lst[0]
#     for i in lst:
#         if type(first_index) == type(i):
#             c+=1
#     if c == len(lst):
#         return True

# print(find_type(list_one))

# lst = [ 1, True, 1 ]

# c = 0
# first_index = lst[0]
# for i in lst:
#     if type(first_index) == type(i):
#         c+=1
# if c == len(lst):
#     print(True)
# else:
#     print(False) 


# the_list = [5, 8, 6, 3, 9, 4]   # [3, 8, 6, 5, 4]
# result = {}

# mixed_sort_finito = True
# counter = 0

# while True:
#     first = the_list[counter]
#     second = the_list[counter+1]

#     if second < first:
#         the_list[counter] = second
#         the_list[counter+1] = first
#         mixed_sort_finito = False
    
#     if counter == len(the_list):

# st = "ab"
# sas = ["za", "ab", "Abc", "Zab", "zbc"]

# def word_search (query, seq):
#     seq_lower = [st.lower() for st in seq]
#     result = []
#     for i in seq_lower:
#         if query not in i:
#             result = None
#         else:
#             result.append(i)
#     return result

# print(word_search('ab', ["za", "ab", "Abc", "Zab", "zbc"]))

# 2, 4, 9  => 1, 1, 1 

# def mean(lst):
#     result = []
#     res_str = ''
#     res_int = 0
#     for i in lst:
#         if i.isalpha() == True:
#             res_str += i
#         else:
#             res_int += int(i)
#     result.append(res_int/10)
#     result.append(res_str)
#     return result

''' ''' 

# activity_status = [{
#   'username': 'David',
#   'status': 'online',
#   'lastActivity': 100
# }, {
#   'username': 'Lucy', 
#   'status': 'offline',
#   'lastActivity': 22
# }, {
#   'username': 'Bob', 
#   'status': 'online',
#   'lastActivity': 104
# }]
# for i in activity_status:
#     if 'online' in i['status']:
#         print('yes')
#     else:
#         print('no')
    # for k, v in i.items():
    #     if v == 'online':
    #         print('yes')
    #     else:
    #         print('No')
    
# def who_is_online(friends):
#     absent_status = []
#     res = {}
    
#     res['offline'] = []
#     for i in friends:
#         if 'online' in i['status'] and i['lastActivity'] <= 10:
#             res['online'].append(i['username'])
#         else:

#             if i['lastActivity'] <= 10:
#                 res['online'].append(i['username'])
#         elif 'offline' in i['status']:
#             res['offline'].append(i['username'])
#         elif 'online' in i['status']:
#             res['away'] = []
#             if i['lastActivity'] > 10:
#                 res['away'].append(i['username'])
#     return res

# print(who_is_online(activity_status)) 

# ''' '''

wordss = {"can","do","have","was","would"}
# speechh = "I do like pizza."
# speechh = "I don't like pizza."
# speechh = "I don't see why it Would be them"
ss = "Wouldn't you believe it? I can't!"
# ss = ss.split()
# print(ss)
# speechh = speechh[0].lower() + speechh[1:]
# test = "aren't you kidding"

''' '''
# [1, 2, 0, 1, 0, 1, 0, 3, 0, 1] -> [1, 2, 1, 1, 3, 1, 0, 0, 0, 0]
# lst = [1, 2, 0, 1, 0, 1, 0, 3, 0, 1] 

# def move_zeros(lst):
#    return sorted(lst, key = bool, reverse=True)

# def move_zeros(lst):
#   zeros = []
#   non_zeros = []
#   for i in lst:
#     if i == 0:
#       zeros.append(i)
#     else:
#       non_zeros.append(i)
#   result = non_zeros + zeros 
#   return result

# not understood
# def move_zeros(array):
#   return sorted(array, key=lambda x: x == 0 and x is not False)

''' '''
# the_list = [1,2,3,4,3,2,1]

# def find_even_index(arr):
#   counter = 0
#   while counter < len(arr):
#     if sum(arr[0:counter]) == sum(arr[(counter+1):]):
#       return counter
#     counter += 1
#   return -1

# print(find_even_index(the_list))

''' ''' 
# snt = "is2 Thi1s T4est 3a"

# def key_function (word):
#   for i in word:
#     if i.isnumeric():
#       return int(i)

# s = snt.split()
# res = sorted(s, key = key_function)
# result = ' '.join(res)
# print(result)

''' '''
# def solution(s):
#   res = []
#   counter = 0
#   if len(s) == 1:
#     res.append(s + '_')
#   else:
#     while counter < len(s):
#       res.append(s[counter:counter+2]) 
#       if counter == len(s) - 3:
#         res.append(s[counter+2:] + '_')
#         break
#       counter += 2
#   return res

# print(solution('dewdfdsdweeet'))

''' https://www.codewars.com/kata/589273272fab865136000108/train/python ''' 

# def black_or_white_key(key_press_count):
#   key_colors = {
#     1: 'white',
#     2: 'black',
#     3: 'white',
#     4: 'white',
#     5: 'black'
#   }
#   if key_press_count <= 88:
#     if key_press_count % 5 == 0:
#       return key_colors[5]
#     else:
#       return key_colors[key_press_count%5]
#   else:
#     return key_colors[key_press_count%88%5]

# print(black_or_white_key(52))

# failed some tests 

''' https://www.codewars.com/kata/58bee820e9f98b215200007c/train/python ''' 

# names = "Albert Einstein, !Sarah Connor, Marilyn Monroe, Abraham Lincoln, Sarah Connor, Sean Connery, Marilyn Monroe, Bjarne Stroustrup, Manson Marilyn, Monroe Mary"
# names = 'Zuleyxa, !Cavad, Samir, Eli, Samir, Husniye, Cavad'
# names = "Jesse Cox, !Selena Gomez"

# def select(memory):
#   hate_list = []
#   beforeMarked = False    
#   names = memory.split(', ')
#   for name in names:
#     if name.startswith('!'):
#       beforeMarked = True            
#       hate_list.append(name.lstrip('!'))
#     elif beforeMarked:
#       beforeMarked = False            
#       hate_list.append(name)
#   result = [name for name in names if name.lstrip('!') not in hate_list]
#   return ', '.join(result)
# print(select(names))  

''' ''' 

# def delete_nth(order, max_e):
#   res = []
#   check_list = []
#   for i in order:
#     if order.count(i) <  max_e:
#       res.append(i)
#     elif order.count(i) >= max_e and i not in check_list:
#       check_list.append(i)
#       res.append(i)
#     elif order.count(i) >= max_e and i in check_list and check_list.count(i) <= max_e - 1:
#       check_list.append(i)
#       res.append(i)

#   # for i in order:
#   #   if res.count(i) < max_e:
#   #     res.append(i)

#   return res
    
# print(delete_nth([9,1,1,2,3,3,7,2,2,2,2], 3))

# def solution(number):
#   l = [i for i in range(1, number+1)]
#   return sum([i for i in l if i % 3 == 0 or i % 5 == 0])
# print(solution(16))

''' '''
# def countZeroRowsAndColumns(list1, list2):
#   res = [lst1[0][i] + lst2[0][i] for i in range(3)]
#   res_two = [lst1[1][i] + lst2[1][i] for i in range(3)]
#   counter = 0
#   if all(res) == False:
#     counter += 1
#   elif all(res_two) == False:
#     counter += 1
#   for i in range(3):
#     if res[i] == 0 and res_two[i] == 0:
#       counter += 1
#   return counter 

# print(countZeroRowsAndColumns([[1, 3,-5], [2,-4, 6]], [[-1,-3, 5],[-2,-4,-6]]))

''''''
# def count_zeros_n_double_fact(n): 
#   res = 1
#   if n % 2:
#     for i in range (1, n+1, 2):
#       res *= i
#   else:
#     for i in range (2, n+1, 2):
#       res *= i
#   if str(res).endswith('0'):
#     return len(str(res)) - len(str(res).rstrip('0'))

''' '''
# def largest_difference(data):
#   res = []
#   counter = 0
#   while counter < len(data):
#     for i in range(1, len(data)):
#       if counter + i < len(data):
#         if data[counter] <= data[counter+i]:
#           res.append(i)
#     counter += 1 
#   if len(res) == 0:
#     return 0
#   return max(res)

# print(largest_difference([1, 2, 3]))

# print(type(largest_difference))

''''''
# def add(n):
#   def sum_function (m):
#     return n + m
#   return sum_function

# add(1)(2)(3)(4)

# def sum_function (2):
#   return 1 + sum_function()

# def s_f (3):
#   return 3 + sum_function

'''
add(1)(2)(3)(4)

def sum_function (n):
  return n + 

factorial = lambda n: 1 if n == 0 else n * factorial(n-1)  
n*(n-1)*n(-2)

'''
# def score(dice):
#   counter = 0
#   res = 0
#   for i in dice:
#     for j in range(2, 7):
#       if i == j and dice.count(i) >= 3 and counter < 1:
#         res += i * 100
#         counter += 1
#     if i == 1 and dice.count(i) >= 3 and counter < 1:
#       res += 1000 + dice.count(i)%3*100
#       counter += 1
#     elif i == 1 and dice.count(i) < 3:
#       res += 100
#     elif i == 5 and dice.count(i) < 3:
#       res += 50
#   return res

''' '''
# def pig_it (text):
#   return ' '.join([(i[1:] + i[0] + 'ay') if i.isalpha() else i for i in text.split()])
''' '''
# numbers = [1, 2, 3]

# def power(a):
#   far_numbers = []
#   result = [[]]
#   for i in range(len(a)):
#     # p = a.remove()
#     if i + 2 <= len(a):
#       result.append([a[i]])
#       result.append(a[i:i+2])
#     elif i + 2 == len(a) + 1:
#       result.append([a[-1]])
#   far_numbers.append(a[0])
#   far_numbers.append(a[2])
#   result.append(far_numbers)
#   result.append(a)
#   return result
# print(power(numbers))

''' '''
# tic_tac_list = \
# [[0, 0, 1],
#   [0, 1, 2],
#   [2, 1, 0]]

# def is_solved(board):
#   check_zeros = []
#   for i in range(3):
#    for j in range(3):
#      check_zeros.append(board[i][j])
#    if len(board[i]) == board[i].count(board[i][0]) and board[i][0] != 0:
#      return board[i][0]
#    elif board[0][i] == board[1][i] == board[2][i] and board[0][i] != 0:
#     return board[0][i]
#    elif i+2 < 3 and board[i][i] != 0 and board[i][i] == board[i+1][i+1] == board[i+2][i+2]:
#     return board[0][0]
#    elif i+2 < 3 and board[i][i+2] != 0 and board[i][i+2] == board[i+1][i+1] == board[i+2][i]:
#     return board[0][2]
#   if 0 in check_zeros:
#     return -1
#   return 0

# print(is_solved(tic_tac_list))

''''''
# x*4-(x-1)*2
# big_area_calc*4-(big_area_calc-1)*2 + one_area_calc*4

# areaa = \
# ["OXOXOX", 
#  "OXOOOO", 
#  "XOOXOX", 
#  "OXXOOO", 
#  "OOXOOX", 
#  "OXOOOO"]
# def check_neighbours (area):
#   one_area_calc = 0
#   big_area_calc = 0
#   # calc_finish = 0
#   # big_area_list = []
#   for l in range(len(area)):
#     for i in range(len(area[l])):

#       if area[l][i] == 'X':
#         if l+1 < len(area) and l != 0 and i+1 < len(area[l]) and i != 0 and (area[l][i+1] == 'X' or area[l+1][i] == 'X' or area[l][i-1] == 'X' or area[l-1][i] == 'X'):
#           big_area_calc += 1
#         elif l+1 < len(area) and l != 0 and i+1 == len(area[l]) and (area[l][i-1] == 'X' or area[l+1][i] == 'X' or area[l-1][i] == 'X'):
#           big_area_calc += 1  
#         elif l+1 < len(area) and l != 0 and i == 0 and (area[l][i+1] == 'X' or area[l+1][i] == 'X' or area[l-1][i] == 'X'):
#           big_area_calc += 1  

#         elif l+1 == len(area) and i+1 < len(area[l]) and i != 0 and (area[l][i-1] == 'X' or area[l][i+1] == 'X' or area[l-1][i] == 'X'):
#           big_area_calc += 1
#         elif l+1 == len(area) and i+1 == len(area[l][i]) and (area[l][i-1] == 'X' or area[l-1][i] == 'X'):
#           big_area_calc += 1
#         elif l+1 == len(area) and i == 0 and (area[l][i+1] == 'X' or area[l-1][i] == 'X'):
#           big_area_calc += 1

#         elif l == 0 and i+1 < len(area[l]) and i != 0 and (area[l][i+1] == 'X' or area[l+1][i] == 'X'):
#           big_area_calc += 1
#         elif l == 0 and i+1 == len(area[l][i]) and (area[l][i-1] == 'X' or area[l+1][i] == 'X'):
#           big_area_calc += 1
#         elif l == 0 and i == 0 and (area[l][i+1] == 'X' or area[l-1][i] == 'X'):
#           big_area_calc += 1

#       if area[l][i] == 'X':
#         if l != 0 and l+1 != len(area) and i+1 < len(area[l]) and i != 0 and area[l][i+1] != 'X' and area[l+1][i] != 'X' and area[l-1][i] != 'X' and area[l][i-1] != 'X':
#           one_area_calc += 1
#         elif l != 0 and l+1 != len(area) and i+1 == len(area[l]) and area[l+1][i] != 'X' and area[l-1][i] != 'X' and area[l][i-1] != 'X':
#           one_area_calc += 1
#         elif l != 0 and l+1 != len(area) and i == 0 and area[l][i+1] != 'X' and area[l+1][i] != 'X' and area[l-1][i] != 'X':
#           one_area_calc += 1
#         elif l+1 == len(area) and i+1 < len(area[l]) and i != 0 and area[l][i+1] != 'X' and area[l-1][i] != 'X' and area[l][i-1] != 'X':
#           one_area_calc += 1
#         elif l+1 == len(area) and i+1 == len(area[l]) and area[l-1][i] != 'X' and area[l-1][i] != 'X':
#           one_area_calc += 1
#         elif l+1 == len(area) and i==0 and area[l][i+1] != 'X' and area[l-1][i] != 'X':
#           one_area_calc += 1
#         elif l == 0 and i+1 < len(area[l]) and i != 0 and area[l+1][i] != 'X' and area[l][i+1] != 'X' and area[l][i-1] != 'X':
#           one_area_calc += 1
#         elif l == 0 and i+1 == len(area[l]) and area[l+1][i] != 'X' and area[l][i-1] != 'X':
#           one_area_calc += 1 
#         elif l == 0 and i == 0 and area[l+1][i] != 'X' and area[l][i+1] != 'X':
#           one_area_calc += 1 

#   return big_area_calc*4-(big_area_calc-1)*2 + one_area_calc*4

# print(check_neighbours(areaa))
