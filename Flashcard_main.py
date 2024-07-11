import json

class Json:
    def __init__(self,name,data=None):
        self.name = f'{name}.json'
        self.data = data if data is not None else {}


    def loadAllFlashcard(self):
        with open(self.name, 'r') as file:
            dane = json.load(file)
            flashcards = dane.get('flashcards')
            flashcards_number = len(dane.get('flashcards'))
            for i in range(flashcards_number):
                front = flashcards[i].get('front')
                back = flashcards[i].get('back')
                repeats = flashcards[i].get('repeats')
                library = flashcards[i].get('library')
                Flashcard(front,back,repeats,library)


    def updateFlashcard(self,front,last_repeats):
        pass

    def saveflashcard(self):
        with open(self.name, 'w') as file:
            json.dump(self.data, file, indent=4, ensure_ascii=False)


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


# F_car = Flashcard('car','samochod',[10010,12546],[{"test1":"Atest1"},{"test2":"Atest2"}])
# F_areoplane = Flashcard('areoplane','samolot',[10010,12546],[{"test1":"Atest1"},{"test2":"Atest2"}])

name = "test"


# flashcards = [F_car,F_areoplane]

# data = {'flashcards': [flashcard.__dict__
#                        for flashcard in flashcards] }

test = Json(name,None).loadAllFlashcard()
# print(len(test.get('flashcards')))

#test.saveflashcard()

all_instances = Flashcard.get_all_instances()
print(Flashcard.get_count())

for instance in all_instances:
    print(instance.front)

