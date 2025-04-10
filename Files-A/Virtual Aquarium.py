"""
Virtual Aquarium - A beautiful, small OOP project in Python
"""
import random
import time
from abc import ABC, abstractmethod
import os
import platform


class AquariumObject(ABC):
    """Abstract base class for all objects in the aquarium"""
    
    def __init__(self, x, y, symbol):
        self.x = x
        self.y = y
        self.symbol = symbol
    
    @abstractmethod
    def update(self, aquarium):
        """Update the object's state"""
        pass


class Creature(AquariumObject):
    """Base class for all living creatures in the aquarium"""
    
    def __init__(self, x, y, symbol, color, speed):
        super().__init__(x, y, symbol)
        self.color = color
        self.speed = speed
        self.direction = random.choice([(0, 1), (1, 0), (0, -1), (-1, 0)])
        self.age = 0
    
    def update(self, aquarium):
        """Update creature position based on direction and speed"""
        # Age the creature
        self.age += 1
        
        # Occasionally change direction
        if random.random() < 0.1:
            self.direction = random.choice([(0, 1), (1, 0), (0, -1), (-1, 0)])
        
        # Move in the current direction
        new_x = self.x + self.direction[0] * self.speed
        new_y = self.y + self.direction[1] * self.speed
        
        # Ensure the creature stays within the aquarium bounds
        if 0 <= new_x < aquarium.width:
            self.x = new_x
        else:
            self.direction = (-self.direction[0], self.direction[1])
            
        if 0 <= new_y < aquarium.height:
            self.y = new_y
        else:
            self.direction = (self.direction[0], -self.direction[1])


class Fish(Creature):
    """Fish class representing different types of fish"""
    
    def __init__(self, x, y, species="goldfish"):
        self.species = species
        
        # Different fish types have different appearance and behavior
        species_traits = {
            "goldfish": {"symbol": "🐠", "color": "yellow", "speed": 1},
            "shark": {"symbol": "🦈", "color": "blue", "speed": 2},
            "tropical": {"symbol": "🐡", "color": "rainbow", "speed": 1.5},
            "jellyfish": {"symbol": "🪼", "color": "purple", "speed": 0.5},
        }
        
        traits = species_traits.get(species, species_traits["goldfish"])
        super().__init__(x, y, traits["symbol"], traits["color"], traits["speed"])
        
        self.hunger = 100  # Full initially
    
    def update(self, aquarium):
        super().update(aquarium)
        
        # Fish get hungrier over time
        self.hunger -= 0.5
        
        # Fish try to find food
        for food in aquarium.objects:
            if isinstance(food, Food):
                # If close to food, eat it
                if abs(self.x - food.x) < 2 and abs(self.y - food.y) < 2:
                    self.hunger = min(100, self.hunger + food.nutrition)
                    aquarium.objects.remove(food)
                    break
        
        # Hungry fish move slower
        if self.hunger < 30:
            self.speed = 0.5
        else:
            # Reset speed based on species
            species_speeds = {"goldfish": 1, "shark": 2, "tropical": 1.5, "jellyfish": 0.5}
            self.speed = species_speeds.get(self.species, 1)
        
        # Very hungry fish might die
        if self.hunger <= 0:
            aquarium.objects.remove(self)
            aquarium.objects.append(Plant(self.x, self.y))  # Circle of life


class Plant(AquariumObject):
    """Plant class representing aquatic vegetation"""
    
    def __init__(self, x, y):
        symbols = ["🌱", "🌿", "🍀", "🌾"]
        super().__init__(x, y, random.choice(symbols))
        self.growth = 0
        self.max_growth = 100
    
    def update(self, aquarium):
        """Plants grow over time and can reproduce"""
        self.growth += 0.5
        
        # Mature plants can reproduce
        if self.growth >= self.max_growth and random.random() < 0.01:
            # Find a nearby empty space
            for _ in range(10):  # Try up to 10 random positions
                dx, dy = random.randint(-2, 2), random.randint(-2, 2)
                new_x, new_y = self.x + dx, self.y + dy
                
                if (0 <= new_x < aquarium.width and 
                    0 <= new_y < aquarium.height and
                    not any(obj.x == new_x and obj.y == new_y for obj in aquarium.objects)):
                    aquarium.objects.append(Plant(new_x, new_y))
                    break


class Food(AquariumObject):
    """Food class representing fish food"""
    
    def __init__(self, x, y):
        super().__init__(x, y, ".")
        self.nutrition = random.randint(20, 50)
        self.lifespan = 100  # Food disappears after some time
    
    def update(self, aquarium):
        """Food sinks slowly and eventually disappears"""
        if random.random() < 0.3 and self.y < aquarium.height - 1:
            self.y += 1
            
        self.lifespan -= 1
        if self.lifespan <= 0:
            aquarium.objects.remove(self)


class Aquarium:
    """The main aquarium class containing all objects"""
    
    def __init__(self, width=80, height=24):
        self.width = width
        self.height = height
        self.objects = []
        self.setup()
    
    def setup(self):
        """Initial aquarium setup with fish and plants"""
        # Add some fish
        for _ in range(5):
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            species = random.choice(["goldfish", "shark", "tropical", "jellyfish"])
            self.objects.append(Fish(x, y, species))
        
        # Add some plants
        for _ in range(8):
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            self.objects.append(Plant(x, y))
    
    def add_food(self, amount=5):
        """Add food to the aquarium"""
        for _ in range(amount):
            x = random.randint(0, self.width - 1)
            y = 0  # Food starts at the top
            self.objects.append(Food(x, y))
    
    def update(self):
        """Update all objects in the aquarium"""
        # Make a copy to avoid modification during iteration
        for obj in list(self.objects):
            if obj in self.objects:  # Check if object still exists
                obj.update(self)
    
    def render(self):
        """Render the aquarium to the console"""
        # Create empty grid
        grid = [[' ' for _ in range(self.width)] for _ in range(self.height)]
        
        # Border elements
        top_border = "╔" + "═" * (self.width - 2) + "╗"
        bottom_border = "╚" + "═" * (self.width - 2) + "╝"
        side_border = "║"
        
        # Fill in objects
        for obj in self.objects:
            x, y = int(obj.x), int(obj.y)
            # Ensure coordinates are within bounds
            if 0 <= x < self.width and 0 <= y < self.height:
                grid[y][x] = obj.symbol
        
        # Draw the aquarium with borders
        print(top_border)
        for row in grid:
            print(side_border + ''.join(row) + side_border)
        print(bottom_border)
        
        # Print stats
        fish_count = sum(1 for obj in self.objects if isinstance(obj, Fish))
        plant_count = sum(1 for obj in self.objects if isinstance(obj, Plant))
        food_count = sum(1 for obj in self.objects if isinstance(obj, Food))
        
        print(f"Fish: {fish_count} | Plants: {plant_count} | Food: {food_count}")


def clear_screen():
    """Clear the console screen"""
    os_name = platform.system()
    if os_name == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def main():
    """Main function running the aquarium simulation"""
    width = 80
    height = 20
    aquarium = Aquarium(width, height)
    
    print("Virtual Aquarium - A Python OOP Project")
    print("---------------------------------------")
    print("Press Ctrl+C to exit")
    print("The ecosystem will evolve on its own, or...")
    print("Press 'f' and Enter to add food")
    print("Press 'p' and Enter to add a plant")
    print("Press 'a' and Enter to add a random fish")
    
    try:
        while True:
            clear_screen()
            aquarium.update()
            aquarium.render()
            
            # Non-blocking input check
            # This is a simple approach that works for demonstration
            # A more sophisticated approach would use a library like keyboard, curses, or pygame
            user_input = input("Command (f/p/a): ")
            if user_input.lower() == 'f':
                aquarium.add_food()
            elif user_input.lower() == 'p':
                x = random.randint(0, width - 1)
                y = random.randint(0, height - 1)
                aquarium.objects.append(Plant(x, y))
            elif user_input.lower() == 'a':
                x = random.randint(0, width - 1)
                y = random.randint(0, height - 1)
                species = random.choice(["goldfish", "shark", "tropical", "jellyfish"])
                aquarium.objects.append(Fish(x, y, species))
            
            time.sleep(0.2)
    except KeyboardInterrupt:
        print("\nThank you for visiting the Virtual Aquarium!")


if __name__ == "__main__":
    main()
