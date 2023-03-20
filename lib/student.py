class Student:
    str_hello = "Hey there! I'm so excited to learn stuff."
    str_rh = "Pick me!"
    def hello(self):
        print(self.str_hello)
    def raise_hand(self):
        print(self.str_rh)
    pass

class ChattyStudent(Student):
    def hello(self):
        print(super().str_hello)
        print("How are you doing today? I'm okay, but I'm kind of tired. Did you watch The Walking Dead last night? You didn't?! Oh man, it was so crazy! What, you don't want any spoilers? Okay well let me just tell you who died...")
    def raise_hand(self):
        for i in range(10):
            print(super().str_rh)

rex = ChattyStudent()
rex.hello()
rex.raise_hand()