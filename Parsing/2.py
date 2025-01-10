import re

# Define the input string
input_string = """
candidates {
  content {
    role: "model"
    parts {
      text: "## Cloud Computing Study Plan - January 16th to March 10th\\n\\n*Green computing\\n\\n Week 1: Study basics of energy-efficient cloud services. (2 hours)\\n* Week 2: Learn about server consolidation and power management tools. (2 hours)\\n* Week 3: Analyze your own cloud-usage habits for energy efficiency. (2 hours)\\n\\n*Dew computing and edge computing\\n\\n Week 4: Study concepts like dew and edge computing. (2 hours)\\n* Week 5: Explore the role of fog computing in cloud architectures. (2 hours)\\n* Week 6: Identify potential use cases for dew and edge computing. (2 hours)\\n\\n*GIS using the cloud\\n\\n Week 7: Research how GIS can be implemented on cloud platforms. (2 hours)\\n* Week 8: Study data storage and processing options for GIS data in the cloud. (2 hours)\\n* Week 9: Find and experiment with a GIS cloud platform. (2 hours)\\n\\n*Cloud security\\n\\n Week 10: Study security models for cloud data. (2 hours)\\n* Week 11: Research best practices for cloud security compliance. (2 hours)\\n* Week 12: Implement basic cloud security measures in your cloud setup. (2 hours)\\n\\n## Schedule:\\n\\n*Monday, Thursday, Friday* 10 AM - 2 PM: Green computing.\\n\\n*Monday, Thursday, Friday* 3 PM - 6 PM: Dew and edge computing.\\n\\n*Saturday, Wednesday:* GIS and cloud security.\\n\\n## Ability Score: 15\\n\\n* Start each study session with a 2-hour block dedicated to green computing. This gives you flexibility in adapting the schedule as needed.\\n* Focus on learning and practical application, adjusting the study sessions as your comfort grows and progress is made.\\n* Seek feedback on your understanding of specific topics when necessary to avoid errors in applying security measures or managing cloud platforms."
    }
  }
  finish_reason: STOP
  safety_ratings {
    category: HARM_CATEGORY_HATE_SPEECH
    probability: NEGLIGIBLE
    probability_score: 0.0542989373
    severity: HARM_SEVERITY_NEGLIGIBLE
    severity_score: 0.0682885423
  }
  safety_ratings {
    category: HARM_CATEGORY_DANGEROUS_CONTENT
    probability: NEGLIGIBLE
    probability_score: 0.171338335
    severity: HARM_SEVERITY_LOW
    severity_score: 0.252384037
  }
  safety_ratings {
    category: HARM_CATEGORY_HARASSMENT
    probability: NEGLIGIBLE
    probability_score: 0.0956869498
    severity: HARM_SEVERITY_NEGLIGIBLE
    severity_score: 0.0679166764
  }
  safety_ratings {
    category: HARM_CATEGORY_SEXUALLY_EXPLICIT
    probability: NEGLIGIBLE
    probability_score: 0.0256627053
    severity: HARM_SEVERITY_NEGLIGIBLE
    severity_score: 0.0316187665
  }
}
usage_metadata {
  prompt_token_count: 78
  candidates_token_count: 418
  total_token_count: 496
}
"""

# Extract the content inside the 'text:' key
match = re.search(r'text:\s*"([^"]*)"', input_string)
if match:
    content = match.group(1)

    # Clean the content by removing asterisks and fixing the formatting
    cleaned_content = content.replace('*', '')  # Remove asterisks
    cleaned_content = cleaned_content.replace('\\n', '\n')  # Replace escaped newlines with actual newlines

    # Print the cleaned content
    print(cleaned_content.strip())  # Strip leading/trailing whitespaces
else:
    print("No content found inside the 'text:' key.")
