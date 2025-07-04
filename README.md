This Project/Assigment showcases an MCP (Modular Content Provider) server built using Educhain library. The Server is designed to generate
educational content like MCQs, lesson plans, and flashcards, and expose them as tools for integration with platform like Claude Desktop.

Features:
a. Built using FastAPI + Educhain
b. Integrated with OpenAI API
c. 3 Working Tools: MCQ Generator, Lesson Plan Generator & Flashcard Generator

It simulates Claude Desktop requests via simulate_claude.py.
Outputs saved as .json and summarize in Sample_Responses.txt

Project Structure: mcp_educhain_claude_project/educhain
1. educhain/ : Educhain source code (provided and required)
2. test_educhain.py - Task 1 for Educhain
3. mcp_server.py - MCP FastAPI server for Task 2
4. simulate_claude.py -Task 3 showing simulation of Claude prompts
5. claude_desktop_config.json - simulated claude config file
6. Sample_Responses.txt - Combined response log
7. *.json - generated content file
8. .env - OpenAI API Key - have just added dotenv in config.py in educhain/core/config.py for accessing key
9. Readme.md - Documentation

How to run?
1. Install all dependencies in activated environment (I have used venv, there is no particular requirements.txt file)
2. Add your openAI key in .env file.
3. Run MCP Server - uvicorn mcp_server:app --reload (Check http://127.0.0.1:8000/docs to test endpoints - can be checked using Swagger UI)
4. Simulate Claude Desktop - in activated environment run python simulate_claude.py. This will hit all 3 endpoints, save json content file and update Sample_Responses.txt

Credits:
1. Educhain library by Satvik314.
2. ChatGPT by OpenAI for code suggestions and error resolution. All implementation and integration work were done manually.

Final Note:
All deliverables are available in this repo. including json files and sample responses. Bonus feature - Flashcard Generation is also included.

   









     

