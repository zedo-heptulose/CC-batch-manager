import json
import copy

def merge_dicts(_d1, _d2):
    d1 = copy.deepcopy(_d1)
    d2 = copy.deepcopy(_d2)
    """Merge two dictionaries, overwriting string, number, and bool values,
    and combining nested dictionary and list objects"""
    merged = {**d1}  # Start with a copy of the first dictionary
    
    for key, value in d2.items():
        if key in merged:
            # Check types and overwrite only for str, int, float, bool
            if isinstance(merged[key], (str, int, float, bool)):
                merged[key] = value  # Overwrite with the value from d2
            elif isinstance(merged[key], list):
                if isinstance(value,list):
                    merged[key].extend(value)
                else:
                    megred[key].append(value)
            elif isinstance(merged[key],dict):
                if isinstance(value,dict):
                    merged[key] = merge_dicts(merged[key],value)
                else:
                    raise ValueError('Tried to mix dict and non-dict objects')
        else:
            merged[key] = value  # Add new key-value pair from d2

    return merged



def load_config_from_file(config_file):
    with open(config_file,'r') as f:
        return json.load(f)