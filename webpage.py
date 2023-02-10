import streamlit as st
import pandas as pd
import front_end_utilities as sf
from PIL import Image

def main():
    
    logo,title = st.columns([1,20])
    #title
    logo.image(Image.open(r"./photo/logo.png"), use_column_width='auto')
    title.markdown('<h1 align="center">NBA Game Predictor 2010’s</h1>',unsafe_allow_html = True)
    #read the dataframe cointaining name players
    top30 = pd.read_csv(r"./dataset/lista_giocatori_front_end.csv")
    
    phc0 = st.empty()
    phc1 = st.empty()
    phc2 = st.empty()
    phc3 = st.empty()
    phc4 = st.empty()
    phc5 = st.empty()
    phc_b = st.empty()

    #Creating columns 
    png1, team1, pts1, pts2, team2, png2 = phc0.columns([1,3,1,1,3,1]) 
    png1_1, team1_1, pts1_1, pts2_1, team2_1, png2_1 = phc1.columns([1,3,1,1,3,1])
    png1_2, team1_2, pts1_2, pts2_2, team2_2, png2_2 = phc2.columns([1,3,1,1,3,1])
    png1_3, team1_3, pts1_3, pts2_3, team2_3, png2_3 = phc3.columns([1,3,1,1,3,1])
    png1_4, team1_4, pts1_4, pts2_4, team2_4, png2_4 = phc4.columns([1,3,1,1,3,1])
    png1_5, team1_5, pts1_5, pts2_5, team2_5, png2_5 = phc5.columns([1,3,1,1,3,1])
    x,y,z = phc_b.columns([4,1,4])
    
    #container for back_end system
    t1_player = [top30.loc[0,'NAME_PLAYER'],top30.loc[0,'NAME_PLAYER'],top30.loc[0,'NAME_PLAYER'],top30.loc[0,'NAME_PLAYER'],top30.loc[0,'NAME_PLAYER']]
    t2_player = [top30.loc[0,'NAME_PLAYER'],top30.loc[0,'NAME_PLAYER'],top30.loc[0,'NAME_PLAYER'],top30.loc[0,'NAME_PLAYER'],top30.loc[0,'NAME_PLAYER']]

    def check_error():  #funzione usata all'attivamento del tasto run per verificare tutti i dati siano inseriti correttamente
        for j in range(5):
            for i in range(5):
                if(j == 0):
                    if((t1_player[i] == top30.loc[0,'NAME_PLAYER']) | (t2_player[i] == top30.loc[0,'NAME_PLAYER'])):
                        phc0.empty()
                        phc1.empty()
                        phc2.empty()
                        phc3.empty()
                        phc4.empty()
                        phc5.empty()
                        phc_b.empty()
                        st.error('ATTENZIONE: non hai selezionato tutti i giocatori delle due squadre. Riprova!')
                        if(y.button('Restart',key='e_1')):
                            main()
                    if(i > 0):
                        if((t1_player[j] == t1_player[i]) | (t2_player[j] == t2_player[i])):
                            phc0.empty()
                            phc1.empty()
                            phc2.empty()
                            phc3.empty()
                            phc4.empty()
                            phc5.empty()
                            phc_b.empty()
                            st.error('ATTENZIONE: hai selezionato due giocatori uguali. Riprova!')
                            if(y.button('Restart',key='e_2')):
                                main()
                if(t1_player[j] == t2_player[i]):
                    phc0.empty()
                    phc1.empty()
                    phc2.empty()
                    phc3.empty()
                    phc4.empty()
                    phc5.empty()
                    phc_b.empty()
                    st.error('ATTENZIONE: hai selezionato due giocatori uguali. Riprova')
                    if(y.button('Restart',key='e_3')):
                        main()
                
                
    team1.write('**TEAM 1**')    
    #Team1 1 riga
    team1_1.selectbox(label='Player1',options= top30['NAME_PLAYER'], index=0, key='player_1') 
    t1_player[0] = st.session_state.player_1
    png1_1.write(' ')
    png1_1.write(' ')
    png1_1.image(sf.select_photo(t1_player[0]), use_column_width='auto')
    #Team1 2 riga
    team1_2.selectbox(label='Player2',options= top30['NAME_PLAYER'], index=0, key='player_2')
    t1_player[1] = st.session_state.player_2
    png1_2.write(' ')
    png1_2.write(' ')
    png1_2.image(sf.select_photo(t1_player[1]), use_column_width='auto')
    #Team1 3 riga
    team1_3.selectbox(label='Player3',options= top30['NAME_PLAYER'], index=0, key='player_3')
    t1_player[2] = st.session_state.player_3
    png1_3.write(' ')
    png1_3.write(' ')
    png1_3.image(sf.select_photo(t1_player[2]), use_column_width='auto')
    #Team1 4 riga
    team1_4.selectbox(label='Player4',options= top30['NAME_PLAYER'], index=0, key='player_4')
    t1_player[3] = st.session_state.player_4
    png1_4.write(' ')
    png1_4.write(' ')
    png1_4.image(sf.select_photo(t1_player[3]), use_column_width='auto')
    #Team1 5 riga
    team1_5.selectbox(label='Player5',options= top30['NAME_PLAYER'], index=0, key='player_5')
    t1_player[4] = st.session_state.player_5
    png1_5.write(' ')
    png1_5.write(' ')
    png1_5.image(sf.select_photo(t1_player[4]), use_column_width='auto')

    team2.write('**TEAM 2**')    
    #Team2 1 riga
    team2_1.selectbox(label='Player1',options= top30['NAME_PLAYER'], index=0, key='player_6')
    t2_player[0] = st.session_state.player_6
    png2_1.write(' ')
    png2_1.write(' ')
    png2_1.image(sf.select_photo(t2_player[0]), use_column_width='auto')
    #Team2 2 riga
    team2_2.selectbox(label='Player2',options= top30['NAME_PLAYER'], index=0, key='player_7')
    t2_player[1] = st.session_state.player_7
    png2_2.write(' ')
    png2_2.write(' ')
    png2_2.image(sf.select_photo(t2_player[1]), use_column_width='auto')
    #Team2 3 riga
    team2_3.selectbox(label='Player3',options= top30['NAME_PLAYER'], index=0, key='player_8')
    t2_player[2] = st.session_state.player_8
    png2_3.write(' ')
    png2_3.write(' ')
    png2_3.image(sf.select_photo(t2_player[2]), use_column_width='auto')
    #Team2 4 riga
    team2_4.selectbox(label='Player4',options= top30['NAME_PLAYER'], index=0, key='player_9')
    t2_player[3] = st.session_state.player_9
    png2_4.write(' ')
    png2_4.write(' ')
    png2_4.image(sf.select_photo(t2_player[3]), use_column_width='auto')
    #Team2 5 riga
    team2_5.selectbox(label='Player5',options= top30['NAME_PLAYER'], index=0, key='player_10')
    t2_player[4] = st.session_state.player_10
    png2_5.write(' ')
    png2_5.write(' ')
    png2_5.image(sf.select_photo(t2_player[4]), use_column_width='auto')

    if y.button('Run',on_click=check_error): #elimina il contenuto visivo della pagina per far posto a quello finale
        phc0.empty()
        phc1.empty()
        phc2.empty()
        phc3.empty()
        phc4.empty()
        phc5.empty()
        phc_b.empty()
        sf.final_page(t1_player, t2_player)
        x,y,z = st.columns([3,1,3])
        if(y.button('Restart',key='b_1')):
            st.cache_resource.clear()
            st.cache_data.clear()
            main()
        
if __name__=="__main__":
    main()            
