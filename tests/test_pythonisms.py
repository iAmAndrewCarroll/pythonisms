from my_collections.the_collection import TheCollection
from decorators.time_decor import time_decor
from dunder_method.point import Point

def test_iterator():
    collection = TheCollection([1, 2, 3, 4, 5])
    result = [item for item in collection]
    assert result == [1, 2, 3, 4, 5]

def test_decorator():
    @time_decor
    def test_func():
        import time
        time.sleep(1)
        print("Function execute")
    assert test_func() is None

def test_dunder_method():
    point1 = Point(1, 2)
    point2 = Point(1, 2)
    assert point1 == point2
    assert point1
    assert not Point(0, 0)