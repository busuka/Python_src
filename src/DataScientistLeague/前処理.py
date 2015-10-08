import pandas as pd


def main():

    #2014年度のファイルを開く.(標準入出力)
    f = open("./DataScientistLeague/2014_J1_Scorer.csv","r",encoding="CP932")
    Score14  = f.read()
    f = open("./DataScientistLeague/2014_J1_CBP.csv","r",encoding="CP932")
    CBP14    = f.read()
    f = open("./DataScientistLeague/2014_J1_Result.csv","r",encoding="CP932")
    Game14   = f.read()

    #Pandasを用いてファイルを開く(DataFrameに変換する)
    Score14 = pd.read_csv("./DataScientistLeague/2014_J1_Scorer.csv",encoding="CP932")
    CBP14   = pd.read_csv("./DataScientistLeague/2014_J1_CBP.csv",encoding="CP932")
    Game14  = pd.read_csv("./DataScientistLeague/2014_J1_Result.csv",encoding="CP932")

    #インデックスの名前を変更する.

    Game14.columns  = ["gameID","date","cupID","chapter","homeID","hometeam","home",
                       "awayID","awayteam","away","homescore","awayscore"]

    Score14.columns = ["gameID","historyNo","teamID","teamname","team",
                       "playerID","playername","action"]

    CBP14.columns   = ["gameID","year","date","kind","chapter","HA","teamID",
                       "team","result","playerID","playername","Pos","No",
                       "Of_time","Ac_time","part","start","start_Pos","shoot_CBP",
                       "pass_CBP","cross_CBP","dribble_CBP","offence_CBP",
                       "defence_CBP","save_CBP"]


if __name__ == "__main__":
    main()