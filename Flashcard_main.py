import json
import time
import random
import sys
from PyQt6.QtWidgets import QApplication,QWidget

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Flashcards")
        self.setGeometry(500,300,400,300)
        stylesheet = (
            'background-color:white'
        )
        self.setStyleSheet(stylesheet)


class Json:
    def __init__(self,name):
        self.name = f'{name}.json'
        self.data = None


    def loadAllFlashcard(self):
        with open(self.name, 'r') as file:
            dane = json.load(file)
            flashcards = dane.get('flashcards')

            for flashcard in flashcards:
                front = flashcard.get('front')
                back = flashcard.get('back')
                repeats = flashcard.get('repeats')
                library = flashcard.get('library')
                goodinrow = flashcard.get('goodinrow')
                Flashcard(front,back,repeats,library,goodinrow)

    def updateFlashcard(self,flashcard,last_repeats):
        pass

    def saveflashcard(self,data):
        with open(self.name, 'w') as file:
            self.data = data
            json.dump(self.data, file, indent=4, ensure_ascii=False)


class Flashcard:
    instances = []
    count = 0

    def __init__(self,front='',back='', repeats=None,library=None,goodinrow = 0):
        Flashcard.instances.append(self)
        Flashcard.count += 1
        self.front = front
        self.back = back
        self.repeats = repeats if repeats is not None else []
        self.library = library if library is not None else []
        self.goodinrow = goodinrow

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
    def repetioinTime(self,goodorbad):
        """
        goodorbad: bad anwser = 0, good anwser = 1

        """
        DAY = 86400
        REP_INTERVAL = [DAY*0.3,DAY*1.9,DAY*3.9,DAY*11.9,DAY*34.9,DAY*60,DAY*90,DAY*120]

        if goodorbad == 0:
            self.goodinrow =0
            self.repeats.append(time.time())
        elif goodorbad == 1:
            self.goodinrow +=1
            if self.goodinrow <= len(REP_INTERVAL):
                self.repeats.append(REP_INTERVAL[self.goodinrow - 1] + time.time())
            else:
                self.repeats.append(REP_INTERVAL[-1] + time.time() )


name = "test"

fc_json = Json(name)
fc_json.loadAllFlashcard()
to_repeat = Flashcard.to_repeat()
print(len(to_repeat))
for rep in to_repeat:
    print(rep.front)
    rep.repetioinTime(1)


# F_cos = Flashcard('something3','cos',[1720894203.576264],[{"test1":"Atest1"},{"test2":"Atest2"}],0)


fc_json.saveflashcard(Flashcard.to_json())

# print(Flashcard.get_count())
# print(Flashcard.to_repeat())

# for instance in all_instances:
#      print(instance.front)

# app = QApplication([])
# window = Window()
# window.show()
# sys.exit(app.exec())