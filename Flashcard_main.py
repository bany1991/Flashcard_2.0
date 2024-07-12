import json
import time

class Json:
    def __init__(self,name):
        self.name = f'{name}.json'
        self.data = None


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


    def updateFlashcard(self,flashcard,last_repeats):
        pass

    def saveflashcard(self,data):
        with open(self.name, 'w') as file:
            self.data = data
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

    @classmethod
    def to_repeat(cls):
        repeats = []
        for instance in cls.instances:
            if instance.repeats[-1] <= time.time():
                repeats.append(instance)
        return repeats

    @classmethod
    def to_json(cls):
        fc_data = {'flashcards': [flashcard.__dict__
                                for flashcard in cls.instances] }
        return fc_data


name = "test"

fc_json = Json(name)
fc_json.loadAllFlashcard()

F_cos = Flashcard('something','cos',[10010,12546],[{"test1":"Atest1"},{"test2":"Atest2"}])

fc_json.saveflashcard(Flashcard.to_json())


# print(Flashcard.get_count())
# print(Flashcard.to_repeat())

# for instance in all_instances:
#      print(instance.front)

