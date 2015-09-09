def PercentileRank(scores,your_score):
    count = 0
    for score in scores:
        if score <= your_score:
            count += 1
    percentile_rank = 100.0 * count / len(scores)
    return percentile_rank
def Percentile(scores,percentile_rank):
    scores.sort()
    for score in scores:
        if PercentileRank(scores,score) >= percentile_rank:
            return score
def Percentile_index(scores,percentile_rank):
    scores.sort()
    index = percentile_rank * (len(scores)-1) / 100
    return scores[int(index)]


alls = [55,56,77,88,99]
yous = 88
print(PercentileRank(alls,yous)) #88点がデータのどの位置にあるか
print(Percentile(alls,80))       #80パーセンタイル値の数値を返す
print(Percentile_index(alls,80)) #インデックスを検索する上の関数の効率化バージョン
