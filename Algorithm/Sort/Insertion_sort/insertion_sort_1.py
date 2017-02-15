def insertion_sort(lst):
    for i in range(len(lst)):
        # print('range: ', range(i, 0, -1))
        for j in range(i, 0, -1):
            # print("getting %s vs next %s" % (lst[j], lst[j+1]))
            print('index', j)
            if j > 1:
                if lst[j] > lst[j+1]:
                    print("+ swapping ", j)
                    lst[j], lst[j + 1] = lst[j+1], lst[j]
                else:
                    break
    return lst
insertion_sort([4, 5, 1, 7, 3, 5, 2])
# print("sorted: ", insertion_sort([4, 5, 1, 7, 3, 5, 2]))
