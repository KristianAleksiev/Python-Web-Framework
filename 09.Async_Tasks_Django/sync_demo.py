import time


def first_worker():
    time.sleep(2)
    return "bread"


def second_worker():
    time.sleep(3)
    return "cheese"


def third_worker():
    time.sleep(4)
    return "ham"


def main():
    sandwich_parts = []
    sandwich_parts.append(first_worker())
    sandwich_parts.append(second_worker())
    sandwich_parts.append(third_worker())
    print(sandwich_parts)


main()
"""
One operation after another, when the first is executed, the second begins 
"""