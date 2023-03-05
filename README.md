# Pet project for test automation
## _Python + Pytest + Selenium_

Pet test automation framework for web testing.

Stack:
 - Python 3
 - Pytest
 - Selenium Library
 - Allure

#### Test cases

Simple tests for online bookshop.

#### Run Tests Options
``` 
 pytest -v --tb=line --language=en test_main_page.py
 pytest -s test_main_page.py
 pytest --alluredir=results test_main_page.py
```
#### Generate Report
```
allure serve results
```
This command will show you generated report in your default browser.