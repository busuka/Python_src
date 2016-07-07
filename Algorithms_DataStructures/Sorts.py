import time
from paiza import ImportCase


def preparelist(vector):
    print("最初のリスト" + str(vector))
    slist = vector.copy()
    start_i = 1
    end_i = slist.__len__()
    return slist, start_i, end_i


def insertionsort(notsortlist):
    """
    配列の最初をソート済みとして、ソートしていない配列の要素がソート済み配列のどこに挿入できるかを精査していく.
    """

    slist, start_i, end_i = preparelist(notsortlist)
    while start_i < (end_i - 1):
        tmp = slist[start_i]
        tmp_position = start_i - 1
        while tmp_position >= 0 and tmp > slist[tmp_position]:
            slist[tmp_position + 1] = slist[tmp_position]
            tmp_position -= 1
        slist[tmp_position + 1] = tmp
        print(str(start_i) + "回目のループ結果 : " + str(slist))
        start_i += 1


def bubblesort(notsortlist):
    """
    配列の後ろから確定していくため、Start_iは後ろからにすべきである.
    """
    slist, start_i, end_i = preparelist(notsortlist)

    while start_i < (end_i - 1):
        start_j = 0
        while start_j < (end_i - start_i - 1):
            if slist[start_j] < slist[start_j + 1]:
                slist[start_j], slist[start_j + 1] = slist[start_j + 1], slist[start_j]
            start_j += 1
        start_i += 1
        print(str(start_i) + "回目のループ結果 : " + str(slist))


def selectionsort(notsortlist):
    slist, start_i, end_i = preparelist(notsortlist)
    start_i = 0
    while start_i < (end_i - 1):
        start_j = start_i + 1
        maxv = slist[start_i]
        mini = start_i
        while start_j < end_i:
            if slist[start_j] > maxv:
                maxv = slist[start_j]
                mini = start_j
            start_j += 1
        slist[start_i], slist[mini] = slist[mini], slist[start_i]
        print(str(start_i) + "回目のループ結果 : " + str(slist))
        start_i += 1


def shellsort(notsortlist):
    slist, start_i, end_i = preparelist(notsortlist)
    start_i = 0
    g = [4, 2, 1]
    for intv in g:
        while start_i < end_i:
            start_j = 0
            while (start_j + intv) < end_i:
                if slist[start_j] < slist[start_j + intv]:
                    slist[start_j], slist[slist + intv] = slist[start_j + intv], slist[start_j]
                start_j += 1


def mergesort(v, left, right):
    if left + 1 < right:  # 長さ1の配列に対しては何も処理をしないための条件文
        mid = (right + left) // 2
        mergesort(v, left, mid)
        mergesort(v, mid, right)
        merge(v, left, mid, right)


def merge(v, left, mid, right):
    n1 = mid - left
    n2 = right - mid
    L = []
    R = []
    for x in range(n1):
        L.append(v[left + x])
    for y in range(n2):
        R.append(v[mid + y])
    L.append(-99999)
    R.append(-99999)

    i = 0
    j = 0
    k = left

    while k <= right - 1:  # right - 1にすることにより番兵同士の判定は行われることはない.(番兵が元の配列に代入されない)
        if L[i] >= R[j]:
            v[k] = L[i]
            i += 1
        else:
            v[k] = R[j]
            j += 1
        k += 1


def partition(v, begin, end):
    endval = v[end]
    firstv_i = begin - 1
    secondv_j = begin
    while secondv_j < end:
        if v[secondv_j] <= endval:
            firstv_i += 1
            v[firstv_i], v[secondv_j] = v[secondv_j], v[firstv_i]
        secondv_j += 1
    v[firstv_i + 1], v[end] = v[end], v[firstv_i + 1]
    print(v)
    return firstv_i + 1


test_listOne = [3, 2, 4, 1]
test_listTwo = [10, 8, 4, 19, 2, 20, 5]
test_listThree = list(range(1, 101))
test_listFour = list(map(int, ImportCase.autoinput_returnlist("ALDS1_1Short.txt")))
test_listFive = [4, 8, 9, 1, 10, 6, 2, 5, 3, 7]
test_listSix = [13,19,9,5,12,8,7,4,21,2,6,11]
# 1000行のデータ:
# 挿入ソート:0.31秒.
# バブルソート:0.45秒
# 選択ソート:0.44秒
# マージソート:0.012秒


#start_time = time.time()
#mergesort(test_listFour, 0, len(test_listFour))
#print(test_listFour)
#print(time.time() - start_time)

print(partition(test_listSix,0,len(test_listSix)-1))
