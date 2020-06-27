
dx = {-1, -1, -1, 1, 1, 1, 0, 0}
dy = {-1, 0, 1, -1, 0, 1, -1, 1}

board = [["U", "R", "L", "P", "M"],
         ["X", "P", "R", "E", "T"],
         ["G", "I", "A", "E", "T"],
         ["X", "T", "N", "Z", "Y"],
         ["X", "O", "Q", "R", "S"]]

test = ["PRETTY",
        "GIRL",
        "REPEAT",
        "KARA",
        "PANDORA",
        "GIAZAPX"]


def hashWord(y, x, word):
    # 기저 사례
    # 범위 밖이면 false
    if x > 4 or y > 4 or x < 0 or y < 0:
        return False
    # 첫 글자가 없으면 false
    if board[y][x] != word[0]:
        return False
    # 단어 길이가 1이면 성공
    if len(word) == 1:
        return True

    for i in range(8):
        nextY = y + dy[i]
        nextX = x + dx[i]
        if hashWord(nextY, nextX, word):
            return True
        else:
            return False
