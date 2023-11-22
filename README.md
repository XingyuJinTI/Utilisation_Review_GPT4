# GPT4-based Utilization Review Nurse

## Description

This project is focused on automating the extraction of information from medical PDF documents using GPT4-Turbo. It leverages large language models to parse and interpret medical records, facilitating tasks for utilization review nurses.

## Features

- Ingest medical records in PDF format.
- Extract key medical information using natural language processing.
- Generate structured output in JSON format for further analysis.

## Installation

To set up this project, follow these steps:

1. **Clone the Repository**

   ```sh
   git clone https://github.com/XingyuJinTI/Utilisation_Review_GPT4.git
   cd Utilisation_Review_GPT4
    ```
2. **Setup a virtual environment (optional)**

    ```sh
    python -m venv openai-env
    source openai-env/bin/activate
    ```
3. **Install the OpenAI Python Library**

    Ensure you have Python 3.7.1 or newer installed, then run:
    
    ```sh
    pip install --upgrade openai
    ```
    Then follow this OpenAI offical [link](https://platform.openai.com/docs/quickstart/step-2-setup-your-api-key) to set up your API key. 

4. **Install Other Dependencies**

    ```sh
    pip install -r requirements.txt
    ```

## Usage
To run the script, use the following command:

```sh
python run.py [pdf_path]
```
pdf_path (optional): Path to the medical record PDF file. If not provided, the script uses 'medical-record.pdf' as the default.

The result will be save `patient_data.json`