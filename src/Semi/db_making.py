import sqlite3

#DBへの接続
con = sqlite3.connect("semi_data.db")

#SQLの実行

#既存DBの削除
con.execute("drop table semi_table")

#データベースの作成
con.execute("create table semi_table(id,month,day,price);")

#データの登録
con.execute("insert into semi_table values(01,1,1,100);")
con.execute("insert into semi_table values(02,1,2,120);")
con.execute("insert into semi_table values(03,1,3,125);")
con.execute("insert into semi_table values(04,1,4,120);")
con.execute("insert into semi_table values(05,1,5,130);")
con.commit()

#カーソル操作(結果の表示)
cursor = con.cursor()
cursor.execute("select * from semi_table;")
result = cursor.fetchall()
print(result)

#DBからクローズ処理
con.close()