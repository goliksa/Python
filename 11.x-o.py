import pprint
position = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', \
                     'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',\
                      'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
pprint.pprint(position)

# print(position(top-L )+ '|' + position[top-M] + '|')

def board (point):
    print(point['top-L'] + '|' + point['top-M'] + '|' + point['top-R'])
    print('-----')
    print(point['mid-L'] + '|' + point['mid-M'] + '|' + point['mid-R'])
    print('-----')
    print(point['low-L'] + '|' + point['low-M'] + '|' + point['low-R'])

    

position[input()]  = 'x' 
    
board(position)    
