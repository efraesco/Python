# list of letters
letras = ['a', 'b', 'd', 'e', 'i', 'j', 'o']

# function that filters vowels
vocales = ['a', 'e', 'i', 'o', 'u']
filtrar_vocales = lambda *args: filter(vocales,args)

print(list((filtrar_vocales(letras))))


    
# def filter_vowels(letter):
#     if(letter in vowels):
#         return True
#     else:
#         return False
# filtered_vowels = filter(filter_vowels, letters)
# print('The filtered vowels are:')
# for vowel in filtered_vowels:
#     print(vowel)