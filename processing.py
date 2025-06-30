def filter_by_state(list_of_dict: list, state='EXECUTED') -> list:
    filtered_list = []
    for dict in list_of_dict:
        for key, value in dict.items():
            if dict.get('state') == state:
                filtered_list.append(dict)
            else:
                continue
    return filtered_list
result = filter_by_state(list_of_dict=eval(input("Enter the list of dictionaries: ")))
print(result)