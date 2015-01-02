Ở phần này ta sẽ chạy script cùng với các tham số truyền vào

Ví dụ ở chương trình sau
```sh
from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
```

Ta dùng 'import' để thêm các tính năng cho script. Điều này làm cho chương trình nhỏ gọn hơn nhưng cũng đồng nghĩa ta phải viết tài liệu cho chương trình

'argv' là một biến luận lý, là một cú pháp chuẩn, chứa các biến được truyền vào khi chạy script. Như trong ví dụ trên là các biến firt, second, third.

### Hold Up! Features Have Another Name


### What You Should See
```sh
$ python ex13.py first 2nd 3rd
The script is called: ex13.py
Your first variable is: first
Your second variable is: 2nd
Your third variable is: 3rd
$ python ex13.py stuff things that
The script is called: ex13.py
Your first variable is: stuff
Your second variable is: things
Your third variable is: that
```
Nếu ta không chuyền đủ 3 tham số đầu vào thì chương trình sẽ báo lỗi
````sh
$ python ex13.py first 2nd
Traceback (most recent call last):
  File "ex13.py", line 3, in <module>
    script, first, second, third = argv
ValueError: need more than 3 values to unpack
```
### Study Drills

Bạn có thể kết hợp với `raw_input` để truyền đối số do bạn nhập vào. Bạn có thể chạy chương trình mở rộng có tên là `ex13_raw_input.py` để xem kết quả. Cách thực hiện chương trình này như sau

```sh
python ex13_raw_input.py To Thanh
```

Lưu ý: Đối số `To` và `Thanh` được truyền vào ngay khi thực thi chương trình. Sau đó bạn sẽ nhập thêm một giá trị tiếp theo ở màn hình nhắc lệnh:


### Câu hỏi chung
