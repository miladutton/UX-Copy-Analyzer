
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from uxcopy.analyzer import analyze
from uxcopy.report import print_report

import argparse

def main():
    parser = argparse.ArgumentParser(description="UX Copy Tester: Analyze tone, clarity, and readability.")
    parser.add_argument("--text", required=True, help="The UX string to analyze")
    args = parser.parse_args()

    result = analyze(args.text)
    print_report(result)

if __name__ == "__main__":
    main()
