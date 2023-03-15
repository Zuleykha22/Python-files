# verbs = ['can', 'are', 'could', 'did', 'do', 'had', 'has', 'have', 'is', 'might', 'must', 'should', 'was', 'were', 'would']
# def toggle(word):
#     original = word
#     word = word.lower()
#     for verb in verbs:
#         if word.startswith(verb) and ("'t") in word:
#             suffix = "'t" if verb == "can" else "n't"
#             word = word.replace(suffix, '')
#             break
#         elif word.startswith(verb):
#             suffix = "'t" if verb == 'can' else "n't"
#             word = word.replace(word, verb+suffix)
#             break

#     if (original[0].isupper() and original[1:].islower()): word = word[0].upper() + word[1:]
#     if (original.isupper()): word = word.upper()      
#     return word
# # print(toggle("can"))

# def speech_correction(words, speech):
#     verbs = ['can', 'are', 'could', 'did', 'do', 'had', 'has', 'have', 'is', 'might', 'must', 'should', 'was', 'were', 'would']
#     splitted_speech = speech.split()
#     for i in splitted_speech:
#         if i in words:
#             splitted_speech[splitted_speech.index(i)] = toggle(i)
#     result = ' '.join(splitted_speech)
#     return result

# wordss = {"can","do","have","was","would"}
# speechh = "I do like pizza."

# print(speech_correction(wordss, speechh))