def read_file(file_name):
    with open(file_name, 'r') as file:
        print(file.read())

VOCALS = 'aeiouAEIOU'

def readlines_file(file_name):
    vocal_word = 0
    non_vocal_word = 0
    with open(file_name, 'r') as file:
        list_of_file = file.readlines()
        for line in list_of_file:
            for word in line.split():
                if word[0] in VOCALS:
                    vocal_word += 1
                else:
                    non_vocal_word += 1
    read_file(file_name)
    print(f'Vowel words: {vocal_word}\nNon-vowel words: {non_vocal_word}')
file_name = input()
readlines_file(file_name)
                    
                
    
        