# Exercise 5: More Variables and Printing

## I. Ví dụ 
Các bài trước bạn đã học được cách in ra màn hình một chuỗi.

Trong bài chúng ta có thể học về cách tạo ra một chuỗi và gắn biến vào chuỗi này. Trong bài này chúng ta sẽ sử dụng một khái niệm format string.

Mình có đoạn code như sau: 

```sh
# -*- coding: utf-8 -*-
my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
my_age, my_height, my_weight, my_age + my_height + my_weight)
```

## II. Output của đoạn code trên 

<img src=http://i.imgur.com/4QdLBd4.png width="60%" height="60%" border="1">


Giải thích code một chút:

Từ dòng 2 đến 8 là khai báo biến.

Băt đầu từ dòng 10 trở đi ta sẽ thấy trong chuỗi in ra màn hình xuất hiện %s hoặc %d nhưng tham số này là format string mục đích là để đưa biến vào trong chuỗi. Sau khi kết thúc 1 chuỗi thì sẽ là %tenbien truyền vào chuỗi. Nếu trong chuỗi của bạn có nhiều format string bạn có truyền biến theo cú pháp sau: %(tenbien1,tenbien2, ...)

Bạn có thể sử dụng `%r` để thay thế các ký tự `%s` và `%d` . Hãy thử và quan sát xem điều gì xảy ra nhé.

`%s` dùng để thay thế cho chuỗi.

`%d` dùng để thay thế cho số

`%r` bạn tự đoán nhé :)

## III. Luyện Tập 

## IV. Câu hỏi 



