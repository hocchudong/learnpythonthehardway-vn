
Bạn đã được học *if-statements*, functions và list. Giờ ta sẽ ôn lại những kiến thức này. thực hiện đoạn chương trình sau và xem chương trình làm những gì:

```sh
from sys import exit

def gold_room():
    print "This room is full of gold.  How much do you take?"

    choice = raw_input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        dead("You greedy bastard!")


def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False

    while True:
        choice = raw_input("> ")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that m

def cthulhu_room():
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"

    choice = raw_input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print why, "Good job!"
    exit(0)

def start():
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"

    choice = raw_input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")


start()
```



### What You Shoud See
Chạy chương trình trên và nhập vào các tùy chọn, ví dụ 

```sh
$ python ex35.py
You are in a dark room.
There is a door to your right and left.
Which one do you take?
>  left
There is a bear here.
The bear has a bunch of honey.
The fat bear is in front of another door.
How are you going to move the bear?
>  taunt bear
The bear has moved from the door. You can go through it now.
>  open door
This room is full of gold.  How much do you take?
>  1000
You greedy bastard! Good job!
```

### Study Drills

1. Vẽ sơ đồ của trò chơi và làm cách nào để vượt qua trò chơi
2. Sữa tất cả các lỗi của bạn, bao gồm cả lỗi cú pháp
3. Viết chú thích cho các funtions mà bạn không hiểu
4. Thêm vào game, đơn giản
5. Trong hàm *gold_room* yêu cầu người dùng nhập vào một số. Bắt lỗi khi người dùng nhập vào không phải là số nguyên. Sử dụng hàm int() để làm việc này
6. 
### Common Student Questions
Q1 : Tại sao lại viết *while True*?

Answer: vòng lặp vô hạn, chỉ thoát ra khi có câu lệnh rẽ nhánh hoặc là lệnh chuyển sang hàm khác

Q2: *exit(0)* để làm gì?

Answer: Rất nhiều hệ thổng có thể hủy bỏ với *exit(0)*, nếu là *exit(1)* thì sẽ có lỗi. như vậy ta có thể sử dụng *exit(1)* và *exit(2)* cho các lỗi khác nhau

Q3: Tại sao trong một vài trường hợp sử dụng raw_input(), một vài trường hợp sử dụng raw_input('> ')?

Answer: tất cả các chuỗi string trong raw_input đều có mục đích gợi ý và nhắc người dùng nhập vào

