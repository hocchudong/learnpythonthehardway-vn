# Exercise 18: Names, Variables, Code, Functions

## Ví dụ 

Trong bài này chúng ta sẽ học cách tạo ra hàm trong python.

Trong python thì sử dụng từ khóa *def* để định nghĩa ra hàm.

Script: 

     # Hàm này tương giống với tham số argv
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

* Hàm được định nghĩa trong python bằng từ khóa def. Cú pháp *def tên_hàm([tham_số_1],[tham_số_2],...):*
* Khối lệnh trong hàm phải cách nề 4 dấu cách và phải bằng nhau.  

## Chạy code 

    $ python ex18.py
    arg1: 'Zed', arg2: 'Shaw'
    arg1: 'Zed', arg2: 'Shaw'
    arg1: 'First!'
    I got nothin'.
    
## Luyện tập 

Tạo ra hàm một checklist dành cho các bài sau khi tạo ra hàm phải sử dụng checklist để kiểm tra. 

* Bạn đã bắt đầu hàm của bạn bằng định nghĩa def chưa ?
* Hàm của bạn có kí tự gạch dưới chưa "_" ?
* Bạn đã đặt kí tự "(" sau tên hàm chưa ?
* Bạn đã đặt tham số sau kí tự "(" chưa ?
* Bạn có tạo ra tên các tham số không bị trùng lặp ko?
* Bạn có đặt tham số bên kết thúc bằng bằng kí tự "):" không ?
* Bạn có đặt các dòng lệnh mà bạn muôn sau 4 dấu cách không ?
* Bạn có kết thúc hàm bằng cách không có dấu thụt ?

Khi bạn run một hàm, kiểm tra điều này: 

* Bạn có chạy hàm này bằng việc gõ tên không ?
* Bạn có đặt tên hàm sau kí tự "(" không ?
* Bạn có đặt giá trị trong giấu ngoặc và cách nhau bởi dấu phẩy ?
* Bạn có kết thúc việc gọi hàm bằng kí tự ")"

## Câu hỏi 

* Kí tự "*" trong *args để làm gì ?

    Điều này sẽ nói giữ tất các thông số đối với các hàm và sau đó đặt chúng trong args như là một list. Nó giống như argv mà bạn sử dụng, nhưng cho hàm. Nó không được sử dụng thông thường thường là cho các trường hợp đặc biêt.
   
* Điều này thật sự chán và đơn điệu ?

     Đó là điều tốt. Nó có nghĩa là bạn đã gõ code và hiểu được code. 
