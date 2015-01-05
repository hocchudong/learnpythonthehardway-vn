Trong những bài trước bạn đã học về list. Dùng vòng lặp while để thêm các phân vào trong list và in chúng ra . Bạn thể quay trở lại những bài trước để xem lại

Trong bài trước, chúng ta đã biết hàm *append* để thêm phần tử vào list. Tuy nhiên có thể bạn chưa hiểu hết được append làm việc với list như thế nào, ví dụ dưới đây sẽ cho bạn thấy rõ hơn điều đó.

When you write mystuff.append('hello') you are actually setting off a chain of events inside Python to cause something to happen to the mystuff list. Đây là cách nó hoạt động

1. Python thấy bạn đề cập đến biến mystuff. Nhận thấy phía sau ta gán "=",là một tham số của hàm , hoặc là một biến toàn cục.
2. Python nhận thấy có dấu "." và xem xét các biến mà là một phần của mystuff
3. Sau đó  list mystuff sẽ tìm tất cả các hàm mà nó sử lý. Nếu hàm append có trong đó thì append được sử dụng
4. Python gọi hàm ra và chèn tham số vào  
5. Thực chất Python gọi hàm append( mystuff, hello) đúng hơn là gọi hàm. mystuff.append('hello')

Đối với hầu hết các phần bạn không cần phải biết rằng điều này đang xảy ra , nhưng nó giúp khi bạn nhận được thông báo lỗi từ Python như thế này :

```sh
$ python
Python 2.6.5 (r265:79063, Apr 16 2010, 13:57:41)
[GCC 4.4.3] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> class Thing(object):
...     def test(hi):
...             print "hi"
...
>>> a = Thing()
>>> a.test("hello")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: test() takes exactly 1 argument (2 given)
>>>


```

Nhìn đoạn code trên, ta đã gọi hàm test trong lớp Thing, tuy nhiên lênh xuất ra màn hình trong hàm vẫn không được chạy. Lỗi thông báo * test() takes exactly 1 argument . trong khi đó ta lại cho 2 argument, Như vậy OpenStack sẽ thay 
a.test("hello") thành test(a,"hello")

Chúng ta xem xét bài tập dưới đây

```sh
ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 things in that list. Let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There are %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1] # whoa! fancy
print stuff.pop()
print ' '.join(stuff) # what? cool!
print '#'.join(stuff[3:5]) # super stellar!
```

##What would you see

Chạy chương trình trên ta sẽ thấy 
```sh
$ python ex38.py
Wait there are not 10 things in that list. Let's fix that.
Adding:  Boy
There are 7 items now.
Adding:  Girl
There are 8 items now.
Adding:  Banana
There are 9 items now.
Adding:  Corn
There are 10 items now.
There we go:  ['Apples', 'Oranges', 'Crows', 'Telephone', 'Light', 'Sugar', 'Boy', 'Girl', 'Banana', 'Corn']
Let's do some things with stuff.
Oranges
Corn
Corn
Apples Oranges Crows Telephone Light Sugar Boy Girl Banana
Telephone#Light
```

## What list can do

Nào bây giờ bạn hãy tạo  trò chơi dựa trên GoFish. Nếu bạn không biết trò GoFish thì hãy dành chút thời 
gian tham khảo trên internet. Những gì bạn phải làm là tạo ra các kịch bản khác nhau và đưa vào chương
trình Python. list là một trong những cấu trúc dữ liệu phổ biến nhất các lập trình viên sử dụng. chỉ đơn giản là số thứ tự của các sự kiện mà bạn muốn để lưu trữ và truy cập ngẫu nhiên hoặc tuyến tính bằng chỉ số . Điều đó là sao?

##When to Use Lists

Bạn sử dụng một danh sách bất cứ khi nào bạn có một cái gì đó phù hợp với các tính năng hữu dụng cấu trúc dữ liệu của danh sách

1. Nếu bạn cần để duy trì trật tự . Hãy nhớ, đây là thứ tự liệt kê, không được sắp xếp theo thứ tự. Danh sách không sắp xếp cho bạn 
2. Nếu bạn cần truy cập vào các nội dung bởi một số ngẫu nhiên . Hãy nhớ rằng, điều này được sử dụng số đếm bắt đầu từ 0
3. Nếu bạn cần đi nội dung từ đầu đến cuối, vòng lặp for sẽ được dùng

## Study Drills

1. Mỗi fuction trong Python hãy chỉ ra từng bước mà Python gọi chúng, ví dụng more_stuff.pop() như là pop(more_stuff)
2. Dịch ra 2 cách để nhìn các hàm. Ví dụ more_stuff.pop() đọc như là" Gọi *pop* trên *more_stuff*. Trong khi ấy pop(more_stuff) gọi hàm *pop* với tham số *more_stuff* và cách nào mà cách hai cách gọi đó tương tự nhau
3. đọc lập trình hướng đội tượng online
4. Đọc lớp trong Python. Không đọc tài liệu sử lớp của các ngôn ngữ khác, nó chỉ làm bạn dối hơn thôi.
5. Nếu bạn thấy khó khăn trong lập trình hướng đối tượng thì cũng đừng quá lo lắng, hãy thữ lập trình chức năng
6. Tìm 10 ví dụ về những thứ bạn tìm thấy trong thực tế và điền trong vào list. và viết script làm việc với chúng

## Common Student Questions
Q: stuff[3:5] có vai trò như thế nào

Answer: Hàm trên lấy ra phần tử 3 và phần tử 4 trong stuff, không lấy ra phần tử thứ 5
