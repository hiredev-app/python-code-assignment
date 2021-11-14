import unittest

from utils.parse_npm_version import parse_npm_version


class ParseNPMVersionCase(unittest.TestCase):
    def test_parse_npm_version(self):
        npm_version = parse_npm_version('packagename@1.2.3')
        self.assertEqual(('packagename', '1.2.3'), npm_version)

    def test_parse_npm_version_with_org_prefix(self):
        npm_version = parse_npm_version('@webscopeio/packagename@1.2.3')
        self.assertEqual(('@webscopeio/packagename', '1.2.3'), npm_version)


if __name__ == '__main__':
    unittest.main()
