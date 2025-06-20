import os
import sys
from google import genai
from google.genai import types
from dotenv import load_dotenv


def main():

    args = sys.argv[1:]

    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here"')
        print('Example: python main.py "How do I build a calculator app?"')
        sys.exit(1)

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    user_prompt = " ".join(args)

    response = client.models.generate_content(
        model='gemini-2.0-flash-001',
        contents=[user_prompt]
    )

    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    print(f"Response: ")
    print(response.text)


if __name__ == "__main__":
    main()
