import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import pandas as pd

import ipl_eda


def gen_accr(t1,t2):
    ### Accronym
    orth = ['Sunrisers Hyderabad','Kings XI Punjab']
    if t1 in orth:
        if t1==orth[0]:
            acr_t1='SRH'
        else:
            acr_t1 = 'KXIP'
    else:
        acr_t1 = "".join([word[0] for word in t1.split()])
    if t2 in orth:
        if t2==orth[0]:
            acr_t2='SRH'
        else:
            acr_t2 = 'KXIP'
    else:
        acr_t2 = "".join([word[0] for word in t2.split()])
    
    return acr_t1,acr_t2


def gen_colors(color_t1,color_t2):
    dictt = {
        'MI':   'blue',
        'CSK':  'yellow',
        'RCB':  'green',
        'SRH':  'orange',
        'DC':   'lightblue',
        'KKR':  'purple',
        'KXIP': 'red',
        'RR':   'magenta' 
    }
    for key in dictt.keys():
        color_t1 = color_t1.replace(key, dictt[key])
        color_t2 = color_t2.replace(key,dictt[key])
    
    return [color_t1,color_t2]

  

def app():
    matches = pd.read_csv('matches.csv')
    matches_lt = ipl_eda.latest_teams(matches,['team1','team2','toss_winner','winner'])
    deliveries = pd.read_csv('deliveries.csv')
    deliveries_latest = ipl_eda.latest_teams(deliveries,['batting_team','bowling_team'])

    combine_df = matches_lt.merge(deliveries_latest,left_on = 'id',right_on = 'match_id',how = 'left')


    st.header('IPL Analysis: Team Vs Team')

    Teams = matches_lt.team1.unique().tolist()

    c1,c2 = st.columns(2)
    with c1:
        t1 = st.selectbox("Choose Team 1",Teams)    
    with c2:
        t2 = st.selectbox("Choose Team 2",Teams) 

    ####################################################################
    ### Accronym
    ####################################################################
    
    acr_t1,acr_t2 = gen_accr(t1,t2)
    colors = gen_colors(acr_t1,acr_t2)

    Analyze = st.button('Analyze')
    if Analyze:
        
        st. markdown(f"<h4 style='text-align: center; color: white;'> {t1}({acr_t1}) vs {t2}({acr_t2}) </h4>", unsafe_allow_html=True)

        ### Total Match Played
        t1_batting = matches_lt[((matches_lt['team1']==t1) & (matches_lt['team2']==t2))]
        t2_batting = matches_lt[((matches_lt['team1']==t2) & (matches_lt['team2']==t1))]
        total = t1_batting.append(t2_batting)
        
        fig = plt.figure(figsize=(6,4))

        ##### plot Parameters   
        #### Viz   
        sns.set_theme(style="whitegrid")
        plt.rcParams.update({'text.color': "white",'axes.labelcolor': "white",'xtick.color':'white', 'ytick.color':'white'})
        
        ####################################################################
        ########## Winners
        ####################################################################

        ax = sns.countplot(total['winner'], palette=colors)
        ax.bar_label(ax.containers[0])
        plt.title(f'{acr_t1} vs {acr_t2} : Match Winners',fontsize=10)
        plt.xlabel('Teams')
        plt.ylabel('Winning Count')
        st.pyplot(fig,transparent=True)
        
        ####################################################################
        ########## Toss Wins
        ####################################################################

        st.write('---')
        fig = plt.figure(figsize=(6,4))
        print(total['toss_winner'].value_counts())
        ax = sns.countplot(total['toss_winner'], palette=colors)
        ax.bar_label(ax.containers[0])
        plt.title(f'{acr_t1} vs {acr_t2} : Toss Winners',fontsize=10)
        plt.xlabel('Teams')
        plt.ylabel('Winning Count')
        st.pyplot(fig,transparent=True)

        ####################################################################
        ################## Player of the Match 
        ####################################################################
        st.write('---')
        fig = plt.figure(figsize=(6,8))
        ax = sns.countplot(y = total['player_of_match'],hue=total['winner'],order=total['player_of_match'].value_counts().index, palette=colors)
        ax.bar_label(ax.containers[0])
        ax.bar_label(ax.containers[1])
        legend = plt.legend()
        frame = legend.get_frame()
        frame.set_facecolor('black')

        plt.title(f'{acr_t1} vs {acr_t2} : Player of The Match',fontsize=10)
        plt.xlabel('Count')
        plt.ylabel('Players')
        st.pyplot(fig,transparent=True)


        t1_batting = combine_df[((combine_df['batting_team']==t1) & (combine_df['bowling_team']==t2))]
        t2_batting = combine_df[((combine_df['batting_team']==t2) & (combine_df['bowling_team']==t1))]
        total_del = t1_batting.append(t2_batting)
        
        ####################################################################
        ####### Batting t1
        ####################################################################
        st.write('---')
        fig = plt.figure(figsize=(10,4))
        temp = total_del.groupby(['Season','match_id', 'inning','batting_team','bowling_team'])['total_runs'].sum().reset_index()
        temp = temp[temp['inning']<3]

        runs = temp[temp.batting_team==t1][['total_runs','Season','match_id','inning']]

        sns.lineplot(data=runs,x='Season',y='total_runs')
        plt.title(f'{acr_t1} vs {acr_t2} : {acr_t1} Average Total Score',fontsize=10)
        plt.xlabel(f'Bowling :{t2}')
        plt.ylabel(f'Runs')
        st.pyplot(fig,transparent=True)

        ####################################################################
        ####### Batting t2
        ####################################################################
        st.write('---')    
        fig = plt.figure(figsize=(10,4))
        temp = total_del.groupby(['Season','match_id', 'inning','batting_team','bowling_team'])['total_runs'].sum().reset_index()
        temp = temp[temp['inning']<3]

        runs = temp[temp.batting_team==t2][['total_runs','Season','match_id','inning']]

        sns.lineplot(data=runs,x='Season',y='total_runs')
        plt.title(f'{acr_t1} vs {acr_t2} :  {acr_t2} Average Total Score',fontsize=10)
        plt.xlabel(f'Bowling :{t1}')
        plt.ylabel(f'Runs')
        st.pyplot(fig,transparent=True)
        
        ####################################################################
        #### Match Win Based On City
        ####################################################################
        st.write('---')       
        st. markdown(f"<h4 style='text-align: center; color: white;'> {acr_t1} vs {acr_t2} : Match Win Based On City  </h4>", unsafe_allow_html=True)
        
        fig = plt.figure(figsize=(10,4))
        ax = sns.countplot(x = total['city'],hue=total['winner'],palette=colors)
        ax.bar_label(ax.containers[0])
        ax.bar_label(ax.containers[1])
        legend = plt.legend()
        frame = legend.get_frame()
        frame.set_facecolor('black')
        plt.title(f'{acr_t1} vs {acr_t2} : Match Win Based On City',fontsize=10)
        plt.xlabel('City Names')
        plt.ylabel('frequency')
        st.pyplot(fig,transparent=True)
        
        st.write('---')
        def info(team):
            t = team
            
            er = total_del[total_del.bowling_team==t]['extra_runs'].sum()
            sixes = total_del[(total_del['batting_team']==t) & (total_del['total_runs']==6)].count()[0]
            fours = total_del[(total_del['batting_team']==t) & (total_del['total_runs']==4)].count()[0]
            doubles = total_del[(total_del['batting_team']==t) & (total_del['total_runs']==2)].count()[0]
            singles = total_del[(total_del['batting_team']==t) & (total_del['total_runs']==1)].count()[0]
            total_runs = total_del[total_del['batting_team']==t]['total_runs'].sum()
            
            return [er,sixes,fours,doubles,singles,total_runs]

        df = pd.DataFrame(columns=['info',f'{t1}',f'{t2}'], index=None)
        df['info'] = ['Extra Runs','Sixes','Fours','Doubles','Singles','Total Runs']
        df[f'{t1}'] = info(t1)
        df[f'{t2}'] = info(t2)
        st. markdown(f"<h4 style='text-align: center; color: white;'> HEAD TO HEAD INFO </h4>", unsafe_allow_html=True)

        st.table(df)

        ####################################################################
        ############# Team t1 (sixes)
        ####################################################################
        st.write('---')
        st. markdown(f"<h4 style='text-align: center; color: white;'>  Team {t1} Players Total Sixes Against {t2} </h4>", unsafe_allow_html=True)

        fig = plt.figure(figsize=(12,10),dpi=150)
        t1_player_six = total_del[(total_del['batting_team']==t1) & (total_del['total_runs']==6)]['batsman']
        ax = sns.countplot(y=t1_player_six,order=t1_player_six.value_counts().iloc[:10].index)
        ax.bar_label(ax.containers[0])
        plt.title(f"Number of Sixes Hitted By Players of Team {acr_t1} vs {acr_t2} ")
        plt.ylabel('Players')
        plt.xlabel('Number of Sixes')
        st.pyplot(fig,transparent=True)


        ####################################################################
        ############# Team t1 (fours)
        ####################################################################
        st.write('---')
        st. markdown(f"<h4 style='text-align: center; color: white;'>  Team {t1} Players Total Fours Against {t2} </h4>", unsafe_allow_html=True)
        fig = plt.figure(figsize=(12,10),dpi=150)
        t1_player_six = total_del[(total_del['batting_team']==t1) & (total_del['total_runs']==4)]['batsman']
        ax = sns.countplot(y=t1_player_six,order=t1_player_six.value_counts().iloc[:10].index)
        ax.bar_label(ax.containers[0])
        plt.title(f"Number of fours Hitted By Players of Team {acr_t1} vs {acr_t2} ")
        plt.ylabel('Players')
        plt.xlabel('Number of fours')
        st.pyplot(fig,transparent=True)

        ####################################################################
        ############# Team t2 (sixes)
        ####################################################################
        st.write('---')        
        st. markdown(f"<h4 style='text-align: center; color: white;'>  Team {t2} Players Total Sixes Against {t1} </h4>", unsafe_allow_html=True)

        fig = plt.figure(figsize=(12,10),dpi=150)
        t1_player_six = total_del[(total_del['batting_team']==t2) & (total_del['total_runs']==6)]['batsman']
        ax = sns.countplot(y=t1_player_six,order=t1_player_six.value_counts().iloc[:10].index)
        ax.bar_label(ax.containers[0])
        plt.title(f"Number of Sixes Hitted By Players of Team {acr_t2} vs {acr_t1} ")
        plt.ylabel('Players')
        plt.xlabel('Number of Sixes')
        st.pyplot(fig,transparent=True)

        ####################################################################
        ############# Team t2 (fours) ##################################
        ####################################################################
        st.write('---')
        st. markdown(f"<h4 style='text-align: center; color: white;'>  Team {t2} Players Total Fours Against {t1} </h4>", unsafe_allow_html=True)

        fig = plt.figure(figsize=(12,10),dpi=150)
        t1_player_six = total_del[(total_del['batting_team']==t2) & (total_del['total_runs']==4)]['batsman']
        ax = sns.countplot(y=t1_player_six,order=t1_player_six.value_counts().iloc[:10].index)
        ax.bar_label(ax.containers[0])
        plt.title(f"Number of fours Hitted By Players of Team {acr_t2}  vs {acr_t1} ")
        plt.ylabel('Players')
        plt.xlabel('Number of fours')
        st.pyplot(fig,transparent=True)
        st.write('---')
        st. markdown(f"<h6 style='text-align: center; color: white;'>   “When you have to work, work with a smile.”– Kapil Dev </h6>", unsafe_allow_html=True)