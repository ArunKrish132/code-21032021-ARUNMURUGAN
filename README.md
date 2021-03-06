## code-21032021-ARUNMURUGAN
BMI Calculator

Problem:
1) Calculate the BMI (Body Mass Index) using Formula 1 , BMI Category and Health risk from Table 1 of the person and add them as 3 new columns 
2) Count the total number of overweight people using ranges in the column BMI Category of Table 1, check this is consistent programmatically and add any other observations in the documentation
3) Create build, tests to make sure the code is working as expected and this can be added to an automation build / test / deployment pipeline

Formula 1 - BMI
BMI(kg/m^2) = mass(kg) / height(m)
The BMI (Body Mass Index) in (kg/m^2) is equal to the weight in kilograms (kg) divided by your height in meters squared (m)^2 . 
For example, if you are 175cm (1.75m) in height and 75kg in weight, you can calculate your BMI as follows: 75kg / (1.75m2) = 24.49kg/m^2

<table>
  <tr>
    <th>BMI Range (kg/m2)</th>
    <th>BMI Category</th>
    <th>Health risk</th>
  </tr>
  <tr>
    <td>18.4 and below</td>
    <td>Underweight</td>
    <td>Malnutrition risk</td>
  </tr>
  <tr>
    <td>18.5 - 24.9</td>
    <td>Normal weight</td>
    <td>Low risk</td>
  </tr>
  <tr>
    <td>25 - 29.9</td>
    <td>Overweight</td>
    <td>Enhanced risk</td>
  </tr>
  <tr>
    <td>30 - 34.9</td>
    <td>Moderately obese</td>
    <td>Medium risk</td>
  </tr>
  <tr>
    <td>35 - 39.9</td>
    <td>Severely obese</td>
    <td>High risk</td>
  </tr>
  <tr>
    <td>40 and above</td>
    <td>Very severely obese</td>
    <td>Very high risk</td>
  </tr>
</table>

Sample Input JSON:
[{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 }, { "Gender": "Male", "HeightCm": 161, "WeightKg":
85 }, { "Gender": "Male", "HeightCm": 180, "WeightKg": 77 }, { "Gender": "Female", "HeightCm": 166,
"WeightKg": 62}, {"Gender": "Female", "HeightCm": 150, "WeightKg": 70}, {"Gender": "Female",
"HeightCm": 167, "WeightKg": 82}]

Pre-requisites:
1. Python 3
2. Python Packages:
  pip install jsonschema==3.2.0

Note:
1. Please update the input file name in bmi_calculator.py for different inputs

Execute 'run.bat' to download the dependency and start the bmi calculation for data in testfile.json

