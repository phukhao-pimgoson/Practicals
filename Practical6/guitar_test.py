from Practical6.guitar_class import Guitar
import random

gibson = Guitar("Gibson L-5 CES", 1922, "16,035.45")
print(gibson)
print("gibson.get_age() - Expected 98, got {}".format(gibson.get_age()))
print("gibson.is_vintage() - Expected True, got {}".format(gibson.is_vintage()))

another = Guitar("Another Guitar", 2013, random.randint(10000, 20000))
print(another)
print("another.get_age() - Expected 7, got {}".format(another.get_age()))
print("another.is_vintage() - Expected False, got {}".format(another.is_vintage()))