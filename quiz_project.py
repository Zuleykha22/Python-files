questions = [
    {
        'text': 'Bunlardan hansi bitkidir?',
        'options': {'a': 'gunebaxan', 'b': 'toyuq', 'c': 'inek'},
        'correct_answer': 'a'
    },
    {
        'text': 'Hansi interpereter proqramlasdirma dilidir',
        'options': {'a': 'C++', 'b': 'Python', 'c': 'C#'},
        'correct_answer': 'b'
    },
    {
        'text': '2 + 2 * 2',
        'options': {'a': '3', 'b': '4', 'c': '6'},
        'correct_answer': 'c'
    },
    {
        'text': 'Helim atomunun isaresi hansidir?',
        'options': {'a': 'He', 'b': 'H', 'c': 'Au'},
        'correct_answer': 'a'
    },
    {
        'text': 'Yasayan en boyuk canli hansidir?',
        'options': {'a': 'balina', 'b': 'inek', 'c': 'qarisqa'},
        'correct_answer': 'a'
    },
]

full_name = input('Write your firstname and lastname: ')

correct_answers_count = 0
for question in questions:
    print(question['text'])
    for option, text in question['options'].items():
        print(f'{option}) {text}')
    answer = input('Your Answer: ').lower()
    
    if answer == question['correct_answer']:
        correct_answers_count += 1
        
    print()
    
print('Duz cavab sayi:', correct_answers_count)


result = f"""
{full_name}: {correct_answers_count} / {len(questions)}
"""

# with open('results.txt', mode='a', encoding='utf-8') as file:
#     file.write(result)