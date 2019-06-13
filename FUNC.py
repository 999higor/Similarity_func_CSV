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


def teste(val1, val2, name):

    if name == 'Hamming':
        
        print(val1, val2, name)
        #The return value is a float between 0 and 1, where 0 means totally different, and 1 equal.
        print("Hamming Similarity: ",  Hamming().normalized_similarity(val1, val2))


def main():

    v1 = 'text'
    v2 = 'text'

    # -----------------------------------------------Edit based ------------------------------------------------------
    print("-------------------------------- Edit based ----------------------------------")
    print("------- HAMMING ---------")
    ed = Hamming()
    #The return value is a float between 0 and 1, where 0 means totally different, and 1 equal.
    print("Hamming Similarity: ",  ed.normalized_similarity(v1, v2))

    print("\n-------- MLIPNS --------")
    ed = MLIPNS()
    print("MLIPNS similarity: ",ed.similarity(v1, v2))

    print("\n-------- JaroWinkler --------")
    ed = JaroWinkler()
    print("JaroWinkler similarity: ",ed.similarity(v1, v2))

    print("\n-------- Jaro --------")
    ed = Jaro()
    print("Jaro similarity: ",ed.similarity(v1, v2))


    # ----------------------------------------------- Token based ------------------------------------------------------

    print("-------------------------------- Token based ----------------------------------")
    print("\n-------- JACCARD --------")
    ed = Jaccard()
    print("JACCARD similarity: ",ed.similarity(v1, v2))
    #considera a quantidade de letras 

    print("\n-------- Sorensen --------")
    ed = Sorensen()
    print("Sorensen similarity: ",ed.similarity(v1, v2))
   
    print("\n-------- Tversky --------")
    ed = Tversky()
    print("Tversky similarity: ",ed.similarity(v1, v2))

    print("\n-------- Overlap --------")
    ed = Overlap()
    print("Overlap similarity: ",ed.similarity(v1, v2))

    print("\n-------- Cosine --------")
    ed = Cosine()
    print("Cosine similarity: ",ed.similarity(v1, v2))
    
    # ----------------------------------------------- Sequence based ------------------------------------------------------
    print("-------------------------------- Sequence based ----------------------------------")

    print("\n-------- RatcliffObershelp --------")
    ed = RatcliffObershelp()
    print("RatcliffObershelp similarity: ",ed.similarity(v1, v2))


    # ----------------------------------------------- Compression based ------------------------------------------------------
    print("-------------------------------- Compression based ----------------------------------")

    print("\n-------- EntropyNCD --------")
    ed = EntropyNCD()
    print("EntropyNCD similarity: ",ed.similarity(v1, v2))

    print("\n-------- BZ2NCD --------")
    ed = BZ2NCD()
    print("BZ2NCD similarity: ",ed.similarity(v1, v2))

    print("\n-------- LZMANCD --------")
    ed = LZMANCD()
    print("LZMANCD similarity: ",ed.similarity(v1, v2))

    print("\n-------- ZLIBNCD --------")
    ed = ZLIBNCD()
    print("ZLIBNCD similarity: ",ed.similarity(v1, v2))

    # ----------------------------------------------- Simple based ------------------------------------------------------
    print("-------------------------------- Simple based ----------------------------------")

    print("\n-------- Prefix --------")
    ed = Prefix()
    print("Prefix similarity: ",ed.similarity(v1, v2))

    print("\n-------- Postfix --------")
    ed = Postfix()
    print("Postfix similarity: ",ed.similarity(v1, v2))
    

    # ----------------------------------------------- strsim function ------------------------------------------------------
    print("-------------------------------- strsim function ----------------------------------")

    print("\n-------- Normalized Levenshtein --------")
    ed = NormalizedLevenshtein()
    print("Normalized Levenshtein similarity: ",ed.similarity(v1, v2))

    print("\n-------- MetricLCS --------")
    ed = MetricLCS()
    print("MetricLCS similarity: ",ed.distance(v1, v2))

    print("\n-------- NGram --------")
    ed = NGram()
    print("NGram similarity: ",ed.distance(v1, v2))

    print("\n-------- Sorensen --------")
    ed = Sorensen()
    print("Sorensen similarity: ",ed.similarity(v1, v2))

if __name__ == "__main__":
    main()