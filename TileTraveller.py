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
        result = 'nes'
    elif tile == '1,3':
        result = 'es'
    elif tile == '2,3':
        result = 'ew'
    elif tile == '3,3':
        result = 'sw'
    elif tile == '3,2':
        result = 'ns'
    elif tile == '3,1':
        result = ""
    elif tile == '2,2':
        result = 'sw'
    elif tile == '2,1':
        result = 'n'
    return result


def room_description(tile):
    print('You can travel: ' + yct(room_directions(tile)))


def move_rooms(tile, direction):
    """ Færir okkur milli kassa (tiles) """
    if direction in room_directions(tile):
        tiles = tile.split(',')
        if direction == 'n':
            tiles[1] = int(tiles[1]) + 1
        if direction == 's':
            tiles[1] = int(tiles[1]) - 1
        if direction == 'e':
            tiles[0] = int(tiles[0]) + 1
        if direction == 'w':
            tiles[0] = int(tiles[0]) - 1
        return str(tiles[0]) + ',' + str(tiles[1])

    else:
        print("Not a valid direction!")
        return tile


def is_victory_condition(tile):
    """ Skilar True ef við erum á lokareit """
    if tile == '3,1':
        result = True
    else:
        result = False
    return result


tile = '1,1'
while not is_victory_condition(tile):
    room_description(tile)
    direction = input("Direction: ")
    tile = move_rooms(tile, direction.lower())


print("Victory!")
