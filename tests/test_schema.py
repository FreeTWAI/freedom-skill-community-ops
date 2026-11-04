import unittest
import json
import os
import re

class TestSchema(unittest.TestCase):
    def setUp(self):
        self.base_dir = os.path.join(os.path.dirname(__file__), '..')

    def test_skill_book_json(self):
        filepath = os.path.join(self.base_dir, 'skill-book.json')
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        required_keys = [
            'format', 'id', 'title', 'version', 'guild_key',
            'entry', 'execution', 'repository', 'license'
        ]
        for key in required_keys:
            self.assertIn(key, data, f"Missing required key '{key}' in skill-book.json")

    def test_skill_md(self):
        filepath = os.path.join(self.base_dir, 'SKILL.md')
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check YAML frontmatter
        frontmatter_match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
        self.assertIsNotNone(frontmatter_match, "Missing YAML frontmatter in SKILL.md")
        frontmatter = frontmatter_match.group(1)
        self.assertIn('name: freedom-skill-community-ops', frontmatter)
        self.assertIn('description:', frontmatter)

        # Check expected H2 headings
        expected_headings = [
            '## 確認新人需要',
            '## 準備一次小活動',
            '## 協助找到夥伴',
            '## 留下交接紀錄',
            '## 完成時交付'
        ]
        for heading in expected_headings:
            self.assertIn(heading, content, f"Missing expected heading '{heading}' in SKILL.md")

    def test_result_template_md(self):
        filepath = os.path.join(self.base_dir, 'RESULT-TEMPLATE.md')
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check expected list items
        expected_items = [
            '- 日期：',
            '- 成果標題：',
            '- 我想幫助的人與問題：',
            '- 本輪可投入的時間：',
            '- 完成條件：',
            '- 我做了什麼：',
            '- 可公開的成果連結：',
            '- 回饋與下一步：'
        ]
        for item in expected_items:
            self.assertIn(item, content, f"Missing expected list item '{item}' in RESULT-TEMPLATE.md")

if __name__ == '__main__':
    unittest.main()
