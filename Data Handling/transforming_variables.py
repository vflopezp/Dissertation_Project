import pandas as pd


data = pd.read_excel('complete_dataset.xlsx')

# map Contract type
data["Contract type"] = data["Contract type"].map({'Fixed Fee': 1, 'Time Based': 2})
print(data["Contract type"])

# map Scope definition adequacy
scope_def_ade_mapping = {
    "Very Poor Scope" : 1,
    "Poor Scope" : 2,
    "Moderate Scope" : 3,
    "Good Scope" : 4,
    "Very Good Scope" : 5
}

data["Scope definition adequacy"] = data["Scope definition adequacy"].map(scope_def_ade_mapping)

# Map Clients’ attitude toward design changes
client_attitude_map = {
    "Very Few Changes / Tight Control" : 1,
    "Few Changes / Good Control" : 2,
    "Occasional Changes / Moderate Control" :3,
    "Frequent Changes / Little Control" : 4,
    "Very Frequent Changes / No Control" : 5
}

data["Clients’ attitude toward design changes"] = data["Clients’ attitude toward design changes"].map(client_attitude_map)

# Client’s level of experience
client_level_map = {
    "Very Low" : 1,
    "Low" : 2,
    "Moderate" : 3,
    "High" : 4,
    "Very High" : 5
}

data["Client’s level of experience"] = data["Client’s level of experience"].map(client_level_map)

# Project phases
project_phases_map = {
    "Design Only" : 1,
    "Construction Only" : 2,
    "Design & Construction" : 3
}

data["Project phases"] = data["Project phases"].map(project_phases_map)

# Level of complexity of the design
level_complexity_map = {
    "Low Complexity" : 1,
    "Moderate Complexity" : 2,
    "High Complexity" : 3
}

data["Level of complexity of the design"] = data["Level of complexity of the design"].map(level_complexity_map)

# Level of adoption of computer-aided design technologies
level_technology_map = {
    "Very low" : 1,
    "Low" : 2,
    "Moderate" : 3,
    "High" : 4,
    "Very high" : 5
}

data["Level of adoption of computer-aided design technologies"] = data["Level of adoption of computer-aided design technologies"].map(level_technology_map)

# Level of communication among the project team
level_communcation_map = {
    "Very low" : 1,
    "Low" : 2,
    "Moderate" : 3,
    "High" : 4,
    "Very high" : 5
}

data["Level of communication among the project team"] = data["Level of communication among the project team"].map(level_communcation_map)

data.to_excel("dataset_quantified.xlsx")
