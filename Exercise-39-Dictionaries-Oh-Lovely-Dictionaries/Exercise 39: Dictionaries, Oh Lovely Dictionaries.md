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
