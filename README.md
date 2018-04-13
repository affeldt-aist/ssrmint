ssrmint
====

## contents

see description in [setup.py](setup.py)

## install

* type `make install`
* has been test on a Debian 9.4 machine with Python 2.7.13 and the python-pygments Debian package installed
* check the style and the lexer have been installed: `pygmentize -L lexers`, `pygmentize -L styles`

## usage

in the LaTeX file, use:

1. for the style: `\usemintedstyle{ssr}` (instead of, say, `\usemintedstyle{emacs}`)
2. for the environment: `\begin{minted}{ssr} ... \end{minted}`

3. for inlined code: `\mintinline{ssr}{...}`

