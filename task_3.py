class FlatIterator:

    def __init__(self, list_of_lists):
        self.list_of_lists = self.flat_list(list_of_lists)

    def __iter__(self):
        self.cursor = -1
        return self

    def __next__(self):
        self.cursor += 1
        if self.cursor == len(self.list_of_lists):
            raise StopIteration
        item = self.list_of_lists[self.cursor]
        return item

    def flat_list(self, bad_list):
        better_list = []
        for item in bad_list:
            if isinstance(item, list):
                better_list.extend(self.flat_list(item))
            else:
                better_list.append(item)
        return better_list


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()
