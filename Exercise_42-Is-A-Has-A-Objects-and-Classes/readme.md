Có một điều quan trọng là bạn phải hiểu sự khác biệt giữa lớp và đối tượng. Vấn đề là , không có " sự khác biệt" thực sự giữa một lớp và một đối tượng. Chúng có những nét tương đồng . Ví dụ như sự khác nhau giữa loài cá và cá hồi. Câu hỏi khiến ta có thể nhầm lẫn. Ta thấy rằng cá hồi và cá có khác nhau nhưng cá hồi là một dạng của cá, điều đó cũng có thể hiểu là không khác nhau giữa cá và cá hồi. Nhưng cá hồi có những điều khác biệt so với các loại cá khác. Cá hồi khác với cá mập. vì vậy cá hồi và cá có những điểm chung nhưng cũng có những điểm khác nhau.
 
 Bạn không cần nghĩ sự khác nhau giữa cá hồi và cá mập bởi vì bạn biết rằng chúng có liên hệ với nhau.Bạn biết cá hồi là một loại cá và có những loại cá khác mà .
 
 Bạn  hãy tưởng tượng rằng trong một bể cá có ba con cá tên là Frank, Joe và Mary. Câu hỏi được đặt ra là sự khác nhau giữa Mary và Salmon. Liên hệ với câu hỏi trước bạn biết rằng Mary là cá hồi. và Mary là một thí dụ của cá
 hồi. Joe và Frank cũng là những thí dụ của cá hồi. 

Bây giờ ta đã có những nhận định sau: Cá là một lớp, và cá hồi cũng là một lớp, Mary cũng là một lớp. lớp cá
là một lớp trừu tượng không chỉ cụ thể cho mội đối tượng nào. Cá là nói chung cho những thực thể mà chúng sống
ở dưới nước. Cá hồi là đối tượng của lớp cá sẽ có những đặc điểm riêng như màu đỏ, lớn, sống ở đại dương 
hoặc ở vùng nước ngọt.

## Code hướng đối tượng

```sh
## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## ??
class Dog(Animal):

    def __init__(self, name):
        ## ??
        self.name = name

## ??
class Cat(Animal):

    def __init__(self, name):
        ## ??
        self.name = name

## ??
class Person(object):

    def __init__(self, name):
        ## ??
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## ??
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## ??
        self.salary = salary

## ??
class Fish(object):
    pass

## ??
class Salmon(Fish):
    pass

## ??
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## ??
satan = Cat("Satan")

## ??
mary = Person("Mary")

## ??
mary.pet = satan

## ??
frank = Employee("Frank", 120000)

## ??
frank.pet = rover

## ??
flipper = Fish()

## ??
crouse = Salmon()

## ??
harry = Halibut()
```

## Tìm hiểu thêm

1. Nghiên cứu tại sao Python thêm lớp đối tượng này , và điều đó có nghĩa là gì.
2. Có thể sử dụng một lớp như một object
3. Thêm vào các lớp animal , fish, và people trong bài tập này với cac hàm
4. Tạo thêm nhiều lớp mới với các mối liên quan đến nhau

## Giải đáp

Q: self.pet = none

Answer: Câu lệnh trên thiết lập thuộc tính self có giá trị rỗng

Q:Lệnh super(Employee, self).__init__(name) để làm gì ?

Answer: Lệnh trên dùng để gọi lớp cha của lớp Employee
