if __name__ == '__main__':
    cases = int(input())
    answers = []
    for _ in range(cases):
        n = int(input())
        arr = list(map(int, input().split(' ')))

        x = max(arr) + 1
        while x >= 0:
            sub_arr = []
            for i in range(n):
                v = abs(arr[i] - x)
                if sub_arr and v < sub_arr[-1]:
                    x -= v
                    break
                sub_arr.append(v)

            if len(sub_arr) == n:
                answers.append(x)
                break
        else:
            answers.append(-1)

    for ans in answers:
        print(ans)
