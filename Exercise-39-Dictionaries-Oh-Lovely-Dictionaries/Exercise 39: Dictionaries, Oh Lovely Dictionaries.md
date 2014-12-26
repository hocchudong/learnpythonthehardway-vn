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

Bây giờ chúng ta sẽ làm một bài tập mà bạn phải chú ý cẩn thận . Tôi muốn bạn gõ code này vào và cố gắng hiểu chúng
Hãy lưu ý khi bạn thêm vào dict , se nhận được một hàm băm. ví dụ này là lập bản đồ các quốc gia để chữ viết tắt của họ , và sau đó là chữ viết tắt về các thành phố ở các bang. Hãy nhớ rằng, "mapping " hoặc " associating " là khái niệm quan trọng trong một từ điển.

```sh
# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print '-' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

# print some states
print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

# do it by using the state then cities dict
print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

# print every state abbreviation
print '-' * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)

# print every city in state
print '-' * 10
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

# now do both at the same time
print '-' * 10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (
        state, abbrev, cities[abbrev])

print '-' * 10
# safely get a abbreviation by state that might not be there
state = states.get('Texas')

if not state:
    print "Sorry, no Texas."

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city
```

## Những gì bạn thấy

```sh
$ python ex39.py
----------
NY State has:  New York
OR State has:  Portland
----------
Michigan's abbreviation is:  MI
Florida's abbreviation is:  FL
----------
Michigan has:  Detroit
Florida has:  Jacksonville
----------
California is abbreviated CA
Michigan is abbreviated MI
New York is abbreviated NY
Florida is abbreviated FL
Oregon is abbreviated OR
----------
FL has the city Jacksonville
CA has the city San Francisco
MI has the city Detroit
OR has the city Portland
NY has the city New York
----------
California state is abbreviated CA and has city San Francisco
Michigan state is abbreviated MI and has city Detroit
New York state is abbreviated NY and has city New York
Florida state is abbreviated FL and has city Jacksonville
Oregon state is abbreviated OR and has city Portland
----------
Sorry, no Texas.
The city for the state 'TX' is: Does Not Exist
```

## Nhưng điều và Dicrionaries có thể làm

Từ điển là một ví dụ về cấu trúc dữ liệu, danh sách trong dictionaries là phổ biến nhất sử dụng cấu trúc dữ liệu trong lập trình. Một dictionary sử dụng map hoặc associate những gì bạn muốn 
lưu theo từ khóa

## Khi nào sử dụng Dictionaries, khi nào dùng List

Như đã đề cập ở bài 38. List được dùng để khi ta muốn lưu trữ hoặc tổ chức những thức theo kiểu danh sách.
Từ điển gần giống như vậy nhưng khác với list, từ điển mapping đối tượng lưu trữ với 
key. Rõ hơn thì ta sử dụng dictionary khi

1. Bạn có để lấy những điều dựa trên một số định danh , như tên, địa chỉ , hoặc bất cứ điều gì mà có thể là chìa khóa 
2. Khi ta không cần quan tâm đến thứ tự. Dictionaries không có khái niệm về thứ tự, list làm việc này
3. khi bạn muốn thêm hay loại phần tử theo từ khóa

## Tìm hiểu thêm

1. Thực hành cùng một loại bản đồ với các thành phố và tiểu bang / vùng lãnh thổ ở nước bạn hay một số nước khác
2. Tìm thêm tài liệu về dictionaries trong Python và cố gắng làm việc với chúng
3. Tìm những thứ mà bạn không thể làm việc với dictionaries. 
4. Tạo một hàm dump giống như list nhưng hàm có đầy đủ nội dung mà bạn có thể gỡ lỗi
5. Hãy chắc chắn rằng bạn hiểu được vai trò của hàm hash trong code. Đó là hàm đặc biệt để chuyển đổi string sang integer. Bạn có thể tìm hiểu thêm vai trò của hàm *hash* ở trên mạng

## Những câu hỏi chung

Q: Sự khác nhau giữa một list và dictionary?

Answer: Một list cho một danh sách có thứ tự. Còn từ điển hay dictionary để mapping giữa các items
keys và các items values

Q: Sử dụng từ điển như thế nào

Answer: khi ta muốn lấy giá trị trong dictionary ta có thể gọi theo từ khóa

Q: Sử dụng list như thế nào

Answer: Sử dụng list cho bất cứ danh sách có thứ tự và gọi chúng theo chỉ số index

Q: Nếu sử dụng dictionary, tôi cần sắp xếp chúng thì làm thế nào

Answer: Ta có thể sử dụng collections.OrderedDict trong Python.

