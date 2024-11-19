from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv

load_dotenv()


def handler(event, context):
    azure_llm = AzureChatOpenAI(
        api_version="2024-10-01-preview",
        azure_deployment="gpt-4o",
        max_retries=2,
    )

    target = event["target"]
    prompt = ChatPromptTemplate.from_template(
        "{target}に最も人気な職業をは?\n職業：",
    )
    second_prompt = ChatPromptTemplate.from_template(
        "{job}の平均年収を教えて",
    )
    chain = prompt | azure_llm | StrOutputParser()
    composed_chain = (
        chain
        | (lambda input: {"job": input})
        | second_prompt
        | azure_llm
        | StrOutputParser()
    )

    result = composed_chain.invoke({"target": target})
    return {"statusCode": 200, "body": result}
