from my_collections.the_collection import TheCollection
from decorators.time_decor import time_decor
from dunder_method.point import Point

def main():
    collection = TheCollection([1, 2, 3, 4, 5])
    for item in collection:
        print(item)

    def some_func():
        import time
        time.sleep(1)
        print("Function execute")
    some_func()

    point1 = Point(1, 2)
    point2 = Point(1, 2)
    print(point1 == point2)
    if point1:
        print("Point is truthy")
    else:
        print("Point is falsy")

if __name__ == '__main__':
    main()