# Write your solution here
def search_by_name(filename: str, word: str):
    found_recipes =  []
    with open(filename) as f:
        attemps = 1
        for line in f:
            line = line.strip()
            line_normalise = line.lower()
            if line == "":
                attemps = 1
                continue
            elif attemps == 1:
                if line_normalise.find(word) != -1:
                    found_recipes.append(line)
            attemps += 1 
    return found_recipes  

def search_by_time(filename: str, prep_time: int):
    recipes = []
    with open(filename) as f:
        attemps = 1
        for line in f:
            line = line.strip()
            if line == "":
                attemps = 1
                continue
            elif attemps == 1:
                recipe = line
            elif attemps == 2 :
                time = int(line)
                if time <= prep_time:
                    recipes.append(f"{recipe}, preparation time {time} min")
            attemps += 1
        return recipes

def search_by_ingredient(filename: str, ingredient: str):
    recipes = []
    with open(filename) as f:
        attemps = 1
        for line in f:
            line = line.strip()
            if line == "":
                attemps = 1
                continue
            elif attemps == 1:
                recipe = line
            elif attemps == 2 :
                time = int(line)
            elif line == ingredient:
                recipes.append(f"{recipe}, preparation time {time} min")
            attemps += 1
        return recipes






if __name__ == "__main__":
    found_recipes = search_by_name("recipes2.txt", "oat")

    for recipe in found_recipes:
        print(recipe)


