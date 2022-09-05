import numpy as np


def random_predict(number: int = 1) -> int:
    min = 1
    max = 99
    number = np.random.randint(min, max)
    count = 0

    while True:
        count += 1
        mid = int((min+max) / 2)

        if mid > number:
            max = mid

        elif mid < number:
            min = mid

        else:
            print(f"Число угадано за {count} попыток. Это число {number}")
            break
    return count


def score_game(random_predict) -> int:
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(int(random_predict(number)))
    score = int(np.mean(count_ls))
    print(f'ваш алгоритм угадывает в среднем за: {score} попыток')
    return(score)
print(f'количество попыток: {random_predict(10)}')
score_game(random_predict)
