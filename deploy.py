import streamlit as st
import numpy as np
import joblib
import pandas as pd
import numpy as np
import streamlit as st

Model = joblib.load("Model.pkl")
Inputs = joblib.load("inputs.pkl")



def prediction(Age, BusinessTravel, DailyRate, Department, DistanceFromHome, Education, EducationField, 
               EnvironmentSatisfaction, Gender, HourlyRate, JobInvolvement, JobLevel, JobRole, 
               JobSatisfaction, MaritalStatus, MonthlyIncome, MonthlyRate, NumCompaniesWorked, 
               OverTime, PercentSalaryHike, PerformanceRating, RelationshipSatisfaction, StockOptionLevel, 
               TotalWorkingYears, TrainingTimesLastYear, WorkLifeBalance, YearsAtCompany, 
               YearsInCurrentRole, YearsSinceLastPromotion, YearsWithCurrManager):
    
    
    # Create a DataFrame and fill in the provided values
    df = pd.DataFrame(columns=Inputs)
    df.at[0, "Age"] = Age
    df.at[0, "BusinessTravel"] = BusinessTravel
    df.at[0, "DailyRate"] = DailyRate
    df.at[0, "Department"] = Department
    df.at[0, "DistanceFromHome"] = DistanceFromHome
    df.at[0, "Education"] = Education
    df.at[0, "EducationField"] = EducationField
    df.at[0, "EnvironmentSatisfaction"] = EnvironmentSatisfaction
    df.at[0, "Gender"] = Gender
    df.at[0, "HourlyRate"] = HourlyRate
    df.at[0, "JobInvolvement"] = JobInvolvement
    df.at[0, "JobLevel"] = JobLevel
    df.at[0, "JobRole"] = JobRole
    df.at[0, "JobSatisfaction"] = JobSatisfaction
    df.at[0, "MaritalStatus"] = MaritalStatus
    df.at[0, "MonthlyIncome"] = MonthlyIncome
    df.at[0, "MonthlyRate"] = MonthlyRate
    df.at[0, "NumCompaniesWorked"] = NumCompaniesWorked
    df.at[0, "OverTime"] = OverTime
    df.at[0, "PercentSalaryHike"] = PercentSalaryHike
    df.at[0, "PerformanceRating"] = PerformanceRating
    df.at[0, "RelationshipSatisfaction"] = RelationshipSatisfaction
    df.at[0, "StockOptionLevel"] = StockOptionLevel
    df.at[0, "TotalWorkingYears"] = TotalWorkingYears
    df.at[0, "TrainingTimesLastYear"] = TrainingTimesLastYear
    df.at[0, "WorkLifeBalance"] = WorkLifeBalance
    df.at[0, "YearsAtCompany"] = YearsAtCompany
    df.at[0, "YearsInCurrentRole"] = YearsInCurrentRole
    df.at[0, "YearsSinceLastPromotion"] = YearsSinceLastPromotion
    df.at[0, "YearsWithCurrManager"] = YearsWithCurrManager
    
    # Predict the result
    result = Model.predict(df)[0]
    
    return result

def Main():
    st.title("Employee Turnover Prediction")
    
    Age = st.slider("Age", min_value=18, max_value=60, step=1, value=25)
    BusinessTravel = st.selectbox("Business Travel", ["Non-Travel", "Travel_Rarely", "Travel_Frequently"])
    DailyRate = st.slider("Daily Rate", min_value=102 , max_value=1499, step=10, value=200)
    Department = st.selectbox("Department", ['Sales','Research & Development', 'Human Resources'])
    DistanceFromHome = st.slider("Distance From Home", min_value=1, max_value=29, step=1, value=5)
    Education = st.selectbox("Education",  [1, 2, 3, 4,5])
    EducationField = st.selectbox("Education Field", ['Life Sciences', 'Other', 'Medical' ,'Marketing', 'Technical Degree' ,'Human Resources'])
    EnvironmentSatisfaction = st.selectbox("Environment Satisfaction", [1, 2, 3, 4])
    Gender = st.selectbox("Gender", ["Male", "Female"])
    HourlyRate = st.slider("Hourly Rate", min_value=30, max_value=100, step=1, value=30)
    JobInvolvement = st.selectbox("Job Involvement", [1, 2, 3, 4])
    JobLevel = st.selectbox("Job Level", [1, 2, 3, 4, 5])
    JobRole = st.selectbox("Job Role", ['Sales Executive' ,'Research Scientist', 'Laboratory Technician'
 ,'Manufacturing Director' ,'Healthcare Representative' ,'Manager',
 'Sales Representative' ,'Research Director', 'Human Resources'])
    JobSatisfaction = st.selectbox("Job Satisfaction", [1, 2, 3, 4])
    MaritalStatus = st.selectbox("Marital Status", ['Single', 'Married', 'Divorced'])
    MonthlyIncome = st.slider("Monthly Income", min_value=1009, max_value=19999, step=100, value=4000)
    MonthlyRate = st.slider("Monthly Rate", min_value=2094 , max_value=26999, step=100, value=2000)
    NumCompaniesWorked = st.slider("Number of Companies Worked", min_value=0, max_value=9, step=1, value=5)
    OverTime = st.selectbox("OverTime", ["No", "Yes"])
    PercentSalaryHike = st.slider("Percent Salary Hike", min_value=11, max_value=25, step=1, value=10)
    PerformanceRating = st.selectbox("Performance Rating", [ 3, 4])
    RelationshipSatisfaction = st.selectbox("Relationship Satisfaction", [1, 2, 3, 4])
    StockOptionLevel = st.selectbox("Stock Option Level", [0, 1, 2, 3])
    TotalWorkingYears = st.slider("Total Working Years", min_value=1, max_value=50, step=1, value=5)
    TrainingTimesLastYear = st.slider("Training Times Last Year", min_value=0, max_value=6, step=1, value=2)
    WorkLifeBalance = st.selectbox("Work Life Balance", [1, 2, 3, 4])
    YearsAtCompany = st.slider("Years at Company", min_value=0, max_value=40, step=1, value=5)
    YearsInCurrentRole = st.slider("Years in Current Role", min_value=0, max_value=18, step=1, value=2)
    YearsSinceLastPromotion = st.slider("Years Since Last Promotion", min_value=0, max_value=15, step=1, value=2)
    YearsWithCurrManager = st.slider("Years with Current Manager", min_value=0, max_value=17, step=1, value=3)
    
    if st.button("Predict"):
        result = prediction(Age, BusinessTravel, DailyRate, Department, DistanceFromHome, Education, 
                            EducationField, EnvironmentSatisfaction, Gender, HourlyRate, JobInvolvement, 
                            JobLevel, JobRole, JobSatisfaction, MaritalStatus, MonthlyIncome, MonthlyRate, 
                            NumCompaniesWorked, OverTime, PercentSalaryHike, PerformanceRating, 
                            RelationshipSatisfaction, StockOptionLevel, TotalWorkingYears, 
                            TrainingTimesLastYear, WorkLifeBalance, YearsAtCompany, YearsInCurrentRole, 
                            YearsSinceLastPromotion, YearsWithCurrManager)
        
        list_result = ["Rejected", "Accepted"]
        st.text(f"Your result is: {list_result[result]}")

Main()