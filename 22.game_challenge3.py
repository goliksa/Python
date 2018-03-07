def rotate_list(elements, rotates):
    print(elements[rotates:] + elements[:rotates])
    return elements[rotates:] + elements[:rotates]

rotate_list([1, 2, 3, 4], 2)
