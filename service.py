# -*- coding: utf-8 -*-


def handler(event, context):
    print("hello world!")
    e = event.get('e')
    pi = event.get('pi')
    print("e is %s and pi is %s" % (e, pi))
    print("about to return")
    return e * pi
