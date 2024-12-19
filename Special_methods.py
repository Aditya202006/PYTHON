# Using of specials methods such as (__str__),(__len__),(__del__)

class Book():
    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages

    def __str__(self):
        return f"{self.title} by {self.author}"
    def __len__(self):
        return self.pages
    def __del__(self):
        print("It is deleted")


b=Book('Wings of Fire','Abdul kalam',257)

print(b)  # Wings of Fire by Abdul kalam

len(b) # 257

del(b) # It is deleted
