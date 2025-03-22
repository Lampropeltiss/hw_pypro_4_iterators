import types


def flat_list(bad_list):
    better_list = []
    for item in bad_list:
        if isinstance(item, list):
            better_list.extend(flat_list(item))
        else:
            better_list.append(item)
    return better_list


def flat_generator(list_of_lists):
    better_list = flat_list(list_of_lists)
    cursor = 0
    while cursor < len(better_list):
        yield better_list[cursor]
        cursor += 1


def test_4():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)


if __name__ == '__main__':
    test_4()
