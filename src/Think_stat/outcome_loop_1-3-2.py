from Think_stat import survey2
table = survey2.Pregnancies()
table.ReadRecords()
table_record = table.records
[i for i in table_record if i.outcome == 1]
