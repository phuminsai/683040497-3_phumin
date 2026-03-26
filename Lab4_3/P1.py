import datetime 

class LibraryItem:
    def __init__(self, title, item_id):
        self.title = title
        self._id = item_id
        self._checked_out = False 
    
    def get_status(self):
        return "Checked out" if self._checked_out else "Available"
    
    def check_out(self):
        if not self._checked_out:
            self._checked_out = True
            return True
        return False

    def return_item(self):
        if self._checked_out:
            self._checked_out = False
            return True
        return False 

    def display_info(self):
        print(f"ID: {self._id}, Title: {self.title}, Status: {self.get_status()}")


class Book(LibraryItem):
    def __init__(self, title, item_id, author):
        super().__init__(title, item_id) 
        self.author = author
        self.pages_count = 0 

    def set_pages(self, pages): 
        self.pages_count = pages

    def display_info(self): 
        status = self.get_status()
        print(f"Title: {self.title}, Author: {self.author}, Pages: {self.pages_count}, Status: {status}")


class TextBook(Book):
    def __init__(self, title, item_id, author, subject, grade_level):
        super().__init__(title, item_id, author) 
        self.subject = subject
        self.grade_level = grade_level

    def display_info(self): 
        status = self.get_status()
        print(f"Textbook: {self.title}, Subject: {self.subject} (Grade {self.grade_level}), Pages: {self.pages_count}, Status: {status}")


class Magazine(LibraryItem):
    def __init__(self, title, item_id, issue_number):
        super().__init__(title, item_id)
        self.issue_number = issue_number

        current_date = datetime.datetime.now()
        self.month = current_date.month
        self.year = current_date.year

    def display_info(self): 
        status = self.get_status()
        print(f"Magazine: {self.title} (Issue: {self.issue_number}), Date: {self.month}/{self.year}, Status: {status}")



print("--- TEST 1: Book ---")
my_book = Book("Harry Potter", "B001", "J.K. Rowling")
my_book.set_pages(350)     # ลองตั้งค่าหน้า
my_book.check_out()        # ลองยืม
my_book.display_info()     # แสดงผล

print("\n--- TEST 2: TextBook ---")
math_book = TextBook("Basic Math", "T001", "Dr. Somchai", "Mathematics", 10)
math_book.set_pages(120)
math_book.display_info()   # แสดงผล (สถานะต้อง Available เพราะยังไม่ยืม)

print("\n--- TEST 3: Magazine ---")
vogue = Magazine("Vogue", "M001", 155)
vogue.check_out()
vogue.return_item()        # ลองยืมแล้วคืน
vogue.display_info()