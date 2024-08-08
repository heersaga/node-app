# analyze_logs.py
import google.generativeai as genai
import os
import sys
import json

# Configure API key
#genai.configure(api_key="AIzaSyCQPJji0ojWd-UuWmwYeF0")
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("API key not found. Please set the GEMINI_API_KEY environment variable.")

genai.configure(api_key=api_key)

# Initialize the model
model = genai.GenerativeModel('gemini-1.5-flash')

# Read logs from stdin or a file
if len(sys.argv) > 1:
    log_file = sys.argv[1]
    with open(log_file, 'r') as f:
        logs = f.read()
else:
    logs = sys.stdin.read()

# Generate analysis
response = model.generate_content(f"Analyze the following logs for issues and what was the command that made pipeline failed:\n\n{logs}")

# Print or handle the response
print(response.text)
