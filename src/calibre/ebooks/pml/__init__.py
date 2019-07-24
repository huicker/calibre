# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

__license__   = 'GPL v3'
__copyright__ = '2009, John Schember <john@nachtimwald.com>'
__docformat__ = 'restructuredtext en'

from polyglot.builtins import range


def r(*a):
    return list(range(*a))


# Uncommon Characters supported by PML. \\a tag codes
A_CHARS = r(160, 256) + r(130, 136) + r(138, 141) + \
    r(145, 152) + r(153, 157) + [159]

# Extended Unicode characters supported by PML
Latin_ExtendedA = r(0x0100, 0x0104) + [0x0105, 0x0107, 0x010C, 0x010D,
    0x0112, 0x0113, 0x0115, 0x0117, 0x0119, 0x011B, 0x011D, 0x011F, 0x012A,
    0x012B, 0x012D, 0x012F, 0x0131, 0x0141, 0x0142, 0x0144, 0x0148] + \
    r(0x014B, 0x014E) + [0x014F, 0x0151, 0x0155] + r(0x0159, 0x015C) + \
    [0x015F, 0x0163, 0x0169, 0x016B, 0x016D, 0x0177, 0x017A, 0x017D, 0x017E]
Latin_ExtendedB = [0x01BF, 0x01CE, 0x01D0, 0x01D2, 0x01D4, 0x01E1, 0x01E3,
    0x01E7, 0x01EB, 0x01F0, 0x0207, 0x021D, 0x0227, 0x022F, 0x0233]
IPA_Extensions = [0x0251, 0x0251, 0x0254, 0x0259, 0x025C, 0x0265, 0x026A,
    0x0272, 0x0283, 0x0289, 0x028A, 0x028C, 0x028F, 0x0292, 0x0294, 0x029C]
Spacing_Modifier_Letters = [0x02BE, 0x02BF, 0x02C7, 0x02C8, 0x02CC, 0x02D0,
    0x02D8, 0x02D9]
Greek_and_Coptic = r(0x0391, 0x03A2) + r(0x03A3, 0x03AA) + \
    r(0x03B1, 0x03CA) + [0x03D1, 0x03DD]
Hebrew = r(0x05D0, 0x05EB)
Latin_Extended_Additional = [0x1E0B, 0x1E0D, 0x1E17, 0x1E22, 0x1E24, 0x1E25,
    0x1E2B, 0x1E33, 0x1E37, 0x1E41, 0x1E43, 0x1E45, 0x1E47, 0x1E53] + \
    r(0x1E59, 0x1E5C) + [0x1E61, 0x1E63, 0x1E6B, 0x1E6D, 0x1E6F, 0x1E91,
    0x1E93, 0x1E96, 0x1EA1, 0x1ECD, 0x1EF9]
General_Punctuation = [0x2011, 0x2038, 0x203D, 0x2042]
Arrows = [0x2190, 0x2192]
Mathematical_Operators = [0x2202, 0x221A, 0x221E, 0x2225, 0x222B, 0x2260,
    0x2294, 0x2295, 0x22EE]
Enclosed_Alphanumerics = [0x24CA]
Miscellaneous_Symbols = r(0x261C, 0x2641) + r(0x2642, 0x2648) + \
    r(0x2660, 0x2664) + r(0x266D, 0x2670)
Dingbats = [0x2713, 0x2720]
Private_Use_Area = r(0xE000, 0xE01D) + r(0xE01E, 0xE029) + \
    r(0xE02A, 0xE052)
Alphabetic_Presentation_Forms = [0xFB02, 0xFB2A, 0xFB2B]

# \\U tag codes.
U_CHARS = Latin_ExtendedA + Latin_ExtendedB + IPA_Extensions + \
    Spacing_Modifier_Letters + Greek_and_Coptic + Hebrew + \
    Latin_Extended_Additional + General_Punctuation + Arrows + \
    Mathematical_Operators + Enclosed_Alphanumerics + Miscellaneous_Symbols + \
    Dingbats + Private_Use_Area + Alphabetic_Presentation_Forms


def unipmlcode(char):
    try:
        val = ord(char.encode('cp1252'))
        if val in A_CHARS:
            return '\\a%i' % val
    except:
        pass
    val = ord(char)
    if val in U_CHARS:
        return '\\U%04x'.upper() % val
    else:
        return '?'
