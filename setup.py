# -*- coding: utf-8 -*-
""" 
trying to customize pygments' coq style...
""" 
from setuptools import setup 

setup( 
    name         = 'ssrmint', 
    version      = '0.1', 
    description  = __doc__, 
    author       = "guess who", 
    install_requires = ['pygments'],
    packages = ['ssrmint'],
    entry_points = {
        'pygments.styles': ['ssr = ssrmint:SSRStyle'],
        'pygments.lexers': ['CoqLexer = ssrmint:SSRLexer'],
    }
) 
