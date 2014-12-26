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
