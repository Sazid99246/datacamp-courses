course_ratings = {"LLM Concepts": 4.7, "Introduction to Data Pipelines": 4.75,
                  "AI Ethics": 4.62, "Introduction to dbt": 4.81}
course_completions = [97, 83, 121, 205, 56, 174, 92, 117, 164]
most_popular_course = "Introduction to dbt"

num_courses = len(course_ratings)
print(num_courses)

num_courses = len(course_completions)
print(num_courses)

title_length = len(most_popular_course)
print(title_length)