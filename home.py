import streamlit as st
def app():
    st.markdown(
        '''
        # IPL MATCH PREDICTIONS AND ANALYSIS
        '''
    )
    st.image('main_app_IPL_img.jpg')
    st.markdown(
        '''
        ――――――――――――――――――――――――――――――――――――――――――――――――――
        ## **IPL** 🏏
        IPL stands for Indian Premier League, a T20 cricket tournament which was originally established in 2008. It is traditionally played from April through to June each year.

        The Indian Premier League starts with a round robin tournament where each franchise will play each other twice: home and away. Sides will earn two points for a win while the teams will earn one point each if there is an abandoned game.

        
        At the end of this sequence, the top four sides in the table will progress to the playoffs while the remaining franchises will be eliminated.The playoffs start with the first qualifier where the top two sides in the table play each other and the winner goes straight through to the final.


        Next up is the eliminator where the third and fourth placed sides face off. The winner goes through to the second qualifier while the loser is eliminated. In the second qualifier, the winner of the eliminator takes on the loser of the first playoff match. The winner of that game progresses to the final.
        '''
    )
    st.text('――――――――――――――――――――――――――――――――――――――――――――――――――')
    st.markdown(
        '''
        ## **Teams** 👨‍💼
        * Chennai Super Kings
        * Royal Challengers Bangalore
        * Delhi Capitals
        * Punjab Kings
        * Sunrisers Hyderabad
        * Mumbai Indians
        * Rajasthan Royals
        * Kolkata Knight Riders
        '''
    )
    st.text('――――――――――――――――――――――――――――――――――――――――――――――――――')
    st.markdown(''' ## You Are Interacting With A **Multipurpose Web App** That Can- ''')

    st.markdown(
        '''
        ###### 1. Predict The First Inning Score Based On Current Situation of The Match.
        ###### 2. Provide A Winner Probability For Any Condition of Second Innings of the Match.
        ###### 3. Detailed Exploratory Data Analysis On Dataset.
        ###### 4. Team vs Team Analysis.
        ###### 5. Player vs Player Analysis.
        ###### 6. Team Past Record Analysis.
        ###### 7. Player Career Analysis As Batsman and Bowler.
        '''
    )

    ## Creator Info
    st.write(''' \n''')
    st.text('――――――――――――――――――――――――――――――――――――――――――――――――――')
    st.subheader(''' ©️ Streamlit Web App Developed By Abhay Parashar ''') 
    st.subheader(''' **Find Him On**''')
    st.write(''' [**Medium**](https://abhayparashar31.medium.com/) | [**LinkedIN**](https://www.linkedin.com/in/abhayparashar31/) | [**GitHub**](https://github.com/abhayparashar31/)''')
    st.write('Sayonara !!!')
    st.write(''' \n''')
    
    st.text('――――――――――――――――――――――――――――――――――――――――――――――――――')
    
    st.info('''**Note**: Open The Web App In Wide Mode For Better View of Visualizations.
           To Do So **[Open Drop Down From Top Right ➡ Settings ➡ Check The Wide Mode Checkbox]**''')
