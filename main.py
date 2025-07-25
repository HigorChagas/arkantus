import sys
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

from prompts import system_prompt
from call_function import available_functions, real_functions

# Carrega variáveis de ambiente só uma vez
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)


def run_agent(prompt, verbose=False):
    if verbose:
        print(f"User prompt: {prompt}\n")

    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)]),
    ]

    for i in range(20):  # no máximo 20 iterações
        if verbose:
            print(f"\n[Iteração {i+1}]")

        try:
            response = client.models.generate_content(
                model="gemini-2.0-flash-001",
                contents=messages,
                config=types.GenerateContentConfig(
                    tools=[available_functions],
                    system_instruction=system_prompt,
                ),
            )

            for candidate in response.candidates:
                if verbose:
                    print(f"Modelo:\n{candidate.content.parts[0].text}\n")
                messages.append(candidate.content)

            if not response.function_calls:
                final_text = response.text
                if verbose:
                    print("Final response:")
                    print(final_text)
                return final_text

            for function_call_part in response.function_calls:
                function_call_result = call_function(function_call_part, verbose)

                if verbose and function_call_result.parts[0].function_response.response:
                    print(
                        "->", function_call_result.parts[0].function_response.response
                    )

                messages.append(function_call_result)

        except Exception as e:
            print(f"[ERRO NA ITERAÇÃO {i+1}] {e}")
            return f"[Erro] {e}"

    return "[Erro] Limite de iterações atingido."


def call_function(function_call_part, verbose=False):
    function_name = function_call_part.name
    args = function_call_part.args

    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")

    if function_name not in real_functions:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )

    args["working_directory"] = "./calculator"

    function_to_call = real_functions[function_name]
    result = function_to_call(**args)

    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"result": result},
            )
        ],
    )


def main():
    args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]
    verbose = "--verbose" in sys.argv

    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here" [--verbose]')
        print('Example: python main.py "How do I fix the calculator?"')
        sys.exit(1)

    user_prompt = " ".join(args)
    result = run_agent(user_prompt, verbose)

    if not verbose:
        print(result)


if __name__ == "__main__":
    main()
