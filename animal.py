class Animal:

    def __init__(self):
        self.num_eyes = 2

    def breath(self):
        print("Inhale, exhale.")


class Fish(Animal):

    def __init__(self):
        super().__init__()

    def breath(self):
        super(Fish, self).breath()
        print('Doing this underwater.')

    @staticmethod
    def swim(self):
        print('Moving in water!')


nemo = Fish()
nemo.swim()
nemo.breath()
print(nemo.num_eyes)
