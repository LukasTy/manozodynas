# encoding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse
from manozodynas.testutils import StatefulTesting


class IndexTestCase(StatefulTesting):
    def test_index_page(self):
        self.open(reverse('index'))
        self.assertStatusCode(200)

class WordTestCase(StatefulTesting):
	def test_random_word_page(self):
		self.open(reverse('random_word'))
		self.assertStatusCode(200)

	def test_new_word(self):
		self.open(reverse('add_word'))
		self.selectForm('#add_word-form')
		self.submitForm({
			'Speaker': 'Garsiakalbis'
			})
		self.assertStatusCode(200)

	def test_words_page(self):
		self.open(reverse('words'))
		self.assertStatusCode(200)
