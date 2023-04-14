"""How can you tell an extrovert from an introvert at NSA?
Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE thl'f fubrf.

I found this joke on USENET, but the punchline is scrambled. Maybe you can decipher it?
According to Wikipedia, ROT13 is frequently used to obfuscate jokes on USENET.

For this task you're only supposed to substitute characters. Not spaces, punctuation, numbers, etc."""

def rot13(message):
    alphabet_string_low = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_string_up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet_string_low_double = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    alphabet_string_up_double = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result_string = []
    for letter in message:
        if letter.isalpha():
            if letter.islower():
                index_letter = alphabet_string_low.index(letter)
                result_string.append(alphabet_string_low_double[abs(index_letter + 13)])
            else:
                index_letter = alphabet_string_up.index(letter)
                result_string.append(alphabet_string_up_double[abs(index_letter + 13)])
        else:
            result_string.append(letter)
    return ''.join(result_string)    
        






rot13("This is my first ROT13 excercise!")
"""ROT13 example."""