

def compare_round(list_array):
    #print("원본 : " + str(list_array))

    i = 0
    n = len(list_array)
    #print("리스트사이즈 : " + str(n))


    for i in range(0, n):
        if i >= 4:
            v1 = list_array[i]['close_plice']
            v2 = list_array[i]['close_plice']
        else:
            v1 = list_array[i]['close_plice']
            v2 = list_array[i + 1]['close_plice']

        #print("v1값 : " + str(v1) + "  v2값 :" + str(v2))
        if v1 < v2:
            try: value = -round(((v2 - v1)/v1*100), 2)
            except: value = - 100
        elif v1 > v2:
            try: value = round(((v1 - v2)/v1*100), 2)
            except: value = 100
        else:
            value = 0

        list_array[i]['close_plice'] = value

        #print("딕셔너리 등락률 : " + str(list_array[i]['close_plice']))






    print("카운트값 : " + str(n))
    print("최종 리스트" + str(list_array))

    return list_array

list_array = [
{'date': '2022-01-12', 'close_plice': 78900},
{'date': '2022-01-11', 'close_plice': 78900},
{'date': '2022-01-10', 'close_plice': 78000},
{'date': '2022-01-07', 'close_plice': 78300},
{'date': '2022-01-06', 'close_plice': 76900}
]

#print(list(l['close_plice'] for l in list_array))

compare_round(list_array)
