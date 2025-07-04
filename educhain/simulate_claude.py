# This script bascially tells how Claude Desktop would send to MCP Server
# and prints both requests and formatted response.

# importing necessary libraries
import requests
import json
from datetime import datetime

# creating a log file
with open("Sample_Responses.txt", "w") as log:
    log.write(f"Sample MCP Responses Log\nGenerated on: {datetime.now()}\n\n") 

# function to make POST request and display results

def test_endpoint(title,url,payload):
    print(f"\n Calude Prompt: {title}")
    print(f"Request Sent to: {url}")
    print(f"Payload: \n{json.dumps(payload, indent=2)}")
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        data = response.json()

        print("\n Response Recieved: \n")
        print(json.dumps(data, indent=2))

        # saving each result to a file
        file_name = title.lower().replace(" ","_").replace(":","") + "_response.json"
        with open(file_name,"w") as f:
            json.dump(data, f, indent=2)
        print(f"\n Response saved to: {file_name}")

        # log to Sample_Responses.txt
        with open("Sample_Responses.txt", "a") as log:
            log.write("=" * 50 + "\n")
            log.write(f"Prompt: {title}\n")
            log.write(f"Endpoint: {url}\n")
            log.write(f"Payload:\n{json.dumps(payload, indent=2)}\n")
            log.write("Response Summary:\n")
            # general summary
            if "questions" in data:
                log.write(f"- {len(data['questions'])} MCQs generated\n")
                log.write(f"- Sample Question: {data['questions'][0].get('question', 'N/A')}\n")
            elif "title" in data:
                log.write(f"- Lesson Title: {data.get('title', 'N/A')}\n")
                log.write(f"- Grade Level: {data.get('grade_level', 'N/A')}\n")
            else:
                log.write("- Response structure unknown (see JSON file)\n")

            log.write(f"Saved to: {file_name}\n\n")

    except requests.exceptions.RequestException as e:
        print(f"Request Failed: {e}")
        with open("Sample_Responses.txt", "a") as log:
            log.write(f"\n ERROR for prompt '{title}': {e}\n")

# simulating Claude command 1: Generate MCQs

mcq_prompt = "Generate 5 multiple-choice questions on Python loops."
mcq_payload = {
    "topic": "Python loops",
    "num": 5
}
test_endpoint(mcq_prompt, "http://127.0.0.1:8000/generate_mcqs", mcq_payload)

# simulating Claude command 2: Generate Lesson Plan

lesson_prompt = "Provide a lesson plan for teaching algebra."
lesson_payload = {
    "topic": "Algebra",
    "grade_level": "9",
    "custom_instructions": "Make it interactive with real-world examples"
}
test_endpoint(lesson_prompt, "http://127.0.0.1:8000/lesson_plan", lesson_payload)

# Simulating claude command 3: Generate Flashcards

flashcard_prompt = "Generate flashcards on Machine Learning"
flashcard_payload = {
    "topic": "Machine Learning",
    "difficulty_level": "Intermediate"
}
test_endpoint(flashcard_prompt, "http://127.0.0.1:8000/generate_flashcards", flashcard_payload)


