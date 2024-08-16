import httpx

def get_spanish_response(user_message: str) -> str:
    prompt = {
        "prompt": f"Please generate a response in Spanish to the following message: {user_message}",
        "max_tokens": 150  # Adjust as needed
    }
    try:
        response = httpx.post("https://example.com/spanish-api", json=prompt)
        response.raise_for_status()  # Raise an error for bad responses
        return f"[[START_SPANISH]]{response.json()['response']}[[END_SPANISH]]"
    except httpx.RequestError as e:
        return f"Error fetching Spanish response: {e}"

def get_english_critique(user_message: str) -> str:
    prompt = {
        "prompt": f"Please generate a critique in English about the following message: {user_message}",
        "max_tokens": 150  # Adjust as needed
    }
    try:
        response = httpx.post("https://example.com/critique-api", json=prompt)
        response.raise_for_status()  # Raise an error for bad responses
        return f"[[START_ENGLISH]]{response.json()['critique']}[[END_ENGLISH]]"
    except httpx.RequestError as e:
        return f"Error fetching English critique: {e}"

def main():
    user_message = input("Escribe tu mensaje: ")  # Prompt user in Spanish
    spanish_response = get_spanish_response(user_message)
    english_critique = get_english_critique(user_message)
    
    print(spanish_response)
    print(english_critique)

if __name__ == "__main__":
    main()

#     Explanation of the Code:
# Functions:
# get_spanish_response(): Sends the user's message to the Spanish API and returns the response with delimiters.
# get_english_critique(): Sends the user's message to the critique API and returns the critique with delimiters.
# Error Handling: Both functions handle potential API errors gracefully.
# Main Function: Collects user input, calls the response and critique functions, and prints the results.
# Make sure to replace the example API URLs with the actual endpoints you intend to use.