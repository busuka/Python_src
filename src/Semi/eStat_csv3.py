import sys
import urllib.request
from lxml import etree
import csv

# 参考サイト http://qiita.com/yh0sh/items/6570d342491fe05dab03
# StatList.txt のTABLE_INFを引数にする.
# python eStat_csv3.py 0000030001


def export_statical_data(writer, api_key, stats_data_id, class_object, start_position):
    """
    統計情報のエクスポート
    """
    url = (
        'http://api.e-stat.go.jp/rest/2.0/app/getStatsData?limit=10000&appId=%s&lang=J&statsDataId=%s&metaGetFlg=N&cntGetFlg=N' % (
            api_key, stats_data_id))
    if start_position > 0:
        url = url + ('&startPosition=%d' % start_position)

    req = urllib.request.Request(url)
    opener = urllib.request.build_opener()
    conn = opener.open(req)
    cont = conn.read()
    parser = etree.XMLParser(recover=True)
    root = etree.fromstring(cont, parser)

    row = []
    datas = {}
    value_tags = root.xpath('//STATISTICAL_DATA/DATA_INF/VALUE')
    for value_tag in value_tags:
        row = []
        for key in class_object:
            val = value_tag.get(key)
            if val in class_object[key]['objects']:
                level = '';
                if 'level' in class_object[key]['objects'][val]:
                    if class_object[key]['objects'][val]['level'].isdigit():
                        level = ' ' * (int(class_object[key]['objects'][val]['level']) - 1)
                text = ("%s%s" % (level, class_object[key]['objects'][val]['name']))
                row.append(text)
            else:
                row.append(val)
        row.append(value_tag.text)
        writer.writerow(row)

    next_tags = root.xpath('//STATISTICAL_DATA/TABLE_INF/NEXT_KEY')
    if next_tags:
        if next_tags[0].text:
            export_statical_data(writer, api_key, stats_data_id, class_object, int(next_tags[0].text))


def get_meta_data(api_key, stats_data_id):
    """
    メタ情報取得
    """
    url = ('http://api.e-stat.go.jp/rest/2.0/app/getMetaInfo?appId=%s&lang=J&statsDataId=%s' % (api_key, stats_data_id))
    req = urllib.request.Request(url)
    opener = urllib.request.build_opener()
    conn = opener.open(req)
    cont = conn.read()
    parser = etree.XMLParser(recover=True)
    root = etree.fromstring(cont, parser)
    class_object_tags = root.xpath('//METADATA_INF/CLASS_INF/CLASS_OBJ')
    class_object = {}

    for class_object_tag in class_object_tags:
        class_object_id = class_object_tag.get('id')
        class_object_name = class_object_tag.get('name')
        class_object_item = {
            'id': class_object_id,
            'name': class_object_name,
            'objects': {}
        }
        class_tags = class_object_tag.xpath('.//CLASS')
        for class_tag in class_tags:
            class_item = {
                'code': class_tag.get('code'),
                'name': class_tag.get('name'),
                'level': class_tag.get('level'),
                'unit': class_tag.get('unit')
            }
            class_object_item['objects'][class_item['code']] = class_item
        class_object[class_object_id] = class_object_item
    return class_object


def export_csv(api_key, stats_data_id, output_path):
    """
    指定の統計情報をCSVにエクスポートする.
    """
    writer = csv.writer(open(output_path, 'w'), quoting=csv.QUOTE_ALL)
    class_object = get_meta_data(api_key, stats_data_id)
    row = []
    for key in class_object:
        title = class_object[key]['name']
        row.append(title)
    row.append('VALUE')
    writer.writerow(row)

    export_statical_data(writer, api_key, stats_data_id, class_object, 1)


def main(argvs, argc):
    if argc != 2:
        print("Usage #python %s api_key stats_data_id output_path" % argvs[0])
        return 1
    api_key = 'ff51248c2fe24af4143b36293482c74b065c81ea'  # 取得したAPI IDを入力
    stats_data_id = argvs[1]
    output_path = 'e-stat' + argvs[1] + '.csv'
    export_csv(api_key, stats_data_id, output_path)


if __name__ == '__main__':
    TABLE_INF = ["0000030001", "0000030002", "0000030003"]
    for inf in TABLE_INF:
        argvs = ["eStat_csv3.py", inf]
        argc = len(argvs)
        main(argvs, argc)
