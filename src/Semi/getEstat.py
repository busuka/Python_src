import urllib.request
from lxml import etree
import sys
import codecs


def main(argvs, argc):
    if argc != 3:
        print("Usage #python %s api_key search_kind stats_code" % argvs[0])
        return 1
    api_key = 'ff51248c2fe24af4143b36293482c74b065c81ea'  # 取得したAPI IDを入力

    #
    search_kind = argvs[1]
    stats_code = argvs[2]
    stats_code = urllib.request.quote(stats_code.encode('utf-8'))


    url = ('http://api.e-stat.go.jp/rest/2.0/app/getStatsList?appId=%s&lang=J&statsCode=%s&searchKind=%s' % (
    api_key, stats_code, search_kind))
    req = urllib.request.Request(url)
    opener = urllib.request.build_opener()
    conn = opener.open(req)
    cont = conn.read()
    parser = etree.XMLParser(recover=True)
    root = etree.fromstring(cont, parser)
    result = root.find('RESULT')
    data_list = root.find('DATALIST_INF')
    table_infs = data_list.xpath('./TABLE_INF')

    for table_inf in table_infs:
        print(('--------------').encode('utf-8'))
        for iterator in table_inf.getiterator():
            if iterator.text is not None:
                itag = iterator.tag.encode('utf-8')
                itext = iterator.text.encode('utf-8')
            if iterator.items() is not None:
                if iterator.get('id') is not None:
                    print(itag, iterator.get('id').encode('utf-8'), itext)
                elif iterator.get('code') is not None:
                    print(itag, iterator.get('code').encode('utf-8'), itext)
                elif iterator.get('no') is not None:
                    print(itag, iterator.get('no').encode('utf-8'), itext)
                else:
                    print(itag, itext)

if __name__ == '__main__':
 argvs = sys.argv
 argc = len(argvs)
 sys.exit(main(argvs, argc))