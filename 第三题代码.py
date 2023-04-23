import numpy as np
import pandas as pd

# 读取数据文件
try:
    candidates = pd.read_csv('C:/Users/29042/PycharmProjects/pythonProject/result1-1.csv.csv')
    recruits = pd.read_csv('C:/Users/29042/PycharmProjects/pythonProject/result1-2.csv.csv')
except FileNotFoundError:
    print("数据文件不存在，请确认文件路径是否正确。")
    exit(-1)
except pd.errors.EmptyDataError:
    print("数据文件中没有数据，请检查数据文件是否为空。")
    exit(-1)

# 将 '不限'、'经验不限' 和时间范围字符串替换为 nan
candidates.replace(['不限', '经验不限', '1-3年', '3-5年', '5-10年','5-7年','7年以上','互联网','计算机软件'], np.nan, inplace=True)
recruits.replace(['不限', '经验不限', '1-3年', '3-5年', '5-10年','5-7年','7年以上','互联网','计算机软件'], np.nan, inplace=True)

# 构建候选人能力矩阵和招聘人员能力矩阵，并计算匹配度和满意度
skills = ['经验要求', '学历要求', '最低薪资', '最高薪资', '招聘人数', '营业范畴']
candidates_skills = candidates[skills].values.astype(float)
candidates_min_skills = candidates['Minimum'].values.astype(float)
recruited_skills = []
for idx, recruit_info in recruits.iterrows():
    recruited_skills.append(recruit_info[skills].values.astype(float))
recruited_skills = np.array(recruited_skills)

matching_matrix = recruited_skills @ candidates_skills.T

matching_degree = []
for i in range(len(matching_matrix)):
    if np.any(np.isnan(matching_matrix[i])) or np.any(matching_matrix[i] < recruits.iloc[i].Requirements):
        matching_degree.append(0)
    else:
        matching_degree.append(np.nanmean(matching_matrix[i] * recruits.iloc[i][skills]))
matching_degree = np.array(matching_degree)

satisfaction_degree = []
for i in range(len(matching_matrix.T)):
    max_matching_index = np.nanargmax(matching_matrix.T[i])
    if np.any(np.isnan(matching_matrix.T[i])) or np.any(matching_matrix.T[i][max_matching_index] < candidates_min_skills[i]):
        satisfaction_degree.append(0)
    else:
        satisfaction_degree.append(np.nanmean(matching_matrix.T[i] * candidates.iloc[i][skills]))
satisfaction_degree = np.array(satisfaction_degree)

# 选取满足条件的数据，分别输出为结果文件
resul3_1 = pd.DataFrame()
resul3_2 = pd.DataFrame()
for idx, recruit_info in recruits.iterrows():
    if matching_degree[idx] > 0:
        resul3_1 = resul3_1.append(pd.Series({
            "Name": recruit_info.Name,
            "Matching Degree": matching_degree[idx]
        }), ignore_index=True)
for idx, candidate_info in candidates.iterrows():
    if satisfaction_degree[idx] > 0:
        resul3_2 = resul3_2.append(pd.Series({
            "Name": candidate_info.Name,
            "Satisfaction Degree": satisfaction_degree[idx]
        }), ignore_index=True)

resul3_1.sort_values(by="Matching Degree", ascending=False, inplace=True)
resul3_2.sort_values(by="Satisfaction Degree", ascending=False, inplace=True)

resul3_1.to_csv("result3-1.csv", index=False)
resul3_2.to_csv("result3-2.csv", index=False)
print("结果已经保存到 result3-1.csv 和 result3-2.csv 文件中。")
