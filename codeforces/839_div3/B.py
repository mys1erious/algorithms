def rotate(m):
    m[0], m[1], m[2], m[3] = m[2], m[0], m[3], m[1]


def is_beautiful(m):
    if m[0] < m[1] and m[2] < m[3] and m[0] < m[2] and m[1] < m[3]:
        return True
    return False


if __name__ == '__main__':
    n = int(input())

    answers = []

    for _ in range(n):
        exp1 = input()
        exp2 = input()

        matrix = []

        [matrix.append(int(v)) for v in exp1.split(' ')]
        [matrix.append(int(v)) for v in exp2.split(' ')]

        ans = 'NO'
        for i in range(4):
            if is_beautiful(matrix):
                ans = 'YES'
                break
            else:
                rotate(matrix)
        answers.append(ans)

    for ans in answers:
        print(ans)
