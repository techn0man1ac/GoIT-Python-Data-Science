# Chat with an intelligent assistant in your terminal
from openai import OpenAI

# Point to the local server
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

history = [
    {"role": "system", "content": "Ви завжди відповідаєте на питання з форматуванням розмітки, використовуючи синтаксис GitHub. Форматування розмітки, яке ви підтримуєте: заголовки, напівжирний, курсив, посилання, таблиці, списки, блоки коду та блок-цитати. Ви повинні опустити те, що ви відповідаєте на питання за допомогою розмітки. Будь-які HTML-теги повинні бути взяті в лапки, наприклад, <html>. Ви будете покарані за не відображення коду в лапках. При поверненні блоків коду вказуйте мову. Ви - корисний, шанобливий і чесний помічник. Завжди відповідайте максимально корисно, але в той же час безпечно. Ваші відповіді не повинні містити шкідливого, неетичного, расистського, сексистського, токсичного, небезпечного або незаконного контенту. Будь ласка, переконайтеся, що ваші відповіді є соціально неупередженими та позитивними за своєю суттю. Якщо питання не має сенсу або не відповідає дійсності, поясніть, чому, замість того, щоб відповідати неправильно. Якщо ви не знаєте відповіді на запитання, будь ласка, не поширюйте неправдиву інформацію."},
    {"role": "user", "content": "Твоя мова українська. Говориш коротко та лаконічно"},
]

while True:
    completion = client.chat.completions.create(
        model="MaziyarPanahi/Llama-3-8B-Instruct-32k-v0.1-GGUF",
        messages=history,
        temperature=0.5,
        stream=True,
    )

    new_message = {"role": "assistant", "content": ""}
    
    for chunk in completion:
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="", flush=True)
            new_message["content"] += chunk.choices[0].delta.content

    history.append(new_message)
    
    # Uncomment to see chat history
    # import json
    # gray_color = "\033[90m"
    # reset_color = "\033[0m"
    # print(f"{gray_color}\n{'-'*20} History dump {'-'*20}\n")
    # print(json.dumps(history, indent=2))
    # print(f"\n{'-'*55}\n{reset_color}")

    print()
    history.append({"role": "user", "content": input("> ")})