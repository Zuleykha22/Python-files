def clean_domain (link):
  reversed_link = link[::-1]
  i = 0
  j = 0
  if '.co.' in link or '.com.' in link:
    while i < len(reversed_link):
      if reversed_link[i] == '.' and j < 2:
        j += 1
      elif reversed_link[i] == '.' and j == 2:
        reversed_link = reversed_link[:i]
      i += 1
  else:
    while i < len(reversed_link):
      if reversed_link[i] == '.' and j < 1:
        j += 1
      elif reversed_link[i] == '.' and j == 1:
        reversed_link = reversed_link[:i]
      i += 1
  return reversed_link[::-1]