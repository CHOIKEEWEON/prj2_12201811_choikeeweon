import pandas as pd


# Project 2-1 Data analysix with pandas
#
# 1) Print the top 10 players in hits (안타, H), batting average (타율, avg), homerun (홈런, HR), and on-
# base percentage (출루율, OBP) for each year from 2015 to 2018. (15 points)
def top10_players(dataset_df):
    data_2015 = dataset_df[dataset_df['p_year'] == 2015]
    data_2016 = dataset_df[dataset_df['p_year'] == 2016]
    data_2017 = dataset_df[dataset_df['p_year'] == 2017]
    data_2018 = dataset_df[dataset_df['p_year'] == 2018]
    
    # 타자 이름과 각 항목으로 컬럼 추출 후 기준 컬럼으로 sorting(내림차순) 후에 상위 10개 항목 출력
    print("============================================")
    print("top 10 players in hits for 2015")
    print(data_2015[['batter_name', 'H']].sort_values(by='H', ascending=False).iloc[:10, :])
    print("============================================")
    print("top 10 players in batting average for 2015")
    print(data_2015[['batter_name', 'avg']].sort_values(by='avg', ascending=False).iloc[:10, :])
    print("============================================")
    print("top 10 players in homerun for 2015")
    print(data_2015[['batter_name', 'HR']].sort_values(by='HR', ascending=False).iloc[:10, :])
    print("============================================")
    print("top 10 players in on-base percentage for 2015")
    print(data_2015[['batter_name', 'OBP']].sort_values(by='OBP', ascending=False).iloc[:10, :])

    print("============================================")
    print("top 10 players in hits for 2016")
    print(data_2016[['batter_name', 'H']].sort_values(by='H', ascending=False).iloc[:10, :])
    print("============================================")
    print("top 10 players in batting average for 2016")
    print(data_2016[['batter_name', 'avg']].sort_values(by='avg', ascending=False).iloc[:10, :])
    print("============================================")
    print("top 10 players in homerun for 2016")
    print(data_2016[['batter_name', 'HR']].sort_values(by='HR', ascending=False).iloc[:10, :])
    print("============================================")
    print("top 10 players in on-base percentage for 2016")
    print(data_2016[['batter_name', 'OBP']].sort_values(by='OBP', ascending=False).iloc[:10, :])
    
    print("============================================")
    print("top 10 players in hits for 2017")
    print(data_2017[['batter_name', 'H']].sort_values(by='H', ascending=False).iloc[:10, :])
    print("============================================")
    print("top 10 players in batting average for 2017")
    print(data_2017[['batter_name', 'avg']].sort_values(by='avg', ascending=False).iloc[:10, :])
    print("============================================")
    print("top 10 players in homerun for 2017")
    print(data_2017[['batter_name', 'HR']].sort_values(by='HR', ascending=False).iloc[:10, :])
    print("============================================")
    print("top 10 players in on-base percentage for 2017")
    print(data_2017[['batter_name', 'OBP']].sort_values(by='OBP', ascending=False).iloc[:10, :])

    print("============================================")
    print("top 10 players in hits for 2018")
    print(data_2018[['batter_name', 'H']].sort_values(by='H', ascending=False).iloc[:10, :])
    print("============================================")
    print("top 10 players in batting average for 2018")
    print(data_2018[['batter_name', 'avg']].sort_values(by='avg', ascending=False).iloc[:10, :])
    print("============================================")
    print("top 10 players in homerun for 2018")
    print(data_2018[['batter_name', 'HR']].sort_values(by='HR', ascending=False).iloc[:10, :])
    print("============================================")
    print("top 10 players in on-base percentage for 2018")
    print(data_2018[['batter_name', 'OBP']].sort_values(by='OBP', ascending=False).iloc[:10, :])

    return


# 2) Print the player with the highest war (승리 기여도) by position (cp) in 2018. (15 points)
# ▪ Position info. - 포수, 1루수, 2루수, 3루수, 유격수, 좌익수, 중견수, 우익수
def top_war_by_pos(dataset_df):
    # 2018년도 데이터만 추출
    data_2018 = dataset_df[dataset_df['p_year'] == 2018]

    # 'tp'가 '포수'인 행들만 추출 후 'war' 컬럼에 대해 최댓값인 인덱스 값으로 선수 정보 추출
    topwar_C = data_df.loc[data_2018[data_2018['tp'] == '포수']['war'].idxmax()]
    topwar_1B = data_df.loc[data_2018[data_2018['tp'] == '1루수']['war'].idxmax()]
    topwar_2B = data_df.loc[data_2018[data_2018['tp'] == '2루수']['war'].idxmax()]
    topwar_3B = data_df.loc[data_2018[data_2018['tp'] == '3루수']['war'].idxmax()]
    topwar_SS = data_df.loc[data_2018[data_2018['tp'] == '유격수']['war'].idxmax()]
    topwar_LF = data_df.loc[data_2018[data_2018['tp'] == '좌익수']['war'].idxmax()]
    topwar_CF = data_df.loc[data_2018[data_2018['tp'] == '중견수']['war'].idxmax()]
    topwar_RF = data_df.loc[data_2018[data_2018['tp'] == '우익수']['war'].idxmax()]

    print("============================================")
    print("the player with highest war by 포수 in 2018")
    print(topwar_C.loc[['batter_name', 'tp', 'war']])
    print("============================================")
    print("the player with highest war by 1루수 in 2018")
    print(topwar_1B.loc[['batter_name', 'tp', 'war']])
    print("============================================")
    print("the player with highest war by 2루수 in 2018")
    print(topwar_2B.loc[['batter_name', 'tp', 'war']])
    print("============================================")
    print("the player with highest war by 3루수 in 2018")
    print(topwar_3B.loc[['batter_name', 'tp', 'war']])
    print("============================================")
    print("the player with highest war by 유격수 in 2018")
    print(topwar_SS.loc[['batter_name', 'tp', 'war']])
    print("============================================")
    print("the player with highest war by 좌익수 in 2018")
    print(topwar_LF.loc[['batter_name', 'tp', 'war']])
    print("============================================")
    print("the player with highest war by 중견수 in 2018")
    print(topwar_CF.loc[['batter_name', 'tp', 'war']])
    print("============================================")
    print("the player with highest war by 우익수 in 2018")
    print(topwar_RF.loc[['batter_name', 'tp', 'war']])

    return


# 3) Among R (득점), H (안타), HR (홈런), RBI (타점), SB (도루), war (승리 기여도), avg (타율), OBP
# (출루율), and SLG (장타율), which has the highest correlation with salary (연봉)? (15 points)
# ▪ Implement code to calculate correlations and print the answer to the above question.
def calculate_top_corr(dataset_df):
    print("============================================")
    # R, H, HR, RBI, SB, war, avg, OBP, SLG과 salary의 상관관계를 계산하기 위해 컬럼 추출
    std_cols = ['R', 'H', 'HR', 'RBI', 'SB', 'war', 'avg', 'OBP', 'SLG', 'salary']
    corr_matrix = dataset_df.loc[:, std_cols].corr()

    # 10 x 10 corr_matrix에서 salary 행만 추출 후 salary 라벨의 값은 항상 1이기 때문에 drop 후 sorting한다.
    corr_with_salary = corr_matrix['salary'].drop('salary').sort_values(ascending=False)
    print("correlations with salary\n")
    print(corr_with_salary, '\n')

    top_idx = corr_with_salary.index[0]
    print(top_idx, "has the highest correlation with salary")
    print("============================================")

    return


if __name__=='__main__':
    data_df = pd.read_csv('2019_kbo_for_kaggle_v2.csv')
    
    top10_players(data_df)
    top_war_by_pos(data_df)
    calculate_top_corr(data_df)