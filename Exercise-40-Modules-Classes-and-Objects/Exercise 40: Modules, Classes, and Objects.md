## Bài 40: Modules, Classes, and Objects

Python được gọi là một "ngôn ngữ lập trình hướng đối tượng . " Sử dụng các lớp trong lập trình để chương trình trở nên rõ ràng hơn. Bây giờ tôi sẽ chỉ cho bạn những bước khởi đầu của lập trình hướng đối tượng, class, object cũng như module.

## Modules giống như Dictionaries

Bạn đã được biết dictionary được tạo ra và sử dụng để map giữa key và value. Điều đó có nghĩa là nếu bạn tao ra một key là "apple" và bạn muốn lấy ra nội dung mà key đó chứa thì làm như sau:
```sh
mystuff = {'apple': "I AM APPLES!"}
print mystuff['apple']
```

Giữ suy nghĩ " get X from Y" trong tâm trí bạn và bây giờ nghĩ về module. Ta tạm định nghĩa nó như là

1. Một file Python với các hàm hoặc các biết trong đó
2. Bạn import file
3. Bạn có thể truy cập các functions hoặc các biến trong module với dấu chấm

Giả sử bạn có một module tên mystuff.py và có funtion *apple*. Nội dung module
*mystuff.py*
```sh
# this goes in mystuff.py
def apple():
    print "I AM APPLES!"
```
Trong chương trình của bạn, bạn có thể sử dụng module MyStuff với hàm *import* và sau đó truy cập vào funtion *apple*:

```sh
import mystuff
mystuff.apple()
```

Bạn cũng có thể đặt thêm biến tên là *tangerine*:
```sh
def apple():
    print "I AM APPLES!"

# this is just a variable
tangerine = "Living reflection of a dream"
```
và truy cập vào biến
```sh
import mystuff

mystuff.apple()
print mystuff.tangerine
```
Nhớ lại dictionary và bạn sẽ bắt đầu thấy nó sử dụng gần giống như dictionary nhưng chỉ khác nhau về cú pháp. Hãy so sánh:
```sh
mystuff['apple'] # get apple from dict
mystuff.apple() # get apple from the module
mystuff.tangerine # same thing, it's just a variable
```
Điều này có nghĩa chúng ta có một kiểu mẫu rất phổ biến trong Python:

1. tạo ra một key = value
2. Lấy ra nội dung bởi tên của key

Ở trong dictionary, key là string và cú pháp là [key] . trong module thì key và dấu hiệu và có cú pháp là .key. Chúng gần tương tự nhau

## Class giống như module

Bạn có thể nghĩ về một module như một từ điển chuyên ngành mà có thể lưu trữ mã Python , do đó bạn có thể truy cập nó với dấu chấm. Python cũng có một cấu trúc phục vụ một mục đích tương tự được gọi là class. Một lớp học là một cách để có một nhóm các chức năng và dữ liệu đặt lên chúng, do đó bạn có thể truy cập chúng qua dấu chấm

Nếu bạn tạo một class như một mystuff module. Bạn làm như sau
```sh
class MyStuff(object):

    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print "I AM CLASSY APPLES!"
```
Có lẽ đến đây bạn sẽ thắc mắc sử dụng class MyStuff thay vì module mystuff với hàm 
apple. Bạn cũng thấy khó hiểu với hàm __init__ cũng như cách khai báo biến 
self.tangerine. Bạn cũng nên biết về object và cách object làm việc với mystuff

## Object như là Import

Nếu class coi như là một mini-module. Khi ta import một class và khởi tạo mới thì 
gọi là instance. Một instance được gọi bởi hàm class như sau
```sh
thing = MyStuff()
thing.apple()
print thing.tangerine
```
Ta xem xét các thành phần tạo lên lớp MyStuff

1.Gọi đến MyStuff() thấy rằng nó là một class mà đã xác định.
2. Python khởi tạo một đối tượng rỗng với tất cả các tính năng bên trong sử dụng
*def*
3. Hàm __init___ gọi là chức năng để khởi tạo đối tượng rỗng vừa tạo .
4. Trong hàm __init__ có biến *seft* là đối tượng rỗng Python làm cho tôi , và tôi có thể thiết lập các biến trên nó giống như bạn làm với một mô-đun , từ điển, hoặc đối tượng khác 
5. Trong trường hợp trên *self.tanger* là một biến
6. Bây giờ Python có thể đưa đối tượng  này gán nó vào biến *thing*

## Getting things from things

Bây giờ ta có ba cách để lấy giá trị  từ key
```sh
# dict style
mystuff['apples']

# module style
mystuff.apples()
print mystuff.tangerine

# class style
thing = MyStuff()
thing.apples()
print thing.tangerine
```
## Ví dụ về lớp 

Có thể bạn sẽ thấy sự tương đông của 3 cách khai báo key = value và có những thắc mắc
```sh
class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
```
## Những gì bạn nhìn thấy
```sh
$ python ex40.py
Happy birthday to you
I don't want to get sued
So I'll stop right there
They rally around tha family
With pockets full of shells
```
## Tìm hiểu thêm

1. viết một vài bài hát và in ra lời bài hát
2. Put the lyrics in a separate variable, then pass that variable to the class to use 
3. Tìm hiểu trên mạng về lập trình hướng đối tượng

## Một số câu hỏi chung

Q. Sử dụng seft trong hàm __init__

Answer: *seft* nghĩa la chính nó. Khi khởi tạo một instance ta sẽ truyền đối tượng này vào seft. 
ví dụ *thing= mystuff()* và sử dụng biến *thing.cheese* thì ánh xạ với seft.cheese trong khai báo lớp
