from statistics import mean


def script(lst1, lst2):
    mean_lst1 = mean(lst1)
    mean_lst2 = mean(lst2)
    return (sum(map(lambda x, y: (x - mean_lst1) * (y - mean_lst2), lst1, lst2)) /
            (sum(map(lambda x: (x - mean_lst1) ** 2, lst1)) *
             sum(map(lambda y: (y - mean_lst2) ** 2, lst2))) ** 0.5)


test_lst1 = [1, 2, 3, 4, 3]
test_lst2 = [1, 2, 3, 4, 5]
print(script(test_lst1, test_lst2))
