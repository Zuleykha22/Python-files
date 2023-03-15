# Scopes

# To convert local variable to global use: global + var name 
# To see all the variables in a project use: globals() function
# To see all the variables in the current local scope use: locals() function 


def convert_to_ascii_letters (text):
    letters_dictionary = {
    'ə': 'e',
    'ı': 'i',
    'ö': 'o',
    'ü': 'u',
    'ğ': 'g',
    'Ö': 'O',
    'Ü': 'U',
    'Ğ': 'G'  
    }
    
    result = ''
    for l in text:
        result += letters_dictionary.get(l, l)
    return result

def convert_ascii(f):
    def wrapper(*args, **kwargs):
        result = f(*args, **kwargs)
        result = convert_to_ascii_letters(result)
        return result
    return wrapper

@convert_ascii
def introduction():
    return 'Zəhmət olmasa, özünüzü təqdim edin'

@convert_ascii
def suggest_playlist():
    return 'Azəri mahnı'



print(suggest_playlist())
