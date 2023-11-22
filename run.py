import argparse
import json
import PyPDF2
from openai import OpenAI

def read_pdf(file_path):
    """Reads a PDF and returns its text content."""
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''.join(page.extract_text() for page in reader.pages)
    return text

def create_query_message(text, query, prompt, format, template):
    """Constructs a query message for the OpenAI API."""
    return text + query + prompt + format + str(template)

def get_response_from_openai(query_message):
    """Sends a query to OpenAI and returns the response."""
    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=[
            {"role": "system", "content": "You are a helpful utilization review nurse."},
            {"role": "user", "content": query_message}
        ],
        temperature=1,
        max_tokens=2048,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].message.content

def process_response(response):
    """Processes the response to extract and format the JSON data."""
    if response[0] != '[' or response[-1] != ']':
        start_index = response.find('[')
        end_index = response.rfind(']')
        response = response[start_index:end_index+1]
    return response

def save_to_json(data, file_path):
    """Saves the data to a JSON file."""
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def parse_arguments():
    """Parses command-line arguments."""
    parser = argparse.ArgumentParser(description='Process a medical record PDF.')
    parser.add_argument('pdf_path', nargs='?', default='medical-record.pdf',
                        help='Path to the medical record PDF file. Default: "medical-record.pdf"')
    
    return parser.parse_args()

# Main execution flow
if __name__ == "__main__":
    args = parse_arguments()
    medical_text = read_pdf(args.pdf_path)

    query_parts = {
        "query": "\n1. According to the medical record, please extract the following information:\n1a. Patient’s chief complaint\n1b. Treatment plan the doctor is suggesting\n1c. A list of allergies the patient has\n1d. A list of medications the patient is taking, with any known side-effects\n2. Answer the following questions and justify its reasoning by providing evidence also provide a confidence score where 10/10 is very confident of its answer\n2a. Does the patient have a family history of colon cancer in their first-degree relatives?\n2b. Has the patient experienced minimal bright red blood per rectum?\n2c. Has the patient had significant loss of blood?\n2d. Does the patient have a history of skin problems?\n2e. Has the patient used hydrocortisone cream for the haemorrhoids that they are\ncurrently experiencing?\n2f. Were any high risk traits found on the patient’s genetic test?\n2g. Has the patient had a colonoscopy in the last 5 years?\n2h. Has the patient had any recent foreign travel?\n2i. How long has the patient been known to healthcare services?",
        "prompt": "\n3a. What's the overal percentaged aproval score based on answers from 2? 0 for Yes, 1 for No, 0.5 for NotMentioned, for 2i, if mentioned, the score's 0.5 times the reciprocal of years. 3b. (short answer) What's the decision based on the approval score, >50% Approved, <20% Rejected, in between nurses review requested",
        "format": "\nPlease keep question numbers and output a json array of question and answer dictonary pairs like" ,
        "template": [{"queston":"", "answer":""}]
    }
    query_message = create_query_message(medical_text, **query_parts)
    openai_response = get_response_from_openai(query_message)

    try:
        json_data = json.loads(process_response(openai_response))
        save_to_json(json_data, 'patient_data.json')
    except json.JSONDecodeError as e:
        print(f"Error processing JSON data: {e}")
