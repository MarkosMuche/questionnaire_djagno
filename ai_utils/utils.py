

from langchain import OpenAI, LLMChain, PromptTemplate
from langchain.chat_models import ChatOpenAI

from langchain.memory import ConversationBufferWindowMemory
from dotenv import load_dotenv

load_dotenv()


template_insight = """""I want you to summerized the given question 
and answeer and give me accurate summerized statement. Summarize the 
key personal values discussed in the Q&A session, including the 
importance of these values in shaping one's beliefs, actions, and 
relationships. Provide a brief overview of how these values can help 
individuals live fulfilling and meaningful lives.you must understand 
Q as question 1,2,3,4 are different answers for that question.

This prompt aims to capture the main ideas and key points of the Q&A 
session on personal values, highlighting the significance of these values
in shaping individual identity, behavior, and social interactions. The 
summary should focus on the values that were discussed, such as honesty,
integrity, empathy, kindness, respect, and responsibility, and how they
can contribute to personal growth, happiness, and well-being. It should 
also emphasize the role of personal values in guiding decision-making,
establishing priorities, and fostering positive relationships with others.



Human: {human_input}
please give me persons vision based on the above data
Assistant:"""

template_vision = """"
Please provide me with a vision statement that reflects your core values 
and aspirations, based on your responses to the following 10 personal value 
questions. For each question, you provided four possible answers (1, 2, 3, 4). 
Please review your answers and use them to guide your vision statement.
Human: {human_input}
Please use these questions and answers to craft a vision statement that 
reflects your core values and aspirations. Your vision statement should be 
a clear and concise statement that reflects who you are, what you want to 
achieve, and what you stand for. Consider your personal and professional goals, 
your values, and your passions when crafting your vision statement. i have give
 you more detail date about me, please give me a more more detail vision statement "
Assistant:"""

prompt_insight = PromptTemplate(
    input_variables=[ "human_input"], 
    template=template_insight
)
prompt_vision = PromptTemplate(
    input_variables=["human_input"], 
    template=template_vision
)


llm_insight = ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo')
llm_vision = ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo')


chain_insight = LLMChain(
    llm=llm_insight,
    prompt=prompt_insight, 
    verbose=True, 
)

chain_vision = LLMChain(
    llm=llm_insight,
    prompt=prompt_vision,
    verbose=True, 
)

def get_vision_statement(data):
    
    insights = chain_insight.predict(human_input=data)

    vision_statement = chain_vision.predict(human_input = insights)

    return vision_statement

def get_chatbot_response(prompt):

    response = chain_insight.predict(human_input=prompt)
    return response



if __name__ == "__main__":

    path = 'sample.txt'
    with open(path, "r") as file:
        data = file.read()

    vision_statement = get_vision_statement(data=data)
    print(vision_statement)