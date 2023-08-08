class TheCollection:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        for item in self.data:
            yield item
    
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, index):
        return self.data[index]