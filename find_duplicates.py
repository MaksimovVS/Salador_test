class FindDuplicates:
    """Класс, экземпляры, которого могут воспользоваться методом find()
    для получения списка повторяющихся значений в исходном списке."""

    def __init__(self, arr):
        self.arr: list = arr

    def find(self) -> list | None:
        """Возращает либо список повторяющихся чисел, либо None."""
        result = set()

        try:
            for i in range(len(self.arr)):
                if self.arr[i] in self.arr[i+1:]:
                    result.add(self.arr[i])
        except TypeError as error:
            raise(f'Не соответствует тип передаваемых данных.\n{error}')

        if result:
            return list(result)
        return None


def test() -> None:
    """Тесты."""

    data = [[1, 2, 3, 4, 1, 4], [1, 2, 3, 4], [], [1, 1, 1, 1]]
    results = [[1, 4], None, None, [1]]
    for i in range(len(data)):
        arr = data[i]
        result = results[i]
        duplicate = FindDuplicates(arr)
        assert duplicate.find() == result


def main() -> None:
    """Главная функция, точка входа."""

    arr1 = [1, 2, 3, 4, 1, 4]
    duplicate = FindDuplicates(arr1)
    result = duplicate.find()
    print(f'Повторяющиеся числа в массиве: {result}')

    # test()


if __name__ == '__main__':
    main()
