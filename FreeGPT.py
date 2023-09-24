import g4f

class FreeGPT:
    def call(self, query: str):
        chat_completion = g4f.ChatCompletion.create(
                         model="gpt-3.5-turbo",
                        messages=[{"role": "user", "content": query}],
                        provider=	g4f.Provider.Aivvm,
                        #  stream=True,
                    )  
        return True,chat_completion
  
freeGPTMgr = FreeGPT()    