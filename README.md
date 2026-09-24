# AWS Bedrock LLM Invocation Example

This example demonstrates how to invoke a Large Language Model (LLM) on AWS Bedrock using `boto3`. It highlights the AWS-specific requirements like explicit region specification and using the `boto3` client for authentication, contrasting with simpler direct API calls to platforms like OpenAI or Anthropic Claude.

## Language

`python`

## How to Run

1. Install the AWS SDK for Python:
   `pip install boto3`
2. Configure your AWS credentials and region as environment variables:
   `export AWS_ACCESS_KEY_ID=YOUR_ACCESS_KEY_ID`
   `export AWS_SECRET_ACCESS_KEY=YOUR_SECRET_ACCESS_KEY`
   `export AWS_REGION=us-east-1` (or your desired region where Bedrock is enabled and the model is available)
3. Ensure the chosen model (e.g., Anthropic Claude v2) is enabled in your AWS Bedrock console for the specified region.
4. Run the Python script:
   `python main.py`

## Original Article

This example accompanies the Turkish article: [OpenAI/Claude'dan Bedrock'a Geçiş: Sadece API Değişikliği Değil!](https://fatihsoysal.com/blog/openai-claudedan-bedrocka-gecis-sadece-api-degisikligi-degil/).

## License

MIT — see [LICENSE](LICENSE).
