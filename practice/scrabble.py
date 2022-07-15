TILE_POINTS = {
    'a':1, 'b':3, 'c':3, 'd':2, 'e':1, 'f':4, 'g':2, 'h':4, 'i':1, 'j':8, 'k':5, 'l':1, 'm':3,
    'n':1, 'o':1, 'p':3, 'q':10, 'r':1, 's':1, 't':1, 'u':1, 'v':4, 'w':4, 'x':8, 'y':4, 'z':10,
    '_': 0
}


def build_tiles_map(tiles: str):
    tiles = list(tiles)
    tiles_map = {}

    for tile in tiles:
        if tile not in tiles_map:
            tiles_map[tile] = 1
        else:
            tiles_map[tile] += 1

    return tiles_map


def word_fully_in_tiles(word, tiles):
    word_len = len(word)
    tiles_len = 0

    for letter in tiles:
        if letter in word or letter == '_':
            tiles_len += 1

    if tiles_len < word_len:
        return False
    return True


# O(t+w)
def get_point_val(word, tiles):
    if not word_fully_in_tiles(word, tiles):
        return -1

    tiles_map = build_tiles_map(tiles)

    res = 0
    for letter in word:
        if letter in tiles_map and tiles_map[letter] > 0:
            tiles_map[letter] -= 1
            res += TILE_POINTS[letter]

    return res


if __name__ == '__main__':
    word1 = 'cat'
    tiles1 = 'tmoca'

    word2 = 'cat'
    tiles2 = 'tmoa_'

    word3 = 'cat'
    tiles3 = 'tmoa'

    word4 = 'cat'
    tiles4 = ''

    word5 = 'caat'
    tiles5 = 'tmoca'

    assert get_point_val(word1, tiles1) == 5
    assert get_point_val(word2, tiles2) == 2
    assert get_point_val(word3, tiles3) == -1
    assert get_point_val(word4, tiles4) == -1
    assert get_point_val(word5, tiles5) == -1
