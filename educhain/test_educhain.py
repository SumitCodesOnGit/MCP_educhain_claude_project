# importing core Educhain class containing required functionalities
from educhain.core.educhain import Educhain
from pydantic import BaseModel
import json

# initializing educhain
edu = Educhain()

# generating 5 questions on the sample topic
questions = edu.get_qna_engine().generate_questions(
    topic = "Python Programming Basics",
    num = 5,
    question_type = 'Multiple Choice'
)

# printing questions
print("\n Generataed MCQs: \n")
for i, q in enumerate(questions.questions, 1):
    print(f"Q{i}: {q.question}")
    for j, opt in enumerate(q.options, 1):
        print(f" {chr( 64 + j)}. {opt}")
    print(f" Answer: {q.answer}")
    print("-" * 50)

# For MCP use, converting to JSON and save/export
if isinstance(questions, BaseModel):
    mcq_data = questions.model_dump()   # dict
    mcq_json = json.dumps(mcq_data, indent=2)

    print("\n JSON-Formatted MCQs (MCP-Ready):\n")
    print(mcq_json)

    # Optional: Save to file
    with open("mcq_output.json", "w") as f:
        f.write(mcq_json)
else:
    print("⚠ Unexpected format: EduChain output is not a Pydantic model")








