

class Phone:
    def __init__(self, color, weight):
        self.color = color
        self.weight= weight

    def info(self):
        print(f"color: {self.color}")
        print(f"weight: {self.weight}")
        return self
    def call(self, number):
        print(f'calling {number}')
        return self

    def ring(self):
        print('ringing ringing')
        return self

    def hang_up(self):
        print('hanging up call')
        return self

class CellPhone(Phone):
    def __init__(self, color, weight): 
        super().__init__(color, weight) #This is calling on above inheritance
        self.type = "Cell Phone"

    def info(self):
        super().info()# this is calling on the parent info function
        print(f"type {self.type}")
        return self

    def text(self,number, msg):
        print(f"sending {number} the message: {msg}")
        return self

class FlipPhone(CellPhone):
    def __init__(self, color, weight):
        super().__init__(color, weight)
        self.flipped_status = "Close"
        self.type = "Flip Cell Phone"

    def info(self):
        super().info()
        print(f"flipped status {self.flipped_status}")
        return self

    def flipped_closed(self):
        self.flipped_status = "Close"
        return self


    def flipped_open(self):
        self.flipped_status = "open"
        return self

    def call(self, number):
        if self.flipped_status == "Close":
            print("must open first")
        else: 
            super().call(number)
        return self





phone1 = FlipPhone("blue", 5)
phone1.info().flipped_open().call(1234567898).text(1234567898, "Just sending this as a reminder")
