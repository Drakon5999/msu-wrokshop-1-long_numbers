import sys
from list_impl import DigitalList, make_number_list_from_string


class BigInteger:
    def __init__(self, str_number=None):
        if str_number is not None:
            self.lst = make_number_list_from_string(str_number)
        else:
            self.lst = None

    def __add__(self, other):
        assert other.lst
        assert other.lst.start

        result = DigitalList()
        cur_this = self.lst.start
        cur_other = other.lst.start

        overhead = 0
        while cur_this or cur_other:
            ctn = cur_this.number if cur_this else 0
            cto = cur_other.number if cur_other else 0
            assert 0 <= ctn <= 9
            assert 0 <= cto <= 9

            s = ctn + cto + overhead
            result.append(s % 10)
            overhead = s // 10

            if cur_this:
                cur_this = cur_this.next()
            if cur_other:
                cur_other = cur_other.next()

        if overhead:
            result.append(overhead)

        result_integer = BigInteger()
        result_integer.lst = result
        return result_integer

    def __eq__(self, other):
        if type(other) == str:
            other = BigInteger(other)

        cur_this = self.lst.start
        cur_other = other.lst.start
        while cur_other or cur_this:
            if not cur_other or not cur_this:
                return False

            if cur_other.number != cur_this.number:
                return False

            cur_other = cur_other.next()
            cur_this = cur_this.next()

        return True

    def __str__(self):
        return (self.lst.join())[-1::-1]


def main():
    assert BigInteger("123").lst.start.number == 3
    assert BigInteger("123").lst.end.number == 1
    assert BigInteger("123") == "123"
    assert BigInteger("123") + BigInteger("321") == "444"
    assert BigInteger("923") + BigInteger("921") == "1844"
    assert BigInteger("0") + BigInteger("921") == "921"
    assert BigInteger("101") + BigInteger("101") == "202"
    assert BigInteger("0") + BigInteger("0") == "0"

    print("Tests OK")
    first = input("First number: ")
    second = input("Second number: ")

    print("Result {}".format(str(BigInteger(first) + BigInteger(second))))
    return 0


if __name__ == "__main__":
    sys.exit(main())
