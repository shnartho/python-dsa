def greedy_activity_selection(activities):
    activities.sort(key=lambda x:x[1]) 
    selected_activities = [activities[0]]

    for activity in activities[1:]:
        if activity[0] >= selected_activities[-1][-1]:
            selected_activities.append(activity)
    return selected_activities

activities = [(1,3), (4,7),(2,5), (6,9), (8,10)]
selected = greedy_activity_selection(activities)
print("Selected activities:", selected)