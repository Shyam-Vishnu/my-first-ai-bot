from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage


load_dotenv()

llm = ChatOpenAI(
    model="gpt-5.6-luna"
)


# This list will store the conversation
messages = [
    SystemMessage(
        content="You are a helpful question-answering assistant."
    )
]


print("My First AI Bot")
print("Type 'exit' to quit.\n")


while True:
    question = input("You: ")

    if question.lower() == "exit":
        print("Bot: Goodbye!")
        break

    # Add the user's question to conversation history
    messages.append(
        HumanMessage(content=question)
    )

    # Send the entire conversation to the model
    response = llm.invoke(messages)

    # Save the AI's answer too
    messages.append(response)

    print(f"Bot: {response.content}\n")