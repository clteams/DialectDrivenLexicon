#!/usr/bin/python3


class LexiconQuery:
    def __init__(self, dd_lexicon):
        self.lexicon = dd_lexicon


class QueryFrame:
    def __init__(self, entries):
        self.entries = entries

    def reduce(self):
