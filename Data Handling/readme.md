## Introduction

<!----> Plrease note the timesheet.csv is too big for github and can be found following this link: https://drive.google.com/file/d/1nylqIDJoRCxpk6StnVVTYsB5UhlUdk0l/view?usp=sharing

The files in this directory address the data handling that was performed to obtained final dataset for the model training. 

The python scripts were executed in following order:
1. adding_additional_data.py
2. transforming_variables.py
3. filling_empty_data.py

### Script Descriptions 

- adding_additional_data.py - adds 2 new variables from Fresh Projects Database to our dataset
- transforming_variables.py - tranforms categorical variables, adjusts for currency diffrences and creates dummies
- filling_empty_data.py - fills Nan values
  
### Datasets Decriptions

- data_survey - holds data obtained from the survey
- company_relevant_data - provides projects data from Fresh Project Database
- timesheet_data - timesheet data from fresh project database
- dataset_quantified - dataset with tranformed variables (created by transforming_variables.py)
- complete_dataset - dataset with two additinal variables (created by adding_additional_data.py)
- final_cleaned_dataset - final dataset used for model development (created by filling_empty_data.py)






