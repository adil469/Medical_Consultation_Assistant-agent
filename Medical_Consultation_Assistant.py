from agents import Agent, RunContextWrapper, Runner,trace
from connection import config
from pydantic import BaseModel
import rich
import asyncio
from dotenv import load_dotenv

load_dotenv()

# ------------------ Exercise 1 ------------------ #
# Medical Consultation Assistant (Intermediate)
# Requirement: Create a dynamic instructions system for a medical consultation agent 
# that adapts based on user_type.
# Patient: Use simple, non-technical language. Explain medical terms in everyday words. 
# Be empathetic and reassuring. 
# Medical Student: Use moderate medical terminology with explanations. Include learning opportunities. 
# Doctor: Use full medical terminology, abbreviations, and clinical language. Be concise and professional.

# ------------- Dynamic Context -------------

class Person(BaseModel):
    person : str
# ----------  a function to identify default role from user input -----------------
def detect_role(user_input: str) -> Person:
    """Detects role from the user input text."""
    text = user_input.lower()
    if "patient" in text:
        return Person(person="patient")
    elif "medical student" in text or "student" in text:
        return Person(person="medical student")
    elif "doctor" in text:
        return Person(person="doctor")
    else:
        return "user please use valid type.patient, medical student or doctor."
    
# ------------------ a dynamic function according to user prompt and picks correct user ------------

def dynamic_medical_assistant(ctx: RunContextWrapper[Person], agents:Agent):
    role = ctx.context.person.lower()
    if "patient" in role: 
        return """
           explain to a patient use simple, non-technical language. Explain medical terms in everyday words.
           Be empathetic and reassuring."""
    elif "medical student" in role:
        return """
          Use moderate medical terminology with clear explanations, 
          and include learning opportunities for the medical student.
        """
    elif "doctor" in role:
        return """
          Use full medical terminology, abbreviations, and clinical 
          language. Be concise and professional .
        """
    else:
        return "Please input a valid type: patient, medical student, or doctor."

triage_Agent = Agent(
    name = "triage agent",
    instructions = dynamic_medical_assistant # Dynamic function that adjusts instructions by role
)

#user prompt
# prompt1 = "explain high blood pressure to a patient in very few words."
# prompt2 = "i am a medical student.explain blood sugar."
# prompt3 = "I am a doctor. Please explain blood sugar in professional medical terms."

async def main():
    user_prompt = input('write your prompt: ')  # change this to try different prompts
    detected_role = detect_role(user_prompt)  #  fix: call the function

    with trace("Dynamic instructions"):
        result = await Runner.run(
            triage_Agent,
            input=user_prompt,
            run_config=config,
            context=detected_role  #  pass Person object
        
    )
    rich.print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())