Bulgarian Stemmer
====================
py-bulgarian-stemmer
--------------------

This stemmer is based on Preslav Nakov's [BULSTEM](http://people.ischool.berkeley.edu/~nakov/bulstem/index.html).

Sample usage
------------
__1) Load a stem rules context:__
The stemmer can load both pickle and plaintext files containing the stemming rules.

	stemmer = BulgarianStemmer('stem_rules_context_1.pkl') # or .txt

__2) Stem a given word:__

	stemmed_word = stemmer('обикновен')
	stemmer.print_word('уникалният') # if you want to print it in the console