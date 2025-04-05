# Understanding the `self` Keyword in Python

### Definition
In simple words, **`self`** is a way for a class to refer to the specific object it is working with. It lets the object access its own attributes and methods. Think of it as the object saying, "I'm talking about me!"

### What Does `self` Do?
- **`self`** is used inside class methods to access or modify the attributes of the current object.
- It ensures that attributes belong to the specific object created from the class, not just the methods.

### Code Example

```python
class Person:
    def __init__(self, name):
        self.name = name  # 'self.name' refers to the object's own attribute

    def greet(self):
        print(f"Hello, my name is {self.name}")  # Accessing 'self.name' inside a method

# Creating multiple objects
p1 = Person("Nerdy")
p2 = Person("Alex")

# Each object holds its unique attribute
p1.greet()  # Output: Hello, my name is Nerdy
p2.greet()  # Output: Hello, my name is Alex
```
### Key Points:
1. `self.name` binds the `name` value to the specific object.
2. Each object created from the class can have its own unique data.
3. Without `self`, the attributes wouldn't belong to the object—they'd just be local variables in the method.

That's the essence of `self`! It ensures every object handles its own data.
