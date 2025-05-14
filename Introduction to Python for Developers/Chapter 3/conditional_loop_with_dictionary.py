courses = {'LLM Concepts': 'AI',
           'Introduction to Data Pipelines': 'Data Engineering',
           'AI Ethics': 'AI',
           'Introduction to dbt': 'Data Engineering',
           'Writing Efficient Python Code': 'Programming',
           'Introduction to Docker': 'Programming'}

for key, value in courses.items():
    if value == "AI":
        print(key, "is an AI course")
    elif value == "Programming":
        print(key, "is a Programming course")
    else:
        print(key, "is a Data Engineering course")
