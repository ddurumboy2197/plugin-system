import unittest
import sys
import os

def run_tests(tests):
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromNames(tests)
    runner = unittest.TextTestRunner()
    runner.run(suite)

def get_tests():
    tests = []
    for file in os.listdir():
        if file.endswith('.py') and file != 'runner.py':
            tests.append(file[:-3])
    return tests

def main():
    tests = get_tests()
    run_tests(tests)

if __name__ == '__main__':
    main()
```

```python
# runner.py
