from os import write


class Book:
    def __init__(self,title:str,author:str,content:str):
        self.title = title
        self.author = author
        self.content = content


class SaveToFile:
    @staticmethod
    def write_to_file(filename,book:Book):
        with open(filename,"w") as f:
            f.write(book.content)





