#-*- coding:utf-8 -*-

import math
from .common import len_in_bits

def s2n(s):
    """
    String to number.
    """
    if not len(s):
        return 0
    if isinstance(s, str):
        s = s.encode('utf8')
    return int.from_bytes(s, 'big')


def n2s(n):
    """
    Number to string.
    """
    s = math.ceil(len_in_bits(n) / 8)
    return n.to_bytes(s, 'big')


def s2b(s):
    """
    String to binary.
    """
    ret = []
    if isinstance(s, str):
        s = s.encode('utf8')
    for c in s:
        ret.append(bin(c)[2:].zfill(8))
    return "".join(ret)


def b2s(b):
    """
    Binary to string.
    """
    ret = []
    if not isinstance(b, str):
        raise TypeError('Expected bin string')
    b = b.zfill((len(b) + 7) // 8 * 8)
    for pos in range(0, len(b), 8):
        ret.append(int(b[pos:pos + 8], 2))
    return bytes(ret)
