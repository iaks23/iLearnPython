MORSE = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '?': '..--..',
    ',': '--..--',
    ' ': ' ',
       
}

def encode(phrase):
    """This function returns the encoded version of the phrase given by the user"""
    encodedphrase = ""
    phrase = phrase.upper()
    for data in phrase:
        encodedphrase += MORSE[data] + " "
    return encodedphrase
    
    
data = input("Please enter the word you wish to encode: ")
print("The encoded data is: ")
encode(data)