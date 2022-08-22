import pandas as pd
import numpy as np

all_found_data = pd.read_excel('company_relevant_data.xlsx')
survey_data = pd.read_excel('data_survey.xlsx')



# Plrease note the timesheet.csv is too big for github and can be found following this link: https://drive.google.com/file/d/1nylqIDJoRCxpk6StnVVTYsB5UhlUdk0l/view?usp=sharing
work_times = pd.read_csv("./timesheet_data.csv")

projects_with_data = survey_data.loc[survey_data['ProjectId'].isin(all_found_data._id)]

# add cost column
cost_mapping = dict(zip(all_found_data._id, all_found_data.totalActualCost))
projects_with_data["cost"] = projects_with_data["ProjectId"].map(cost_mapping)

# calucalte missing costs
missing_costs_projects = projects_with_data[projects_with_data['cost'].isnull()]["ProjectId"]
for id in missing_costs_projects:
    costs_from_work_time = work_times.loc[work_times['projectId'] == id]
    projects_with_data.loc[projects_with_data.ProjectId == id, 'cost'] = costs_from_work_time["cost"].sum()

number_of_workers_dict = {}
# add number of team members
for id in projects_with_data['ProjectId']:
    only_project_work = work_times.loc[work_times['projectId'] == id]
    unquie_works = only_project_work["_p_employee"].unique()
    number_of_workers_dict[id] = len(unquie_works)
    

projects_with_data["team size"] = projects_with_data["ProjectId"].map(number_of_workers_dict)

# add intensity 
# calculate total hours and divide by number of weeks to get average per week
# then divide by number of people in team to get average hour per week per member of team
hours_per_week_per_emploeyee_dict = {}
for id in projects_with_data['ProjectId']:
    only_project_work = work_times.loc[work_times['projectId'] == id]
    only_project_work['weekStart']= pd.to_datetime(only_project_work['weekStart'])

    
    total_hours = only_project_work["hours"].sum()
    total_amount_of_time = only_project_work['weekStart'].max() - only_project_work['weekStart'].min()
    try:
        
        total_weeks = int(total_amount_of_time / np.timedelta64(1, 'W'))
        number_of_team_members = len(only_project_work["_p_employee"].unique())
        
        average_per_week = total_hours / total_weeks
        hours_per_week_per_emploeyee_dict[id] = average_per_week / number_of_team_members
    except:
        hours_per_week_per_emploeyee_dict[id] = 0

projects_with_data["intensity"] = projects_with_data["ProjectId"].map(hours_per_week_per_emploeyee_dict)

projects_with_data.to_excel("complete_dataset.xlsx")
