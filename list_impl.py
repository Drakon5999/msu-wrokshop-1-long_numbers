import sys
from builtins import print


class DigitalNode:
    def __init__(self, number):
        self.number = number
        self._next = None

    def next(self):
        return self._next

    def append(self, number):
        self._next = DigitalNode(number)
        return self._next


class DigitalList:
    def __init__(self, number=None):
        if number is not None:
            self.start = DigitalNode(number)
            self._len = 1
        else:
            self.start = None
            self._len = 0

        self.end = self.start

    def __len__(self):
        return self._len

    def _find_split(self, number):
        last  = None
        current = self.start
        i = 0
        while current:
            if current.number == number:
                return last, current, i
            i += 1
            last = current
            current = current.next()

        return None, None, None

    def find(self, number):
        last, current, i = self._find_split(number)
        if current:
            lst = DigitalList()
            lst.start = current
            lst.end = self.end
            lst._len = self._len - i
            return lst

        return DigitalList()

    def erase(self, number):
        last, current, i = self._find_split(number)
        if last:
            last._next = current.next()
        elif current:
            self.start = self.start.next()

        self._len -= 1
        if self.end == current:
            self.end = last

        return self

    def append(self, number):
        if not self.start:
            self.start = DigitalNode(number)
            self.end = self.start
        else:
            self.end = self.end.append(number)

        self._len += 1
        return self


def make_list_from_number(number=0):
    lst = DigitalList(number % 10)
    while number >= 10:
        number //= 10
        lst.append(number % 10)
    return lst


def main():
    # basic tests
    assert DigitalList().start is None
    assert DigitalList(10).start.number == 10
    assert DigitalList(10).end.number == 10
    assert DigitalList(10).append(12).end.number == 12
    assert DigitalList(10).append(12).start.number == 10
    assert DigitalList().append(12).start.number == 12
    assert DigitalList().append(12).end.number == 12

    # find tests
    assert DigitalList(10).append(12).append(14).find(10).start.number == 10
    assert DigitalList(10).append(12).append(14).find(12).start.number == 12
    assert DigitalList(10).append(12).append(14).find(14).start.number == 14
    assert DigitalList(10).append(12).append(14).find(16).start is None
    assert DigitalList(10).find(10).start.number == 10
    assert DigitalList().find(10).start is None
    assert DigitalList().append(10).find(10).start.number == 10

    # len tests
    assert len(DigitalList(10).append(12).append(14).find(10)) == 3
    assert len(DigitalList(10).append(12).append(14).find(12)) == 2
    assert len(DigitalList(10).append(12).append(14).find(14)) == 1
    assert not DigitalList(10).append(12).append(14).find(16)
    assert len(DigitalList(10).find(10)) == 1
    assert not DigitalList().find(10)
    assert DigitalList().append(10).find(10)

    # erase tests
    assert len(DigitalList(10).append(12).append(14).erase(12)) == 2
    assert len(DigitalList(10).append(12).append(14).find(12).erase(10)) == 1
    assert DigitalList(10).append(12).append(14).erase(10).start.number == 12
    assert DigitalList(10).append(12).append(14).erase(12).start.number == 10
    assert DigitalList(10).append(12).append(14).erase(12).start.next().number == 14
    assert DigitalList(10).append(12).append(14).erase(14).end.number == 12
    assert DigitalList(10).append(12).append(14).erase(16).end.number == 14
    assert DigitalList(10).append(12).append(14).erase(16).start.number == 10

    # make_list_from_number tests
    assert make_list_from_number(123).start.number == 3
    assert make_list_from_number(123).end.number == 1
    assert make_list_from_number(0).start.number == 0
    assert make_list_from_number(0).end.number == 0

    print("Tests OK")

    return 0


if __name__ == "__main__":
    sys.exit(main())
