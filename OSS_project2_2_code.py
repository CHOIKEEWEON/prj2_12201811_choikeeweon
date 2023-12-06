import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR


def sort_dataset(dataset_df):
	#TODO: Implement this function
	# dataframe을 연도 별로 sort
	sorted_df = dataset_df.sort_values(by='p_year')
	
	return sorted_df

def split_dataset(dataset_df):	
	#TODO: Implement this function
	# df.info()로 확인했을 때 numerical 컬럼들에는 null값이 없었기 때문에 전처리 x
	# 'salary' 컬럼을 label로, 나머지 컬럼들을 train으로 설정
	x = dataset_df.drop('salary', axis=1)
	y = dataset_df['salary'] * 0.001

	# index 0~1717: 2018년도, index 1718~1913: 2019년도로 train/test 데이터셋 분리
	X_train, X_test = x.iloc[:1718, :], x.iloc[1718:, :]
	Y_train, Y_test = y[:1718], y[1718:]
	
	return X_train, X_test, Y_train, Y_test

def extract_numerical_cols(dataset_df):
	#TODO: Implement this function
	# numerical colunms 추출
	num_cols = ['age', 'G', 'PA', 'AB', 'R', 'H', '2B', '3B', 'HR', 'RBI', 
            	'SB', 'CS', 'BB', 'HBP', 'SO', 'GDP', 'fly', 'war']
	extracted_df = dataset_df.loc[:, num_cols]
	
	return extracted_df
	

def train_predict_decision_tree(X_train, Y_train, X_test):
	#TODO: Implement this function
	# 의사 결정 트리 모델로 학습 후 test 데이터에 대해 추론 수행
	df_reg = DecisionTreeRegressor()
	df_reg.fit(X_train, Y_train)
 
	predictions = df_reg.predict(X_test)
	return predictions

def train_predict_random_forest(X_train, Y_train, X_test):
	#TODO: Implement this function
	# 랜덤포레스트 모델로 학습 후 test 데이터에 대해 추론 수행
	rf_reg = RandomForestRegressor()
	rf_reg.fit(X_train, Y_train)

	predictions = rf_reg.predict(X_test)
	return predictions

def train_predict_svm(X_train, Y_train, X_test):
	#TODO: Implement this function
	# StandardScaler와 SVM으로 구성된 파이프라인으로 모델 학습 후 test 데이터에 대해 추론 수행
	svm_pipe = make_pipeline(
		StandardScaler(),
		SVR()
	)
	svm_pipe.fit(X_train, Y_train)
	
	predictions = svm_pipe.predict(X_test)
	return predictions

def calculate_RMSE(labels, predictions):
	#TODO: Implement this function
	return np.sqrt(np.mean((labels - predictions)**2))

if __name__=='__main__':
	#DO NOT MODIFY THIS FUNCTION UNLESS PATH TO THE CSV MUST BE CHANGED.
	data_df = pd.read_csv('2019_kbo_for_kaggle_v2.csv')
	
	sorted_df = sort_dataset(data_df)	
	X_train, X_test, Y_train, Y_test = split_dataset(sorted_df)
	
	X_train = extract_numerical_cols(X_train)
	X_test = extract_numerical_cols(X_test)

	dt_predictions = train_predict_decision_tree(X_train, Y_train, X_test)
	rf_predictions = train_predict_random_forest(X_train, Y_train, X_test)
	svm_predictions = train_predict_svm(X_train, Y_train, X_test)
	
	print ("Decision Tree Test RMSE: ", calculate_RMSE(Y_test, dt_predictions))	
	print ("Random Forest Test RMSE: ", calculate_RMSE(Y_test, rf_predictions))	
	print ("SVM Test RMSE: ", calculate_RMSE(Y_test, svm_predictions))