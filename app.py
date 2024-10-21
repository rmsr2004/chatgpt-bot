from langchain.memory import ConversationBufferMemory
from langchain_groq import ChatGroq
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os, sys, signal

def signal_handler(sig, frame):
    print('\nExiting...')
    sys.exit(0)

def main():
    signal.signal(signal.SIGINT, signal_handler)

    load_dotenv()

    template = """
        Você é um assistente virtual.
        Responda apenas em Português.

        Histórico da conversa:
        {chat_history}

        Input: {input}
    """

    base_prompt = PromptTemplate(input_variables=["input", "chat_history"], template=template)

    llm = ChatGroq(model_name='llama3-8b-8192', api_key=os.getenv("API_KEY"))

    memory = ConversationBufferMemory(memory_key="chat_history", input_key='input')

    llm_chain = LLMChain(llm=llm, memory=memory, prompt=base_prompt)

    os.system("clear")

    user_input = None

    print("Olá! Eu sou um assistente virtual. Como posso te ajudar?")

    while user_input != "exit":
        user_input = input("-> ")
        response = llm_chain.invoke(input=user_input)
        print(f"\n{response['text']}\n")

if __name__ == "__main__":
    main()
    
# end of app.py