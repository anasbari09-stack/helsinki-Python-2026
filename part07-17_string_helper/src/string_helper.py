# Write your solution here
import string
def change_case(orig_string: str) -> str:
    new_str = ""
    for s in orig_string:
        if s.islower():
            new_str += s.upper()
        else:
            new_str += s.lower()
    return new_str

def split_in_half(orig_string: str) -> tuple:
    half_string = len(orig_string) // 2
    return(orig_string[:half_string], orig_string[half_string:])

def remove_special_characters(orig_string: str) -> str:
    new_str = "".join(char for char in orig_string if char.isalnum() or char.isspace() )
    return new_str

if __name__ == "__main__" : 
    m2 = remove_special_characters("Thi§ is a test test")
    print(m2)

