import sys


def create_objects_from_dicts(type_class, dict_list):
    objects = []
    for obj in dict_list:
        try:
            instance = type_class(**obj)
            objects.append(instance)
        except Exception as ex:
            print(f"Failed to create {type_class.__name__}: {ex}", file=sys.stderr)
    return objects
