import os
import yaml
from typing import Dict, Any
from dotenv import load_dotenv
from loguru import logger
from swarm_models import OpenAIChat
from swarms.agents.create_agents_from_yaml import create_agents_from_yaml

def load_company_variables() -> Dict[str, str]:
    """Load company-specific variables from environment or config file."""
    return {
        "COMPANY_NAME": os.getenv("COMPANY_NAME", "Default Company"),
        "PRODUCT_NAME": os.getenv("PRODUCT_NAME", "Default Product"),
        "INDUSTRY": os.getenv("INDUSTRY", "Technology"),
        "PAIN_POINT": os.getenv("PAIN_POINT", "efficiency"),
        "DESIRED_OUTCOME": os.getenv("DESIRED_OUTCOME", "increased productivity"),
        "TARGET_AUDIENCE": os.getenv("TARGET_AUDIENCE", "business professionals"),
        "EXPERTISE_AREA": os.getenv("EXPERTISE_AREA", "process optimization"),
        "LEAD_MAGNET": os.getenv("LEAD_MAGNET", "free consultation"),
        "CONSULTATION_TYPE": os.getenv("CONSULTATION_TYPE", "strategy"),
        "TOPIC": os.getenv("TOPIC", "business optimization"),
        "WORKSHOP_NAME": os.getenv("WORKSHOP_NAME", "masterclass"),
        "TIMEFRAME": os.getenv("TIMEFRAME", "30 days"),
        "WEBSITE": os.getenv("WEBSITE", "www.example.com"),
        "CALENDAR_LINK": os.getenv("CALENDAR_LINK", "calendly.com/example")
    }

def replace_variables_in_string(text: str, variables: Dict[str, str]) -> str:
    """Replace all bracketed variables in a string with their values."""
    for key, value in variables.items():
        text = text.replace(f"[{key}]", value)
    return text

def process_yaml_with_variables(yaml_path: str, variables: Dict[str, str]) -> str:
    """Process YAML file and replace all variables with actual values."""
    # Read the original YAML file
    with open(yaml_path, 'r') as file:
        content = file.read()

    # Replace variables in the content
    processed_content = replace_variables_in_string(content, variables)

    # Write to a temporary file
    temp_yaml_path = "processed_agents.yaml"
    with open(temp_yaml_path, 'w') as file:
        file.write(processed_content)

    return temp_yaml_path

def main():
    # Load environment variables
    load_dotenv()

    # Load company-specific variables
    company_variables = load_company_variables()

    # Original YAML file path
    yaml_file = "agents.yaml"

    # Process YAML file with variables
    processed_yaml_file = process_yaml_with_variables(yaml_file, company_variables)

    # Get the API key
    api_key = os.getenv("GROQ_API_KEY")

    # Initialize the model
    model = OpenAIChat(
        openai_api_base="https://api.groq.com/openai/v1",
        openai_api_key=api_key,
        model_name="llama-3.1-70b-versatile",
        temperature=0.1,
    )

    try:
        # Create and run agents with processed YAML
        task_results = create_agents_from_yaml(
            model=model,
            yaml_file=processed_yaml_file,
            return_type="run_swarm"
        )

        logger.info(f"Results from agents: {task_results}")

        # Clean up temporary file
        os.remove(processed_yaml_file)

    except Exception as e:
        logger.error(f"An error occurred: {e}")
        if os.path.exists(processed_yaml_file):
            os.remove(processed_yaml_file)

if __name__ == "__main__":
    main()