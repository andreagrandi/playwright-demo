# playwright-demo
Demo usage of `playwright` and `pytest-bdd`. I found a tutorial on these two libraries, but the code was difficult to read (shown with images instead of text) so I rewrote the example in a way that was easy to read, download and try locally. In addition to the existing test case, I also wrote a similar test case for a different website, to practice and learn better about elements selectors.

# Installation
```bash
pip install -r requirements.txt
playwright install
```

# Running tests
```bash
pytest --html=report.html
```

# Features and Scenarios

This demo project contains the following features and scenarios:
- login tests for the [saucedemo.com](https://www.saucedemo.com/v1/) website
- login tests for the [practicetestautomation.com](https://practicetestautomation.com) website

# References

- https://www.linkedin.com/pulse/bdd-automation-playwright-pytest-bdd-odyssey-sachith-palihawadana/
- https://playwright.dev/python/docs/writing-tests
