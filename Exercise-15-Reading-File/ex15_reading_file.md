Như chúng ta biết nhận dữ liệu nhập vào từ người dùng với raw_input hoặc argv. Giờ ta sẽ lấy dữ liệu từ file. Ở đây trong
cùng một thư muc ta cần có hai file. Một file ex15.py và một file ex15_test.txt. Giả sử ta muốn in ra màn hình
 nội dung file ex15_test.txt 
```sh
Phong nghien cuu và phat trien giai phap Cloud-Computing
Trung tam VDC-IT
Nguyen Phong Sac, Cau Giay, Ha Noi
```
Giải pháp đưa ra là kết hợp argv và raw_input để lấy dữ liệu tên file
```sh
from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
```
### What You Should See

Tạo file ex15_test.py và chạy script
```sh
$ python ex15.py ex15_test.txt
Phong nghien cuu và phat trien giai phap Cloud-Computing
Trung tam VDC-IT
Nguyen Phong Sac, Cau Giay, Ha Noi

Type the filenae again:
>  ex15_test.txt
Phong nghien cuu và phat trien giai phap Cloud-Computing
Trung tam VDC-IT
Nguyen Phong Sac, Cau Giay, Ha Noi
```
### Study Drills

### Common Student Questions


