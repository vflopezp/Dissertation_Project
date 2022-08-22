import pandas as pd
import numpy as np
quantified_data = pd.read_excel('dataset_quantified.xlsx')

"""
replace unknown value with average of Approx Construction Cost of projects with 
engginering service cost being 25% bigger or smaller than of project with missing value
since there is only one value we will only produce solution for this single value
"""
missing_project_enginering_cost = list(quantified_data[quantified_data["Approx Construction Cost"]  == "unkown"]["cost"])[0]
costs_25_percent_of_missing_cost = quantified_data[quantified_data["cost"]
                                  .between(missing_project_enginering_cost * 0.75, 
                                           missing_project_enginering_cost * 1.25)]
costs_25_percent_of_missing_cost = costs_25_percent_of_missing_cost[costs_25_percent_of_missing_cost["cost"] != missing_project_enginering_cost]

costs_25_percent_of_missing_cost["Approx Construction Cost"].replace(' ', '',regex=True,inplace=True)
costs_25_percent_of_missing_cost["Approx Construction Cost"] = costs_25_percent_of_missing_cost["Approx Construction Cost"].astype(int)
replacment_const_cost = costs_25_percent_of_missing_cost["Approx Construction Cost"].mean()
quantified_data["Approx Construction Cost"].replace("unkown", replacment_const_cost, inplace=True)


# # convert construction cost to int
quantified_data["Approx Construction Cost"].replace(' ', '',regex=True,inplace=True)
quantified_data["Approx Construction Cost"] = quantified_data["Approx Construction Cost"].astype(np.int64)


# convert ZAR to GDP
quantified_data.loc[quantified_data["Currency"] == "ZAR", "Approx Construction Cost"] = quantified_data[quantified_data["Currency"] == "ZAR"]["Approx Construction Cost"] * 0.05
quantified_data.loc[quantified_data["Currency"] == "ZAR", "cost"] = quantified_data[quantified_data["Currency"] == "ZAR"]["cost"] * 0.05


# # fill missing values in Project manager’s experience (years)
quantified_data["Project manager’s experience (years)"].replace(np.nan, 5,regex=True,inplace=True)
quantified_data["Project manager’s experience (years)"].replace("unknown", 5,regex=True,inplace=True)
quantified_data["Project manager’s experience (years)"].replace(">10", 5,regex=True,inplace=True)

# # fill mising values team size
for missing_team_size_id in quantified_data[quantified_data["team size"]  == 0]["ProjectId"]:
    missing_project_enginering_cost = list(quantified_data[quantified_data["ProjectId"]  == missing_team_size_id]["cost"])[0]
    missing_project_multidiplinarity = list(quantified_data[quantified_data["ProjectId"]  == missing_team_size_id]["How many disciplines involved in project  team"])[0]
    
    missing_team_size = quantified_data[quantified_data["How many disciplines involved in project  team"]
                                  .between(missing_project_multidiplinarity * 0.75, 
                                           missing_project_multidiplinarity * 1.25)]
    
    missing_team_size = missing_team_size[missing_team_size["team size"] != 0]
    missing_team_size_found = missing_team_size["team size"].mean()
    # print(quantified_data[quantified_data["ProjectId"] == missing_team_size_id])
    quantified_data.loc[quantified_data["ProjectId"] == missing_team_size_id, 'team size'] = int(round(missing_team_size_found)),

    # quantified_data[quantified_data["ProjectId"] == missing_team_size_id]["team size"].replace(0, 
    #                                                                               int(round(missing_team_size_found)), 
    #                                                                               inplace=True)
    # print(df)

# delete index columns and id column
quantified_data.drop(columns=["Unnamed: 0.1", "Unnamed: 0", "ProjectId"], inplace=True)

# tranform currency to country 
quantified_data["Currency"].replace("ZAR", "South Africa", inplace=True, regex=True)
quantified_data["Currency"].replace("GBP", "United Kingdom", inplace=True, regex=True)

# create dummy variables
quantified_data = pd.get_dummies(quantified_data)



quantified_data.to_excel("final_cleaned_dataset.xlsx", index=False)