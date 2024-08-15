import sys


class Window:
    def exit(self):
        sys.exit(0)


class Document:
    def __init__(self, filename):
        self.filename = filename
        self.contents = "This file cannot be modified"

    def save(self):
        with open(self.filename, 'w') as file:
            file.write(self.contents)


class ToolbarDocument:
    def __init__(self, name, iconname):
        self.name = name
        self.iconname = iconname

    def click(self):
        self.command.execute()


class MenuItem:
    def __init__(self, menu_name, item_name):
        self.menu = menu_name
        self.item = item_name

    def click(self):
        self.command.execute()


class KeyboardShortcut:
    def __init__(self, key, modifier):
        self.key = key
        self.modifier = modifier

    def keypress(self):
        self.command.execute()


class SaveCommand:
    def __init__(self, document):
        self.document = document

    def execute(self):
        self.document.save()


class ExitCommand:
    def __init__(self, window):
        self.window = window

    def execute(self):
        self.window.exit()


#####################################################################


class Window:
    def exit(self):
        print("Exiting the window...")


class Document:

    def save(self):
        print("Saving the document...")


class ToolbarDocument:

    def click(self):
        print("Toolbar document clicked.")


class MenuItem:

    def click(self):
        print("Menu item clicked.")


class KeyboardShortcut:

    def keypress(self):
        print("Keyboard shortcut pressed.")


class SaveCommand:
    def __init__(self, document):
        self.document = document

    def execute(self):
        self.document.save()


class ExitCommand:
    def __init__(self, window):
        self.window = window

    def execute(self):
        self.window.exit()


window = Window()
document = Document()
save_command = SaveCommand(document)
exit_command = ExitCommand(window)

save_command.execute()  # Output: Saving the document...
exit_command.execute()  # Output: Exiting the window...