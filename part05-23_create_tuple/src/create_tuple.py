# Write your solution here
def create_tuple(x: int, y: int, z: int):
    my_list = [x, y, z]
    tuple_create = (min(my_list), max(my_list), sum(my_list))
    return tuple_create


if __name__ == "__main__":
    print(create_tuple(5, 3, -1))