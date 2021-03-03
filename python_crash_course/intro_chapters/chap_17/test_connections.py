# Test the api connections for github and hacker news
import unittest
from python_repos_visual import call_github_api
from python_repos_visual import call_hn_api


class TestReturnCode(unittest.TestCase):
    def test_github_status(self):
        r_github, response_dict_github = call_github_api()
        self.assertEqual(r_github.status_code, 200)

    def test_github_response_count(self):
        r_github, response_dict_github = call_github_api()
        print(response_dict_github['total_count'])
        self.assertGreater(response_dict_github['total_count'], 6000000)

    def test_github_returned_count(self):
        r_github, response_dict_github = call_github_api()
        self.assertEqual(len(response_dict_github['items']), 35)

    def test_hn(self):
        r_hn, response_dict_hn = call_hn_api()
        self.assertEqual(200, r_hn.status_code)


if __name__ == '__main__':
    print('Testing api connections ...')
    unittest.main()

