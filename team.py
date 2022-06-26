import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import pandas as pd

import ipl_eda
import team_vs_team


def app():
    matches = pd.read_csv('matches.csv')
    matches_lt = ipl_eda.latest_teams(matches,['team1','team2','toss_winner','winner'])
    deliveries = pd.read_csv('deliveries.csv')
    deliveries_latest = ipl_eda.latest_teams(deliveries,['batting_team','bowling_team'])

    combine_df = matches_lt.merge(deliveries_latest,left_on = 'id',right_on = 'match_id',how = 'left')

    st.markdown(''' 
    <center>―――――――――――――――――――――――――――――――――――――――――――――</center>
    <h1 style='text-align:center;'> IPL Analysis: Team </h1> 
    <center>―――――――――――――――――――――――――――――――――――――――――――――</center>
    <br>
    ''',unsafe_allow_html=True)
    

    
    Teams = matches_lt.team1.unique().tolist()
    team = st.selectbox("Choose a Team",Teams)  
    Analyze = st.button('Analyze')
    if Analyze:
            
        deliveries_lt = deliveries_latest[deliveries_latest['batting_team']==team]

        st. markdown(f"<h4 style='text-align: center; color: white;'> Team : {team} </h4>", unsafe_allow_html=True)

        st. markdown(f"<h5 style='text-align: center; color: white;'> {team} Average Score Against Different Opponents </h5>", unsafe_allow_html=True)
        plt.rcParams.update({'text.color': "white",'axes.labelcolor': "white",'xtick.color':'white', 'ytick.color':'white'})
        

        #### Average Total Against Each Team
        innings_data = deliveries_lt.groupby(['match_id','inning','bowling_team'])['total_runs'].sum().reset_index()
        innings_data_scores = innings_data.groupby('bowling_team')['total_runs'].mean().round().astype(int)

        fig = plt.figure(figsize=(15,6))
        ax = sns.lineplot(x=innings_data_scores.index,y=innings_data_scores.values,markers=True)
        for x,y in zip(innings_data_scores.index,innings_data_scores.values):
            plt.text(x = x, y = y, s = '{:.0f}'.format(y), color='white').set_backgroundcolor('blue')
        ax.set_xticks(range(0,7,1))
        st.pyplot(fig,transparent=True)
        st.write('---')
        st. markdown(f"<h5 style='text-align: center; color: white;'> Average Runs Scored By {team} In Different Overs </h5>", unsafe_allow_html=True)


        #### Average Runs Scored In Different Overs
        team_over_data = (deliveries_lt.groupby('over')['total_runs'].mean()*6).round().astype(int).reset_index()
        team_over_data

        fig = plt.figure(figsize=(10,6))
        ax = sns.lineplot(data=team_over_data,x='over',y='total_runs',markers=True)
        for x,y in zip(team_over_data['over'],team_over_data['total_runs']):
            plt.text(x = x, y = y, s = '{:.0f}'.format(y), color='black').set_backgroundcolor('lightgreen')
        ax.set_xticks(range(0,21,1))
        st.pyplot(fig,transparent=True)
        st.write('---')
        st. markdown(f"<h5 style='text-align: center; color: white;'> {team} Toss Decision </h5>", unsafe_allow_html=True)
        ####### Toss Decision
        fig = plt.figure(figsize=(5,4))
        team_toss_decision = matches_lt[matches_lt['toss_winner']==team]['toss_decision']
        ax=sns.countplot(team_toss_decision)
        ax.bar_label(ax.containers[0])
        st.pyplot(fig,transparent=True)


        st.write('---')
        st. markdown(f"<h5 style='text-align: center; color: white;'> {team} Match Wins Based On Venue </h5>", unsafe_allow_html=True)
     
        #### Most Win Based On Venue,City
        venue_win = matches_lt[matches_lt['winner']==team]['venue'].value_counts()[:10]

        fig = plt.figure(figsize=(20,5))
        ax = sns.barplot(x=venue_win.index,y=venue_win.values)
        ax.bar_label(ax.containers[0])
        plt.xlabel('Venues')
        plt.ylabel('Wins')
        plt.xticks(fontsize=12,rotation='vertical')
        st.pyplot(fig,transparent=True)


        st.write('---')

        st. markdown(f"<h5 style='text-align: center; color: white;'> {team} 200+ Runs </h5>", unsafe_allow_html=True)
     
        #### Top 10 Highest Runs
        fig = plt.figure(figsize=(12,10))
        team_runs_over_200_df = deliveries_lt.groupby(['match_id','bowling_team','inning'])['total_runs'].sum().reset_index().sort_values(by='total_runs',ascending=False)
        team_runs_over_200 = team_runs_over_200_df[team_runs_over_200_df['total_runs']>200]
        team_runs_over_200['data'] = team_runs_over_200['match_id'].astype(str)+"_"+team_runs_over_200['bowling_team']
        ax = sns.barplot(data=team_runs_over_200,y='data',x='total_runs')
        ax.bar_label(ax.containers[0])
        plt.title(f'{team} 200+ Runs : Total({len(team_runs_over_200)})')
        plt.xlabel('Runs')
        plt.ylabel('Opponents')
        plt.xticks(fontsize=12,rotation='vertical')
        st.pyplot(fig,transparent=True)

        st.write('---')
        st. markdown(f"<h5 style='text-align: center; color: white;'> {team} Top 10 Lowest Runs </h5>", unsafe_allow_html=True)
     

        #### Top 10 Lowest Runs
        fig = plt.figure(figsize=(12,10))
        team_runs_over_df = deliveries_lt.groupby(['match_id','bowling_team','inning'])['total_runs'].sum().reset_index().sort_values(by='total_runs',ascending=True)
        team_runs_over_df = team_runs_over_df[team_runs_over_df['inning']<3]
        team_runs_over_df = team_runs_over_df[:10]


        team_runs_over_df['data'] = team_runs_over_df['match_id'].astype(str)+"_"+team_runs_over_df['bowling_team']


        ax = sns.barplot(data=team_runs_over_df,y='data',x='total_runs')
        ax.bar_label(ax.containers[0])
        plt.title(f'{team} Top 10 Lowest Runs')
        plt.xlabel('Runs')
        plt.ylabel('Opponents')
        plt.xticks(fontsize=12,rotation='vertical')
        st.pyplot(fig,transparent=True)


        st.write('---')
        st. markdown(f"<h6 style='text-align: center; color: white;'> “When people throw stones at you, you turn them into milestones.”– Sachin Tendulkar </h6>", unsafe_allow_html=True)
     
