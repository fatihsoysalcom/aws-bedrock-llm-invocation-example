import boto3
import json
import os

def invoke_bedrock_llm(prompt_text: str, region_name: str = None) -> str:
    """
    Invokes a Large Language Model on AWS Bedrock.
    This demonstrates the AWS-specific setup (region, boto3 client)
    compared to a direct API call to OpenAI/Claude.
    """
    if region_name is None:
        region_name = os.environ.get("AWS_REGION", "us-east-1") # Default region if not specified

    # --- ARTICLE CONCEPT: AWS Bedrock requires a boto3 client and region specification ---
    # This is different from directly calling an OpenAI/Claude API endpoint
    # where you typically just need an API key and the endpoint URL.
    try:
        client = boto3.client(
            service_name="bedrock-runtime",
            region_name=region_name
        )
    except Exception as e:
        print(f"Error initializing Bedrock client. Ensure AWS credentials and region are configured. Error: {e}")
        print("Please set AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, and optionally AWS_REGION environment variables.")
        return "Error: Bedrock client initialization failed."

    # --- ARTICLE CONCEPT: Model ID and specific request body format for Bedrock ---
    # Bedrock acts as a unified interface for multiple models (Anthropic Claude, Amazon Titan, etc.).
    # Each model has its own specific request/response body format.
    # We'll use Anthropic Claude V2 as an example, as it's mentioned in the article.
    model_id = "anthropic.claude-v2"
    
    # Claude's specific request format (Anthropic's prompt format)
    body = json.dumps({
        "prompt": f"\n\nHuman: {prompt_text}\n\nAssistant:",
        "max_tokens_to_sample": 300,
        "temperature": 0.5,
        "top_p": 0.9
    })

    print(f"Invoking Bedrock model: {model_id} in region: {region_name}...")
    try:
        response = client.invoke_model(
            body=body,
            modelId=model_id,
            accept="application/json",
            contentType="application/json"
        )
        response_body = json.loads(response.get("body").read())
        
        # Claude's specific response format
        return response_body.get("completion")
    except client.exceptions.ModelNotReadyException:
        return f"Error: Model '{model_id}' is not ready or not available in region '{region_name}'. Ensure it's enabled in Bedrock settings."
    except client.exceptions.ValidationException as e:
        return f"Error: Validation failed. Check model ID and request body format. Details: {e}"
    except Exception as e:
        return f"An unexpected error occurred during model invocation: {e}"

if __name__ == "__main__":
    # --- Conceptual contrast with OpenAI/Claude direct API ---
    # For OpenAI or direct Claude API, you might just do:
    # import openai
    # openai.api_key = os.environ.get("OPENAI_API_KEY")
    # response = openai.Completion.create(model="text-davinci-003", prompt="Hello")
    #
    # With Bedrock, you first need to configure the AWS environment (credentials, region)
    # and then use boto3 to interact with the Bedrock service, which then routes to the model.

    # Example prompt (in Turkish, matching article context)
    user_prompt = "AWS Bedrock nedir ve neden önemlidir?"

    # Attempt to get region from environment, default to 'us-east-1'
    aws_region = os.environ.get("AWS_REGION", "us-east-1")

    print(f"Sending prompt to Bedrock: '{user_prompt}'")
    llm_response = invoke_bedrock_llm(user_prompt, region_name=aws_region)

    print("\n--- LLM Response from AWS Bedrock ---")
    print(llm_response)
    print("\n-------------------------------------")

    # Reminder for users about Bedrock model access
    print("\nNOTE: Ensure the selected model (e.g., Anthropic Claude v2) is enabled in your AWS Bedrock console for the specified region.")
