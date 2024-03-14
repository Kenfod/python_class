class Person:
    def __init__(self, name, age, gender):
        """
        Initializes a Person object with the given attributes.

        Args:
            name (str): Name of the person.
            age (int): Age of the person.
            gender (str): Gender of the person.
        """
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        """
        Prints a message introducing the person with their name, age, and gender.
        """
        print(f"Hello! My name is {self.name}. I am {self.age} years old and I am a {self.gender}.")

# Create an instance of the Person class
person1 = Person("Alice", 30, "Female")

# Call the introduce method to display the person's information
person1.introduce()
