import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import pandas as pd

import ipl_eda

def app():
    matches = pd.read_csv('matches.csv')
    matches_lt = ipl_eda.latest_teams(matches,['team1','team2','toss_winner','winner'])
    deliveries = pd.read_csv('deliveries.csv')
    deliveries_latest = ipl_eda.latest_teams(deliveries,['batting_team','bowling_team'])


    st.header('IPL Analysis: Batsman Vs Bowler')

    Batsman = deliveries['batsman'].unique().tolist()
    Bowler = deliveries['bowler'].unique().tolist()

    c1,c2 = st.columns(2)
    with c1:
        batsman = st.selectbox("Choose Batsman",Batsman)    
    with c2:
        bowler = st.selectbox("Choose Bowler",Bowler)

    Analyze = st.button('Analyze')
    if Analyze:

        st. markdown(f"<h4 style='text-align: center; color: white;'> {batsman} vs {bowler} </h4>", unsafe_allow_html=True)

        head_to_head = deliveries[(deliveries['batsman']==batsman) & (deliveries['bowler']==bowler)]
        if len(head_to_head) != 0: 
            st. markdown(f"<h6 style='text-align: center; color: white;'> Head to Head Meet </h6>", unsafe_allow_html=True)
            st.dataframe(head_to_head[['match_id','batting_team','bowling_team','over','batsman','non_striker','bowler','total_runs']])

            ##################################################
            ########### BASIC INFO ###########################
            ##################################################
            total_bowls = len(head_to_head)
            total_runs = head_to_head['total_runs'].sum()
            sixes = head_to_head[head_to_head['batsman_runs']==6].count()[0]
            fours = head_to_head[head_to_head['batsman_runs']==4].count()[0]
            dot_balls = head_to_head[head_to_head['batsman_runs']==0].count()[0]
            wide_balls = head_to_head[head_to_head['wide_runs']>0].count()[0]




            df = pd.DataFrame(columns=['info',f'{batsman} vs {bowler}'])
            df['info'] = ['Total Bowls Bowled','Total Runs','Six','Fours','Dot Balls','Wide Balls']

            df[f'{batsman} vs {bowler}'] = [total_bowls,total_runs,sixes,fours,dot_balls,wide_balls]
            st.table(df)
        else: 
            st.write(f'OOPS! No Data Found For {batsman} vs {bowler} In IPL')

        st.write('---')
        st. markdown(f"<h6 style='text-align: center; color: white;'> “I have failed at times, but I never stop trying.” , Rahul Dravid </h6>", unsafe_allow_html=True)
