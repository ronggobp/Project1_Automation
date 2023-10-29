from modules.library_item import LibraryItem

class Magazine(LibraryItem):
    def __init__(self, title, upc, subject, volume, issue):
        LibraryItem.__init__(self, title,  upc, subject)
        self.volume = volume
        self.issue = issue
