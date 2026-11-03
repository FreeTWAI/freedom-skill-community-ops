import unittest
import os
import glob
import re
import json

class TestSecurity(unittest.TestCase):
    def setUp(self):
        # We will scan files in the root directory
        self.md_files = glob.glob('*.md')
        self.json_files = glob.glob('*.json')
        self.all_files = self.md_files + self.json_files

    def test_credential_exposure(self):
        """Scan .md and .json files for sensitive regex patterns."""
        patterns = {
            'AWS Key': r'AKIA[0-9A-Z]{16}',
            'Private Key': r'-----BEGIN [A-Z ]+ PRIVATE KEY-----',
            'GitHub Token': r'gh[pousr]_[a-zA-Z0-9]{36}',
            'JWT Token': r'eyJ[A-Za-z0-9-_=]+\.[A-Za-z0-9-_=]+\.?[A-Za-z0-9-_.+/=]*'
        }

        for filepath in self.all_files:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                for name, pattern in patterns.items():
                    matches = re.finditer(pattern, content)
                    for match in matches:
                        # Exclude some false positive cases if any, but we will just assert no match
                        self.fail(f"Found {name} in {filepath}")

    def test_input_sanitization(self):
        """Check .json files for <script> tags."""
        for filepath in self.json_files:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                self.assertNotIn('<script>', content.lower(), f"Found <script> tag in {filepath}")
                self.assertNotIn('</script>', content.lower(), f"Found </script> tag in {filepath}")

    def test_parameter_validation(self):
        """Verify skill-book.json contains the exact keys and their values are strings."""
        filepath = 'skill-book.json'
        self.assertTrue(os.path.exists(filepath), f"{filepath} does not exist")

        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        expected_keys = {
            'format', 'id', 'title', 'version', 'guild_key',
            'entry', 'execution', 'repository', 'license'
        }

        # Check if all expected keys are present
        self.assertEqual(set(data.keys()), expected_keys, f"Keys in {filepath} do not match expected keys")

        # Check if all values are strings
        for key, value in data.items():
            self.assertIsInstance(value, str, f"Value for key '{key}' in {filepath} is not a string")

if __name__ == '__main__':
    unittest.main()
