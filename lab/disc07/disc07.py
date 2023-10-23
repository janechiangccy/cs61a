# Q2: Email
class Email:
    """
    Every email object has 3 instance attributes: the
    message, the sender name, and the recipient name.
    >>> email = Email('hello', 'Alice', 'Bob')
    >>> email.msg
    'hello'
    >>> email.sender_name
    'Alice'
    >>> email.recipient_name
    'Bob'
    """

    def __init__(self, msg, sender_name, recipient_name):
        "*** YOUR CODE HERE ***"
        self.msg = msg
        self.sender = sender_name
        self.recipient = recipient_name


class Client:
    """
    Every Client has three instance attributes: name (which is
    used for addressing emails to the client), server
    (which is used to send emails out to other clients), and
    inbox (a list of all emails the client has received).

    >>> s = Server()
    >>> a = Client(s, 'Alice')
    >>> b = Client(s, 'Bob')
    >>> a.compose('Hello, World!', 'Bob')
    >>> b.inbox[0].msg
    'Hello, World!'
    >>> a.compose('CS 61A Rocks!', 'Bob')
    >>> len(b.inbox)
    2
    >>> b.inbox[1].msg
    'CS 61A Rocks!'
    """

    def __init__(self, server, name):
        self.inbox = []
        "*** YOUR CODE HERE ***"
        self.inbox = []
        self.server = server
        self.client = name
        self.server.register_client(self, self.name)

    def compose(self, msg, recipient_name):
        """Send an email with the given message msg to the given recipient client."""
        "*** YOUR CODE HERE ***"
        # self.recipient = recipient_name
        # recipient_name.inbox.append = msg

        email = Email(msg, self.name, recipient_name)
        self.server.send(email)

    def receive(self, email):
        """Take an email and add it to the inbox of this client."""
        "*** YOUR CODE HERE ***"
        self.inbox.append(email)


class Server:
    """
    Each Server has one instance attribute: clients (which
    is a dictionary that associates client names with
    client objects).
    """

    def __init__(self):
        self.clients = {}

    def send(self, email):
        """
        Take an email and put it in the inbox of the client
        it is addressed to.
        """
        "*** YOUR CODE HERE ***"

    def register_client(self, client, client_name):
        """
        Takes a client object and client_name and adds them
        to the clients instance attribute.
        """
        "*** YOUR CODE HERE ***"

# Q3: Keyboard


class Button:
    def __init__(self, pos, key):
        self.pos = pos
        self.key = key
        self.times_pressed = 0


class Keyboard:
    """A Keyboard stores an arbitrary number of Buttons in a dictionary. 
    Each dictionary key is a Button's position, and each dictionary
    value is the corresponding Button.
    >>> b1, b2 = Button(5, "H"), Button(7, "I")
    >>> k = Keyboard(b1, b2)
    >>> k.buttons[5].key
    'H'
    >>> k.press(7)
    'I'
    >>> k.press(0) # No button at this position
    ''
    >>> k.typing([5, 7])
    'HI'
    >>> k.typing([7, 5])
    'IH'
    >>> b1.times_pressed
    2
    >>> b2.times_pressed
    3
    """
    # 先將 keyword 裡面的 b1, b2 放在 keyword 裡面的 bottons，並用字典的方式存放 bottons's pos and key

    def __init__(self, *args):
        self.buttons = {}
        for button in args:
            self.buttons[button.pos] = button

    # press 是將 pos 對應的 key 值印出來，而 pos 在字典裡面扮演的是 key, key 則是 value，並把 times_pressed + 1
    def press(self, pos):
        """Takes in a position of the button pressed, and
        returns that button's output."""
        if pos in self.buttons.keys():
            b = self.buttons[pos]
            b.times_pressed += 1
            return b.key
        return ''

    # 將 typing_input 對應的 key type 出來，因為 typying_input 對應的是 pos，所以需要用 pos 去找對應的 value, 透過 press 的方式累加後再 return
    def typing(self, typing_input):
        """Takes in a list of positions of buttons pressed, and
        returns the total output."""
        accumulate = ''
        for pos in typing_input:
            accumulate += self.press(pos)
        return accumulate

# Q4: That's inheritance, init?


class Butterfly():
    def __init__(self, wings=2):
        self.wings = wings


class Monarch(Butterfly):
    def __init__(self):
        # Monarch 繼承 butterfly 的 wing = 2
        # super() 表示某部分的 init 是繼承 parent class 的 method，則在 init 的 () 如果只有 self 可不放值；若有 self 以外的參數，則要放值
        super().__init__()  # = Butterfly.__init__(self)
        self.colors = ['orange', 'black', 'white']


class MimicButterfly(Butterfly):
    def __init__(self, mimic_animal):
        super().__init__()
        self.name = mimic_animal

# Q5: Cat


class Pet():

    def __init__(self, name, owner):
        self.is_alive = True    # It's alive!!!
        self.name = name
        self.owner = owner

    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")

    def talk(self):
        print(self.name)


class Cat(Pet):

    def __init__(self, name, owner, lives=9):
        "*** YOUR CODE HERE ***"
        super().__init__(name, owner)
        self.live = lives

    def talk(self):
        """Print out a cat's greeting.

        >>> Cat('Thomas', 'Tammy').talk()
        Thomas says meow!
        """
        "*** YOUR CODE HERE ***"
        return f'{self.name} says meow!'

    def lose_life(self):
        """Decrements a cat's life by 1. When lives reaches zero,
        is_alive becomes False. If this is called after lives has
        reached zero, print 'This cat has no more lives to lose.'
        """
        "*** YOUR CODE HERE ***"
        if self.lives > 0:
            self.lives -= 1
            if self.lives == 0:
                self.is_alive = False
        else:
            print("This cat has no more lives to lose.")

    def revive(self):
        """Revives a cat from the dead. The cat should now have 
        9 lives and is_alive should be true. Can only be called
        on a cat that is dead. If the cat isn't dead, print 
        'This cat still has lives to lose.'
        """
        if not self.is_alive:
            self.__init__(self.name, self.owner)
        else:
            print('This cat still has lives to lose.')

# Q8: Cat Representation
# (The rest of the Cat class is omitted here, but assume all methods from the Cat class above are implemented)
    def __repr__(self):
        return self.name + ", " + str(self.lives) + " lives"

    def __str__(self):
        return self.name

# Q6: NoisyCat


class NoisyCat(Cat):
    """A Cat that repeats things twice."""

    def __init__(self, name, owner, lives=9):
        # Is this method necessary? Why or why not?
        # No, this method is not necessary because NoisyCat already inherits Cat's __init__ method
        "*** YOUR CODE HERE ***"
        super().__init__(name, owner, lives)

    def talk(self):
        """Talks twice as much as a regular cat.
        >>> NoisyCat('Magic', 'James').talk()
        Magic says meow!
        Magic says meow!
        """
        "*** YOUR CODE HERE ***"
        for i in range(2):
            super().talk()

# Q7: WWPD: Repr-esentation


class Car:
    def __init__(self, color):
        self.color = color

    def __repr__(self):
        return self.color

    def __str__(self):
        return self.color * 2


class Garage:
    def __init__(self):
        print('Vroom!')
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def __repr__(self):
        print(len(self.cars))
        ret = ''
        for car in self.cars:
            ret += str(car)
        return ret
