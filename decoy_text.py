


alphabet = list('abcdefghijklmnopqrstuvwxyz')
Alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
total_alphabet = []
for i in range(len(alphabet)):
    total_alphabet.append(Alphabet[i])
    total_alphabet.append(alphabet[i])
print(total_alphabet)    

decoy = 'asdfgb cmtz srux vjkjokeay rec DQwEPXY EGUWCNVF znyix'
deocy_key = list('asdfgbcmtzsruxvjkjokeayrec')
lower_decoy = decoy.lower()

def shift_decoy(n, decoy_in, key_list, alphabet_list):
    decoy_out = list(decoy_in)
    for i, letter in enumerate(list(decoy_out)):
        if letter in key_list:
            decoy_out[i] = key_list[(key_list.index(letter) + n) % len(key_list)]
    return ''.join(decoy_out)

if __name__ == '__main__':
