class MySet:
    def __init__(self, your_list = []):
        self.my_list = your_list
        self.dictionary = {}
        for value in self.my_list:
            self.dictionary[value] = True

    def __repr__(self):
        return f'{[key for key in self.dictionary.keys()]}'

    def has(self, value):
        return value in self.dictionary

    def add(self, value):
        self.dictionary[value] = True
        return self

    def delete(self,value):
        return self.dictionary.pop(value, None)

    def size(self):
        return len(self.dictionary)

    def clear(self):
        return self.dictionary.clear()

