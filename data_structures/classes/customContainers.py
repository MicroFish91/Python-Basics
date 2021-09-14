class TagCloud:
    def __init__(self):
        self.__tags = {}

    def __str__(self):
        display = ""
        for tag, count in self.__tags.items():
            display += f"{tag}: {count}\n"
        return display

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, value):
        self.__tags[tag.lower()] = value

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1


cloud = TagCloud()
cloud.add("Python")
cloud.add("Python")
cloud.add("Python")

print(cloud)
# print(cloud.__tags)  # prefix with __ to make private

print(cloud.__dict__)
print(cloud._TagCloud__tags)
