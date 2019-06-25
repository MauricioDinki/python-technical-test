import json

singular_list = []  # List whit unordered items
segmented_list = []  # Array of lists with ordered and segmented items by parent
ordered_singular_list = []  # List with ordered and segmented items by parent


def get_priority(priority):
    """
    This function returns a number value for each priority
    """
    if priority == 'lowest':
        value = 1
    elif priority == 'low':
        value = 2
    elif priority == 'medium':
        value = 3
    elif priority == 'high':
        value = 4
    elif priority == 'highest':
        value = 5
    else:
        value = 0
    return value


def read_dict(data, parent):
    """
    This function read the json data and add the parent
    attribute to be able to order the items
    """
    for key in data:
        rec = data[key]
        if type(rec) is dict:
            singular_list.append({
                'name': data[key]['name'],
                'priority': data[key]['priority'],
                'parent': parent
            })
            read_dict(rec, data[key]['name'])


def show_child(name, level):
    """
    This function prints every child for item on the list
    """
    for osl_item in ordered_singular_list:
        if name == osl_item['parent']:
            new_name = osl_item['name']
            for line in range(0, level):
                print('\t', end='')
            print(' %s' % new_name)
            show_child(new_name, level + 1)


def show():
    """
    This function prints the 'fathers' of the items
    """
    for list_item in ordered_singular_list:
        if list_item['parent'] is None:
            name = list_item['name']
            print(name)
            show_child(name, 1)


with open('data.json') as file:
    file_data = json.load(file)
    read_dict(file_data, None)
    # Get all the different parents in the data
    parents = []
    for record in singular_list:
        if not record['parent'] in parents:
            parents.append(record['parent'])

    # Segment the data by child's and parents
    for parent in parents:
        parent_list = []
        for record in singular_list:
            if parent == record['parent']:
                parent_list.append(record)
        segmented_list.append(parent_list)

    # Order every item in the segmented list using bubble sort
    for li in segmented_list:
        for i in range(1, len(li)):
            for j in range(0, len(li) - i):
                priority_1 = get_priority(li[j + 1]['priority'])
                priority_2 = get_priority(li[j]['priority'])
                if priority_1 > priority_2:
                    aux = li[j]
                    li[j] = li[j + 1]
                    li[j + 1] = aux

    # Parse all the items in the segmented list as a single list to print it
    for ordered_list in segmented_list:
        for ordered_item in ordered_list:
            ordered_singular_list.append(ordered_item)

    show()







