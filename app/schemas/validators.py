def normalize(name: str) -> str:
    return ' '.join((word.capitalize()) for word in name.split(' '))


def len_validator_4_to_20(string: str):
    if not 4 <= len(string) <= 20:
        raise ValueError(
            "must be higher than 4 and lower than 20 characters")
    else:
        return string


def len_validator_10_to_255(string: str):
    if not 10 <= len(string) <= 255:
        raise ValueError(
            "must be higher than 10 and lower than 255 characters")
    else:
        return string
