# Hebe: Test Automation Framework
## Hebe web application:

Hebe.pl is a Polish online store specializing in selling cosmetics, perfumes, household chemicals, cleaning products, and other home goods.

For more information please visit www.hebe.pl 


## Test Automation Framework:

This a Python-based test automation framework utilizing Pytest and Selenium libraries.
It was created according to POM pattern to test main functionality of the online store.

### Pytest settings

To adjust Pytest settings used when running your tests, use **pytest.ini** config file.
By default, tests are run with the following parameters:
```
[pytest]
addopts =
    -sv
    --tb=short
    --showlocals
    --reruns 3
    --alluredir=allure-results
    -r a
```

## GitHub Actions:

This project utilizes GitHub Actions for automating various tasks such as running tests, generating an Allure report and publishing it to GitHub pages.

### Configuration in GitHub:

Setting up deployment to GitHub pages from GitHub Actions:
- Navigate to *GitHub -> Repository -> Settings -> Pages* and set GitHub Actions as **Source**.


### run_tests.yml file

The following jobs are configured in run_test.yml file:

- **test**: Runs automated tests and saves results.
- **generate-report**: Generates a comprehensive Allure test report.
- **publish-report**: Publishes the generated report on GitHub Pages.

### How to run tests:

- Navigate to *GitHub -> Actions -> Automated tests* and click on **Run workflow**.

Once the test run is complete, the Allure report will be generated and posted to GitHub pages.

## Running tests locally:

To run tests locally, follow the steps below:

**1. Clone this repository to your machine:**
```
git clone https://github.com/nika-archakava/tms_final_project
```

**2. Create a virtual environment:**
```
python -m venv venv
```

**3. Install project dependencies:**
```
pip install -r requirements.txt
```

**4. Run tests:**
```
pytest
```

## Allure report generation:

Once test run is complete, you can generate Allure report using the following command:
```
allure serve allure-results
```
It will consolidate test results into a visual report which will be hosted locally until terminated.

To be able to use Allure report generation, make sure to install Allure and all its dependencies.
For more information follow [Allure Report installation](https://allurereport.org/docs/gettingstarted-installation/).