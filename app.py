from fastapi import FastAPI, Path
from typing import Optional #cleaner code - better to use this- check where I have used this Optional in the program, you can understand

app = FastAPI()

players = {
    1:{
        "name": "Cristiano Ronaldo",
        "age" : 35,
        "team" : "Manchester United",
        "is_elite" : True,
     },
     2:{
        "name": "Lionel Messi",
        "age" : 33,
        "team" : "PSG",
        "is_elite" : True,
     }
}

@app.get("/")
def home():
    return {"Hello": "World"}

@app.get("/allplayers")
def all_players():
    return players

#Path Parameter - to retrieve player using playerID ie Key in Dict
@app.get("/player/{player_id}")
def player_one(player_id:int = Path(None, description= "The ID of player that you want to view", gt=0, lt=3)):
    return players[player_id]

#Query Parameter - to retrieve player using playername
@app.get("/player_name")
def player_name(name: Optional[str] = None):
    for player_id in players:
        if players[player_id]["name"] == name:
            return players[player_id]
    return {"Data": "Player Not found"}