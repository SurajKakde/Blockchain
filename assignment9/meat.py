from food import Food

class Meat(Food):

    def cook(self):
        print('Cook the meat before eating')


m1 = Meat('chicken', 'meat')
m1.cook()
m1.describe()
print(m1)
