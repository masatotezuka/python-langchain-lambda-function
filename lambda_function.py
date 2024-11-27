from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()


class OutputModel(BaseModel):
    """
    食材の構成要素
    """

    name: str = Field(description="食材の名前")
    weight: str = Field(description="食材の重さ")
    protein: str = Field(description="食材の蛋白質")
    fat: str = Field(description="食材の脂肪")
    carbohydrate: str = Field(description="食材の炭水化物")


def handler(event, context):
    azure_llm = AzureChatOpenAI(
        api_version="2024-10-01-preview",
        azure_deployment="gpt-4o",
        max_retries=2,
    )
    target = event["target"]

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """
            与えられた質問に対して、構成要素を返してください
            """,
            ),
            ("placeholder", "{messages}"),
        ]
    )

    chain = prompt | azure_llm.with_structured_output(OutputModel)
    result = chain.invoke({"messages": [f"{target}の構成要素を教えて？"]})

    return {"statusCode": 200, "body": result.dict()}
