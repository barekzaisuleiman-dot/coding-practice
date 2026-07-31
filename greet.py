def greet(name):
    """Return a friendly greeting for name."""
    return f"Hello, {name}!"


def shout(text):
    """Return text in uppercase with an exclamation mark."""
    return text.upper() + "!"


if __name__ == "__main__":
    print(greet("world"))
    print(shout("this is fine"))
