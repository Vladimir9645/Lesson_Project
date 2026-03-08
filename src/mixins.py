class CreationLoggerMixin:
    def __init__(self, *args, **kwargs):
        # Проверяем, есть ли у родителя __init__, который принимает аргументы
        if hasattr(super(), '__init__') and callable(super().__init__):
            try:
                super().__init__(*args, **kwargs)
            except TypeError:
                # Если родительский __init__ не принимает аргументы, пропускаем
                pass
        else:
            # Если родителя нет или у него нет __init__, просто пропускаем
            pass

        print(f"Создан объект класса {self.__class__.__name__}")
        print(f"Параметры: name='{self.name}', price={self.price}, quantity={self.quantity}")