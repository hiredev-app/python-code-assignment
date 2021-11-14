import unittest

from api_task.github_organisation_info import get_organisation_info_markdown, get_orgnisation_info


class GitHubOrganisationVersionCase(unittest.TestCase):
    def test_organisation_name(self):
        info = get_orgnisation_info()
        name = ''
        self.assertEqual('Webscope.io', name)

    def test_organisation_location(self):
        info = get_orgnisation_info()
        location = ''
        self.assertEqual('Czech Republic', location)

    def test_organisation_info(self):
        # the goal of this task to to provide a text representation of a company
        # please note that data in this expected string serve as an illustration
        info = get_organisation_info_markdown(slug='webscopeio')
        self.assertEqual(
            """
            Webscope.io (Verified ✓)
            ------------
            Location: Czech Republic | httsp://www.webscope.io | hello@webscope.io
            ------------
            Public Repos: 31
            Members: 
            - member1
            - member2
            """
            , info)


if __name__ == '__main__':
    unittest.main()
