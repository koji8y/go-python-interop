#!/usr/bin/env python3
# See: https://medium.com/learning-the-go-programming-language/calling-go-functions-from-other-languages-4c7d8bcc69bf
import ctypes as T

lib = T.cdll.LoadLibrary("./awesome.so")

def strWithType(v, fmt=''):
    return ('{' + fmt + '}: {}').format(v, type(v).__name__)

lib.Add.argtype = [T.c_longlong, T.c_longlong]
print('awesome.Add(12,99) = {}'.format(strWithType(lib.Add(12, 99))))

lib.Cosine.argtypes = [T.c_double]
lib.Cosine.restype = T.c_double
cos = lib.Cosine(1)
print('awesome.Cosine(1) = {}'.format(strWithType(cos)))

class GoSlice(T.Structure):
    _fields_ = [('data', T.POINTER(T.c_void_p)),
                ('len', T.c_longlong), ('cap', T.c_longlong)]

    def __init__(self, values):
        es = tuple(values)
        siz = len(es)
        super().__init__((T.c_void_p * siz)(*es), siz, siz)

    @property
    def values(self):
        return (self.data[i] for i in range(0, self.len))

    def __str__(self):
        return ', '.join(str(v) for v in self.values)


nums = GoSlice([74, 4, 122, 9, 12])
lib.Sort.argtypes = [GoSlice]
lib.Sort.restype = None
print('nums = {}'.format(strWithType(nums)))
lib.Sort(nums)
print('awesome.Sort(nums) = {}'.format(strWithType(nums)))


class GoString(T.Structure):
    _fields_ = [('p', T.c_char_p), ('n', T.c_longlong)]

    def __init__(self, s):
        bs = s.encode('utf-8')
        super().__init__(bs, len(bs))


lib.Log.argtypes = [GoString]
msg = GoString('Hello Python!')
lib.Log(msg)
