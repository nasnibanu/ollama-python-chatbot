import ollama

while True:
    prompt = input("You: ")

    if prompt.lower() == "exit":
        break

    response = ollama.generate(
        model="llama3.2:1b",
        prompt=prompt
    )

    print("Bot:", response["response"])