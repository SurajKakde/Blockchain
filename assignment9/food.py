class Food:
    # name = None
    # kind = None
    def __init__(self, name, kind):
        self.name = name
        self.kind = kind

    def describe(self):
        print('Name of food is: {}'.format(self.name))
        print('and it\'s kind is : {}'.format(self.kind))

    def __repr__(self):
        return 'we have food {} of kind {}'.format(self.name, self.kind)

    # @staticmethod
    # def describe(name, kind):
    #     print('Name of food is: {}'.format(name))
    #     print('and it\'s kind is : {}'.format(kind))

    # @classmethod
    # def describe(cls, name, kind):
    #     print('Name of food is: {}'.format(name))
    #     print('and it\'s kind is : {}'.format(kind))


# # food1 = Food('Banana', 'fruit')
# food2 = Food()
# # food1.describe()
# food2.describe('Banana', 'Fruit')


class Meat(Food):
    @staticmethod
    def cook():
        print('\nCook the meat before eating')


m1 = Meat('chicken', 'meat')
m1.cook()
m1.describe()
print(m1)


class Fruit(Food):
    @staticmethod
    def clean():
        print('\nClean the friut before eating')


f1 = Fruit('Banana', 'fruit')
f1.clean()
f1.describe()
print(f1)