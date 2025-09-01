from agents import Agent, RunContextWrapper, Runner,trace
from connection import config
from pydantic import BaseModel
import rich
import asyncio
from dotenv import load_dotenv

load_dotenv()

#          Exercise 2: Airline Seat Preference Agent (Intermediate-Advanced)

# Requirement: Build a dynamic instructions system for an airline booking agent 
# that customizes responses based on seat_preference and travel_experience.

# Window + First-time: Explain window benefits, mention scenic views, reassure about flight experience 
# Middle + Frequent: Acknowledge the compromise, suggest strategies, offer alternatives 
# Any + Premium: Highlight luxury options, upgrades, priority boarding

# Context Fields: seat_preference (window/aisle/middle/any), 
# travel_experience  (first_time/occasional/frequent/premium)

class ASP(BaseModel):
    name : str = "adil"
    seat_pref : str
    travel_experiance : str
    
def seat_prf(exp:str):
    if "first time" in exp:
        return ASP(seat_pref="window",travel_experiance="first time")
    
    elif "occasional" in exp:
        return ASP(seat_pref="aisle",travel_experiance="occasional")
    
    elif "frequent" in exp:
        return ASP(seat_pref="middle",travel_experiance="frequent")
    
    elif "premium" in exp:
        return ASP(seat_pref="any",travel_experiance="premium")
    else:
        return "explain airline options and benefits"
# asp = ASP(seat_pref="any",travel_experiance="premium")

def traveler_requirments(ctx:RunContextWrapper[ASP],agent:Agent):
    seat = ctx.context.seat_pref
    exp = ctx.context.travel_experiance

    if seat == "window" and exp == "first time":
        return "Explain window benefits, mention scenic views, reassure about flight experience"
    
    elif (seat == "middle" and exp == "frequent") or (seat == "aisle" and exp == "occasional"):
        return "Acknowledge the compromise, suggest strategies, offer alternatives "
    
    elif seat == "any" or exp == "premium":
        return "Highlight luxury options, upgrades, priority boarding"
    
    else:
        return "explain airline fasility to passenger"



triage_agent = Agent(
    name = "triage agent",
    instructions = traveler_requirments
)

async def main():
    with trace("Dynamic instructions(LLM Context)"):
        
        exp_input = input("""HELLO GUEST\nPlease provide us your travel experiance
                          (first_time/occasional/frequent/premium): """)
        input_field = seat_prf(exp_input)

        result = await Runner.run(
            triage_agent,
            input=exp_input,
            run_config = config,
            context = input_field
    )
    rich.print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())