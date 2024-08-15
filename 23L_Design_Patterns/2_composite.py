from sysconfig import get_path


class Component:
    def __init__(self, name):
        self.name = name
        self.parent = None

    def move(self, new_path):
        new_folder = get_path(new_path)

        del self.parent.children[self.name]

        new_folder.children[self.name] = self
        self.parent = new_folder

    def delete(self):
        del self.parent.children[self.name]



class Folder(Component):
    def __init__(self, name):
        super.__init__(name)
        self.children = {}

    def add_child(self, child):
        self.parent = self
        self.children[child.name] = child


class File(Component):
    def __init__(self, name, contents):
        super.__init__(name)
        self.contents = contents


root = Folder('')


def get_path(path):
    names = path.split('/')[1:]
    node = root
    for name in names:
        node = node.children[name]
    return node

###################################################################################################


from abc import ABC, abstractmethod

class Component(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def move(self, new_location):
        pass

    @abstractmethod
    def delete(self):
        pass

    @abstractmethod
    def get_path(self):
        pass

class File(Component):
    def __init__(self, name):
        super().__init__(name)

    def move(self, new_location):
        # Logic for moving a file to a new location
        print(f"Moving file '{self.name}' to {new_location}")

    def delete(self):
        # Logic for deleting the file
        print(f"Deleting file '{self.name}'")

    def get_path(self):
        # Return the path of the file
        return self.name

class Folder(Component):
    def __init__(self, name):
        super().__init__(name)
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def move(self, new_location):
        # Logic for moving the folder and its contents to a new location
        print(f"Moving folder '{self.name}' and its contents to {new_location}")
        for child in self.children:
            child.move(new_location)

    def delete(self):
        # Logic for deleting the folder and its contents
        print(f"Deleting folder '{self.name}' and its contents")
        for child in self.children:
            child.delete()
        self.children = []

    def get_path(self):
        # Return the path of the folder
        return self.name

    def get_full_path(self):
        # Recursive method to get the full path from the root
        path = [self.name]
        for child in self.children:
            child_path = child.get_path()
            if isinstance(child, Folder):
                child_path = child.get_full_path()
            path.append(child_path)
        return '/'.join(path)


root = Folder('root')
folder1 = Folder('folder1')
file1 = File('file1.txt')
file2 = File('file2.txt')

root.add_child(folder1)
folder1.add_child(file1)
root.add_child(file2)
print(root.get_full_path())