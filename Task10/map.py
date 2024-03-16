"""
Ассоциативный массив.
"""


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HMap:
    """
    Ассоциативный массив.
    """

    def __init__(
            self, keys: iter = [],
            values: iter = [],
            _types: object = (None, None)):
        self.keys = list(keys)
        self.values = list(values)

        l, n = len(_types), 2
        if l == n:
            self._ktype, self._vtype = _types
        else:
            if l < n:
                raise ValueError(
                    f"Not enough values to unpack. Expected {n}, got {l}.")
            else:
                raise ValueError(
                    f"Too many values to unpack. Expected {n}, got {l}.")

        if len(self.keys) != len(self.values):
            raise ValueError(
                "Keys and values passed must have the same size.\n" + \
                f"len{self.keys} != len{self.values}")

        
        self.hash_set = set( hash(i) for i in self.keys )
        # self.hash_table

    def resolve_collision(self):
        pass

    def __getitem__(self, key):
        if key in self.keys:
            return 1
        raise IndexError(
            f"No key {key} present in {type(self).__name__}.")

    def __setitem__(self, key, value):
        pass


if __name__ == "__main__":
    hmap1 = HMap()
    hmap2 = HMap((1, 2, 4), ["vadim", "eugene", "igor"])
