from copy import copy


class IterableDescuentos:
    # NO MODIFICAR
    def __init__(self, mascotas):
        self.mascotas = mascotas

    def __iter__(self):
        return IteradorDescuentos(self)


class IteradorDescuentos:
    def __init__(self, iterable):
        # NO MODIFICAR
        self.iterable = copy(iterable)

    def iter(self):
        return self

    def next(self):
        if self.iterable is None:
            raise StopIteration("No existen más datos con los que iterar")
        else:
            return self.iterable
