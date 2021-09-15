class Text(str):
    def duplicate(self):
        return self + self


class TrackableList(list):
    def append(self, value):
        print("Append called")
        super().append(value)


list = TrackableList()
list.append("1")
