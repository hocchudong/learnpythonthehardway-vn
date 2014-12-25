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
