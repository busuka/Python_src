def PercentileRank(scores,your_score):
    count = 0
    for score in scores:
        if score <= your_score:
            count += 1
    percentile_rank = 100.0 * count / len(scores)
    return percentile_rank
def Percentilt(scores,percentile_rank):
    scores.sort()
    for score in scores:
        if PercentileRank(scores,score) >= percentile_rank:
            return score

alls = [55,56,77,88,99]
yous = 88
print(PercentileRank(alls,yous)) #88点がデータのどの位置にあるか
print(Percentilt(alls,80))       #80パーセンタイル値の数値を返す
