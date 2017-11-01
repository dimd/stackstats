import json
import unittest

import mock

from stats import calc


class CalcTest(unittest.TestCase):
    def setUp(self):
        with open('tests/fixtures/answers.json') as f:
            self.answers = json.load(f)
        with open('tests/fixtures/comments.json') as f:
            self.comments = json.load(f)

    def test_get_accepted_answers(self):
        accepted = calc.get_accepted_answers(self.answers)

        assert len(accepted) == 30

    def test_avg_score(self):
        avg = calc.get_avg_score(self.answers)

        assert avg == 1.3

    def test_avg_answers_per_question(self):
        result = calc.get_avg_answers_per_question(self.answers)

        assert result == 1.2

    @mock.patch('stats.fetch.get')
    def test_top_ten_comments_count(self, get_mock):
        get_mock.side_effect = self.comments
        result = calc.get_top_ten_comments_count(self.answers)

        assert result == {
            37584848: 0,
            37584962: 2,
            37584827: 10,
            37584935: 1,
            37584880: 2,
            37584785: 0,
            37584886: 1,
            37584793: 2,
            37584923: 1,
            37584797: 0
        }
