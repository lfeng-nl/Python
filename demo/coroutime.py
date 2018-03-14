def consumer():
    r = 100
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming n = %s...' % n)
        r += 1

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing n = %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: r = %d' % r)
    c.close()

c = consumer()
produce(c)