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


    st.header('IPL Analysis: Player')

    Batsman = deliveries['batsman'].unique().tolist()
    Bowler = deliveries['bowler'].unique().tolist()
    Batsman.extend(Bowler)
    Players = list(set(Batsman))

    player = st.selectbox("Choose A Player",Players)
    Analyze = st.button('Analyze')
    if Analyze:    
        st. markdown(f"<h4 style='text-align: center; color: white;'> {player} </h4>", unsafe_allow_html=True)

    ###########################################################
    ############## player as batsman ##########################
    ###########################################################
        player_df = deliveries[deliveries['batsman']==player]
        if len(player_df)!=0:
        ###########################################################
            #### Runs Against Other Teams
        ###########################################################
            st. markdown(f"<h5 style='text-align: center; color: white;'> {player} Performance Against Different Teams</h5>", unsafe_allow_html=True)
            player_df_latest = deliveries_latest[deliveries_latest['batsman']==player]
            player_runs_against_teams = player_df_latest.groupby('bowling_team')['total_runs'].sum().reset_index().sort_values(by='total_runs',ascending=False)
            fig = plt.figure(figsize=(12,6))
            ax = sns.barplot(data=player_runs_against_teams,x='bowling_team',y='total_runs')
            ax.bar_label(ax.containers[0])

            plt.xticks(fontsize=10)
            
            plt.xlabel('Teams')
            plt.ylabel('Runs')
            

            st.pyplot(fig,transparent=True)
            st.write('---')
        #############################################################
        #### Runs Against Different Bowlers
        #############################################################

            st. markdown(f"<h5 style='text-align: center; color: white;'> {player} Performance Against Different Bowlers (Top 15)  </h5>", unsafe_allow_html=True)


            player_runs_against_bowlers = player_df.groupby('bowler')['total_runs'].sum().reset_index().sort_values(by='total_runs',ascending=False)
            player_runs_against_bowlers = player_runs_against_bowlers[:15]
            fig = plt.figure(figsize=(20,5))
            ax = sns.barplot(data=player_runs_against_bowlers,x='bowler',y='total_runs')
            ax.bar_label(ax.containers[0])
            plt.title(f'{player} Performance Against Different Bowlers (Top 15)')
            plt.xlabel('Bewlers')
            plt.ylabel('Runs')
            plt.xticks(fontsize=12)
            st.pyplot(fig,transparent=True)
            st.write('---')            
        #############################################################
        ### Partnership runs
        #############################################################

            st. markdown(f"<h5 style='text-align: center; color: white;'> {player} Runs With Partner At non-striker (Top 15)  </h5>", unsafe_allow_html=True)


            player_partnership_runs = player_df.groupby('non_striker')['total_runs'].sum().reset_index().sort_values(by='total_runs',ascending=False)
            player_partnership_runs = player_partnership_runs[:15]
            fig = plt.figure(figsize=(20,5))
            ax = sns.barplot(data=player_partnership_runs,x='non_striker',y='total_runs')
            ax.bar_label(ax.containers[0])
            plt.title(f'{player} Runs With Partner At non-striker (Top 15)')
            plt.xlabel('Players')
            plt.ylabel('Runs')
            plt.xticks(fontsize=12)


            st.pyplot(fig,transparent=True)
            st.write('---')            
        #############################################################    
        ### Player Runs In Different Innings
        #############################################################
            st. markdown(f"<h5 style='text-align: center; color: white;'> {player} Runs On Different Innings  </h5>", unsafe_allow_html=True)




            fig = plt.figure(figsize=(8,4))
            innings_runs = player_df[player_df['inning']<3]
            innings = innings_runs.groupby('inning')['total_runs'].sum()
            ax = sns.barplot(x=innings.index,y=innings.values)
            ax.bar_label(ax.containers[0])
            plt.title(f'{player} Runs On Different Innings')
            plt.xlabel('Innings')
            plt.ylabel('Runs')
            plt.xticks(fontsize=12)
            st.pyplot(fig,transparent=True)
            st.write('---')
        

        else:
            st. markdown(f"<h5 style='text-align: center; color: red;'> OOPS! No Data Found For Batting Carrer of {player} in IPL') </h5>", unsafe_allow_html=True)
    #############################################################   
    ###### Player as bowler ####################################
    #############################################################   


        player_df_bowl = deliveries[deliveries['bowler']==player]

        if len(player_df_bowl)!=0:
            tr = player_df_bowl['total_runs'].sum()
            st. markdown(f"<h5 style='text-align: center; color: white;'> Runs Given Against Different Players For {player} (Top 15)  </h5>", unsafe_allow_html=True)

            ##### Runs Given Against Different Players
            player_df_bowl_players = player_df_bowl.groupby('batsman')['total_runs'].sum().reset_index().sort_values(by='total_runs',ascending=False)[:15]
            fig = plt.figure(figsize=(20,5))
            ax = sns.barplot(data=player_df_bowl_players,x='batsman',y='total_runs')
            ax.bar_label(ax.containers[0])
            #plt.title(f'Runs Given Against Different Players For {player} (Top 15) ')
            plt.xlabel('Players')
            plt.ylabel('Runs')
            plt.xticks(fontsize=12)
            st.pyplot(fig,transparent=True)
            st.write('---')
            ##### Runs Given In Different Overs



            st. markdown(f"<h5 style='text-align: center; color: white;'> Total Runs Given By {player} in different overs </h5>", unsafe_allow_html=True)



            player_df_bowl_overs = player_df_bowl.groupby('over')['total_runs'].sum().reset_index().sort_values(by='over',ascending=True)
            fig = plt.figure(figsize=(10,6))
            ax = sns.lineplot(data=player_df_bowl_overs,x='over',y='total_runs',markers=True)
            for x,y in zip(player_df_bowl_overs['over'],player_df_bowl_overs['total_runs']):
                plt.text(x = x, y = y, s = '{:.0f}'.format(y), color='white').set_backgroundcolor('purple')
            ax.set_xticks(range(0,21,1))
            #ax.set_title(f'Total Runs Given By {player} in different overs')
            st.pyplot(fig,transparent=True)
            st.write('---')
            
            st. markdown(f"<h5 style='text-align: center; color: white;'> Overs Thrown By {player} </h5>", unsafe_allow_html=True)



            ##### Number of Times a Over is Balled By The Player
            player_df_bowl_overs_n = player_df_bowl['over'].value_counts().reset_index()
            player_df_bowl_overs_n = player_df_bowl_overs_n.rename(columns={'index':'over',"over":'count'})
            player_df_bowl_overs_n = player_df_bowl_overs_n.sort_values(by='over')
            player_df_bowl_overs_n['count'] = (player_df_bowl_overs_n['count']/6).round(2)


            fig = plt.figure(figsize=(10,6))
            ax = sns.lineplot(data=player_df_bowl_overs_n,x='over',y='count',markers=True)
            for x,y in zip(player_df_bowl_overs_n['over'],player_df_bowl_overs_n['count']):
                plt.text(x = x, y = y, s = '{:.2f}'.format(y), color='white').set_backgroundcolor('purple')
            ax.set_xticks(range(0,21,1))
            #ax.set_title(f'Overs Thrown By {player}')
            st.pyplot(fig,transparent=True)
            st.write('---')
            st. markdown(f"<h5 style='text-align: center; color: white;'> Runs Given Against Different Teams For {player} </h5>", unsafe_allow_html=True)



            ### Runs Given Against Different Teams
            player_df_bowl_n = deliveries_latest[deliveries_latest['bowler']==player]
            player_df_bowl_teams = player_df_bowl_n.groupby('batting_team')['total_runs'].sum().reset_index().sort_values(by='total_runs',ascending=False)[:15]


            fig = plt.figure(figsize=(20,5))
            ax = sns.barplot(data=player_df_bowl_teams,x='batting_team',y='total_runs')
            ax.bar_label(ax.containers[0])
            #plt.title(f'Runs Given Against Different Teams For {player}')
            plt.xlabel('Teams')
            plt.ylabel('Runs')
            plt.xticks(fontsize=12)
            

            st.pyplot(fig,transparent=True)
            st.write('---')
            
        else:
            st. markdown(f"<h5 style='text-align: center; color: red;'> OOPS! No Data Found For Bowling Carrer of {player} in IPL') </h5>", unsafe_allow_html=True)

        st.write('---')
        st. markdown(f"<h6 style='text-align: center; color: white;'> “A wise man learns by the mistakes of others, a fool by own.”– Adam Gilchrist </h6>", unsafe_allow_html=True)
            
