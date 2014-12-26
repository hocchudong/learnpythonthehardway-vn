Giờ ta sẽ tìm hiểu một khái niệm quan trọng trong Python và được thường xuyên sử dụng là "dicts". Một số ngôn
ngữ khác gọi là "hashes". Ta có xu hướng sử dụng cả hai tên nhưng điều đó không quá quan trọng
. Ta hãy xem danh sách list làm được những gì

```sh
>>> things = ['a', 'b', 'c', 'd']
>>> print things[1]
b
>>> things[1] = 'z'
>>> print things[1]
z
>>> things
['a', 'z', 'c', 'd']
```
Ta có thể sử dụng chỉ số để lấy các phần tử trong danh sách. Trường hợp ta muốn lấy một đối tượng đi theo từ khóa thì list không làm được việc này, khi đó ta cần sử dụng dict. Với dict thì gắn khóa với giá trị. Xem ví dụ dưới đây

```sh
>>> stuff = {'name': 'Zed', 'age': 39, 'height': 6 * 12 + 2}
>>> print stuff['name']
Zed
>>> print stuff['age']
39
>>> print stuff['height']
74
>>> stuff['city'] = "San Francisco"
>>> print stuff['city']
San Francisco
```
Bạn sẽ thấy thay vì dùng số chúng ta sử dụng string khi chúng ta muốn gọi ra
các đối tượng. Chúng ta cũng có thể chèn thêm các đối tượng khác vào trong 
từ điển. chúng ta cũng có thể truyền vào key là một số

```sh
>>> stuff[1] = "Wow"
>>> stuff[2] = "Neato"
>>> print stuff[1]
Wow
>>> print stuff[2]
Neato
>>> stuff
{'city': 'San Francisco', 2: 'Neato', 'name': 'Zed', 1: 'Wow', 'age': 39, 'height': 74}
```
Trong đoạn code này, tôi sử dụng các con số, và sau đó bạn có thể  thấy những con số và chuỗi string như là chìa khóa trong dict khi tôi muốn in chúng ra.

Ta cũng có thể xóa các phần tử trong từ điển với *del*

```sh
>>> del stuff['city']
>>> del stuff[1]
>>> del stuff[2]
>>> stuff
{'name': 'Zed', 'age': 39, 'height': 74}
```

## Ví dụ cho Dictionary

Bây giờ chúng ta sẽ làm một bài tập mà bạn phải chú ý cẩn thận . Tôi muốn bạn gõ code này vào và cố gắng hiểu những gì đang .


