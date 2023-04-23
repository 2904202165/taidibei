import pandas as pd
import matplotlib.pyplot as plt

# 读取招聘信息和求职信息
recruit_data = pd.read_excel('C:/Users/29042/PycharmProjects/pythonProject/result1-1.xlsx')
jobseeker_data = pd.read_excel('C:/Users/29042/PycharmProjects/pythonProject/result1-2.xlsx')

# 招聘信息画像
recruit_profile = pd.DataFrame()
recruit_profile['岗位名称'] = recruit_data['岗位名称']
recruit_profile['学历要求'] = recruit_data['学历要求']
recruit_profile['地点'] = recruit_data['工作地点']
recruit_profile['薪酬'] = recruit_data['薪资']

# 按照学历要求统计招聘数量和薪酬水平
recruit_by_education = recruit_data.groupby('学历要求')['岗位名称'].count()
salary_by_education = recruit_data.groupby('学历要求')['薪资'].mean()
plt.figure(figsize=(8, 5))
plt.subplot(1, 2, 1)
plt.bar(recruit_by_education.index, recruit_by_education.values)
plt.title('招聘数量')
plt.xticks(rotation=45)
plt.subplot(1, 2, 2)
plt.bar(salary_by_education.index, salary_by_education.values)
plt.title('平均薪资')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 求职者画像
jobseeker_profile = pd.DataFrame()
jobseeker_profile['岗位名称'] = jobseeker_data['求职意向岗位']
jobseeker_profile['薪资要求'] = jobseeker_data['期望月薪']
jobseeker_profile['学历'] = jobseeker_data['学历']
jobseeker_profile['工作经验'] = jobseeker_data['工作经验']

# 按照求职岗位统计求职者数量和薪资要求
jobseekers_by_job = jobseeker_data.groupby('求职意向岗位')['求职者姓名'].count()
salary_by_job = jobseeker_data.groupby('求职意向岗位')['期望月薪'].mean()
plt.figure(figsize=(8, 5))
plt.subplot(1, 2, 1)
plt.bar(jobseekers_by_job.index, jobseekers_by_job.values)
plt.title('求职者数量')
plt.xticks(rotation=45)
plt.subplot(1, 2, 2)
plt.bar(salary_by_job.index, salary_by_job.values)
plt.title('平均期望薪资')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
