import os
import openai
import dotenv

## Flag to show citations
showCitations = False

dotenv.load_dotenv()

endpoint = os.environ.get("AZURE_OAI_ENDPOINT")
api_key = os.environ.get("AZURE_OAI_KEY")
deployment = os.environ.get("AZURE_OAI_DEPLOYMENT")
azure_search_endpoint = os.environ.get("AZURE_SEARCH_ENDPOINT")
azure_search_key = os.environ.get("AZURE_SEARCH_KEY")
azure_search_index = os.environ.get("AZURE_SEARCH_INDEX")

client = openai.AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=api_key,
    api_version="2024-02-01",
)

# Configure your data source


# Get user input
text = input('\nEnter a question:\n')

# Send request to Azure OpenAI model
completion = client.chat.completions.create(
    model=deployment,
    messages=[{"role": "user", "content": text}],
    extra_body=extension_config
)
print(completion.choices[0].message.content)

if showCitations:
    print(f"\n{completion.choices[0].message.context}")
