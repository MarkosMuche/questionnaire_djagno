

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
please give me person's  4 personal core values. 
 on the above data
Assistant:"""

template_vision = """"

Human: {human_input}
   Based on the provided information, please suggest up to 4 potential company values that might resonate with the client's business ethos. List each value followed by a brief description, separated by a colon, and return each value on a new line.
"""

template_company_value = """"

Human: {human_input}

   Based on the provided information, please suggest up to 4 potential company values that might resonate with the client's business ethos. List each value followed by a brief description, separated by a colon, and return each value on a new line.

"""

template_value_idea = """"

Human: {human_input}

   Based on the provided information, please suggest onely 10 potential ideas that might discribed the selected company value  how they can begin integrating their chosen values into their company. List each idea, separated by a colon, and return each value on a new line. i don't want any additional ideas i only need just 10 ideas

"""



template_person_value = """"

Human: {human_input}

   Based on the provided information, please suggest up to 4 potential 4 personal core values  that might resonate with the client's business ethos. List each value followed by a brief description, separated by a colon, and return each value on a new line.

"""

prompt_insight = PromptTemplate(
    input_variables=[ "human_input"], 
    template=template_insight
)

prompt_company_value = PromptTemplate(
    input_variables=[ "human_input"], 
    template=template_company_value
)

prompt_value_idea = PromptTemplate(
    input_variables=[ "human_input"], 
    template=template_value_idea
)

prompt_person_value = PromptTemplate(
    input_variables=[ "human_input"], 
    template=template_person_value
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
    verbose=False, 
)

chain_company_value = LLMChain(
    llm=llm_insight,
    prompt=prompt_company_value, 
    verbose=False, 
)

chain_value_idea = LLMChain(
    llm=llm_insight,
    prompt=prompt_value_idea, 
    verbose=False, 
)


chain_person_value = LLMChain(
    llm=llm_insight,
    prompt=prompt_person_value, 
    verbose=False, 
)

chain_vision = LLMChain(
    llm=llm_insight,
    prompt=prompt_vision,
    verbose=False, 
)

def get_vision_statement(data):
    
    # insights = chain_insight.predict(human_input=data)

    vision_statement = chain_vision.predict(human_input = data)

    return vision_statement

def get_chatbot_response(prompt):

    response = chain_insight.predict(human_input=prompt)
    return response


def get_company_value(data):
    
    compny_value = chain_company_value.predict(human_input=data)
    compny_value=parse_llm_output(compny_value)
    return compny_value

def get_value_ideas(data):
    
    compny_value = chain_value_idea.predict(human_input=data)
    compny_value=parse_llm_output(compny_value)
    return compny_value

def get_person_value(data):
    
    compny_value = chain_person_value.predict(human_input=data)
    compny_value=parse_llm_output(compny_value)
    return compny_value


def parse_llm_output(output_string):
    # Split the output string by newline to get individual values
    values = output_string.split('\n')
    
    # Optionally, filter out any empty lines or unwanted content
    values = [v.strip() for v in values if v.strip()]
    
    return values




if __name__ == "__main__":

    path = 'sample.txt'
    with open(path, "r") as file:
        data = file.read()

    vision_statement = get_vision_statement(data=data)
    print(vision_statement)