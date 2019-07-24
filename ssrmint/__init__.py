from pygments.style import Style
from pygments.token import Text, Comment, Operator, Keyword, Name, String, \
    Number, Punctuation, Generic, Whitespace, Error
from pygments.lexer import RegexLexer, default, words

class SSRStyle(Style):
    """
    adjust emacs stylesheet to look more like proof general with default emacs settings
    """

    default_style = "emacs"

    styles = {
        Comment:		"italic #228B22",		# forest green
        Operator:               '#696969',			# dim gray
        Keyword:                "#0000AA",
        Keyword.Constant:	"#0000CD",			# tactics (medium blue)
        Keyword.Type:		"#228B22",			# sorts (forest green)
        Keyword.Namespace:	"#8B008B",	        	# vernacular (dark magenta)
        Keyword.Pseudo:	        "#EE0000",	        	# terminators (red)
	Keyword.Reserved:	"#9400D3",			# tacticals (dark violet)
        Number:			"#191970",			# midnight blue
        Name.Literal:		"#000000"			# black
    }

class SSRLexer(RegexLexer):
    """
    originally copy-pasted from /usr/lib/python2.7/dist-packages/pygments/lexers/theorem.py [2018-04-06]

    which has the following copyright

    :copyright: Copyright 2006-2017 by the Pygments team
    :license: BSD

    changes are marked as [NB(rei): ...]
    """

    name = 'Coq'
    aliases = ['ssr']
    filenames = ['*.v']
    mimetypes = ['text/x-coq']

    keywords1 = (
        # Vernacular commands
        'Section', 'Module', 'End', 'Require', 'Import', 'Export', 'Variable',
        'Variables', 'Parameter', 'Parameters', 'Axiom', 'Hypothesis',
        'Hypotheses', 'Notation', 'Local', 'Tactic', 'Reserved', 'Scope',
        'Open', 'Close', 'Delimit', 'Definition', 'Let', 'Ltac',
        'Fixpoint', 'CoFixpoint', 'Morphism', 'Relation', 'Implicit',
        'Arguments', 'Set', 'Unset', 'Contextual', 'Strict', 'Prenex',
        'Implicits', 'Inductive', 'CoInductive', 'Record', 'Structure',
        'Canonical', 'Coercion', 'Theorem', 'Lemma', 'Corollary',
        'Proposition', 'Fact', 'Remark', 'Example', 'Proof', 'Goal', 'Save',
        'Qed', 'Defined', 'Hint', 'Resolve', 'Rewrite', 'View', 'Search',
        'Show', 'Print', 'Printing', 'All', 'Graph', 'Projections', 'inside',
        'outside', 'Check', 'Global', 'Instance', 'Existing',
        'Universe', 'Polymorphic', 'Monomorphic', 'Context',
        'Program', 'Eval', 'Obligation', 'Obligations', 'Solve' #[NB(rei): added]
        #[NB(rei): removed 'Bind', 'Class']
    )
    keywords2 = (
        # Gallina
        'forall', 'exists', 'exists2', 'fun', 'fix', 'cofix', 'struct',
        'match', 'end',  'in', 'return', 'let', 'if', 'is', 'then', 'else',
        'for', 'of', 'nosimpl', 'with', 'as',
    )
    keywords3 = (
        # Sorts
        'Type', 'Prop',
    )
    keywords4 = (
        # Tactics
        'pose', 'set', 'move', 'case', 'elim', 'apply', 'clear', 'hnf', 'intro',
        'intros', 'generalize', 'rename', 'pattern', 'after', 'destruct',
        'induction', 'using', 'refine', 'inversion', 'injection', 'rewrite',
        'congr', 'unlock', 'compute', 'ring', 'field', 'replace', 'fold',
        'unfold', 'change', 'cutrewrite', 'simpl', 'have', 'suff', 'wlog',
        'suffices', 'without', 'loss', 'nat_norm', 'cut', 'trivial',
        'revert', 'bool_congr', 'nat_congr', 'transitivity', 'auto',
        'split', 'left', 'right', 'autorewrite', 'tauto', 'setoid_rewrite',
        'intuition', 'eauto', 'eapply', 'econstructor', 'etransitivity',
        'constructor', 'erewrite', 'red', 'cbv', 'lazy', 'vm_compute',
        'native_compute', 'subst',
        'fourier', 'nstaz', 'lra', 'program_simpl' #[NB(rei): added]
        #[NB(rei): removed 'assert', 'symmetry']
    )
    keywords5 = (
        # Terminators
        'by', 'done', 'exact', 'reflexivity', 'tauto', 'romega', 'omega',
        'assumption', 'solve', 'contradiction', 'discriminate',
        'congruence',
    )
    keywords6 = (
        # Control
        'do', 'last', 'first', 'try', 'idtac', 'repeat'
    )
    # 'as', 'assert', 'begin', 'class', 'constraint', 'do', 'done',
    # 'downto', 'else', 'end', 'exception', 'external', 'false',
    # 'for', 'fun', 'function', 'functor', 'if', 'in', 'include',
    # 'inherit', 'initializer', 'lazy', 'let', 'match', 'method',
    # 'module', 'mutable', 'new', 'object', 'of', 'open', 'private',
    # 'raise', 'rec', 'sig', 'struct', 'then', 'to', 'true', 'try',
    # 'type', 'val', 'virtual', 'when', 'while', 'with'
    keyopts = (
        '!=', '#', '&', '&&', r'\(', r'\)', r'\*', r'\+', ',', '-', r'-\.',
        '->', r'\.', r'\.\.', ':', '::', ':=', ':>', ';', ';;', '<', '<-',
        '<->', '=', '>', '>]', r'>\}', r'\?', r'\?\?', r'\[', r'\[<', r'\[>',
        r'\[\|', ']', '_', '`', r'\{', r'\{<', r'\|', r'\|]', r'\}', '~', '=>',
        r'/\\', r'\\/', r'\{\|', r'\|\}',
        u'Π', u'λ',
    )
    operators = r'[!$%&*+\./:<=>?@^|~-]'
    prefix_syms = r'[!?~]'
    infix_syms = r'[=<>@^|&+\*/$%-]'
    primitives = ('unit', 'nat', 'bool', 'string', 'ascii', 'list')

    tokens = {
        'root': [
            (r'\s+', Text),
            (r'false|true|\(\)|\[\]', Name.Builtin.Pseudo),
            (r'\(\*', Comment, 'comment'),
            (words(keywords1, prefix=r'\b', suffix=r'\b'), Keyword.Namespace),	# definitions, etc.
            # [NB(rei): was "(words(keywords2, prefix=r'\b', suffix=r'\b'), Keyword),"]
            (words(keywords2, prefix=r'\b', suffix=r'\b'), Keyword.Type),	# forall, etc.
            (words(keywords3, prefix=r'\b', suffix=r'\b'), Keyword.Type),	# types and sorts
            # [NB(rei): was "(words(keywords4, prefix=r'\b', suffix=r'\b'), Keyword),"]
            (words(keywords4, prefix=r'\b', suffix=r'\b'), Keyword.Constant), 	# tactics
            (words(keywords5, prefix=r'\b', suffix=r'\b'), Keyword.Pseudo), 	# terminators
            (words(keywords6, prefix=r'\b', suffix=r'\b'), Keyword.Reserved),
            # (r'\b([A-Z][\w\']*)(\.)', Name.Namespace, 'dotted'),
            (r'\b([A-Z][\w\']*)', Name),
            (r'(%s)' % '|'.join(keyopts[::-1]), Operator),
            (r'(%s|%s)?%s' % (infix_syms, prefix_syms, operators), Operator),
            # [NB(rei): was "(r'\b(%s)\b' % '|'.join(primitives), Keyword.Type),"]
            (r'\b(%s)\b' % '|'.join(primitives), Name.Literal),			# unit, nat, etc.

            (r"[^\W\d][\w']*", Name),

            (r'\d[\d_]*', Number.Integer),
            (r'0[xX][\da-fA-F][\da-fA-F_]*', Number.Hex),
            (r'0[oO][0-7][0-7_]*', Number.Oct),
            (r'0[bB][01][01_]*', Number.Bin),
            (r'-?\d[\d_]*(.[\d_]*)?([eE][+\-]?\d[\d_]*)', Number.Float),

            (r"'(?:(\\[\\\"'ntbr ])|(\\[0-9]{3})|(\\x[0-9a-fA-F]{2}))'",
             String.Char),
            (r"'.'", String.Char),
            (r"'", Keyword),  # a stray quote is another syntax element

            (r'"', String.Double, 'string'),

            (r'[~?][a-z][\w\']*:', Name),
        ],
        'comment': [
            (r'[^(*)]+', Comment),
            (r'\(\*', Comment, '#push'),
            (r'\*\)', Comment, '#pop'),
            (r'[(*)]', Comment),
        ],
        'string': [
            (r'[^"]+', String.Double),
            (r'""', String.Double),
            (r'"', String.Double, '#pop'),
        ],
        'dotted': [
            (r'\s+', Text),
            (r'\.', Punctuation),
            (r'[A-Z][\w\']*(?=\s*\.)', Name.Namespace),
            (r'[A-Z][\w\']*', Name.Class, '#pop'),
            (r'[a-z][a-z0-9_\']*', Name, '#pop'),
            default('#pop')
        ],
    }

    def analyse_text(text):
        if text.startswith('(*'):
            return True
