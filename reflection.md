1.	Which issues were the easiest to fix, and which were the hardest? Why?
    => Adding docstrings for each functions and renaming the functions to snake_case format were the easiest to fix. Even fixing eval() was straightforward.
    => Global variable usage and improper input validation were harder to fix as avoiding global state would require restructuring functions to pass stock_data as an argument, and adding input validation requires type checking and possibly error handling logic.
2.	Did the static analysis tools report any false positives? If so, describe one example.
    =>  Yes, one example of a false positive came from the tool flagging the commented-out line: #import logging
3.	How would you integrate static analysis tools into your actual software development workflow? Consider continuous integration (CI) or local development practices.
    =>During development:
        Run tools like pylint, flake8, or bandit locally before committing code. These tools can automatically check style, potential bugs, and security issues.
    =>In CI/CD pipelines:
        Integrate static analysis in GitHub Actions, GitLab CI, or Jenkins.
        For example, every pull request could automatically run:
            pylint inventory.py --exit-zero > pylint-report.txt
        This ensures that code pushed to the repository meets a minimum quality threshold (e.g., pylint score > 8).
    =>Pre-commit hooks:
        Use pre-commit framework to automatically format (using black or autopep8) and lint code before commits.
4.	What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?
    =>Readability:
        Clearer function names (add_item instead of addItem) and added docstrings make the code self-explanatory.
    =>Maintainability:
        Structured naming and consistent formatting make it easier to modify and debug later.
    =>Reliability:
        Fixing the mutable default argument prevents subtle bugs.
        Removing eval() eliminates a serious security risk.
    =>Professionalism:
        Overall code style improving the pylint score and making it closer to production-level quality.
