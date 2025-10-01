def greet() -> None:
    print("Hello")
    print("How do you do?")
    print("Isn't the weather nice?")


greet()

# Function that allows for inputs

def greet_with_name(name: str) -> None:
    print(f"Hello {name}")
    print(f"How do you do {name}?")
    print("Isn't the weather nice?")

greet_with_name("Jack Baur")