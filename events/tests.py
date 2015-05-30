import json
from django.test import TestCase
from django.core.urlresolvers import reverse
from .utils import parse_command

class UtilsTests(TestCase):

	def test_parse_command(self):
		"""
		Test that commands are parsed correctly
		"""
		parsed_cmd = parse_command('play -f batman.wav -r 2')
		self.assertEqual(parsed_cmd['cmd'], 'play')
		self.assertEqual(parsed_cmd['args']['-f'], 'batman.wav')
		self.assertEqual(parsed_cmd['args']['-r'], '2')

class ViewsTests(TestCase):

	def test_executes_correct_command(self):
		"""
		Test that send endpoint executes the correct command
		"""
		response = self.client.post(reverse('events:send'), {'cmd': 'play -f batman.wav -r 2'})
		data = json.loads(response.content)
		self.assertEqual(data['command'], 'play')

	def test_error_on_get(self):
		"""
		Test that send endpoint do not work on GET
		"""
		response = self.client.get(reverse('events:send'))
		data = json.loads(response.content)
		self.assertEqual(data['error'], 'You cannot use GET request')

	def test_error_if_cmd_string_is_empty(self):
		"""
		Test that we return an error if cmd is not specified
		"""
		response = self.client.post(reverse('events:send'), {'cmd': ''})
		data = json.loads(response.content)
		self.assertEqual(data['error'], 'Command string cannot be empty')

	def test_error_if_cmd_not_found(self):
		"""
		Test that we return an error if cmd is not supported
		"""
		response = self.client.post(reverse('events:send'), {'cmd': 'wrong'})
		data = json.loads(response.content)
		self.assertEqual(data['error'], 'Command not found: wrong')