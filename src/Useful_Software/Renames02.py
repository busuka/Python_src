#coding: UTF-8
import os
import glob

direct = "../../Desktop/unit/RenameTest/"
files=glob.glob("*.txt") #拡張子が.txtのものを探索

for oldname in files:
 newname = oldname.replace('test','miffy')
 os.rename(oldname,newname)