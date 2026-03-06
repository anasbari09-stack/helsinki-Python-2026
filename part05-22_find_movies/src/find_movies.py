# Write your solution here
def  find_movies(database: list, search_term: str):
    new_list = []
    for item in database:
        clean_item = item["name"]
        clean_item = clean_item.lower()
        if clean_item.find(search_term) != -1:
            new_list.append(item)
    return new_list
            

if __name__ == "__main__":
    database = [{"name": "Gone with the Python", "director": "Victor Pything", "year": 2017, "runtime": 116},
    {"name": "Pythons on a Plane", "director": "Renny Pytholin", "year": 2001, "runtime": 94},
    {"name": "Dawn of the Dead Programmers", "director": "M. Night Python", "year": 2011, "runtime": 101}]

    my_movies = find_movies(database, "python")
    print(my_movies)
    