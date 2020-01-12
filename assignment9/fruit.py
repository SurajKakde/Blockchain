from food import Food

class Fruit(Food):
    def clean(self):
        print('Clean the friut before eating')


f1 = Fruit('Banana', 'fruit')
f1.clean()
f1.describe()
print(f1)