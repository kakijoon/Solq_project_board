def order(l, order_key):

    print("오리지널 :" + str(l))

    if(order_key == "ticker"):
        order_key = 'ticker'
    elif(order_key == "close_price"):
        order_key = 'close_price'
    else:
        order_key = input("정렬기준을 다시 입력해 주세요(ticker, close_price)")

    sort_array = sorted(l, key=lambda x: x[order_key])
    print("정렬 :" + str(sort_array))


l = [
{"ticker": '238490', "open_price": 10000, "high_price": 20000, "low_price": 30000, "close_price": 40000},
{"ticker": '037440', "open_price": 100, "high_price": 200, "low_price": 300, "close_price": 400},
{"ticker": '003280', "open_price": 100000, "high_price": 200000, "low_price": 300000, "close_price": 400000},
{"ticker": '000545', "open_price": 30000, "high_price": 60000, "low_price": 90000, "close_price": 120000},
{"ticker": '000547', "open_price": 50000, "high_price": 100000, "low_price": 150000, "close_price": 200000},
{"ticker": '069260', "open_price": 200, "high_price": 400, "low_price": 600, "close_price": 800},
{"ticker": '078890', "open_price": 17200, "high_price": 17700, "low_price": 17000, "close_price": 17200},
]

order_key = input("정렬기준을 입력해 주세요(ticker, close_price)")

order(l, order_key)