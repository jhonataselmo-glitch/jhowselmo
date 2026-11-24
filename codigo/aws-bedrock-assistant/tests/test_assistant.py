import unittest
from unittest.mock import Mock
from assistant import summarize


def response(text='Resumo'):
    return {'stopReason': 'end_turn', 'output': {'message': {'content': [{'text': text}]}},
            'usage': {'inputTokens': 20, 'outputTokens': 5, 'totalTokens': 25}}


class SummaryTests(unittest.TestCase):
    def setUp(self):
        self.client = Mock()
        self.client.converse.return_value = response()

    def test_blank_input_never_calls_provider(self):
        for text in ['', '  ', None, 123]:
            with self.subTest(text=text), self.assertRaises(ValueError):
                summarize(text, 'model', self.client)
        self.client.converse.assert_not_called()

    def test_character_limit_never_calls_provider(self):
        with self.assertRaises(ValueError):
            summarize('a' * 12001, 'model', self.client)
        self.client.converse.assert_not_called()

    def test_utf8_byte_limit_never_calls_provider(self):
        with self.assertRaises(ValueError):
            summarize('😀' * 10000, 'model', self.client)
        self.client.converse.assert_not_called()

    def test_missing_model_never_calls_provider(self):
        with self.assertRaises(ValueError):
            summarize('Texto', '', self.client)
        self.client.converse.assert_not_called()

    def test_summary_preserves_usage_and_limits_generation(self):
        result = summarize('  Texto  ', 'my-model', self.client)
        self.assertEqual(result, {'summary': 'Resumo', 'usage': {
            'inputTokens': 20, 'outputTokens': 5, 'totalTokens': 25}})
        kwargs = self.client.converse.call_args.kwargs
        self.assertEqual(kwargs['modelId'], 'my-model')
        self.assertEqual(kwargs['inferenceConfig']['maxTokens'], 512)
        self.assertEqual(kwargs['messages'][0]['content'], [{'text': 'Texto'}])

    def test_truncated_response_is_not_reported_as_success(self):
        self.client.converse.return_value['stopReason'] = 'max_tokens'
        with self.assertRaises(RuntimeError):
            summarize('Texto', 'model', self.client)

    def test_empty_response_is_failure(self):
        self.client.converse.return_value = response('  ')
        with self.assertRaises(RuntimeError):
            summarize('Texto', 'model', self.client)

    def test_provider_failure_propagates_without_retry_loop(self):
        self.client.converse.side_effect = TimeoutError()
        with self.assertRaises(TimeoutError):
            summarize('Texto', 'model', self.client)
        self.assertEqual(self.client.converse.call_count, 1)


if __name__ == '__main__':
    unittest.main()
