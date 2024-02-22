'''МОдуль хранит в себе класс для сравгения двух списков'''
class ListComparator:
    '''Класс для сравнения средних значений двух списков'''
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def calculate_average(self, lst):
        '''Принимает список, возвращает среднее значение переменных'''
        if not lst:
            return 0
        return sum(lst) / len(lst)

    def compare_lists(self):
        '''Вызывает функцию среднего значения и возвращает результат сравнения списков'''
        average1 = self.calculate_average(self.list1)
        average2 = self.calculate_average(self.list2)

        if average1 > average2:
            return "Первый список имеет большее среднее значение"
        elif average2 > average1:
            return "Второй список имеет большее среднее значение"
        return "Средние значения равны"
