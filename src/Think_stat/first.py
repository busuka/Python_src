from Think_stat import survey #moduleとPackageは違うことに注意
table = survey.Pregnancies()
table.ReadRecords()
print ("妊娠レコードの総数:",len(table.records))