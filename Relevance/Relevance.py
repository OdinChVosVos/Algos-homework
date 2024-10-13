class Relevance:

    def __init__(self, parameters: list[int], digit_characteristics: list[list[int]] ):
        for i, j in enumerate(digit_characteristics):
            j.append(i + 1)

        self.a = parameters
        self.f = digit_characteristics

    def get_relevance_sort_indexes(self) -> list[int]:
        f = sorted(
            self.f,
            key = lambda sublist: sum( self.a[i] * sublist[i] for i in range(len(self.a)) ),
            reverse = True
        )

        return list(map(lambda sublist: sublist[-1], f))