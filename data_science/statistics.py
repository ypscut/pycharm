__author__ = 'Administrator'

day_numbers = [1,2,3,4,5,6,7]
snail_crawl_length = [.5,2,5,10,1,.25,4]
cars_in_parking_lot = [5,6,4,2,1,7,8]

import matplotlib.pyplot as plt
plt.plot(day_numbers, snail_crawl_length)


plt.plot(day_numbers, cars_in_parking_lot)
plt.show()

survey_responses = ["none", "some", "a lot", "none", "a few", "none", "none"]
survey_scale = ["none", "a few", "some", "a lot"]
survey_numbers = [survey_scale.index(response) for response in survey_responses]
average_smoking = sum(survey_numbers) / len(survey_numbers)

gender = ["male", "female", "female", "male", "male", "female"]
savings = [1200, 5000, 3400, 2400, 2800, 4100]
male_savings_list = [savings[i] for i in range(0, len(gender)) if gender[i] == "male"]
female_savings_list = [savings[i] for i in range(0, len(gender)) if gender[i] == "female"]

male_savings = sum(male_savings_list) / len(male_savings_list)
female_savings = sum(female_savings_list) / len(female_savings_list)