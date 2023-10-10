def create_an_empty_list():
    return []

def create_a_list():
    list = [1, 2, 3, 4]
    return list

def add_element_to_end_of_list(l, element):
    new_list = list(l)
    new_list.append(element)
    return new_list

def add_element_to_start_of_list(l, element):
    new_list = []
    new_list.append(element)
    new_list.append(l)
    return new_list

def remove_element_from_end_of_list(l):
    new_list = list(l)
    new_list.pop(-1)
    return new_list

def remove_element_from_start_of_list(l):
    new_list = list(l)
    new_list.pop(0)
    return new_list

def retrieve_first_element_from_list(l):
    new_list = list(l)
    return new_list.pop(0)

def retrieve_element_from_index(l, index):
    new_list = list(l)
    return new_list[index]

def retrieve_last_element_from_list(l):
    new_list = list(l)
    return new_list.pop(-1)
