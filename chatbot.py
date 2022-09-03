import openai

openai.api_key = "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"
conversation = ""

def obtener_respuesta(recibido):
    global conversation
    conversation += f"\nHumano:{recibido}\nBot:"
    response = openai.Completion.create(
            engine="davinci",
            prompt=conversation,
            temperature=0.9,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=["\n", " Humano:", " Bot:"]
        )
    answer = response.choices[0].text.strip()
    conversation += answer
    return answer

def main():
    while 1:
        mensaje = input("Tu mensaje: ")
        respuesta = f"Bot: {obtener_respuesta(mensaje)}"
        print(respuesta)

main()

