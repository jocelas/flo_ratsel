import numpy as np

alphabet = list('abcdefghijklmnopqrstuvwxyz')

numbers = np.array([
    [13,14,19,0,6,21,1,24,19,7],
    [13,4,22,14,23,4,12,10,16,25],
    [13,15,15,10,16,15,25,24,10,11],
    [9,12,1,4,10,24,24,25,24,4],
    [17,5,0,5,10,16,10,4,5,1],
    [5,21,17,0,19,8,25,2,12,16],
    [22,-1,8,15,17,17,8,-1,24,4],
    [2,16,3,4,18,21,17,8,10,1],
    [1,18,6,11,1,1,21,19,5,3],
    [23,12,4,20,0,12,1,17,12,2],
    ])

def numbers_to_text(array_in, alphabet):
    array = array_in.copy()
    text_array = np.empty_like(array, dtype='<U1')
    for i in range(len(array)):
        for j in range(len(array[0])):
            index = array[i,j]
            if index == -1:
                text_array[i,j] = '0'
                continue
            text_array[i,j] = alphabet[index]
    return text_array

if __name__ == '__main__':
    np.savetxt("data/grid_jonas.dat", numbers, fmt='%d')