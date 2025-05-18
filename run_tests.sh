#!/bin/bash

# Task 6: Run pytest automatically in CI pipeline

# Step 1: Activate the virtual environment
source .venv/Scripts/activate

# Step 2: Run the test suite
pytest test_app.py
TEST_RESULT=$?

# Step 3: Return appropriate exit code
if [ $TEST_RESULT -eq 0 ]; then
  echo "✅ All tests passed."
  exit 0
else
  echo "❌ Some tests failed."
  exit 1
fi
