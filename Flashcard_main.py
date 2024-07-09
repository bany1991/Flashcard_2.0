class Flashcard:
    instances = []
    count = 0

    def __init__(self,front='',back='',repeats=None,library=None):
        Flashcard.instances.append(self)
        Flashcard.count += 1
        self.front = front
        self.back = back
        self.repeats = repeats if repeats is not None else []
        self.library = library if library is not None else []

    @classmethod
    def get_all_instances(cls):
        return cls.instances

    @classmethod
    def get_count(cls):
        return cls.count

F_car = Flashcard('car','samochod',[10010,12546],[{"test1":"Atest1"},{"test2":"Atest2"}])
F_areoplane = Flashcard('areoplane','samolot',[10010,12546],[{"test1":"Atest1"},{"test2":"Atest2"}])


all_instances = Flashcard.get_all_instances()
print(Flashcard.get_count())

for instance in all_instances:
    print(instance.front)

