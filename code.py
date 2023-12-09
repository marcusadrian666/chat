import requests

def chat_with_gpt(prompt):
    url = "https://api.openai.com/v1/chat/completions"
    api_key = "YOUR_API_KEY"  # 替换为你的ChatGPT API密钥

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    data = {
        "prompt": prompt,
        "max_tokens": 50  # 设置生成的回复的最大长度
    }

    response = requests.post(url, headers=headers, json=data)
    response_json = response.json()

    if "choices" in response_json:
        choices = response_json["choices"]
        if len(choices) > 0 and "text" in choices[0]:
            return choices[0]["text"]
    
    return None

# 主程序
while True:
    user_input = input("你: ")
    response = chat_with_gpt(user_input)
    if response:
        print("ChatGPT: " + response)
    else:
        print("出了点问题，无法生成回复。")
