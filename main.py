import pandas as pd
import numpy as np
import streamlit as st

#df=pd.read_csv("D:/University/3rd Year/2nd Semester/ST3082 Statistical Learning/Project APP/pythonProject/mydata.csv")
#df1=pd.read_csv("D:/University/3rd Year/2nd Semester/ST3082 Statistical Learning/Project APP/pythonProject/mydata.csv")
#Y=df['actual_productivity']
#df=df.drop(columns=['actual_productivity','date_num', 'date','team'], axis=1)
#df=pd.get_dummies(df, columns=['department', 'day','quarter'])
#print(df.columns)
#print(Y)

#Stream Lit Components
st.title("Garment Worker Productivty Prediction")

st.sidebar.header('User Input Parameters')

def user_input_features():
    targeted_productivity= st.sidebar.slider('Targetted Productivty', 0.00, 0.51,1.00)
    smv = st.sidebar.slider('Standard Minute Value', 0.00, 25.00,50.00)
    wip = st.sidebar.slider('Work in Progress', 0.00, 500.00,1500.00)
    over_time = st.sidebar.slider('Expected Overtime Pay', 0.00, 500.00, 1500.00)
    incentive= st.sidebar.slider('Expected Incentive Pay', 0.00, 500.00, 1500.00)
    idle_time = st.sidebar.slider('Expected Idle Time', 0.00, 5.00,12.00)
    no_of_workers = st.sidebar.slider('No of workers at the task', 0.00, 30.00, 60.00)
    idle_men = st.sidebar.selectbox("Expected Number of Idle Men", options=(0,1,2,3,4,5))
    no_of_style_changes=st.sidebar.selectbox("Expected Number of style changes", options=(0,1,2,3))
    department = st.sidebar.selectbox("Department", options=("Sewing","Finishing"))
    day = st.sidebar.selectbox("Workday of the Week", options=("Monday","Tuesday","Wednesday","Thursday","Saturday","Sunday"))
    quarter = st.sidebar.selectbox("Quarter of the Month",options=("1st Quarter","2nd Quarter","3rd Quarter","4th Quarter"))

    if department=="Sewing":
        department_sewing=1
        department_finishing=0
    else:
        department_sewing=0
        department_finishing=1

    if day=="Monday":
        day_Monday=1
        day_Saturday=day_Sunday=day_Thursday=day_Tuesday=day_Wednesday=0
    elif day=="Tuesday":
        day_Tuesday=1
        day_Saturday=day_Sunday=day_Thursday=day_Monday=day_Wednesday=0
    elif day=="Wednesday":
        day_Wednesday=1
        day_Saturday=day_Sunday=day_Thursday=day_Monday=day_Tuesday=0
    elif day=="Thursday":
        day_Thursday=1
        day_Saturday=day_Sunday=day_Tuesday=day_Monday=day_Wednesday=0
    elif day=="Saturday":
        day_Saturday=1
        day_Thursday=day_Sunday=day_Tuesday=day_Monday=day_Wednesday=0
    else:
        day_Sunday=1
        day_Thursday=day_Saturday=day_Tuesday=day_Monday=day_Wednesday=0

    if quarter=="1st Quarter":
        quarter_1=1
        quarter_2=quarter_3=quarter_4=0
    elif quarter=="2nd Quarter":
        quarter_2=1
        quarter_1=quarter_3=quarter_4=0
    elif quarter=="3rd Quarter":
        quarter_3=1
        quarter_1=quarter_2=quarter_4=0
    else:
        quarter_4=1
        quarter_1=quarter_2=quarter_3=0

    data = {'targeted_productivity': targeted_productivity,
            'smv': smv,
            'wip': wip,
            'over_time': over_time,
            'incentive': incentive,
            'idle_time': idle_time,
            'idle_men': idle_men,
            'no_of_style_change': no_of_style_changes,
            'no_of_workers': no_of_workers,
            'department_finishing': department_finishing,
            'department_sewing': department_sewing,
            'day_Monday': day_Monday,
            'day_Saturday': day_Saturday,
            'day_Sunday': day_Sunday,
            'day_Thursday': day_Thursday,
            'day_Tuesday': day_Tuesday,
            'day_Wednesday': day_Wednesday,
            'quarter_1': quarter_1,
            'quarter_2': quarter_2,
            'quarter_3': quarter_3,
            'quarter_4': quarter_4}
    features = pd.DataFrame(data, index=[0])

    if 'clicked' not in st.session_state:
        st.session_state.clicked = False

    def click_button():
        st.session_state.clicked = True

    st.sidebar.button('Click me', on_click=click_button)
    if st.session_state.clicked:
        st.write('Button clicked!')

    return features

df2 = user_input_features()