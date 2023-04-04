import openai

openaiKey = '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'

def chatingGPT(msg):
    modelGPT = "gpt-3.5-turbo"
    question = openai.ChatCompletion.create(model=modelGPT, max_tokens=100, messages=[{"role": "user", "content": msg}])
    return question.choices[0].message.content