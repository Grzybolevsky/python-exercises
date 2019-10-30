# coding=utf-8
while True:
    val = raw_input()
    if val == 'stop':
        print "Koniec"
        break
    try:
        val = float(val)
        print (val, val), val ** 3
    except ValueError:
        print "Zły typ wejścia"
