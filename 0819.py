import openai
import streamlit as st
import requests


headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {st.secrets["api_key"]}"
        }


st.markdown("""#### 當你在為未來的重要目標（如購房、退休或子女教育）存錢時，你通常會怎麼規劃這筆資金？你會更注重資金的安全，還是希望能夠獲得更高的回報？""")
with st.popover("See Q1 keywords"):
    st.caption("""保守型關鍵字: 安全、保值、低風險、存款、保護、穩定\n
穩健型關鍵字: 穩定增長、回報、債券、保守型基金、分散投資\n
成長型關鍵字: 成長性、股票、基金、提高回報、部分投入\n
積極型關鍵字: 冒險、高風險高回報、快速增長、新興市場、創業""")

prompt_1 = st.text_input('請輸入Q1答案')

st.markdown("""#### 如果你突然得到一筆意外之財，你會怎麼處理這筆錢？你會選擇保存下來以備不時之需，還是希望利用這筆錢去嘗試新的投資機會？""")
with st.popover("See Q2 keywords"):
    st.caption("""保守型關鍵字: 存起來、償還貸款、保存、保險、避免風險\n
穩健型關鍵字: 穩健型產品、穩定回報、部分投資、保守選擇\n
成長型關鍵字: 增長潛力、投資、分散、部分投入\n
積極型關鍵字: 高回報、投資機會、大膽投入、迅速增值、冒險""")

prompt_2 = st.text_input('請輸入Q2答案')

st.markdown("""#### 當你要做出一個重要的購買或投資決定時，你通常會考慮什麼？是更注重安全感，還是希望能獲得更高的回報？""")
with st.popover("See Q3 keywords"):
    st.caption("""保守型關鍵字: 安全性、保護資金、保值、避免風險、穩定\n
穩健型關鍵字: 風險與回報、穩定增長、可接受風險、長期回報\n
成長型關鍵字: 潛在回報、成長機會、回報率、適度風險\n
積極型關鍵字: 高回報、高風險、快速增長、大膽嘗試、冒險""")

prompt_3 = st.text_input('請輸入Q3答案')

col1, col2, col3 = st.columns(3)
with col1:
     st.caption('Q1判別')
with col2:
     st.caption('Q2判別')
with col3:
     st.caption('Q3判別')


if prompt_1:
    prompt = f"""接下來你要根據使用者的回答，從五個類別中選擇一個作為最終的結果，這五個類別分別是「保守」、「穩健」、「成長」、「積極」、「無法判斷」。以下提供你前四種類別可能會出現的關鍵字：
    保守型關鍵字: 安全、保值、低風險、存款、保護、穩定
    穩健型關鍵字: 穩定增長、回報、債券、保守型基金、分散投資
    成長型關鍵字: 成長性、股票、基金、提高回報、部分投入
    積極型關鍵字: 冒險、高風險高回報、快速增長、新興市場、創業

    此外，若使用者的回答與問題毫不相關，或無法判別屬於「保守」、「穩健」、「成長」、「積極」任一類別，皆判斷為「無法判斷」。請不要給出任何解釋，最後只需要回答屬於何種類別即可。

    Ｑ：當你在為未來的重要目標（如購房、退休或子女教育）存錢時，你通常會怎麼規劃這筆資金？你會更注重資金的安全，還是希望能夠獲得更高的回報？

    Ａ：我希望可以得到較多高的回報。

    Ｌ：積極

    Ｑ：當你在為未來的重要目標（如購房、退休或子女教育）存錢時，你通常會怎麼規劃這筆資金？你會更注重資金的安全，還是希望能夠獲得更高的回報？

    Ａ：我喜歡吃牛肉麵

    Ｌ：無法判斷

    Ｑ：當你在為未來的重要目標（如購房、退休或子女教育）存錢時，你通常會怎麼規劃這筆資金？你會更注重資金的安全，還是希望能夠獲得更高的回報？

    Ａ：{prompt_1}

    Ｌ："""

    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {
            "role": "user",
            "content": [
                {
                "type": "text",
                "text": prompt
                },
            ]
            }
        ],
        "max_tokens": 300
        }
    
    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

    message_1 = response.json()['choices'][0]['message']['content']

    # completion = openai.ChatCompletion.create(
    #     model="gpt-4o",
    #     messages = [{"role": "user", "content": prompt}],
    #     max_tokens = 2048,
    #     temperature = 0.8)

    # message_1 = completion.choices[0].message.content


    with col1:
        # st.caption('Q1判別')
        st.write(message_1)

if prompt_2:
    promptt = f"""接下來你要根據使用者的回答，從五個類別中選擇一個作為最終的結果，這五個類別分別是「保守」、「穩健」、「成長」、「積極」、「無法判斷」。以下提供你前四種類別可能會出現的關鍵字：
保守型關鍵字: 存起來、償還貸款、保存、保險、避免風險
穩健型關鍵字: 穩健型產品、穩定回報、部分投資、保守選擇、生育
成長型關鍵字: 增長潛力、投資、分散、部分投入
積極型關鍵字: 高回報、投資機會、大膽投入、迅速增值、冒險

此外，若使用者的回答與問題毫不相關，或無法判別屬於「保守」、「穩健」、「成長」、「積極」任一類別，皆判斷為「無法判斷」。請不要給出任何解釋，最後只需要回答屬於何種類別即可。

Ｑ：如果你突然得到一筆意外之財，你會怎麼處理這筆錢？你會選擇保存下來以備不時之需，還是希望利用這筆錢去嘗試新的投資機會？

Ａ：存下來

Ｌ：保守

Ｑ：如果你突然得到一筆意外之財，你會怎麼處理這筆錢？你會選擇保存下來以備不時之需，還是希望利用這筆錢去嘗試新的投資機會？

Ａ：你有病嗎

Ｌ：無法判斷

Ｑ：如果你突然得到一筆意外之財，你會怎麼處理這筆錢？你會選擇保存下來以備不時之需，還是希望利用這筆錢去嘗試新的投資機會？

Ａ：{prompt_2}

Ｌ："""
    payloadd = {
    "model": "gpt-4o-mini",
    "messages": [
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": promptt
            },
        ]
        }
    ],
    "max_tokens": 300
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payloadd)

    message_2 = response.json()['choices'][0]['message']['content']

    # completion = openai.ChatCompletion.create(
    #     model="gpt-4o",
    #     messages = [{"role": "user", "content": promptt}],
    #     max_tokens = 2048,
    #     temperature = 0.8)

    # message_2 = completion.choices[0].message.content

    with col2:
        # st.caption('Q2判別')
        st.write(message_2)

if prompt_3:
    prompttt = f"""接下來你要根據使用者的回答，從五個類別中選擇一個作為最終的結果，這五個類別分別是「保守」、「穩健」、「成長」、「積極」、「無法判斷」。以下提供你前四種類別可能會出現的關鍵字：
保守型關鍵字: 安全性、保護資金、保值、避免風險、穩定
穩健型關鍵字: 風險與回報、穩定增長、可接受風險、長期回報
成長型關鍵字: 潛在回報、成長機會、回報率、適度風險
積極型關鍵字: 高回報、高風險、快速增長、大膽嘗試、冒險、更高

此外，若使用者的回答與問題毫不相關，或無法判別屬於「保守」、「穩健」、「成長」、「積極」任一類別，皆判斷為「無法判斷」。請不要給出任何解釋，最後只需要回答屬於何種類別即可。

Ｑ：當你要做出一個重要的購買或投資決定時，你通常會考慮什麼？是更注重安全感，還是希望能獲得更高的回報？

Ａ：我希望回報率有成長空間

Ｌ：成長

Ｑ：當你要做出一個重要的購買或投資決定時，你通常會考慮什麼？是更注重安全感，還是希望能獲得更高的回報？

Ａ：我愛國泰

Ｌ：無法判斷

Ｑ：當你要做出一個重要的購買或投資決定時，你通常會考慮什麼？是更注重安全感，還是希望能獲得更高的回報？

Ａ：{prompt_3}
Ｌ："""
    
    payloaddd = {
    "model": "gpt-4o-mini",
    "messages": [
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": prompttt
            },
        ]
        }
    ],
    "max_tokens": 300
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payloaddd)

    message_3= response.json()['choices'][0]['message']['content']

    # completion = openai.ChatCompletion.create(
    #     model="gpt-4o",
    #     messages = [{"role": "user", "content": prompttt}],
    #     max_tokens = 2048,
    #     temperature = 0.8)

    # message_3 = completion.choices[0].message.content

    with col3:
        # st.caption('Q3判別')
        st.write(message_3)

