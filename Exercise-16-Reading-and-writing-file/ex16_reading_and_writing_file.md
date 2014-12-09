Làm việc với file ta cần nhớ tác dụng của một số hàm sau:

+ close: Đóng file. Giống như File -> Save trong soạn thảo
+ read : Đọc nội dung của file, ta có thể gán nội dung cho biến
+ readline: Đọc từng dòng của file 
+ truncate:  Làm rỗng file
+ write('stuff')- Ghi "stuff" vào file

Đoạn script sau ta sẽ truyền vào tên file và ghi nội dung vào file theo từng dòng

```sh
from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file.  Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()
```
### What You Shoud See
Chạy chương trình ta được kết quả sau

```sh
$ python ex16.py test.txt
We're going to erase 'test.txt'.
If you don't want that, hit CTRL-C (^C).
If you do want that, hit RETURN.
?
Opening the file...
Truncating the file.  Goodbye!
Now I'm going to ask you for three lines.
line 1:  Mary had a little lamb
line 2:  Its fleece was white as snow
line 3:  It was also tasty
I'm going to write these to the file.
And finally, we close it.
```
### Study Drills

### Common Student Questions

