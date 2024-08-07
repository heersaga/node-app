# analyze_logs.py
import google.generativeai as genai
import os
import sys
import json

# Configure API key
genai.configure(api_key=os.environ["API_KEY"])

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
response = model.generate_content(f"Analyze the following logs for issues:\n\n{logs}")

# Print or handle the response
print(response.text)
