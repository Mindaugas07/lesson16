def list_to_string(some_list: list) -> str:
    new_string = ""
    for member in some_list:
        new_string += str(member)
    
    return new_string

if __name__ == "__main__":
    print(list_to_string(some_list))
