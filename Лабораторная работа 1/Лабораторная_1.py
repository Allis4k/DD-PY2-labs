# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class flower:
    def __init__(self, count_petal: int, diam_centre: float):
        """
        Создание и подготовка к работе объекта "Цветок"

        :param count_petal: Количество лепестков на цветке
        :param diam_centre: Диаметр центра

        Примеры:
        >>> flower = Flower(5, 3)  # инициализация экземпляра класса
        """
        if not isinstance(count_petal, int):
            raise TypeError("Количество лепестков должно быть типа int")
        if count_petal < 0:
            raise ValueError("Количество лепестков не должно быть отрицательным числом")
        self.count_petal = count_petal

        if not isinstance(diam_centre, (int, float)):
            raise TypeError("Диаметр центра должен быть int или float")
        if diam_centre <= 0:
            raise ValueError("Диаметр центра должен быть положительным числом")
        self.diam_centre = diam_centre

    def is_empty_flower(self) -> bool:
        """
        Функция которая проверяет есть ли на цветке лепестки

        :return: Есть ли на цветке лепестки

        Примеры:
        >>> flower = Flower(5, 3)
        >>> flower.is_empty_flower()
        """
        ...

    def tear_petal_from_flower(self, removable_petal: int) -> None:
        """
        Отрывание лепестков с цветка.

        :param removable_petal: Количество отрываемых лепестков
        :raise ValueError: Если количество отрываемых лепестков превышает количество лепестков на цветке,
        то возвращается ошибка.

        :return: Количество реально оторванных лепестков

        Примеры:
        >>> flower = Flower(5, 3)
        >>> flower.tear_petal_from_flower(3)
        """
        if not isinstance(removable_petal, int):
            raise TypeError("Количество отрываемых лепестков должно быть типа int")
        if removable_petal <= 0:
            raise ValueError("Количество отрываемых лепестков должно быть положительным числом")
        ...

class ladybug:
    def __init__(self, count_point: int, diam_body: float):
        """
        Создание и подготовка к работе объекта "Божья коровка"

        :param count_point: Количество точек на крыльях
        :param diam_body: Диаметр тела

        Примеры:
        >>> ladybug = Ladybug(6, 2)  # инициализация экземпляра класса
        """
        if not isinstance(count_point, int):
            raise TypeError("Количество точек на крыльях должно быть типа int")
        if count_point < 0:
            raise ValueError("Количество точек на крыльях не должно быть отрицательным числом")
        self.count_point = count_point

        if not isinstance(diam_body, (int, float)):
            raise TypeError("Диаметр тела должен быть int или float")
        if diam_body <= 0:
            raise ValueError("Диаметр тела должен быть положительным числом")
        self.diam_body = diam_body

    def is_empty_ladybug(self) -> bool:
        """
        Функция которая проверяет есть ли на крыльях точки

        :return: Есть ли на крыльях точки

        Примеры:
        >>> ladybug = Ladybug(2, 4)
        >>> ladybug.is_empty_ladybug()
        """
        ...

    def put_ladybug_to_flower(self, diam_centre: float) -> None:
        """
        Размещение божьей коровки на цветке.
        :param diam_centre: Диаметр цветка, на который садится божья коровка

        :raise ValueError: Если диаметр тела божьей коровки превышает диаметр цветка, то вызываем ошибку

        Примеры:
        >>> ladybug = Ladybug(3, 6)
        >>> ladybug.put_ladybug_to_flower(8)
        """
        if not isinstance(diam_centre, (int, float)):
            raise TypeError("Диаметр цветка должен быть типа int или float")
        if diam_centre <= 0:
            raise ValueError("Диаметр цветка должен быть положительным числом")
        ...

class vase:
    def __init__(self, capacity_volume: float, occupied_volume: float, height: float):
        """
        Создание и подготовка к работе объекта "Ваза"

        :param capacity_volume: Объем вазы
        :param occupied_volume: Объем занимаемой жидкости
        :param height: Высота вазы

        Примеры:
        >>> vase = Vase(3, 0, 16)  # инициализация экземпляра класса
        """
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Объем вазы должен быть типа int или float")
        if capacity_volume <= 0:
            raise ValueError("Объем вазы должен быть положительным числом")
        self.capacity_volume = capacity_volume

        if not isinstance(height, (int, float)):
            raise TypeError("Высота вазы должна быть int или float")
        if height <= 0:
            raise ValueError("Высота вазы должна быть положительным числом")
        self.height = height

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Количество жидкости должно быть типа int или float")
        if occupied_volume <= 0:
            raise ValueError("Количество жидкости должно быть положительным числом")
        self.occupied_volume = occupied_volume

    def is_empty_vase(self) -> bool:
        """
        Функция которая проверяет есть ли в вазе вода

        :return: Есть ли в вазе вода

        Примеры:
        >>> vase = Vase(2, 0, 10)
        >>> vase.is_empty_vase()
        """
        ...

    def put_flower_to_vase(self, fl_height: float) -> None:
        """
        Размещение цветка в вазе.
        :param fl_height: Выста цветка, который ставят в вазу

        :raise ValueError: Если высота цветка превышает высоту вазы, то вызываем ошибку

        Примеры:
        >>> vase = Vase(3, 6, 17)
        >>> vase.put_flower_to_vase(15)
        """
        if not isinstance(fl_height, (int, float)):
            raise TypeError("Выста цветка должна быть типа int или float")
        if fl_height <= 0:
            raise ValueError("Выста цветка должна быть положительным числом")
        ...


if __name__ == "__Лабораторная_1__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации