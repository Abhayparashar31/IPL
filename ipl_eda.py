import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

import pandas as pd


def latest_teams(df,cols):
    temp = df.copy()
    teams = [
        'Sunrisers Hyderabad',
        'Mumbai Indians',
        'Royal Challengers Bangalore',
        'Kolkata Knight Riders',
        'Kings XI Punjab',
        'Chennai Super Kings',
        'Rajasthan Royals',
        'Delhi Capitals'
    ]
    
    for col in cols:
        temp[col] = temp[col].str.replace('Deccan Chargers','Sunrisers Hyderabad')
        temp[col] = temp[col].str.replace('Delhi Daredevils','Delhi Capitals')

    for col in cols:
        temp = temp[(temp[col].isin(teams))]
    
    return temp


def app():
    st.title(''' EXPLORATORY DATA ANALYSIS ON IPL DATA ''')

    st.subheader('▶️ Sneak Peak of Matches Data')
    matches = pd.read_csv('matches.csv')
    st.write(matches.head(10))

    st.subheader('▶️ Sneak Peak of Deliveries Data')
    deliveries = pd.read_csv('deliveries.csv')
    st.write(deliveries.head(10))

    matches_lt = latest_teams(matches,['team1','team2','toss_winner','winner'])

#################################################################
################## MATCHES PER SEASON ###########################
#################################################################
    with st.expander(" 1) Matches Per Season (2008-2019) "):
        season = matches['Season'].apply(lambda x:x.split('-')[1]).astype(int)
        fig = plt.figure(figsize=(12, 8))
        plt.rcParams.update({'text.color': "white",'axes.labelcolor': "white",'xtick.color':'white', 'ytick.color':'white'})

        ax = sns.countplot(y = season,palette='deep',order=season.value_counts().index)
        ax.bar_label(ax.containers[0])
        plt.title('Matches Per Season (2008-2019)')
        plt.xlabel(f'Average Matches Per Season Are: {int(season.value_counts().mean())}')
        st.pyplot(fig,transparent=True)

        if st.checkbox(label="View Code",key=0):
            st.code('''
season = matches['Season'].apply(lambda x:x.split('-')[1]).astype(int) 
fig = plt.figure(figsize=(12, 8))
ax = sns.countplot(y = season,palette='deep',order=season.value_counts().index)
ax.bar_label(ax.containers[0])
plt.title('Matches Per Season (2008-2019)')
plt.xlabel(f'Average Matches Per Season Are: {int(season.value_counts().mean())}')
plt.show();
            ''',language='python')
        

####################################################################
########## Most Man of The Match Award Received By Players #########
###################################################################
    with st.expander(" 2) Player Of The Match Award Received By Players "):
        fig = plt.figure(figsize=(15,8))
        plt.rcParams.update({'text.color': "white",'axes.labelcolor': "white",'xtick.color':'white', 'ytick.color':'white'})
        ax = sns.countplot('player_of_match', data=matches,order=matches['player_of_match'].value_counts().iloc[:20].index)
        ax.bar_label(ax.containers[0])
        font = {"size":18}
        plt.xticks(rotation='vertical')
        plt.title("Player of The Match Award Distribution Between Players",fontdict=font)
        plt.xlabel("Players",fontdict=font)
        plt.ylabel("Number of Times Player Received Award",fontdict=font)
        st.pyplot(fig,transparent=True)

        if st.checkbox(label="View Code",key=1):
            st.code('''
fig = plt.figure(figsize=(15,8))
ax = sns.countplot('player_of_match', data=matches,order=matches['player_of_match'].value_counts().iloc[:20].index)
ax.bar_label(ax.containers[0])
font = {"size":18}
plt.xticks(rotation='vertical')
plt.title("Player of The Match Award Distribution Between Players",fontdict=font)
plt.xlabel("Players",fontdict=font)
plt.ylabel("Number of Times Player Received Award",fontdict=font)
plt.show();
            ''',language='python')
        

##########################################################################
################ Venues With Most Matches ################################
##########################################################################
    with st.expander("3) Top 20 Venues With Most Matches"):
        fig = plt.figure(figsize=(15,8))
        plt.style.use('default')
        plt.rcParams.update({'text.color': "white",'axes.labelcolor': "white",'xtick.color':'white', 'ytick.color':'white'})
        ax = sns.countplot('venue', data=matches,order=matches['venue'].value_counts().iloc[:20].index)
        ax.bar_label(ax.containers[0])
        font = {"size":15}
        plt.xticks(rotation='vertical')
        plt.title("Venues With Most Matches",fontdict=font)
        plt.xlabel("Venue Name",fontdict=font)
        plt.ylabel("Number of Matches",fontdict=font)
        st.pyplot(fig,transparent=True)

        if st.checkbox(label="View Code",key=2):
            st.code(''' 
fig = plt.figure(figsize=(15,8))
ax = sns.countplot('venue', data=matches,order=matches['venue'].value_counts().iloc[:20].index)
ax.bar_label(ax.containers[0])
font = {"size":15}
plt.xticks(rotation='vertical')
plt.title("Venues With Most Matches",fontdict=font)
plt.xlabel("Venue Name",fontdict=font)
plt.ylabel("Number of Matches",fontdict=font)
plt.show();
            ''',language='python')
        
    
##########################################################################
########### Team With Most Toss Wins ################
###########################################################################
    
    with st.expander('4) Team With Most Match Wins'):
        fig = plt.figure(figsize=(15,8))
                
        plt.rcParams.update({'text.color': "white",'axes.labelcolor': "white",'xtick.color':'white', 'ytick.color':'white'})
        
        ax = sns.countplot(y='winner', data=matches_lt,order=matches_lt['winner'].value_counts().index)
        ax.bar_label(ax.containers[0])
        font = {"size":15}
        plt.xticks(rotation='vertical',fontsize=10)
        plt.title("Match Winners",fontdict=font)
        plt.xlabel("Team Name",fontdict=font)
        plt.ylabel("Match Win Count",fontdict=font)
        st.pyplot(fig,transparent=True)

        if st.checkbox(label="View Code",key=3):
            st.code(''' 
fig = plt.figure(figsize=(15,8))
ax = sns.countplot(y='winner', data=matches_lt,order=matches_lt['winner'].value_counts().index)
ax.bar_label(ax.containers[0])
font = {"size":15}
plt.xticks(rotation='vertical',fontsize=10)
plt.title("Match Winners",fontdict=font)
plt.xlabel("Team Name",fontdict=font)
plt.ylabel("Match Win Count",fontdict=font)
plt.show();
            ''',language='python')

##################################################################
#################### Team With Most Toss Wins ####################
#################################################################
    with st.expander('5) Team With Most Toss Wins'):
        fig = plt.figure(figsize=(10,5))
        
        plt.rcParams.update({'text.color': "white",'axes.labelcolor': "white",'xtick.color':'white', 'ytick.color':'white'})
        
        ax = sns.countplot('toss_winner', data=matches_lt,order=matches_lt['toss_winner'].value_counts().index)
        ax.bar_label(ax.containers[0])

        font = {"size":10}
        plt.xticks(rotation='vertical',fontsize=7)
        plt.title("Toss Winners",fontdict=font)
        plt.xlabel("Team Name",fontdict=font)
        plt.ylabel("Toss Winning Count",fontdict=font)
        st.pyplot(fig,transparent=True)

        if st.checkbox(label="View Code",key=4):
            st.code(''' 
fig = plt.figure(figsize=(10,5))
ax = sns.countplot('toss_winner', data=matches_lt,order=matches_lt['toss_winner'].value_counts().index)
ax.bar_label(ax.containers[0])

font = {"size":10}
plt.xticks(rotation='vertical',fontsize=7)
plt.title("Toss Winners",fontdict=font)
plt.xlabel("Team Name",fontdict=font)
plt.ylabel("Toss Winning Count",fontdict=font)
plt.show();
        ''',language='python')
    
#####################################################################
#### Chances of A Team Wiining Match if They Win The Toss ###########
#####################################################################
    with st.expander('6) Chances of A Team Wiining Match if They Win The Toss'):
        fig = plt.figure(figsize=(20,5))
        db = round((matches_lt[matches_lt['toss_winner']==matches_lt['winner']]['winner'].value_counts()/matches_lt['toss_winner'].value_counts())*100).sort_values(ascending=False)
        explode = (0.1,0,0,0,0,0,0,0)
        
        plt.rcParams.update({'text.color': "white",
                'axes.labelcolor': "black"})
        
        db.plot(kind='pie',autopct='%1.1f%%',explode=explode,shadow=True, startangle=90)
        plt.ylabel('')

        col1, col2 = st.columns(2)
        with col1:
            st.pyplot(fig,transparent=True)
        with col2:
            st.write('Based On Team Overall Record')
            dt = round((matches_lt[matches_lt['toss_winner']==matches_lt['winner']]['winner'].value_counts()/matches_lt['toss_winner'].value_counts())*100).sort_values(ascending=False)
            st.write(dt)


#####################################################################
################### Team Wins Toss and Matches #######################
#####################################################################

    with st.expander('7) Teams Winning Toss and Matches Both Since 2008'):
        fig = plt.figure(figsize=(10,6))
        color=['white','yellow','purple', 'red', 'green', 'magenta', 'cyan']
        winners = matches_lt[matches_lt['toss_winner']==matches_lt['winner']]['winner'].value_counts()

        plt.rcParams.update({'text.color': "white",'axes.labelcolor': "white",'xtick.color':'white', 'ytick.color':'white'})
        
        winners.plot(kind='bar',color=color)
        font = {"size":20}
        plt.xticks(fontsize=18)
        plt.title("Teams Winning Toss and Matches Both Since 2008",fontdict=font)
        plt.xlabel("Team Name",fontdict=font)
        plt.ylabel("Matches Win",fontdict=font)

        col1, col2 = st.columns(2)

        with col1:
            st.pyplot(fig,transparent=True)
        with col2:
            st.dataframe(winners,width=500,height=650)


############################################################################
############ Player With Most Runs #########################################
###########################################################################

    with st.expander('8) Top 20 Players With Most Runs'):
        fig = plt.figure(figsize=(10,6))
        top_20_run_scorer = deliveries.groupby('batsman')['batsman_runs'].sum().sort_values(ascending=False)[:20]
        
        plt.rcParams.update({'text.color': "white",'axes.labelcolor': "white",'xtick.color':'white', 'ytick.color':'white'})
        
        plt.barh(top_20_run_scorer.index[::-1],top_20_run_scorer.values[::-1],color=color)
        
        font = {"size":20}
        plt.xticks(fontsize=25)
        plt.title("Player With Most Runs",fontdict=font)
        plt.xlabel("Player Name",fontdict=font)
        plt.ylabel("Runs",fontdict=font)

        col1, col2 = st.columns(2)

        with col1:
            st.pyplot(fig,transparent=True)
        with col2:
            st.dataframe(top_20_run_scorer,width=500,height=250)


#############################################################################
############### MOST EXPENSIVE BOWLER #######################################
#############################################################################
    with st.expander("9) Most Expensive Bowler"):
        st.write("> Overall Expensive Bowler")
        col1, col2 = st.columns(2)
        with col1:
            fig = plt.figure(figsize=(10,6))
            overall = deliveries.groupby('bowler')['total_runs'].agg('sum').reset_index().sort_values('total_runs', ascending=False).head(30)
            ax = sns.barplot(x='bowler',y='total_runs',data=overall[:10])
            plt.xticks(rotation='vertical',fontsize=10)
            ax.bar_label(ax.containers[0])
            plt.title('Overall Expensive Bowler')
            st.pyplot(fig,transparent=True)
            
        with col2:
            st.dataframe(overall,400,height=400)
        
        st.write('> 1st Over Most Expensive Bowler')
        col3, col4 = st.columns(2) 

        with col3:
            fig = plt.figure(figsize=(10,6))
            first_over = deliveries[deliveries['over']==1]
            group = first_over.groupby('bowler')['total_runs'].agg('sum').reset_index().sort_values('total_runs', ascending=False).head(30)
            ax = sns.barplot(x='bowler',y='total_runs',data=group[:10])
            plt.xticks(rotation='vertical',fontsize=10)
            ax.bar_label(ax.containers[0])
            plt.title('Most Expensive Bowler In 1st Over')
            st.pyplot(fig,transparent=True)
        with col4:
            st.dataframe(group,400,height=400)
        
        st.write('> 20th Over Most Expensive Bowler')
        col5, col6 = st.columns(2)
        with col5:
            fig = plt.figure(figsize=(10,6))
            twenty_over = deliveries[deliveries['over']==20]
            group= twenty_over.groupby('bowler')['total_runs'].agg('sum').reset_index().sort_values('total_runs', ascending=False).head(30)
            ax = sns.barplot(x='bowler',y='total_runs',data=group[:10])
            plt.xticks(rotation='vertical',fontsize=10)
            ax.bar_label(ax.containers[0])
            plt.title('Most Expensive Bowler In 20th Over')
            st.pyplot(fig,transparent=True)
        with col6:
            st.dataframe(group,400,height=400)
                        


    deliveries_latest = deliveries.copy()
    deliveries_latest = latest_teams(deliveries_latest,['batting_team','bowling_team'])

#######################################################################
############################# Overwise Runs for Each Team #############
#######################################################################
    with st.expander('10) Overwise Average Runs For Each Team Since 2008'):
        fig = plt.figure(figsize=(10,8))
        x = deliveries_latest.pivot_table(values='total_runs',index='batting_team',columns='over')*6
        sns.heatmap(x, cmap='YlGn')
        plt.title('Overwise Average Runs For Each Team')
        st.pyplot(fig,transparent=True)


########################################################################
############### Toss Decision Based On Top Venues ######################
########################################################################

    with st.expander('11) Toss Decision Based On Top Venues'):
        top_venues = matches['venue'].value_counts()[:15].index.to_list()
        top_20_venues_matches = matches[matches['venue'].isin(top_venues)]
        top_20_venues_matches['venue'] = top_20_venues_matches['venue']+", "+top_20_venues_matches['city']
        top_20 = top_20_venues_matches.groupby(['venue','toss_decision']).count()['toss_winner'].reset_index().sort_values('venue',ascending=False)
 
        fig = plt.figure(figsize=(20,5))
        plt.rcParams.update({'text.color': "white",'axes.labelcolor': "white",'xtick.color':'white', 'ytick.color':'white'})
       
        ax = sns.barplot(y='toss_winner',x='venue',hue='toss_decision',data=top_20)
        ax.bar_label(ax.containers[0])
        ax.bar_label(ax.containers[1])
        leg = plt.legend()
        for text in leg.get_texts():
            text.set_color("black")
        plt.xticks(rotation='vertical',fontsize=16)
        plt.title('Toss Winner Choice Based On Venue',fontsize=16)

        st.pyplot(fig,transparent=True)
        top_20 = top_20.rename(columns={'toss_winner':'Count'})
        st.dataframe(top_20,width=700,height=300)

    

#############################################################################
################# Average Runs By Different Teams In Last Over ##############
#############################################################################

    with st.expander('12) Average Runs Scored By Different Teams In Last Over'):
        
        fig = plt.figure(figsize=(10,6))
        twenty = deliveries_latest[deliveries_latest['over']==20]
        twenty_over_scores = round(twenty.groupby('batting_team')['total_runs'].mean()*6).round(2).sort_values(ascending=False)
        ax = sns.barplot(twenty_over_scores.values,twenty_over_scores.index)
        ax.bar_label(ax.containers[0])
        plt.title('Average Runs By Different Teams In Last Over')
        plt.xlabel('Score')
        plt.ylabel('Playing Team')
        st.pyplot(fig,transparent=True)
    

##############################################################################
##### Total Runs Score By Different Teams In Last Over Till Start of IPL #####
##############################################################################
    with st.expander('13) Total RUns By Different Teams In Last Over Since Start of IPL'):
        fig = plt.figure(figsize=(12,8))
        twenty = deliveries_latest[deliveries_latest['over']==20]
        twenty_over_scores = (twenty.groupby('batting_team')['total_runs'].sum()).sort_values(ascending=False)
        #plt.barh(twenty_over_scores.index,twenty_over_scores.values);
        ax = sns.barplot(twenty_over_scores.values,twenty_over_scores.index)
        ax.bar_label(ax.containers[0])
        plt.title('Total Runs By Different Teams In Last Over')
        plt.xlabel('Score')
        plt.ylabel('Playing Team')
        st.pyplot(fig,transparent=True)



    ######### COMBINING BOTH DATASETS (Latest)
    combine_df = matches_lt.merge(deliveries_latest,left_on = 'id',right_on = 'match_id',how = 'left')

###############################################################################
##### Total Runs By Different Teams In Last Over In First Edition (2008) ######
###############################################################################

    with st.expander('14) Runs By Different Teams In Last Over In First Edition (2008)'):

        st.write('> Total Runs')
        
        fig = plt.figure(figsize=(12,8))
        twenty = combine_df[(combine_df['over']==20) & (combine_df['Season']=='IPL-2008')]
        twenty_over_scores = (twenty.groupby('batting_team')['total_runs'].sum()).sort_values(ascending=False)
        #plt.barh(twenty_over_scores.index,twenty_over_scores.values);
        ax = sns.barplot(twenty_over_scores.values,twenty_over_scores.index)
        ax.bar_label(ax.containers[0])
        plt.title('Total Runs By Different Teams In Last Over')
        plt.xlabel('Score')
        plt.ylabel('Playing Team')
        st.pyplot(fig,transparent=True)
    


###############################################################################
##### Average Runs By Different Teams In Last Over In First Edition (2008) ####
###############################################################################
        
        st.write('> Average Runs')

        fig = plt.figure(figsize=(12,8))
        twenty = combine_df[(combine_df['over']==20) & (combine_df['Season']=='IPL-2008')]
        twenty_over_scores = (twenty.groupby('batting_team')['total_runs'].sum()).sort_values(ascending=False)
        #plt.barh(twenty_over_scores.index,twenty_over_scores.values);
        ax = sns.barplot(twenty_over_scores.values,twenty_over_scores.index)
        ax.bar_label(ax.containers[0])
        plt.title('Average Runs By Different Teams In Last Over')
        plt.xlabel('Score')
        plt.ylabel('Playing Team')
        st.pyplot(fig,transparent=True)


##############################################################################
### Total Runs Scored in Each Season #########################
##############################################################################

    with st.expander('15) Total Runs Scored in Each Season'):
        fig = plt.figure(figsize=(10,8))
        plt.rcParams.update({'text.color': "white",'axes.labelcolor': "white",'xtick.color':'white', 'ytick.color':'white'})
       
        combine_df['Season'] = combine_df['Season'].apply(lambda x:x.split('-')[-1])
        season = combine_df.groupby('Season')['total_runs'].sum().reset_index()
        temp4=season.set_index('Season')
        ax = sns.relplot(x=temp4.index,y=temp4['total_runs'],kind='line',height=5, aspect=2)
        plt.title("Total Runs Scored In Each Season",fontsize=16)
        plt.xticks(fontsize=16)
        plt.xlabel("IPL Season",fontdict={'size':18})
        plt.ylabel("Total Runs",fontdict={'size':18})        
        col00, col01 = st.columns(2)
        with col00:
            st.pyplot(ax,transparent=True)
        with col01:    
            st.dataframe(temp4,width=500,height=300)

#####################################################################
############ Count of Matches By Different Umpires ##################
#####################################################################


    with st.expander('16) Count of Matches By Different Umpires'):
        fig = plt.figure(figsize=(15,8))
        umpires = pd.concat([matches['umpire1'],matches['umpire2']]).value_counts()
        top_10_umpires = umpires.nlargest(10)
        ax = sns.barplot(top_10_umpires.index,top_10_umpires.values)
        ax.bar_label(ax.containers[0])
        plt.title('Maches Played By Umpires')
        plt.xlabel('Umpire Name')
        plt.ylabel('Matches Played')
        st.pyplot(fig,transparent=True)
          

###########################################################################
############ Lucky Venue For Teams ########################################
###########################################################################

    with st.expander('17) Lucky Venue For Teams'):
        teams = matches_lt.team1.unique().tolist()
        matches_lt['venue'] = matches_lt['venue']+", "+matches_lt['city']
        for team in teams:
            fig = plt.figure(figsize=(15,8))
            team_name = team
            lucky_venues = matches_lt[matches_lt['winner']==team_name]['venue'].value_counts().nlargest(10)
            explode = (0.1,0.1,0,0,0,0,0,0,0,0)
            colors = ['turquoise', 'lightblue', 'lightgreen', 'crimson', 'magenta','orange']
            plt.rcParams.update({'text.color': "white",'axes.labelcolor': "white",'xtick.color':'white', 'ytick.color':'white'})
            lucky_venues.plot(kind='pie',autopct='%1.1f%%',explode=explode,shadow=True, startangle=20,textprops={'fontsize': 10},colors=colors)
            plt.title(f'Win at different Venues for {team}')
            plt.ylabel('')
            st.pyplot(fig,transparent=True)


#####################################################################
#################### Teams with more than 200+ scores ###############
#####################################################################


    with st.expander('18) Teams With More Than 200+ Scores'):
        fig = plt.figure(figsize=(10,7))
        plt.rcParams.update({'text.color': "white",'axes.labelcolor': "white",'xtick.color':'white', 'ytick.color':'white'})
        runs = deliveries_latest.groupby(['match_id', 'inning','batting_team','bowling_team'])['total_runs'].sum().reset_index() 
        runs_over_200_df = runs[runs['total_runs']>200]
        runs_over_200 = runs_over_200_df['batting_team'].value_counts()

        ax = sns.barplot(runs_over_200.index,runs_over_200.values)
        ax.bar_label(ax.containers[0])
        plt.xticks(rotation='vertical')
        plt.title('Most 200+ Runs Scored By Teams')
        plt.xlabel('Teams')
        plt.ylabel('Runs')
        st.pyplot(fig,transparent=True)
    


    
