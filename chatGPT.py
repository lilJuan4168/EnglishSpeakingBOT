import openai

openaiKey = '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'

def chatingGPT(msg):
    modelGPT = "text-davinci-003"
    question = openai.Completion.create(model=modelGPT, max_tokens=100, prompt=msg)
    return question.choices[0].text