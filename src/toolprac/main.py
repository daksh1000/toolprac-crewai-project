#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from toolprac.crew import Toolprac

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    """
    Run the crew.
    """
    topic = input("What is the topic for the motivational email? (default: loneliness and self-worth): ")
    if not topic:
        topic = "loneliness and self-worth"

    try:
        result = Toolprac().crew().kickoff(inputs={"topic": topic})
        print(result.raw)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


if __name__ == "__main__":
    run()
