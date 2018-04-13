# -*- coding: utf-8 -*-
from setuptools import setup 

setup( 
    name         = 'ssrmint', 
    version      = '0.1', 
    description  = "ad-hoc pygments style and lexer for LaTeX pretty-printing of SSReflect",
    author       = "rei",
    install_requires = ['pygments'],
    packages = ['ssrmint'],
    license = ['TBD'],
    entry_points = {
        'pygments.styles': ['ssr = ssrmint:SSRStyle'],
        'pygments.lexers': ['CoqLexer = ssrmint:SSRLexer'],
    }
) 
