Có hai cách để tạo ra chuỗi string có nhều dòng. Các thứ nhất là chèn " \n" vào giữa. Các thứ hai là trong chuỗi nhập vào đễ xuống dòng ta gõ " Enter"

Ví dụ
```sh
print("thanh \n ha")
```
hoặc là 
    
    print("""thanh
    ha""")

Để tạo ra khoảng trắng tương đương gõ phím "Tab" ta dùng \t . Một lưu ý nữa là khi ta muốn thêm dấu nháy kép " vào trong chuỗi ta không thể nhập chuỗi vào theo cách sau

    print(" thanh ha lam tai "VDC"")
    
khi đó ta phải sử dụng dấu nháy đơn ' thay cho nháy kép
```sh
print('thanh ha lam tai "VDC"')
```
Ta cũng có thể dùng """ trong trường hợp này.

Trường hợp ta muốn thêm dấu nháy đơn vào chuỗi thì làm ngược lại

Ví dụ
```sh
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
```
Chạy ví dụ ta sẽ thấy 
```sh
  I'm tabbed in.
I'm split
on a line.
I'm \ a \ cat.

I'll do a list:
        * Cat food
        * Fishies
        * Catnip
        * Grass
```
