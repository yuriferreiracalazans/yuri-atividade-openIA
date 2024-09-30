from openai import OpenAI


client = OpenAI(api_key="sk-ZsWo8_E659sw2p354hGR_lCBfwLfKiqZDp1eZZfSY9T3BlbkFJ3qBzPD14vheEvd_P9brZR3YR8Fk-vHhjaj3FeFPEcA")

def chat_with_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choises[0].message.content.strip()

if __name__ == "__main__":
    while True:
        user_input = input("Você: ")
        if user_input.lower() in ["quit", "exit", "bye", "sair", "tchau"]:
            break

        response = chat_with_gpt(user_input)
        print("Chatbot: ", response)
