import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.font_manager.fontManager.addfont(r'C:\Windows\Fonts\arial unicode ms.ttf')
matplotlib.rcParams['font.sans-serif'] = ['Arial Unicode MS']

# 读取招聘信息和求职信息
recruit_data = pd.read_excel('C:/Users/29042/PycharmProjects/pythonProject/result1-1.xlsx')
jobseeker_data = pd.read_excel('C:/Users/29042/PycharmProjects/pythonProject/result1-2.xlsx')

# 修改recruit_data和jobseeker_data两个DataFrame中的列名
recruit_data.rename(columns={'学历要求': '学历', '最低薪资': '最低薪资/月', '最高薪资': '最高薪资/月'},
                    inplace=True)
jobseeker_data.rename(columns={'求职岗位': '期望岗位', '期望薪资/月': '最高薪资'}, inplace=True)

# 统计招聘信息中的薪酬和学历要求分布情况
recruit_by_education = recruit_data.groupby('学历')['招聘人数'].sum()
salary_by_education = recruit_data.groupby('学历')['最低薪资/月'].mean()
plt.figure(figsize=(8, 5))
plt.subplot(1, 2, 1)
plt.bar(recruit_by_education.index, recruit_by_education.values)
plt.title('招聘人数分布（按学历）')
plt.xticks(rotation=45)
plt.subplot(1, 2, 2)
plt.bar(salary_by_education.index, salary_by_education.values)
plt.title('薪酬分布（按学历）')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 按照求职岗位统计求职者数量和薪资要求
jobseekers_by_job = jobseeker_data.groupby('期望岗位')['期望岗位'].count()
salary_by_job = jobseeker_data.groupby('期望岗位')['最高薪资'].mean()

# 求职者画像
jobseeker_profile = pd.DataFrame()
jobseeker_profile['期望岗位'] = jobseeker_data['期望岗位'].str.split(' ').str[0].str.strip()
jobseeker_profile['最高薪资'] = jobseeker_data['最高薪资']
jobseeker_profile['学历'] = jobseeker_data['学历']

# 统计求职者画像中的期望薪资和学历分布情况
plt.figure(figsize=(8, 5))
plt.subplot(1, 2, 1)
plt.hist(jobseeker_profile['最高薪资'], bins=10, alpha=0.8)
plt.title('期望薪资分布情况')
plt.xlabel('期望薪资')
plt.ylabel('数量')
plt.subplot(1, 2, 2)
jobseeker_profile['学历'].value_counts().plot(kind='bar', width=0.5, alpha=0.8)
plt.title('学历分布情况')
plt.xlabel('学历')
plt.ylabel('数量')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# 按照学历要求统计招聘人数和平均薪酬水平
recruit_by_education = recruit_data.groupby('学历')['招聘人数'].sum()
salary_by_education = recruit_data.groupby('学历')['最低薪资/月'].mean()

# 绘制招聘信息中学历要求的招聘人数和薪酬水平分布图
plt.figure(figsize=(8, 5))
plt.subplot(1, 2, 1)
plt.bar(recruit_by_education.index, recruit_by_education.values)
plt.title('招聘人数（按学历）')
plt.xticks(rotation=45)
plt.subplot(1, 2, 2)
plt.bar(salary_by_education.index, salary_by_education.values)
plt.title('薪酬平均值（按学历）')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 统计求职者画像中的工作经验分布情况
jobseeker_profile['工作经验'] = jobseeker_data['经验'].str.extract('(\d+)')
jobseeker_profile['工作经验'] = jobseeker_profile['工作经验'].fillna(0).astype('int')
plt.hist(jobseeker_profile['工作经验'], bins=5, alpha=0.8, rwidth=0.8)
plt.title('工作经验分布情况')
plt.xlabel('工作经验（年）')
plt.ylabel('数量')
plt.tight_layout()
plt.show()
