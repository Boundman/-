class Unique(object):

    def __init__(self, items, **kwargs):
        self.items = []
        if type(items) == list:
            self.items = items
        else:
            self.items = [x for x in items]
        self.index = 0
        self.ignore_case = kwargs
        self.length = len(self.items)

    def __next__(self):
        if self.index == self.length-1:
            raise StopIteration

        arr = []
        if self.ignore_case:
            arr = [i.lower() for i in self.items]

        if self.ignore_case and arr.count(self.items[self.index].lower()) != 1:
            del self.items[self.index]
            self.length -= 1
        elif self.items.count(self.items[self.index]) != 1:
            del self.items[self.index]
            self.length -= 1
        else:
            self.index += 1
        return self.items[self.index]

    def __iter__(self):
        return self
