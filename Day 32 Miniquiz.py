class Book_store:
    def __init__(self,n):
        self.name = n
        self.title_list = []
    def add_title(self,title_string):
        self.title_list.append(title_string)
    def count_titles(self,title_letter):
        count = 0
        for item in self.title_list:
            if title_letter.lower() == item[0].lower():
                count += 1
            else:
                continue
        return count
        



# testing code
store1 = Book_store("Barnes and Noble")
store1.add_title("Call of the Wild")
store1.add_title("War and Peace")
store1.add_title("Catcher in the Rye")
print(store1.count_titles("c"))  # should print 2
print(store1.count_titles("k"))  # should print 0
