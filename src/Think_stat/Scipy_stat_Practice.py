from scipy import stats

box = [1,1,2,3,3,3,3,4,5,5]     #10個のデータリストを準備.
stats.scoreatpercentile(box,90) #90パーセンタイル値を取得.