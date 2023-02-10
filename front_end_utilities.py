import streamlit as st
import pandas as pd
from PIL import Image
import time
import back_end as be

top30 = pd.read_csv(r"./dataset/lista_giocatori_front_end.csv") #lista in cui sono messi i giocatori

def select_photo(player): #switch che seleziona le immagini dei giocatori
    if(player == top30.loc[1,"NAME_PLAYER"]):
        return Image.open(r"./photo/LBJ_photo.png")
    if(player == top30.loc[2,"NAME_PLAYER"]):
        return Image.open(r"./photo/SC_photo.png")
    if(player == top30.loc[3,"NAME_PLAYER"]):
        return Image.open(r"./photo/KD_photo.png")
    if(player == top30.loc[4,"NAME_PLAYER"]):
        return Image.open(r"./photo/KL_photo.png")
    if(player == top30.loc[5,"NAME_PLAYER"]):
        return Image.open(r"./photo/GA_photo.png")
    if(player == top30.loc[6,"NAME_PLAYER"]):
        return Image.open(r"./photo/KB_photo.png")
    if(player == top30.loc[7,"NAME_PLAYER"]):
        return Image.open(r"./photo/DW_photo.png")
    if(player == top30.loc[8,"NAME_PLAYER"]):
        return Image.open(r"./photo/DN_photo.png")
    if(player == top30.loc[9,"NAME_PLAYER"]):
        return Image.open(r"./photo/JH_photo.png")
    if(player == top30.loc[10,"NAME_PLAYER"]):
        return Image.open(r"./photo/TD_photo.png")
    if(player == top30.loc[11,"NAME_PLAYER"]):
        return Image.open(r"./photo/CP_photo.png")
    if(player == top30.loc[12,"NAME_PLAYER"]):
        return Image.open(r"./photo/RW_photo.png")
    if(player == top30.loc[13,"NAME_PLAYER"]):
        return Image.open(r"./photo/DM_photo.png")
    if(player == top30.loc[14,"NAME_PLAYER"]):
        return Image.open(r"./photo/KI_photo.png")
    if(player == top30.loc[15,"NAME_PLAYER"]):
        return Image.open(r"./photo/AD_photo.png")
    if(player == top30.loc[16,"NAME_PLAYER"]):
        return Image.open(r"./photo/PG_photo.png")
    if(player == top30.loc[17,"NAME_PLAYER"]):
        return Image.open(r"./photo/JM_photo.png")
    if(player == top30.loc[18,"NAME_PLAYER"]):
        return Image.open(r"./photo/KT_photo.png")
    if(player == top30.loc[19,"NAME_PLAYER"]):
        return Image.open(r"./photo/DH_photo.png")
    if(player == top30.loc[20,"NAME_PLAYER"]):
        return Image.open(r"./photo/PAG_photo.png")
    if(player == top30.loc[21,"NAME_PLAYER"]):
        return Image.open(r"./photo/DR_photo.png")
    if(player == top30.loc[22,"NAME_PLAYER"]):
        return Image.open(r"./photo/CA_photo.png")
    if(player == top30.loc[23,"NAME_PLAYER"]):
        return Image.open(r"./photo/LA_photo.png")
    if(player == top30.loc[24,"NAME_PLAYER"]):
        return Image.open(r"./photo/KLO_photo.png")
    if(player == top30.loc[25,"NAME_PLAYER"]):
        return Image.open(r"./photo/DG_photo.png")
    if(player == top30.loc[26,"NAME_PLAYER"]):
        return Image.open(r"./photo/TP_photo.png")
    if(player == top30.loc[27,"NAME_PLAYER"]):
        return Image.open(r"./photo/AI_photo.png")
    if(player == top30.loc[28,"NAME_PLAYER"]):
        return Image.open(r"./photo/MG_photo.png")
    if(player == top30.loc[29,"NAME_PLAYER"]):
        return Image.open(r"./photo/KLOW_photo.png")
    if(player == top30.loc[30,"NAME_PLAYER"]):
        return Image.open(r"./photo/MAG_photo.png")
    return Image.open(r"./photo/white.png")

def trans_to_result():  #funzione che abbellisce la transizione
    my_bar = st.empty()
    my_bar.progress(0)
    for progress_range in range(100):
        time.sleep(0.001)
        my_bar.progress(progress_range + 1)
    st.balloons()
    my_bar.empty()
    

def who_win(res):  #funzione che ha il compito di mostrare il vincitore
    t1 = []
    t2 = []
    for i in range(10): #divide della lista contenente i risultati
        if(i < 5):
            t1.append(res[i])
        else:
            t2.append(res[i])
    png1_res, team1_res, pts1_res, pts2_res, team2_res, png2_res = st.columns([1,3,1,1,3,1])
    if(sum(t1) == sum(t2)):  #possono essere uguali
        st.info('Non può succedere, ma è successo. Hai fortuna o sfortuna, dipende dai punti di vista....')
    else:
        if(sum(t1) > sum(t2)): 
           png1_res.image(Image.open(r"./photo/win.png")) 
           team1_res.write('**WINNER**')
           pts1_res.write(' ')
           pts1_res.write(' ')
           pts1_res.write(f"""
                        <style>
                        p.a {{
                            font: bold 30px Courier;
                            }}
                        </style>
                        <p class="a">{sum(t1)}</p>
                        """, unsafe_allow_html = True)
           png2_res.image(Image.open(r"./photo/lose.png"))             
           team2_res.write('**LOSER**')
           pts2_res.write(' ')
           pts2_res.write(' ')
           pts2_res.write(f"""
                        <style>
                        p.a {{
                            font: bold 30px Courier;
                            }}
                        </style>
                        <p class="a">{sum(t2)}</p>
                        """, unsafe_allow_html = True)
        else:
            png2_res.image(Image.open(r"./photo/win.png")) 
            team2_res.write('**WINNER**')
            pts2_res.write(' ')
            pts2_res.write(' ')
            pts2_res.write(f"""
                         <style>
                         p.a {{
                             font: bold 30px Courier;
                             }}
                         </style>
                         <p class="a">{sum(t2)}</p>
                         """, unsafe_allow_html = True)
            png1_res.image(Image.open(r"./photo/lose.png"))             
            team1_res.write('**LOSER**')
            pts1_res.write(' ')
            pts1_res.write(' ')
            pts1_res.write(f"""
                         <style>
                         p.a {{
                             font: bold 30px Courier;
                             }}
                         </style>
                         <p class="a">{sum(t1)}</p>
                         """, unsafe_allow_html = True)
    

def final_page(player1,player2): #pagina finale statica con i risultati
    
    res = be.predict_score(player1,player2) #chiamata alla predizione
    
    trans_to_result()
    
    png1, team1, pts1, pts2, team2, png2 = st.columns([1,3,1,1,3,1]) 
    png1_1, team1_1, pts1_1, pts2_1, team2_1, png2_1 = st.columns([1,3,1,1,3,1])
    png1_2, team1_2, pts1_2, pts2_2, team2_2, png2_2 = st.columns([1,3,1,1,3,1])
    png1_3, team1_3, pts1_3, pts2_3, team2_3, png2_3 = st.columns([1,3,1,1,3,1])
    png1_4, team1_4, pts1_4, pts2_4, team2_4, png2_4 = st.columns([1,3,1,1,3,1])
    png1_5, team1_5, pts1_5, pts2_5, team2_5, png2_5 = st.columns([1,3,1,1,3,1])
    
    team1.write('**TEAM 1**')    
    #Team1 1 riga
    png1_1.write(' ')
    png1_1.write(' ')
    png1_1.image(select_photo(player1[0]), use_column_width='auto')
    team1_1.text_input(label='Player1', key='player_11', placeholder=player1[0], disabled=True )
    pts1_1.write(' ')
    pts1_1.write(' ')
    pts1_1.write(f"""
                 <style>
                 p.a {{
                     font: bold 30px Courier;
                     }}
                 </style>
                 <p class="a">{res[0]}</p>
                 """, unsafe_allow_html = True)
    #Team1 2 riga
    png1_2.write(' ')
    png1_2.write(' ')
    png1_2.image(select_photo(player1[1]), use_column_width='auto')
    team1_2.text_input(label='Player2', key='player_12', placeholder=player1[1], disabled=True)
    pts1_2.write(' ')
    pts1_2.write(' ')
    pts1_2.write(f"""
                 <style>
                 p.a {{
                     font: bold 30px Courier;
                     }}
                 </style>
                 <p class="a">{res[1]}</p>
                 """, unsafe_allow_html = True)
    #Team1 3 riga
    png1_3.write(' ')
    png1_3.write(' ')
    png1_3.image(select_photo(player1[2]), use_column_width='auto')
    team1_3.text_input(label='Player3', key='player_13', placeholder=player1[2], disabled=True)
    pts1_3.write(' ')
    pts1_3.write(' ')
    pts1_3.write(f"""
                 <style>
                 p.a {{
                     font: bold 30px Courier;
                     }}
                 </style>
                 <p class="a">{res[2]}</p>
                 """, unsafe_allow_html = True)
    #Team1 4 riga
    png1_4.write(' ')
    png1_4.write(' ')
    png1_4.image(select_photo(player1[3]), use_column_width='auto')
    team1_4.text_input(label='Player4', key='player_14', placeholder=player1[3], disabled=True)
    pts1_4.write(' ')
    pts1_4.write(' ')
    pts1_4.write(f"""
                 <style>
                 p.a {{
                     font: bold 30px Courier;
                     }}
                 </style>
                 <p class="a">{res[3]}</p>
                 """, unsafe_allow_html = True)
    #Team1 5 riga
    png1_5.write(' ')
    png1_5.write(' ')
    png1_5.image(select_photo(player1[4]), use_column_width='auto')
    team1_5.text_input(label='Player5', key='player_15', placeholder=player1[4], disabled=True)
    pts1_5.write(' ')
    pts1_5.write(' ')
    pts1_5.write(f"""
                 <style>
                 p.a {{
                     font: bold 25px Courier;
                     }}
                 </style>
                 <p class="a">{res[4]}</p>
                 """, unsafe_allow_html = True)

    team2.write('**TEAM 2**')    
    #Team2 1 riga
    png2_1.write(' ')
    png2_1.write(' ')
    png2_1.image(select_photo(player2[0]), use_column_width='auto')
    team2_1.text_input(label='Player1', key='player_16', placeholder=player2[0], disabled=True)
    pts2_1.write(' ')
    pts2_1.write(' ')
    pts2_1.write(f"""
                 <style>
                 p.a {{
                     font: bold 30px Courier;
                     }}
                 </style>
                 <p class="a">{res[5]}</p>
                 """, unsafe_allow_html = True)
    #Team2 2 riga
    png2_2.write(' ')
    png2_2.write(' ')
    png2_2.image(select_photo(player2[1]), use_column_width='auto')
    team2_2.text_input(label='Player2', key='player_17', placeholder=player2[1], disabled=True)
    pts2_2.write(' ')
    pts2_2.write(' ')
    pts2_2.write(f"""
                 <style>
                 p.a {{
                     font: bold 30px Courier;
                     }}
                 </style>
                 <p class="a">{res[6]}</p>
                 """, unsafe_allow_html = True)
    #Team2 3 riga
    png2_3.write(' ')
    png2_3.write(' ')
    png2_3.image(select_photo(player2[2]), use_column_width='auto')
    team2_3.text_input(label='Player3', key='player_18', placeholder=player2[2], disabled=True)
    pts2_3.write(' ')
    pts2_3.write(' ')
    pts2_3.write(f"""
                 <style>
                 p.a {{
                     font: bold 30px Courier;
                     }}
                 </style>
                 <p class="a">{res[7]}</p>
                 """, unsafe_allow_html = True)
    #Team2 4 riga
    png2_4.write(' ')
    png2_4.write(' ')
    png2_4.image(select_photo(player2[3]), use_column_width='auto')
    team2_4.text_input(label='Player4', key='player_19', placeholder=player2[3], disabled=True)
    pts2_4.write(' ')
    pts2_4.write(' ')
    pts2_4.write(f"""
                 <style>
                 p.a {{
                     font: bold 30px Courier;
                     }}
                 </style>
                 <p class="a">{res[8]}</p>
                 """, unsafe_allow_html = True)
    #Team2 5 riga
    png2_5.write(' ')
    png2_5.write(' ')
    png2_5.image(select_photo(player2[4]), use_column_width='auto')
    team2_5.text_input(label='Player5', key='player_20', placeholder=player2[4], disabled=True)
    pts2_5.write(' ')
    pts2_5.write(' ')
    pts2_5.write(f"""
                 <style>
                 p.a {{
                     font: bold 30px Courier;
                     }}
                 </style>
                 <p class="a">{res[9]}</p>
                 """, unsafe_allow_html = True)
    
    who_win(res) #chiamata alla funzione che determina il vincitore
