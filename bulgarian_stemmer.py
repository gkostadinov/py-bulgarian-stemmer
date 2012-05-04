#!/usr/bin/python
# -*- coding: cp1251 -*-

import re
import pickle
import os

class BulgarianStemmer(object):
    def __init__(self, filename='stem_rules_context_1.pkl'):
        self.stem_boundary = 1

        file_extension = os.path.splitext(filename)[1]
        if file_extension == '.pkl':
            self.load_pickle_context(filename)
        elif file_extension == '.txt':
            self.load_text_context(filename)
        else:
            raise IOError("Wrong file extension! .txt or .pkl files only!")

    def __call__(self, word):
        return self.stem(word)

    def load_pickle_context(self, filename):
        context_file = open(filename, 'rb')
        self.stemming_rules = pickle.load(context_file)

    def load_text_context(self, filename):
        self.stemming_rules = dict()

        stemming_context = open(filename, 'r')
        for line in stemming_context:
            rule_match = re.search('([\xe0-\xff]+)\s==>\s([\xe0-\xff]+)\s([0-9]+)', line)
            
            if rule_match:
                if int(rule_match.group(3)) > self.stem_boundary:
                    self.stemming_rules[rule_match.group(1)] = rule_match.group(2)

    def stem(self, word):
        valid_word = re.search('[^\xe0\xfa\xee\xf3\xe5\xe8\xff\xfe]*[\xe0\xfa\xee\xf3\xe5\xe8\xff\xfe]', word)
        word_length = len(word)

        if valid_word and word_length > 1:
            for i in range(word_length):
                suffix = word[i:]

                if suffix in self.stemming_rules:
                    return word[:i] + self.stemming_rules[suffix]

        return word

    def print_word(self, word):
        print self(word).decode('cp1251')

if __name__ == '__main__':
    stemmer = BulgarianStemmer('stem_rules_context_1.pkl')

    stemmer.print_word('обикновен')
    stemmer.print_word('английският')
    stemmer.print_word('човекът')
    stemmer.print_word('уникалният')
    stemmer.print_word('негодувания')
    