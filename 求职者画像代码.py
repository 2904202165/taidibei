import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
# 读取招聘信息和求职信息
recruit_data = pd.read_excel('C:/Users/29042/PycharmProjects/pythonProject/result1-1.xlsx')
jobseeker_data = pd.read_excel('C:/Users/29042/PycharmProjects/pythonProject/result1-2.xlsx')

# 修改recruit_data和jobseeker_data两个DataFrame中的列名
recruit_data.rename(columns={'招聘信息ID': '序号', '学历要求': '学历', '最低薪资': '最低薪资/月', \
                             '最高薪资': '最高薪资/月', '招聘人数': '招聘人数/职位', '招聘发布时间': '发布时间'}, inplace=True)
jobseeker_data.rename(columns={'求职岗位': '期望岗位', '期望月薪': '期望薪资/月', '工作经验': '经验', '职位福利': '福利'}, inplace=True)

# 按照学历要求统计招聘数量和薪酬水平
recruit_by_education = recruit_data.groupby('学历')['招聘人数/职位'].sum()
salary_by_education = recruit_data.groupby('学历')['最低薪资/月'].mean()
plt.figure(figsize=(8, 5))
plt.subplot(1, 2, 1)
plt.bar(recruit_by_education.index, recruit_by_education.values)
plt.title('招聘人数/职位')
plt.xticks(rotation=45)
plt.subplot(1, 2, 2)
plt.bar(salary_by_education.index, salary_by_education.values)
plt.title('平均薪资/月')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 求职者画像
jobseeker_profile = pd.DataFrame()
jobseeker_profile['期望岗位'] = jobseeker_data['期望岗位']
jobseeker_profile['期望薪资/月'] = jobseeker_data['最高薪资']
jobseeker_profile['学历'] = jobseeker_data['学历']
jobseeker_profile['经验'] = jobseeker_data['经验']

# 按照求职岗位统计求职者数量和薪资要求
jobseekers_by_job = jobseeker_data.groupby('期望岗位')['期望岗位'].count()
salary_by_job = jobseeker_data.groupby('期望岗位')['最高薪资'].mean()
plt.figure(figsize=(8, 5))
plt.subplot(1, 2, 1)
plt.bar(jobseekers_by_job.index, jobseekers_by_job.values)
plt.title('求职者数量')
plt.xticks(rotation=45)
plt.subplot(1, 2, 2)
plt.bar(salary_by_job.index, salary_by_job.values)
plt.title('平均期望薪资/月')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
