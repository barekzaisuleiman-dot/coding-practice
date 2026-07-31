from greet import greet, shout


def test_greet():
    assert greet("world") == "Hello, world!"


def test_shout():
    assert shout("this is fine") == "THIS IS FINE!"
