#!/usr/bin/env python
# -*- coding: utf-8 -*-

# CAVEAT UTILITOR
#
# This file was automatically generated by Grako.
#
#    https://pypi.python.org/pypi/grako/
#
# Any changes you make to it will be overwritten the next time
# the file is generated.


from __future__ import print_function, division, absolute_import, unicode_literals

from grako.parsing import graken, Parser
from grako.util import re, RE_FLAGS


__version__ = (2016, 1, 5, 17, 39, 0, 1)

__all__ = [
    'CLDataTypeParser',
    'CLDataTypeSemantics',
    'main'
]


class CLDataTypeParser(Parser):
    def __init__(self,
                 whitespace=None,
                 nameguard=None,
                 comments_re=None,
                 eol_comments_re=None,
                 ignorecase=None,
                 left_recursion=True,
                 **kwargs):
        super(CLDataTypeParser, self).__init__(
            whitespace=whitespace,
            nameguard=nameguard,
            comments_re=comments_re,
            eol_comments_re=eol_comments_re,
            ignorecase=ignorecase,
            left_recursion=left_recursion,
            **kwargs
        )

    @graken()
    def _result_(self):
        self._expr_()

    @graken()
    def _expr_(self):
        with self._optional():
            self._address_space_qualifier_()

        def block0():
            self._pre_data_type_type_qualifiers_()
        self._closure(block0)
        self._data_type_()
        with self._optional():
            self._is_pointer_()
            with self._optional():
                self._post_data_type_type_qualifier_()

    @graken()
    def _data_type_(self):
        with self._choice():
            with self._option():
                self._scalar_data_type_()
            with self._option():
                self._vector_data_type_()
            with self._option():
                self._user_data_type_()
            self._error('no available options')

    @graken()
    def _is_pointer_(self):
        self._token('*')

    @graken()
    def _scalar_data_type_(self):
        with self._choice():
            with self._option():
                self._token('bool')
            with self._option():
                self._token('char')
            with self._option():
                self._token('cl_char')
            with self._option():
                self._token('unsigned char')
            with self._option():
                self._token('uchar')
            with self._option():
                self._token('cl_uchar')
            with self._option():
                self._token('short')
            with self._option():
                self._token('cl_short')
            with self._option():
                self._token('unsigned short')
            with self._option():
                self._token('ushort')
            with self._option():
                self._token('int')
            with self._option():
                self._token('unsigned int')
            with self._option():
                self._token('uint')
            with self._option():
                self._token('long')
            with self._option():
                self._token('unsigned long')
            with self._option():
                self._token('ulong')
            with self._option():
                self._token('float')
            with self._option():
                self._token('half')
            with self._option():
                self._token('size_t')
            with self._option():
                self._token('ptrdiff_t')
            with self._option():
                self._token('intptr_t')
            with self._option():
                self._token('uintptr_t')
            with self._option():
                self._token('void')
            with self._option():
                self._token('double')
            with self._option():
                self._token('half')
            self._error('expecting one of: bool char cl_char cl_short cl_uchar double float half int intptr_t long ptrdiff_t short size_t uchar uint uintptr_t ulong unsigned char unsigned int unsigned long unsigned short ushort void')

    @graken()
    def _vector_data_type_(self):
        self._pattern(r'(char|uchar|short|ushort|int|uint|long|ulong|float|double|half|mot_float_type)\d+')

    @graken()
    def _user_data_type_(self):
        self._pattern(r'\w+')

    @graken()
    def _address_space_qualifier_(self):
        with self._choice():
            with self._option():
                self._token('__local')
            with self._option():
                self._token('local')
            with self._option():
                self._token('__global')
            with self._option():
                self._token('global')
            with self._option():
                self._token('__constant')
            with self._option():
                self._token('constant')
            with self._option():
                self._token('__private')
            with self._option():
                self._token('private')
            self._error('expecting one of: __constant __global __local __private constant global local private')

    @graken()
    def _pre_data_type_type_qualifiers_(self):
        with self._choice():
            with self._option():
                self._token('const')
            with self._option():
                self._token('restrict')
            with self._option():
                self._token('volatile')
            self._error('expecting one of: const restrict volatile')

    @graken()
    def _post_data_type_type_qualifier_(self):
        self._token('const')


class CLDataTypeSemantics(object):
    def result(self, ast):
        return ast

    def expr(self, ast):
        return ast

    def data_type(self, ast):
        return ast

    def is_pointer(self, ast):
        return ast

    def scalar_data_type(self, ast):
        return ast

    def vector_data_type(self, ast):
        return ast

    def user_data_type(self, ast):
        return ast

    def address_space_qualifier(self, ast):
        return ast

    def pre_data_type_type_qualifiers(self, ast):
        return ast

    def post_data_type_type_qualifier(self, ast):
        return ast


def main(filename, startrule, trace=False, whitespace=None, nameguard=None):
    import json
    with open(filename) as f:
        text = f.read()
    parser = CLDataTypeParser(parseinfo=False)
    ast = parser.parse(
        text,
        startrule,
        filename=filename,
        trace=trace,
        whitespace=whitespace,
        nameguard=nameguard)
    print('AST:')
    print(ast)
    print()
    print('JSON:')
    print(json.dumps(ast, indent=2))
    print()

if __name__ == '__main__':
    import argparse
    import string
    import sys

    class ListRules(argparse.Action):
        def __call__(self, parser, namespace, values, option_string):
            print('Rules:')
            for r in CLDataTypeParser.rule_list():
                print(r)
            print()
            sys.exit(0)

    parser = argparse.ArgumentParser(description="Simple parser for SimpleCLDataType.")
    parser.add_argument('-l', '--list', action=ListRules, nargs=0,
                        help="list all rules and exit")
    parser.add_argument('-n', '--no-nameguard', action='store_true',
                        dest='no_nameguard',
                        help="disable the 'nameguard' feature")
    parser.add_argument('-t', '--trace', action='store_true',
                        help="output trace information")
    parser.add_argument('-w', '--whitespace', type=str, default=string.whitespace,
                        help="whitespace specification")
    parser.add_argument('file', metavar="FILE", help="the input file to parse")
    parser.add_argument('startrule', metavar="STARTRULE",
                        help="the start rule for parsing")
    args = parser.parse_args()

    main(
        args.file,
        args.startrule,
        trace=args.trace,
        whitespace=args.whitespace,
        nameguard=not args.no_nameguard
    )
