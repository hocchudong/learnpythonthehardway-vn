# Exercise 20: Functions and Files

## Ví dụ 

Trong bài chúng ta học về cách kết hợp giữa hàm và file.

Script: 

    from sys import argv
    script, input_file = argv
    # đọc file 
    def print_all(f):
        print f.read()
    # di chuyển đến byte đầu tiên của file
    def rewind(f):
        f.seek(0)
    #In ra dòng thứ và in ra dòng 
    def print_a_line(line_count, f):
        print line_count, f.readline()
    current_file = open(input_file)
    print "First let's print the whole file:\n"
    print_all(current_file)
    print "Now let's rewind, kind of like a tape."
    rewind(current_file)
    print "Let's print three lines:"
    current_line = 1
    print_a_line(current_line, current_file)
    current_line = current_line + 1
    print_a_line(current_line, current_file)
    current_line = current_line + 1
    print_a_line(current_line, current_file)

## Chạy code 

    $ python ex20.py test.txt
    First let's print the whole file:

    This is line 1
    This is line 2
    This is line 3

    Now let's rewind, kind of like a tape.
    Let's print three lines:
    1 This is line 1

    2 This is line 2

    3 This is line 3

## Luyện tâp

* Viết comment trên mỗi dòng để hiểu dòng này làm gì
* Với mỗi lần print_a_line đang chạy, bạn đang truyền một biến là current_line
* Tìm đến mỗi một hàm được sử dụng, kiểm tra lại *def* để chắc chắn rằng bạn đã truyền đúng tham số.
* Nghiên cứu về hàm seek(). Thử pydoc file
* Nghiên cứu lại kí tự +=

## Câu hỏi

* f là gì trong hàm print_all và các hàm khác?

    Biến f là giống như các hàm trong bài 18. Một file trong python sẽ giống như một ổ đĩa lơn, hoặc một ổ đĩa DVD. Nó có "read head" , và bạn có thể "seek" như một đầu đọc sẽ di chuyển đên con trỏ một ví trị nào trong file, và sau đó làm việc với nó. Mỗi làn bạn chạy f.seek(0) bạn sẽ di chuyển đến ví trị đầu tiên của file. Mỗi lần bạn chạy f.readline() bạn đang đọc một dòng từ file, và di chuyển từ đầu đến cuối file bởi kí tự "\n".

* Tại sao là ko đặt seek(current_line) thay bằng seek(0) ?

    Đầu tiên, hàm seek() là byte không phải line. Hàm seek(0) di chuyển đến byte đầu tiên của file. 

* readline() biết được mỗi dòng như thế nào ?

    Bên trong readline() là code mà có thể quét mỗi byte của file cho đến khi tìm đến kí tự "\n", sau đó dừng lại việc đọc file trả lại chuối. File f chịu trách nhiệm duy trì vị trí hiện tại của file.
