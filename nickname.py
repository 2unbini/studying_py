#making exception
# -*- coding: utf-8 -*-

class MyError(Exception):
    def __str__(self):
        return "허용되지 않은 별명"
    pass


def call_me(nick):
    if nick == "바보" :
        raise MyError()
    print(nick)

try:
    call_me("짱")
    call_me("바보")
except MyError as e:
    print(e)
