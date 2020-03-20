import json

with open('../data/login_data.json', encoding='utf-8') as f:
    data = json.load(f)
    # 声明空列表
    data_list = list()
    # print(data.values())
    for i in data.values():
        data_list.append((i.get('username'),
                          i.get('password'),
                          i.get('code'),
                          i.get('expect')))
    print(data_list)
