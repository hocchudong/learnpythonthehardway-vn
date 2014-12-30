# Exercise 21: Functions Can Return Something

## Ví dụ 

Bạn đã sử dụng kí tự "=" để đặt tên và gán trị số và chuỗi cho chúng. Bây giờ chúng tôi sẽ thổi cho bạn ý tưởng lại lần nữa bởi việc chỉ ra cho bạn làm thế nào để sử dụng kí tự "=" và một từ mới return để thiết lập giá trị bằng hàm trong python. 

Script: 

    def add(a, b):
        print "ADDING %d + %d" % (a, b)
        return a + b
    
    def subtract(a, b):
        print "SUBTRACTING %d - %d" % (a, b)
        return a - b
    def multiply(a, b):
        print "MULTIPLYING %d * %d" % (a, b)
        return a * b
    def divide(a, b):
        print "DIVIDING %d / %d" % (a, b)
        return a / b


    print "Let's do some math with just functions!"
    age = add(30, 5)
    height = subtract(78, 4)
    weight = multiply(90, 2)
    iq = divide(100, 2)
    print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)
    print "Here is a puzzle."
    what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
    print "That becomes: ", what, "Can you do it by hand?"


Đoán script trên thì làm ra các hàm toán học của chúng ta. Nhưng thứ quan trọng là dòng cuối ở đây chúng tôi nói là return a + b 

## Chạy code 

    python ex21.py
    Let's do some math with just functions!
    ADDING 30 + 5
    SUBTRACTING 78 - 4
    MULTIPLYING 90 * 2
    DIVIDING 100 / 2
    Age: 35, Height: 74, Weight: 180, IQ: 50
    Here is a puzzle
    DIVIDING 50 / 2
    MULTIPLYING 180 * 25
    SUBTRACTING 74 - 4500 
    ADDING 35 + -4426
    That becomes:  -4391 Can you do it by hand?

## Luyện tập

* Nếu bạn chưa chắc về return, thử viết một vài hàm của mình và trả lại một vài giá trị
* Hơi ngươc, Viết một công thức đơn giản và sử dụng các hàm như một cách để tính

## Câu hỏi

* Tôi có thể sử dụng raw_input() để nhập giá trị của mình không ?

    Hãy nhớ đến int(raw_input())? vấn đề với điều này là bạn không thể nhập được kiểu float, thay vào đó hãy sử dụng float(raw_input()).
    

