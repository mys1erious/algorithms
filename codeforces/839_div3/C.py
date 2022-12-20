def calc_characteristic(arr):
    uniques = set()
    for i in range(len(arr)-1):
        uniques.add(arr[i+1] - arr[i])

    return len(uniques)


if __name__ == '__main__':
    cases = int(input())

    answers = []

    for _ in range(cases):
        inp = input()
        k, n = map(int, inp.split(' '))

        a = [v for v in range(1, n)]

        max_char = 1
        ans = []
        while len(ans) < k:
            ...

        answers.append(' '.join(str(v) for v in a))

    for ans in answers:
        print(ans)
