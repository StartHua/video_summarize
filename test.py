import g4f

chat_completion = g4f.ChatCompletion.create(
                         model="gpt-3.5-turbo",
                        messages=[{"role": "user", "content": "你是谁？"}],
                        provider=	g4f.Provider.Aivvm,
                        #  stream=True,
                    )  
print(chat_completion)