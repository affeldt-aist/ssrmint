ssrmint
====

## contents

see description in [setup.py](setup.py)

## requirements

python-setuptools, python-pygments (Debian packages)
(has been tested on a Debian 9.4 machine with Python 2.7.13)

## install

* type `make install`
* check the style and the lexer have been installed: `pygmentize -L lexers`, `pygmentize -L styles`

## usage

in the LaTeX file, use:

1. for the style: `\usemintedstyle{ssr}` (instead of, say, `\usemintedstyle{emacs}`)
2. for the environment: `\begin{minted}{ssr} ... \end{minted}`
3. for inlined code: `\mintinline{ssr}{...}`

to compile, use:

`pdflatex -shell-escape`

## FAQ

### How to compile without the option `-shell-escape` and without ssrmint installed?

1. first compile with the option `finalizecache`:
   `\usepackage[finalizecache]{minted}`
   (with the option `-shell-escape` and with ssrmint installed)
2. change the option to:
   `\usepackage[frozencache]{minted}`
3. ship the TeX files with the sub-directory `_minted-whatever`
4. you can now compile without the option `-shell-escape` and without ssrmint installed

[reference](https://github.com/gpoore/minted/issues/113#issuecomment-223451550)

