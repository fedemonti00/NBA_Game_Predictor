import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
import string

#Estraggo le informazioni che serviranno nella deserializzazione dei risultati
d = pd.read_csv(r"C:\Users\fedem\Desktop\ML_Barbon_project\Test_numeric.csv")
d_min = d.PTS.min()
d_max = d.PTS.max()

#Dichiaro i 'contenitori' dei nosti dataset
players = [0,0,0,0,0,0,0,0,0,0]
dataset = [0,0,0,0,0,0,0,0,0,0]
merge_data = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
temp_res = [0,0,0,0,0] #contenitore risultati singolo giocatore
f_res = [0,0,0,0,0,0,0,0,0,0] #contenitore risultati finali float
res = [] #contenitore risultati finali int



#funzione che ha il compito di calcolare i punteggi dei giocatori
def predict_score(t1_player,t2_player):
    
    for i in range(5): #merging dei due array in un unico array per ridurre il quantitativo di codice e semplificare
        players[i] = t1_player[i]  #la leggibilità del codice
        players[i+5] = t2_player[i]

    for i in range(10): #estrazione dei dataset
        dataset[i] = pd.read_csv(r'C:\Users\fedem\Desktop\ML_Barbon_project\Dataset' + players[i].translate({ord(c): None for c in string.whitespace}) + '.csv')
    
    for j in range(5):  #merging dei vari dataset
        for i in range(5):
            merge_data[i+5*j] = dataset[j].merge(dataset[i+5],left_on='GAME_ID',right_on='GAME_ID')
    
    for j in range(10): #calcolo del punteggio per ogni giocatore
        np = players[j].translate({ord(c): None for c in string.whitespace})
        X = dataset[j][['PTS_home_'+np,'FG_PCT_home_'+np,'FT_PCT_home_'+np,'FG3_PCT_home_'+np,'AST_home_'+np,'REB_home_'+np,'PTS_away_'+np,'FG_PCT_away_'+np,'FT_PCT_away_'+np,'FG3_PCT_away_'+np,'AST_away_'+np,'REB_away_'+np,'MIN_'+np,'FGM_'+np,'FGA_'+np,'FG_PCT_'+np,'FG3M_'+np,'FG3A_'+np,'FG3_PCT_'+np,'FTM_'+np,'FTA_'+np,'FT_PCT_'+np,'OREB_'+np,'DREB_'+np,'REB_'+np,'AST_'+np,'STL_'+np,'BLK_'+np,'TO_'+np,'PF_'+np,'PLUS_MINUS_'+np]] #parametri in ingresso
        y = dataset[j][['PTS_'+np]] #risultato predetto
        #fase di apprendimento, creazione del modello
        x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.26, random_state=0)
        knn = KNeighborsRegressor(n_neighbors = 7)
        knn.fit(x_train, y_train) 
        y_pred = knn.predict(x_test)
            
        for i in range(5): #fase di predizione per singolo giocatore
            if(j < 5):
                X_res = merge_data[i+5*j][['PTS_home_'+np,'FG_PCT_home_'+np,'FT_PCT_home_'+np,'FG3_PCT_home_'+np,'AST_home_'+np,'REB_home_'+np,'PTS_away_'+np,'FG_PCT_away_'+np,'FT_PCT_away_'+np,'FG3_PCT_away_'+np,'AST_away_'+np,'REB_away_'+np,'MIN_'+np,'FGM_'+np,'FGA_'+np,'FG_PCT_'+np,'FG3M_'+np,'FG3A_'+np,'FG3_PCT_'+np,'FTM_'+np,'FTA_'+np,'FT_PCT_'+np,'OREB_'+np,'DREB_'+np,'REB_'+np,'AST_'+np,'STL_'+np,'BLK_'+np,'TO_'+np,'PF_'+np,'PLUS_MINUS_'+np]]
                norm_res = knn.predict(X_res)
            else:
                X_res = merge_data[5*i+(j-5)][['PTS_home_'+np,'FG_PCT_home_'+np,'FT_PCT_home_'+np,'FG3_PCT_home_'+np,'AST_home_'+np,'REB_home_'+np,'PTS_away_'+np,'FG_PCT_away_'+np,'FT_PCT_away_'+np,'FG3_PCT_away_'+np,'AST_away_'+np,'REB_away_'+np,'MIN_'+np,'FGM_'+np,'FGA_'+np,'FG_PCT_'+np,'FG3M_'+np,'FG3A_'+np,'FG3_PCT_'+np,'FTM_'+np,'FTA_'+np,'FT_PCT_'+np,'OREB_'+np,'DREB_'+np,'REB_'+np,'AST_'+np,'STL_'+np,'BLK_'+np,'TO_'+np,'PF_'+np,'PLUS_MINUS_'+np]]
                norm_res = knn.predict(X_res)
            temp_res[i] = (norm_res*(d_max - d_min) + d_min).mean() #media dei punteggi del singolo giocatore
        f_res[j] = round((sum(temp_res) / len(temp_res)), 0) #punteggi finali float
    for k in f_res:
        res.append(int(k))
        
    return res #ritorno dei punteggi finali

                