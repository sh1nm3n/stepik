import wikipedia

wikipedia.set_lang('ru')

question = input('Что хотите узнать?')
answer = wikipedia.summary(question)

print(answer)
#print(wikipedia.summary('Wikipedia'))