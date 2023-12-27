def to_list(var: tuple) -> list:
    lst = []
    for item in var:
        lst.append(item)
    return lst


def to_str(var: tuple, split="") -> str:
    rstr = ""
    for item in var:
        rstr = f"{rstr}{split}{item}"
    if rstr[:len(split)] != split:
        return rstr
    return rstr[len(split):]
