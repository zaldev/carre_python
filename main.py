
# a canvas with mobile objects
class Canvas:
    def __init__(self):
        self.objects = []

    def add(self, obj):
        self.objects.append(obj)

    def draw(self):
        for obj in self.objects:
            obj.draw()

    def move(self):
        for obj in self.objects:
            obj.move()



if __name__ == '__main__':
    print("ok")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
