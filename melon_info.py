"""Print out all the melons in our inventory."""


from doctest import master
from melons import master_dictionary


def print_melon(melons):
    """Print each melon with corresponding attribute information."""
    for key, value in melons.items():
        print(key.upper())
        for k, v in value.items():
            print(k,':', v)
        print('-' * 40)
    return 
print('\n')
print_melon(master_dictionary)