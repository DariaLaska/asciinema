class str_from_file:
    def __init__(self):
        file_obj = open("1148.cast", "r")

        file_data = file_obj.read()
        self.lines = file_data.splitlines(keepends=True)

        self.now = -1
        self.lenn = len(self.lines)-1

    def __iter__(self):
        return self

    def __next__(self):
        if self.now < self.lenn:
            self.now+=1
            return self.lines[self.now]
        else:
            raise StopIteration
            file_obj.close()




my_iter = iter(str_from_file())
for i in my_iter:
    print(i)

