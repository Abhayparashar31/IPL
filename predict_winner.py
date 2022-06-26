import streamlit as st
import pickle
import pandas as pd
import random


def app():
    
    st.markdown(''' 
    <center>―――――――――――――――――――――――――――――――――――――――――――――</center>
    <h1 style='text-align:center;'> IPL Winner Prediction Based On Second Innings </h1> 
    <center>―――――――――――――――――――――――――――――――――――――――――――――</center>
    <br>
    ''',unsafe_allow_html=True)
    


    ### Load Saved Model
    model = pickle.load(open('predict_match_winner_2nd_innings.pkl','rb'))

    TEAMS = ['Chennai Super Kings','Delhi Capitals','Kings XI Punjab',
    'Kolkata Knight Riders','Mumbai Indians','Rajasthan Royals',
    'Royal Challengers Bangalore','Sunrisers Hyderabad']
    
    ### DATA
    # [bat_team, bowl_team, cities, runs_left, ball_left ,wickets_left,total_runs,crr,rrr]


    ### Batting Team & Bowling Team
    col1, col2 = st.columns(2)
    with col1:
        batting_team = st.selectbox('Batting Team At The Moment',random.choices(TEAMS, k = len(TEAMS))) ## randomizing choices
    with col2:
        bowling_team = st.selectbox('Bowling Team At The Moment',random.choices(TEAMS, k = len(TEAMS)))
    
    ### Cities
    cities = ['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
       'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
       'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
       'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
       'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
       'Sharjah', 'Mohali', 'Bengaluru']
    
    city = st.selectbox("Choose The Host City For The Match.",sorted(cities))

    ### Target
    target = st.number_input('Target Score Need To Chased (First Playing Team Score)',value=156)


    current_score = st.number_input('Current Score of The Playing Team.',value=100)

    col3, col4 = st.columns(2)
    with col3:
        overs_left = st.number_input('Overs Left To Achieve The Target',value=7)
        overs_completed = 20-overs_left
    with col4:
        wickets = st.number_input('Wickets Lost By Playing Team',value=4)

    
    runs_left = target - current_score
    balls_left = 120 - (overs_completed*6)
    wickets_left = 10-wickets

    crr = current_score/overs_completed
    rrr = (runs_left*6)/balls_left

    data = pd.DataFrame({'batting_team':[batting_team],
    'bowling_team':[bowling_team],
    'city':[city],
    'runs_left':[runs_left],
    'ball_left':[balls_left],
    'wickets_left':[wickets_left],
    'total_runs':[target],
    'crr':[crr],
    'rrr':[rrr]})

    st.write('---')
    st.write('Encoded Input Data:',data)

    if st.button('Predict Winner'):
        result = model.predict_proba(data)
        loss = result[0][0]
        win = result[0][1]
        st.subheader(batting_team + "- " + str(round(win*100)) + "%")
        st.subheader(bowling_team + "- " + str(round(loss*100)) + "%")





