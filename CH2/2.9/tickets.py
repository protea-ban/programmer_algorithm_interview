# 如何从给定车票中找到旅途
def travel_tickets(inputs):
    reverseInput = dict()
    for k,v in inputs.items():
        reverseInput[v] = k

    start = None
    for k,v in inputs.items():
        if k not in reverseInput:
            start = k
            break

    if start is None:
        print("输入不合理")
        return

    to = inputs[start]
    res = "{}->{},".format(start, to)
    print(res, end=' ')
    start = to
    to = inputs[to]
    while to is not None:
        res = "{}->{},".format(start, to)
        print(res, end=' ')
        start = to
        to = inputs.get(to, None)


if __name__ == '__main__':
    inputs = dict()
    inputs["西安"] = "成都"
    inputs["北京"] = "上海"
    inputs["大连"] = "西安"
    inputs["上海"] = "大连"
    travel_tickets(inputs)
