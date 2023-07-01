def lookup_key(dictionary: dict, value) -> list:
    result = []
    for key, values1 in dictionary.items():
        if value == values1:
            result.append(key)
    return result