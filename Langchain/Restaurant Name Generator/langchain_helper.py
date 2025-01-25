from langchain_openai import ChatOpenAI
from langchain.chains import SequentialChain
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from secret_key import openapi_key
import os

# Set OpenAI API key
os.environ["OPENAI_API_KEY"] = openapi_key

# Initialize model
model = ChatOpenAI(model="gpt-4o-mini", temperature=0.6)


def generate_restaurant_name_and_items(cuisine):
    # Prompt for a single concise restaurant name
    prompt_template_name = PromptTemplate(
        input_variables=['cuisine'],
        template="I want to open a restaurant for {cuisine} food. Suggest only the name of the restaurant in a concise and fancy format, without any additional explanation."
    )
    name_chain = LLMChain(llm=model, prompt=prompt_template_name, output_key="restaurant_name")

    # Prompt for menu items
    prompt_template_item = PromptTemplate(
        input_variables=['restaurant_name'],
        template="Suggest some unique and delicious menu items for the restaurant named {restaurant_name}. Return them as a comma-separated list."
    )
    food_item_chain = LLMChain(llm=model, prompt=prompt_template_item, output_key="menu_item")

    # Combine name generation and menu generation into a sequential chain
    chain = SequentialChain(
        chains=[name_chain, food_item_chain],
        input_variables=['cuisine'],
        output_variables=['restaurant_name', "menu_item"]
    )

    # Get the response
    response = chain({'cuisine': cuisine})
    return response


if __name__=="__main__":
    print(generate_restaurant_name_and_items('Mexico'))
