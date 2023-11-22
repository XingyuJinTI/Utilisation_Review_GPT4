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

## Docker Setup (Alternative)
### Prerequisites
Docker installed on your machine. [Install Docker](https://docs.docker.com/get-docker/)

### Building the Docker Image
To containerize the application, build the Docker image using the provided Dockerfile.

**1. Navigate to the Project Directory:**

Ensure you are in the root directory of the cloned repository.

**2. Build the Docker Image:**
Run the following command to create the Docker image:
```sh
docker build -t utilization-review-gpt4 .
```
This command creates an image named utilization-review-gpt4.

### Running the Application Using Docker

**1. Run the Docker Container:**
Execute the following command to run the application:

```sh
docker run -p 4000:80 -v /path/to/your/project:/usr/src/app/ -v /path/to/your/medical-record.pdf:/usr/src/app/medical-record.pdf -e OPENAI_API_KEY='<your-API-key>' utilization-review-gpt4
```
- Replace /path/to/your/project with the absolute path to your project directory. 
- Replace /path/to/your/medical-record.pdf with the absolute path to your medical record pdf. 
- Replace `<your-API-key>` with your OpenAI API Key.

This command mounts your project directory to the container, passes your API keys to container environment and starts the application.

### Accessing the Output
The output JSON file (patient_data.json) will be saved in your project directory.


### Notes
The -p 4000:80 option maps port 80 inside the container to port 4000 on your host machine. Adjust this as per your requirements.
