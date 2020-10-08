# TileTraveller
LEVER_ROOM = ['1,2', '2,2', '2,3', '3,2']


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


def room_description(tile, coins, did_move):
    if did_move and tile in LEVER_ROOM:
        answer = input("Pull a lever (y/n): ").lower()
        if answer == "y":
            coins += 1
            print(f"You received 1 coin, your total is now {coins}.")
    print('You can travel: ' + yct(room_directions(tile)))
    return coins


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
        return str(tiles[0]) + ',' + str(tiles[1]), True

    else:
        print("Not a valid direction!")
        return tile, False


def is_victory_condition(tile):
    """ Skilar True ef við erum á lokareit """
    if tile == '3,1':
        result = True
    else:
        result = False
    return result


def play():
    tile = '1,1'
    coins = 0
    did_move = False
    while not is_victory_condition(tile):
        coins = room_description(tile, coins, did_move)
        direction = input("Direction: ")
        tile, did_move = move_rooms(tile, direction.lower())

    print(f"Victory! Total coins {coins}.")


def main():
    play_again = 'y'
    while play_again == 'y':
        play()
        play_again = input("Play again (y/n): ").lower()


main()
