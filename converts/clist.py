def to_tuple(var: list) -> tuple:
    return (*var, )


def to_str(var: list, split="") -> str:
    rstr = ""
    for item in var:
        rstr = f"{rstr}{split}{item}"
    if rstr[:len(split)] != split:
        return rstr
    return rstr[len(split):]
