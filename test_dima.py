import pytest

from dima import ListComparator

@pytest.fixture
def list_comparator():
    return ListComparator([4, 5, 6], [1, 2, 3])

def test_calculate_average_empty_list(list_comparator):
    assert list_comparator.calculate_average([]) == 0

def test_calculate_average_non_empty_list(list_comparator):
    assert list_comparator.calculate_average([1, 2, 3]) == 2

def test_compare_lists_first_greater(list_comparator):
    assert list_comparator.compare_lists() == "Первый список имеет большее среднее значение"

def test_compare_lists_second_greater(list_comparator):
    list_comparator.list1 = [1, 2, 3]
    list_comparator.list2 = [4, 5, 6, 7]
    assert list_comparator.compare_lists() == "Второй список имеет большее среднее значение"

def test_compare_lists_equal(list_comparator):
    list_comparator.list1 = [1, 2, 3]
    list_comparator.list2 = [1, 2, 3]
    assert list_comparator.compare_lists() == "Средние значения равны"
