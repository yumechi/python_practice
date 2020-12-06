from typing import Dict


def dict_merge(d1: Dict[str, any], d2: Dict[str, any]) -> Dict[str, any]:
    return d1 | d2


if __name__ == "__main__":
    print(
        dict_merge(
            d1={"key1": "value1 from x", "key2": "value2 from x"},
            d2={"key2": "value2 from y", "key3": "value3 from y"},
        )
    )

    print(
        dict_merge(
            d1={"key2": "value2 from y", "key3": "value3 from y"},
            d2={"key1": "value1 from x", "key2": "value2 from x"},
        )
    )
