import sqlite3
import docx

import tools

import regex as re
import simplejson as json

class LectionParser:

    def evalLection(self, data):
        for p in data:
            self.calcMetrics(p)
            self.evalIsolated(p)

        for index, p in enumerate(data):
            self.evalInContext(data, index)
            print(
                ("X " if p['dist_start'] else "  ")
                + f"|{str(p['e_dist_isolated']).rjust(4)}|{str(p['e_example_isolated']).rjust(3)}|{tools.truncate(p['text'])}")

    def evalDistIsolated(self, paragraph):
        paragraph['e_dist_isolated'] = paragraph['chars_card_specific'] * \
            9 + paragraph['chars_card_vague'] * 3 - paragraph['chars_non_card']

    def evalExampleIsolated(self, paragraph):
        paragraph['e_example_isolated'] = paragraph['word_example'] * \
            100 - paragraph['chars_non_card'] - len(paragraph)

    def evalDistStart(self, paragraphs, index):
        para = paragraphs[index]
        if index != 0 and paragraphs[index-1]['e_dist_isolated'] > 10:
            para['dist_start'] = False
        elif index > 4 and sum([paragraphs[index-1]['e_dist_isolated'] > 30, paragraphs[index-2]['e_dist_isolated'] > 40, paragraphs[index-3]['e_dist_isolated'] > 40, paragraphs[index-4]['e_dist_isolated'] > 40]) >= 2:
            para['dist_start'] = False
        elif paragraphs[index]['e_dist_isolated'] > 30:
            para['dist_start'] = True
        elif len(paragraphs) - index < 3:
            para['dist_start'] = False
        elif paragraphs[index+1]['e_dist_isolated'] > 15 and paragraphs[index]['e_dist_isolated'] > 40:
            para['dist_start'] = True
        elif paragraphs[index]['e_dist_isolated'] > 5 and len(paragraphs) - index > 4 and sum([paragraphs[index+1]['e_dist_isolated'] > 20, paragraphs[index+2]['e_dist_isolated'] > 40, paragraphs[index+3]['e_dist_isolated'] > 30, paragraphs[index+4]['e_dist_isolated'] > 30]) >= 2:
            para['dist_start'] = True
        else:
            para['dist_start'] = False

    def calcMetrics(self, paragraph):

        t = paragraph['text']

        # count metrics

        paragraph['chars_card_specific'] = len(re.findall(
            r'([AKQJ98765432]|10),|-(?=\s{2,})|-(?<=\s{2,})', t))
        paragraph['chars_card_vague'] = len(re.findall(
            r'[AKQJ98765432]|10|-(?=\s{2,})|-(?<=\s{2,})', t))
        paragraph['chars_non_card'] = len(re.findall(r'[a-zB-IL-PR-Z]', t))

        # presence metrics

        paragraph['word_example'] = 1 if re.match(r'(?i)Příklad', t) else 0
        paragraph['word_contract'] = 1 if re.match(r'(?i)závazek', t) else 0
        paragraph['word_vynos'] = 1 if re.match(r'(?i)výnos', t) else 0

    def evalIsolated(self, paragraph):
        self.evalDistIsolated(paragraph)
        self.evalExampleIsolated(paragraph)

    def evalInContext(self, paragraphs, index):

        self.evalDistStart(paragraphs, index)
