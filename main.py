import home
import predict_score
import predict_winner
import ipl_eda
import team_vs_team
import bat_vs_bowl
import player
import team

import streamlit as st

PAGES = {
    "HOME":home,
    "Predict First Innings Score": predict_score,
    "Predict Winner Probability Based On Second Innings": predict_winner,
    "EDA":ipl_eda,
    "Team vs Team":team_vs_team,
    "Player Analysis":player,
    "Team Analysis":team,
    "Batsman vs Bowler":bat_vs_bowl
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Choose One Option", list(PAGES.keys()))
page = PAGES[selection]
page.app()