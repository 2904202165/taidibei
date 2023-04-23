import pandas as pd
import numpy as np
from numpy.linalg import norm


# 构建技能要求向量和权重向量
skills = ['C++', 'Java', 'Python', 'Machine Learning', 'Data Mining', 'Communication']
weights = [0.2, 0.2, 0.2, 0.15, 0.15, 0.1]
skill_req = np.array([0.9, 0.8, 0.7, 0.6, 0.5, 0.4])  # 技能要求向量

def calc_similarity(s, r):
    """
    计算求职者技能掌握情况和岗位技能要求之间的匹配度
    :param s: list, 求职者技能掌握情况向量
    :param r: list, 岗位技能要求向量
    :return: float, 匹配度
    """
    s_vec = np.array(s)
    r_vec = np.array(r)
    sim = np.dot(s_vec, r_vec) / (norm(s_vec) * norm(r_vec))
    return sim

# 读取求职者和招聘信息数据
try:
    candidates = pd.read_csv('C:/Users/29042/PycharmProjects/pythonProject/result1-1.csv.csv')
    recruits = pd.read_csv('C:/Users/29042/PycharmProjects/pythonProject/result1-2.csv.csv')
except FileNotFoundError:
    print("数据文件不存在，请确认文件路径是否正确。")
    exit(-1)
except pd.errors.EmptyDataError:
    print("数据文件中没有数据，请检查数据文件是否为空。")
    exit(-1)
# 计算每个求职者和每条招聘信息的匹配度和满意度，并记录非0匹配度的求职者和非0满意度的招聘信息
matched_candidates = {}
satisfied_recruits = {}
for _, recruit_info in recruits.iterrows():
    recruited_skills = recruit_info[skills].values.astype(float)
    # 计算匹配度
    recruit_similarities = {}
    for _, candidate_info in candidates.iterrows():
        candidate_skills = candidate_info[skills].values.astype(float)
        sim = calc_similarity(candidate_skills, recruited_skills)
        if sim > 0:
            recruit_similarities[candidate_info['ID']] = sim
    if len(recruit_similarities) > 0:
        matched_candidates[recruit_info['ID']] = recruit_similarities
    # 计算满意度
    recruit_scores = {}
    for _, candidate_info in candidates.iterrows():
        candidate_skills = candidate_info[skills].values.astype(float)
        score = weights.dot(candidate_skills * recruited_skills)
        if score > 0:
            recruit_scores[candidate_info['ID']] = score
    if len(recruit_scores) > 0:
        satisfied_recruits[recruit_info['ID']] = recruit_scores

# 输出非0匹配度的求职者和非0满意度的招聘信息
matched_df = pd.DataFrame.from_dict(matched_candidates, orient='index')
matched_df.index.name = 'Recruit ID'
long_matched_df = pd.melt(matched_df.reset_index(), id_vars=['Recruit ID'], var_name='Candidate ID',
                           value_name='Matching Degree')
matched_df = long_matched_df[long_matched_df['Matching Degree'] > 0].sort_values(by=['Recruit ID', 'Matching Degree'], ascending=[True, False])
matched_df.to_csv('result3-1.csv', index=False)

satisfied_df = pd.DataFrame.from_dict(satisfied_recruits, orient='index')
satisfied_df.index.name = 'Candidate ID'
long_satisfied_df = pd.melt(satisfied_df.reset_index(), id_vars=['Candidate ID'], var_name='Recruit ID',
                           value_name='Satisfaction Score')
satisfied_df = long_satisfied_df[long_satisfied_df['Satisfaction Score'] > 0].sort_values(by=['Candidate ID', 'Satisfaction Score'], ascending=[True, False])
satisfied_df.to_csv('result3-2.csv', index=False)
