class Relevance:

    def __init__(self, parameters: list[int], digit_characteristics: list[list[int]] ):
        for i, j in enumerate(digit_characteristics):
            j.append(i + 1)

        self.a = parameters
        self.f = digit_characteristics

        self.f = sorted(
            self.f,
            key=lambda sublist: self.__get_score(sublist),
            reverse=True
        )

    def update_digit_characteristics(self, i, j, new_value):
        # Step 1: Find the object to update using binary search
        update_object, cur_index = self.__search_by_index(i)

        # Step 2: Get the old value and update it
        old_value = update_object[j - 1]
        update_object[j - 1] = new_value

        # Step 3: Compare and perform binary search to determine new position
        if new_value < old_value:
            left, right = cur_index, len(self.f) - 1
        elif new_value > old_value:
            left, right = 0, cur_index
        else:
            return

        self.f.pop(cur_index)  # Remove the updated object from the old position

        # Insert the updated object in the correct place by recalculating the score
        # Using binary search to find the correct position

        # Binary search to find the correct insertion point
        while left <= right:
            mid = (left + right) // 2
            mid_score = self.__get_score(self.f[mid])
            update_score = self.__get_score(update_object)

            if mid_score < update_score:
                right = mid - 1
            else:
                left = mid + 1

        # Step 4: Insert the updated object in the right position (at 'left')
        self.f.insert(left, update_object)


    def __get_score(self, object):
        return sum(self.a[i] * object[i] for i in range(len(self.a)))

    def __search_by_index(self, index):
        for new_index, el in enumerate(self.f):
            if el[-1] == index:
                return el, new_index


    def get_relevance_sort_indexes(self, k) -> list[int]:
        return list(map(lambda sublist: sublist[-1], self.f))[:k]