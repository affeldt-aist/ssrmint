contents:
tentative modification of pygments to customize pretty-printing of Coq code in LaTeX documents

install:
make install

check that the lexer has been installed:
pygmentize -L lexers | grep ssr

check that the style has been installed:
pygmentize -L styles | grep ssr

usage:
in the LaTeX file, use
\usemintedstyle{ssr} (instead if say \usemintedstyle{emacs}
and for the environment:
\begin{minted}{ssr}
...
\end{minted}

