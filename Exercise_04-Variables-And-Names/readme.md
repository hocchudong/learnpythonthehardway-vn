# Exercise 4: Variables And Names 

## I. Ví dụ
Bây giờ bạn đã có thể in mọi thứ với print và bạn có thể làm với các phép toán. Bước tiếp theo là học về biến. Trong lập trình, biến chẳng qua là một cái tên, tương tự như "Tên tôi là Zed, người đã viết ra cuốn sách này". 

Biến thường là tên để gợi nhớ trong các đoạn code. Nếu biến được đặt tên không tốt, rất có thể khi đọc lại bạn sẽ quên rằng bạn đã viết gì.

Cú pháp:

```sh
tên biến = giá trị
```

Có đoạn code: 

```sh
# -*- coding: utf-8 -*-
# Khái báo biến cars
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90 
cars_not_driven = cars - drivers 
cars_driven = drivers 
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
```

## II. Output của đoạn code trên 

<img src=http://i.imgur.com/Fbz84x0.png width="60%" height="60%" border="1">

## III. Luyện Tập 

## IV. Câu hỏi 
