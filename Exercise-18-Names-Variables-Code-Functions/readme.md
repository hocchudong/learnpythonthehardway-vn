# Exercise 18: Names, Variables, Code, Functions

## Ví dụ 

Trong bài này chúng ta sẽ học cách tạo ra hàm trong python.

Trong python thì sử dụng từ khóa *def* để định nghĩa ra hàm.

Script: 
    # Hàm này tương giống với tham số *argv* 
    def print_two(*args):
        arg1, arg2 = args
        print "arg1: %r, arg2: %r" % (arg1, arg2)
    # Định ra hàm có 2 tham số 
    def print_two_again(arg1, arg2):
        print "arg1: %r, arg2: %r" % (arg1, arg2)
    # Định nghĩa ra hàm có 1 tham số 
    def print_one(arg1):
        print "arg1: %r" % arg1
    # Định nghĩa ra hàm không tham số 
    def print_none():
        print "I got nothin'."
    print_two("Zed","Shaw")
    print_two_again("Zed","Shaw")
    print_one("First!")
    print_none()

## Giải thích một script.

* Hàm được định nghĩa trong python bằng từ khóa def. Cú pháp * def tên_hàm([tham_số_1],[tham_số_2],...):

## Chạy code 

    $ python ex18.py
    arg1: 'Zed', arg2: 'Shaw'
    arg1: 'Zed', arg2: 'Shaw'
    arg1: 'First!'
    I got nothin'.

