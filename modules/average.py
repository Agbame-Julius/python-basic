import statistics as st

grades = [50, 60, 89, 90, 79, 30]
average_grade = st.mean(grades)
median_grade = st.median(grades)
print(f"The average grade is {average_grade:.2f}")
print(f"The median grade is {median_grade}")
