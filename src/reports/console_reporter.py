from .base_reporter import BaseReporter
import json

class ConsoleReporter(BaseReporter):
    def report(self, findings: dict):
        for category, issues in findings.items():
            print(f"\n🔍 {category.upper()} Findings:")
            if not issues:
                print("✅ No issues found.")
            for issue in issues:
                print(json.dumps(issue, indent=2))
