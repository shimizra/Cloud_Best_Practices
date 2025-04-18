from .base_reporter import BaseReporter
import json
import os
from datetime import datetime

class JSONReporter(BaseReporter):
    def __init__(self, output_dir="reports/output"):
        os.makedirs(output_dir, exist_ok=True)
        self.output_dir = output_dir

    def report(self, findings: dict):
        timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
        file_path = os.path.join(self.output_dir, f"findings_{timestamp}.json")

        with open(file_path, "w") as f:
            json.dump(findings, f, indent=2)

        print(f"📁 Findings saved to: {file_path}")
