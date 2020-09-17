# TileTraveller


def add_or(res):
    if res != '':
        res += ' or '
    return res


def yct(directions):
    result = ''
    for ch in directions:
        if ch == 'n':
            result = '(N)orth'
        if ch == 's':
            result = add_or(result)
            result += '(S)outh'
        if ch == 'e':
            result = add_or(result)
            result += '(E)ast'
        if ch == 'w':
            result = add_or(result)
            result += '(W)est'
    return result + '.'


def room_directions(tile):
    result = ''
    if tile == '1,1':
        result = 'n'
    elif tile == '1,2':
        result = 'nse'
    return result


def room_description(tile):
    print('You can travel: ' + yct(room_directions(tile)))


def move_rooms(tile, direction):
    # commit
    pass


def is_victory_condition(tile):
    if tile == '3,1':
        result = True
    else:
        result = False
    return result


tile = '1,1'
while not is_victory_condition(tile):
    room_description(tile)
    direction = input("Direction: ")
    move_rooms(tile, direction)
