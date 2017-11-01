import unittest

import requests
import mock

from stats import config, fetch


@mock.patch('stats.fetch.requests', spec=requests)
class FetchTest(unittest.TestCase):
    def test_get_comments(self, requests_mock):
        mocked_data = {
            'has_more': False,
            'items': [1, 2, 3]
        }
        requests_mock.get.return_value.json.return_value = mocked_data
        result = fetch.get_comment('123123')

        assert result == [1, 2, 3]

    def test_get_answers(self, requests_mock):
        mocked_data = {
            'has_more': False,
            'items': ['foo', 'bar']
        }
        requests_mock.get.return_value.json.return_value = mocked_data
        result = fetch.get_answers(
                    since='2015-10-09 11:00:00',
                    until='2015-10-09 12:00:00'
                 )

        requests_params = config.API_PARAMETERS
        requests_params.update({
            'page': 1,
            'fromdate': '1444377600',
            'todate': '1444381200'
        })
        requests_mock.get.assert_called_once_with(
            '{0}answers'.format(config.API_URL),
            requests_params
        )

        assert result == ['foo', 'bar']
