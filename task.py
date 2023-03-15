# Task: https://www.codewars.com/kata/595120ac5afb2e5c1d000001/train/python

doms ="*.amazon.co.uk', '89', \n '*.doubleclick.net', '139', '*.fbcdn.net', '212', \
'*.in-addr.arpa', '384', '*.l.google.com', '317', '1.client-channel.google.com', '110', \
'6.client-channel.google.com', '45', 'a.root-servers.net', '1059', \
'apis.google.com', '43', 'clients4.google.com', '71', 'clients6.google.com', '81', \
'connect.facebook.net', '68', 'edge-mqtt.facebook.com', '56', 'graph.facebook.com', '150', \
'mail.google.com', '128', 'mqtt-mini.facebook.com', '47', 'ssl.google-analytics.com', '398', \
'star-mini.c10r.facebook.com', '46', 'staticxx.facebook.com', '48', 'www.facebook.com', '178', \
'www.google.com', '162', 'www.google-analytics.com', '127', 'www.googleapis.com', '87'"

domains = '''\
*.amazon.co.uk    89
*.doubleclick.net    139
*.fbcdn.net    212
*.in-addr.arpa    384
*.l.google.com    317
1.client-channel.google.com    110
6.client-channel.google.com    45
a.root-servers.net    1059
apis.google.com    43
clients4.google.com    71
clients6.google.com    81
connect.facebook.net    68
edge-mqtt.facebook.com    56
graph.facebook.com    150
mail.google.com    128
mqtt-mini.facebook.com    47
ssl.google-analytics.com    398
star-mini.c10r.facebook.com    46
staticxx.facebook.com    48
www.facebook.com    178
www.google.com    162
www.google-analytics.com    127
www.googleapis.com    87'''

# def count_domains(domains, min_hits=0):
# counts = {}
# for domain_info in domains.splitlines():
#   domain, count = domain_info.split('\t')
#   pieces = domain.split('.')
#   if pieces[-2] in ('co', 'com'):
#     base = '.'.join(pieces[-3:])
#   else:
#     base = '.'.join(pieces[-2:])
#   if base not in counts:
#     counts[base] = int(count)
#   else:
#     counts[base] += int(count)
# result = []
# count_list = list(counts.items())
# count_list.sort(key=lambda item: item[0])
# count_list.sort(reverse=True, key=lambda item: item[1])
# for domain, count in count_list:
#   if count >= 500:
#     result.append(f'{domain} ({count})')
# res = '\n'.join(result)
# print(res)  
# print(count_domains(domains_list, 500))

d = '*.amazon.co.uk    89'
s = d.split()
print(s)

# def clean_domain (link):
#   reversed_link = link[::-1]
#   i = 0
#   j = 0
#   if '.co.' in link or '.com.' in link:
#     while i < len(reversed_link):
#       if reversed_link[i] == '.' and j < 2:
#         j += 1
#       elif reversed_link[i] == '.' and j == 2:
#         reversed_link = reversed_link[:i]
#       i += 1
#   else:
#     while i < len(reversed_link):
#       if reversed_link[i] == '.' and j < 1:
#         j += 1
#       elif reversed_link[i] == '.' and j == 1:
#         reversed_link = reversed_link[:i]
#       i += 1
#   return reversed_link[::-1]

# def count_domains(domains, min_hits):
#   clean_domains = []
#   for d in range(0, len(domains), 2):
#     clean_domains.append(clean_domain(domains[d]))
#     clean_domains.append(domains[d+1])
#   shortened_domain_list = []
#   for i in range(0, len(clean_domains), 2):
#     if clean_domains[i] not in shortened_domain_list:
#       shortened_domain_list.append(clean_domains[i])
#       shortened_domain_list.append(int(clean_domains[i+1]))
#     elif clean_domains[i] in shortened_domain_list:
#       shortened_domain_list[shortened_domain_list.index(clean_domains[i])+1] += int(clean_domains[i+1])
#   unsorted_result = []
#   for i in range(0, len(shortened_domain_list), 2):
#     if shortened_domain_list[i+1] >= min_hits:
#       unsorted_result.append(shortened_domain_list[i] + ' ' + f'({str(shortened_domain_list[i+1])})')
#   def sort_accesses (r):
#     return int((r[r.index('(')+1:]).rstrip(')'))
#   result = sorted(unsorted_result, key = sort_accesses, reverse=True)
#   return result

# print(count_domains(doms, 500))