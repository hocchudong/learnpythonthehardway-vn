#Exercise 17: More Files

## Ví dụ 

Bây giờ ta sẽ làm nhiều hơn về file, trong bài này viết một đoạn script để copy nội dung từ file này đến file khác. 

Code: 

    from sys import argv
    from os.path import exists
    script, from_file, to_file = argv
    # In ra tên 2 file 
    print "Copying from %s to %s" % (from_file, to_file)
    # Mở file muốn copy
    in_file = open(from_file)
    # Đọc toàn bộ nội dung của in_file và trả về một chuỗi được lưu trong indata. hàm read() trả về 1 chuỗi. 
    indata = in_file.read()
    print "The input file is %d bytes long" % len(indata)
    # Kiểm tra xem file copy đến có tồn tại không
    print "Does the output file exist? %r" % exists(to_file)
    # Có chắc muốn tiếp tục copy hay không nếu có ấn một nút bất kì nếu không ctrl-c
    print "Ready, hit RETURN to continue, CTRL-C to abort."
    raw_input()
    # Mở file nếu file này tồn tại sẽ xóa hết nội dung file nay, nếu chưa sẽ tạo ra file mới.
    out_file = open(to_file, 'w')
    # ghi nội dung lấy từ from_file vào to_file 
    out_file.write(indata)
    print "Alright, all done."
    # đòng 2 file lại. 
    out_file.close()
    in_file.close()


## Chạy file code 

    $ echo "This is a test file." > test.txt
    $ python ex17.py test.txt new_file.txt
    Copying from test.txt to new_file.txt
    The input file is 21 bytes long
    Does the output file exist? False
    Ready, hit RETURN to continue, CTRL-C to abort.

Kiểm tra nội dung của new_file.txt bằng lệnh *cat* để xem kết quả. 

## Luyện tập 

* Tìm hiểu tại sao bạn phải dùng out_file.close() trong code 

## Câu hỏi 

* Hàm len() là gì ?

      Nó trả về độ dài của chuỗi

* Tôi nhân được lỗi sau: *Syntax:EOL while scanning string literal*

     Bạn quên không kết thúc chuỗi với với dấu ngoặc kép.
















