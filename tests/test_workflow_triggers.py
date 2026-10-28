import unittest
import os

class TestCommunityWorkflowTriggers(unittest.TestCase):
    def setUp(self):
        # Ensure we are reading relative to the workspace root
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        skill_path = os.path.join(base_dir, 'SKILL.md')
        result_path = os.path.join(base_dir, 'RESULT-TEMPLATE.md')

        with open(skill_path, 'r', encoding='utf-8') as f:
            self.skill_content = f.read()

        with open(result_path, 'r', encoding='utf-8') as f:
            self.result_content = f.read()

    def test_member_onboarding_steps(self):
        """Verify that onboarding steps are defined in the skill document."""
        self.assertIn("## 確認新人需要", self.skill_content)
        self.assertIn("先問對方希望參與什麼", self.skill_content)
        self.assertIn("## 協助找到夥伴", self.skill_content)

    def test_community_event_triggers(self):
        """Verify that community event triggers are defined."""
        self.assertIn("## 準備一次小活動", self.skill_content)
        self.assertIn("寫明主題、對象、時間、參與方式與主持人", self.skill_content)
        self.assertIn("## 留下交接紀錄", self.skill_content)

    def test_checklist_validations(self):
        """Verify that completion checklists and validation templates exist."""
        # Check SKILL.md deliverables
        self.assertIn("## 完成時交付", self.skill_content)
        self.assertIn("- 歡迎流程", self.skill_content)
        self.assertIn("- 活動說明", self.skill_content)
        self.assertIn("- 去識別的交接摘要", self.skill_content)

        # Check RESULT-TEMPLATE.md fields
        self.assertIn("- 成果標題：", self.result_content)
        self.assertIn("- 完成條件：", self.result_content)
        self.assertIn("- 可公開的成果連結：", self.result_content)

if __name__ == '__main__':
    unittest.main()
