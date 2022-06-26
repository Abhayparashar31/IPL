import home
import predict_score
import predict_winner
import ipl_eda
import team_vs_team
import bat_vs_bowl
import player
import team

import streamlit as st
st.set_page_config(
    page_title = "IPL ANALYSIS",
    page_icon = "🏏",
    initial_sidebar_state='expanded',
    #layout="wide"
)

st.markdown(
    """
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
    """,
    unsafe_allow_html=True,
)

PAGES = {
    "HOME":home,
    "EDA":ipl_eda,
    "Team vs Team":team_vs_team,
    "Player Analysis":player,
    "Team Analysis":team,
    "Batsman vs Bowler":bat_vs_bowl,
    "Predict First Innings Score": predict_score,
    "Predict Winner Probability Based On Second Innings": predict_winner
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Choose One Option", list(PAGES.keys()))
page = PAGES[selection]
page.app()
