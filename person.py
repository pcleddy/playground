import pprint as pp


class Person(object):
    def __init__(self, **kwargs):
        self.name = kwargs.pop('name', 'No Name')
        self.age = kwargs.pop('age', 0)

class Kid(Person):
    def __init__(self, **kwargs):
        self.mom = kwargs.pop('mom')
        self.grade = kwargs.pop('grade', 0)
        super(Kid, self).__init__(**kwargs)

class Adult(Person):
    def __init__(self, **kwargs):
        self.kids = kwargs.pop('kids')
        self.job = kwargs.pop('job', 'unemployed')
        self.mom = kwargs.pop('mom')
        super(Adult, self).__init__(**kwargs)

bob = Kid(name='bobz', age=13, mom='jill', grade=6)
jack = Kid(name='jack', age=9, mom='jill', grade=2)
jane = Adult(kids=[jack, bob], name='jane', age=39, mom='wilma', job='banker')


kids = [bob, jack]
for person in kids:
    pp.pprint(person.__dict__)

adults = [jane]
for person in adults:
    pp.pprint(person.__dict__)


print("\n\n")
print('END')
