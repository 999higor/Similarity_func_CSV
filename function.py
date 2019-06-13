# textdistance

# edit based
from textdistance import Hamming
from textdistance import MLIPNS
from textdistance import JaroWinkler
from textdistance import Jaro
from textdistance import StrCmp95

# token based
from textdistance import Jaccard
from textdistance import Sorensen
from textdistance import Tversky
from textdistance import Overlap
from textdistance import Cosine

# sequence based
from textdistance import RatcliffObershelp

# compression based
from textdistance import EntropyNCD
from textdistance import BZ2NCD
from textdistance import LZMANCD
from textdistance import ZLIBNCD

# simple based
from textdistance import Prefix
from textdistance import Postfix

# strsim

from similarity.normalized_levenshtein import NormalizedLevenshtein
from similarity.metric_lcs import MetricLCS
from similarity.ngram import NGram
from similarity.sorensen_dice import SorensenDice

def similaridade(function_name, string_1, string_2):

    if function_name == 'Hamming':
        ed = Hamming()
        return ed.normalized_similarity(string_1, string_2)

    elif function_name == 'MLIPNS':
        ed = MLIPNS()
        return ed.similarity(string_1, string_2)

    elif function_name == 'JaroWinkler':
        ed = JaroWinkler()
        return ed.similarity(string_1, string_2)

    elif function_name == 'Jaro':
        ed = Jaro()
        return ed.similarity(string_1, string_2)

    elif function_name == 'Jaccard':
        ed = Jaccard()
        return ed.similarity(string_1, string_2)

    elif function_name == 'Sorensen':
        ed = Sorensen()
        return ed.similarity(string_1, string_2)

    elif function_name == 'Tversky':
        ed = Tversky()
        return ed.similarity(string_1, string_2)

    elif function_name == 'Overlap':
        ed = Overlap()
        return ed.similarity(string_1, string_2)

    elif function_name == 'Cosine':
        ed = Cosine()
        return ed.similarity(string_1, string_2)

    elif function_name == 'RatcliffObershelp':
        ed = RatcliffObershelp()
        return ed.similarity(string_1, string_2)

    elif function_name == 'EntropyNCD':
        ed = EntropyNCD()
        return ed.similarity(string_1, string_2)

    elif function_name == 'BZ2NCD':
        ed = BZ2NCD()
        return ed.similarity(string_1, string_2)

    elif function_name == 'LZMANCD':
        ed = LZMANCD()
        return ed.similarity(string_1, string_2)

    elif function_name == 'ZLIBNCD':
        ed = ZLIBNCD()
        return ed.similarity(string_1, string_2)

    elif function_name == 'Prefix':
        ed = Prefix()
        return ed.similarity(string_1, string_2)

    elif function_name == 'Postfix':
        ed = Postfix()
        return ed.similarity(string_1, string_2)

    elif function_name == 'NormalizedLevenshtein':
        ed = NormalizedLevenshtein()
        return ed.similarity(string_1, string_2)

    elif function_name == 'MetricLCS':
        ed = MetricLCS()
        return ed.distance(string_1, string_2)

    elif function_name == 'NGram':
        ed = NGram()
        return ed.distance(string_1, string_2)

    elif function_name == 'StrCmp95':
        ed = StrCmp95()
        return ed.distance(string_1, string_2)


    