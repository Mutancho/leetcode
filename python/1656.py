class OrderedStream:

    def __init__(self, n: int):
        self.arr = n * [None]
        self.stored_packages = {}

    def insert(self, idKey: int, value: str) -> list[str]:
        if not idKey == 1:
            for i in range(idKey - 1):
                if self.arr[i] is None:
                    self.stored_packages[idKey] = value
                    return []

        output = []
        counter = idKey
        output.append(value)
        self.arr[counter - 1] = value
        while True:
            counter += 1
            if counter not in self.stored_packages:
                return output
            self.arr[counter - 1] = value
            output.append(self.stored_packages[counter])


stream = OrderedStream(5)
print(stream.insert(3, "ccccc"))
print(stream.insert(1, "aaaaa"))
print(stream.insert(2, "bbbbb"))
print(stream.insert(5, "eeeee"))
print(stream.insert(4, "ddddd"))
print(stream.arr)
