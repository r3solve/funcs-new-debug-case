import os
from openai import AzureOpenAI


def get_response(query:str)->str:
    model_name = "gpt-4.1"
    deployment = "gpt-4.1"

    subscription_key = os.environ.get("OPENAI_ENDPOINT")
    endpoint = "https://af-ailab-we-poc-001.openai.azure.com/"
    api_version = "2024-12-01-preview"

    client = AzureOpenAI(
        api_version=api_version,
        azure_endpoint=endpoint,
        api_key=subscription_key,
    )

    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant.",
            },
            {
                "role": "user",
                "content": query,
            }
        ],
        max_completion_tokens=13107,
        temperature=1.0,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        model=deployment
    )
    return  response.choices[0].message.content

# if __name__ == "__main__":
#     query = "What is the capital of France?"
#     response = get_response(query)
#     print(f"Response: {response}")