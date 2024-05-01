from fastapi import FastAPI, HTTPException,Request
from pydantic import BaseModel
from typing import List
import json
from matchmaking_algorithm import dynamic_grouping_based_on_performance

app = FastAPI()

@app.post("/group-teams")
async def group_teams(request: Request, num_teams: int = 2):
   
    try:
        teams = await request.json()
        matched_teams = dynamic_grouping_based_on_performance(teams, num_teams)
        return matched_teams
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))