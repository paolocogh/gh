# POC automation framework

POC automation framework for testing SOAP webservice. The framework uses pytest for assertions and test case management. Allure is used for reporting and displays as a dashboard in Jenkins. The SUDS library is used for SOAP requests. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software.

#### Client side 

Python libraries used are in \\APIFramework\Reports\requirements.txt

```
pip install -r requirements.txt
```
#### Jenkins side

* Allure commandline: https://docs.qameta.io/allure/#_commandline
* Allure-pytest integration: https://pypi.org/project/allure-pytest/

#### Server side

Proprietary Algorithm (there is no free version of the algorithm right now, and this read me is for demo purposes)

## Running the tests 

Pytest has a feature to 'mark' test cases with a keyword. This is similar to Gmail's labels.
Running all smoke tests would look like: 

```
pytest -m smoke 
```
Available tags are in pytest.ini:
  smoke:  all smoke tests
  HER2: all tests related to HER2 algorithm
  PD-L1: all tests related to PD-L1 algorithm 
  in_test: script currently in test, used in debugging

Running all smoke tests and displaying results in Allure dashboard

```
pytest -m smoke --alluredir=C:\software\APIFramework\Reports TestCases
```

## Framework POC architecture

### Folder Structure

```
.
├── Configuration
│   └── requirements.txt
├── README.md
├── Reports *HTML reports for Allure*
├── __init__.py
├── allure-results *This is where raw test results are stored*
├── classes
│   ├── algorithms.py  *Main testing functions called at the script level*
│   ├── helper.py *Helper functions that are segragated from script level*
│   ├── ims.py 
│   └── properties.py *Global configurations like IP of Webservice to hit*
├── pytest.ini
├── test_cases 
│   ├── test_UID280_Restrict_to_BIF.py
│   ├── test_UID314_WSA_Cancel.py
│   ├── test_UID395_Restrict_to_Scanners.py
│   └── test_UID418_Restrict_to_20x.py
└── wsdl
    ├── ImageAnalysisDefinitions.wsdl
    └── ImageAnalysisSchema.xsd
```

### Classes

![alt text](https://i.imgur.com/MU7CF6O.png "Logo Title Text 1")


## Acknowledgments

* Hat tip to anyone whose code was used
* Shout out to my mom
* Special mention to Ducky for helping me debug

