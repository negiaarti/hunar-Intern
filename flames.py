def remove_common_characters(name1, name2):
    name1 = list(name1)
    name2 = list(name2)
    
    for char in name1[:]:
        if char in name2:
            name1.remove(char)
            name2.remove(char)
    
    return name1, name2

def flames_game(name1, name2):
    name1 = name1.lower().replace(" ", "")
    name2 = name2.lower().replace(" ", "")
    
    name1, name2 = remove_common_characters(name1, name2)
    
    count = len(name1) + len(name2)
    
    flames = ["F", "L", "A", "M", "E", "S"]
    
    while len(flames) > 1:
        split_index = (count % len(flames)) - 1
        
        if split_index >= 0:
            right = flames[split_index + 1:]
            left = flames[:split_index]
            flames = right + left
        else:
            flames = flames[:len(flames) - 1]
    
    result = flames[0]
    
    result_dict = {
        "F": "Friends",
        "L": "Lovers",
        "A": "Affectionate",
        "M": "Marriage",
        "E": "Enemies",
        "S": "Siblings"
    }
    
    return result_dict[result]

# Input names
name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")

# Get the result
result = flames_game(name1, name2)
print(f"The relationship between {name1} and {name2} is: {result}")
