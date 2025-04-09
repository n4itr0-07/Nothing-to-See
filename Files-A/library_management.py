# Simple Library Management System
# This program has two basic classes: Book and Student
# It shows how to perform basic operations for a library

class Book:
    """
    A simple Book class to represent books in a library
    """
    # We'll store all our books in this list
    book_list = []
    
    def __init__(self, book_id, title, author):
        """
        Create a new book with given details
        """
        self.book_id = book_id        # Unique ID for the book
        self.title = title            # Title of the book
        self.author = author          # Author of the book
        self.available = True         # Is the book available to borrow?
    
    def addbook(book_id, title, author):
        """
        Add a new book to the library
        """
        # Create the new book
        new_book = Book(book_id, title, author)
        # Add to our list of books
        Book.book_list.append(new_book)
        print(f"Added book: {title} by {author}")
        return new_book
    
    def removebook(book_id):
        """
        Remove a book from the library using its ID
        """
        # Go through each book in our list
        for book in Book.book_list:
            # If we find the book with matching ID
            if book.book_id == book_id:
                # Remove it from the list
                Book.book_list.remove(book)
                print(f"Removed book with ID: {book_id}")
                return True
                
        # If we didn't find any matching book
        print(f"Book with ID {book_id} not found")
        return False


class Student:
    """
    A simple Student class to represent library members
    """
    # We'll store all our students in this list
    student_list = []
    
    def __init__(self, student_id, name):
        """
        Create a new student with given details
        """
        self.student_id = student_id  # Unique ID for the student
        self.name = name              # Name of the student
        self.books = []               # Books borrowed by this student
    
    def add(student_id, name):
        """
        Add a new student to the library system
        """
        # Create the new student
        new_student = Student(student_id, name)
        # Add to our list of students
        Student.student_list.append(new_student)
        print(f"Added student: {name} with ID {student_id}")
        return new_student
    
    def remove(student_id):
        """
        Remove a student from the library system using their ID
        """
        # Go through each student in our list
        for student in Student.student_list:
            # If we find the student with matching ID
            if student.student_id == student_id:
                # Check if they have any books
                if len(student.books) > 0:
                    print(f"Cannot remove student {student.name}. They need to return books first.")
                    return False
                    
                # If no books, remove the student
                Student.student_list.remove(student)
                print(f"Removed student with ID: {student_id}")
                return True
                
        # If we didn't find any matching student
        print(f"Student with ID {student_id} not found")
        return False
    
    def issue_book(self, book_id):
        """
        Allow a student to borrow a book
        """
        # Go through each book in our list
        for book in Book.book_list:
            # If we find the book with matching ID
            if book.book_id == book_id:
                # Check if the book is available
                if book.available:
                    # Mark as not available
                    book.available = False
                    # Add to student's books
                    self.books.append(book)
                    print(f"{self.name} borrowed '{book.title}'")
                    return True
                else:
                    print(f"Book '{book.title}' is not available")
                    return False
                    
        # If we didn't find any matching book
        print(f"Book with ID {book_id} not found")
        return False
    
    def return_book(self, book_id):
        """
        Allow a student to return a book
        """
        # Go through books borrowed by this student
        for book in self.books:
            # If we find the book with matching ID
            if book.book_id == book_id:
                # Mark as available
                book.available = True
                # Remove from student's books
                self.books.remove(book)
                print(f"{self.name} returned '{book.title}'")
                return True
                
        # If the student doesn't have this book
        print(f"You don't have a book with ID {book_id}")
        return False


# Example of how to use these classes
if __name__ == "__main__":
    # Add some books to the library
    Book.addbook(1, "Python Basics", "John Smith")
    Book.addbook(2, "Learn Python", "Jane Doe")
    Book.addbook(3, "Python for Beginners", "Mike Johnson")
    
    # Add some students
    student1 = Student.add(101, "Alice")
    student2 = Student.add(102, "Bob")
    
    # Student borrows a book
    student1.issue_book(1)  # Alice borrows "Python Basics"
    student2.issue_book(2)  # Bob borrows "Learn Python"
    
    # Try to borrow an unavailable book
    student2.issue_book(1)  # Book 1 is already borrowed by Alice
    
    # Return a book
    student1.return_book(1)  # Alice returns "Python Basics"
    
    # Now Bob can borrow that book
    student2.issue_book(1)  # Bob borrows "Python Basics"
    
    # Try to remove a student who has books
    Student.remove(102)  # Should fail because Bob has books
    
    # Return books first
    student2.return_book(1)
    student2.return_book(2)
    
    # Now we can remove the student
    Student.remove(102)  # Should succeed
    
    # Let's remove a book
    Book.removebook(3)  # Remove "Python for Beginners"
