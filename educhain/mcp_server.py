# import necessary libraries
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from educhain.core.educhain import Educhain
from educhain.engines.qna_engine import MCQList
from educhain.engines.content_engine import LessonPlan

# initialize FastAPI
app = FastAPI(title='Educhain MCP Server')

# initialize educhain
edu = Educhain()

# Tool: Generate MCQs

class MCQRequest(BaseModel):
    topic: str
    num: int = 5

@app.post("/generate_mcqs")
def generate_mcqs(req: MCQRequest):
    try:
        questions: MCQList = edu.get_qna_engine().generate_questions(
            topic = req.topic,
            num = req.num,
            question_type="Multiple Choice"
        )
        return questions.model_dump()
    except Exception as e:
        return {"error": str(e)}
    


# Resource: Generate Lesson Plan

class LessonPlanRequest(BaseModel):
    topic: str
    grade_level: Optional[str] = None
    custom_instructions: Optional[str] = None

@app.post("/lesson_plan")
def generate_lesson_plan(req: LessonPlanRequest):
    try:
        plan: LessonPlan = edu.get_content_engine().generate_lesson_plan(
            topic = req.topic,
            grade_level = req.grade_level,
            custom_instructions = req.custom_instructions
        )
        return plan.model_dump()
    except Exception as e:
        return {"error": str(e)}
    

# Tool 3: Generate Flashcards

class FlashcardRequest(BaseModel):
    topic: str
    difficulty_level: str = "Intermediate"

@app.post("/generate_flashcards")
def generate_flashcards(req: FlashcardRequest):
    content_engine = edu.get_content_engine()
    result = content_engine.generate_flashcards(
        topic = req.topic,
        difficulty_level = req.difficulty_level
    )
    return result.model_dump() if hasattr(result, "model_dump") else result
    


# Health Check

@app.get("/")
def root():
    return {"message": "Educhain MCP Server is running."}







