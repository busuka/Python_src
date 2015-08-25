from Think_stat import survey2
table = survey2.Pregnancies()
table.ReadRecords()
table_record = table.records
a = 0
for i in table_record:
    if i.outcome == 1:
        a = a + 1
print("出産した子どもの数 :",a)