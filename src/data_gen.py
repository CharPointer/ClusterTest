import google.generativeai as genai
import os
import time

folder = "data"
api_key = "niuniuniu"

# 1. Configure API key
genai.configure(api_key=api_key)

# 2. Choose model
model = genai.GenerativeModel("gemini-2.5-flash-lite")  

# 3. Your prompt
prompt = """
Write a dummy legal document in Lithuanian, several hundred words long. Your entire response must be the document, and nothing else - no narration of any kind. Make any kind of dummy legal document - court, fine, agreement, whatever, not just a specific kind. One document per response. 
"""

for _ in range(30):
    # 4. Generate response
    response = model.generate_content(prompt)

    # 5. Extract text
    output_text = response.text

    # 6. Save to file
    num_files = sum(
    1 for entry in os.scandir(folder) if entry.is_file()
    )
    with open(f"data/{num_files+1}.txt", "w", encoding="utf-8") as f:
        f.write(output_text)

    print(f"Response saved to data/{num_files+1}.txt")
    time.sleep(10)