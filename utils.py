from langchain.llms import OpenAI
from langchain.tools import BaseTool, StructuredTool, Tool, tool
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.tools import DuckDuckGoSearchRun


search=DuckDuckGoSearchRun()

def get_info(prompt,video_length, creativity, api_key):

    DuckDuckGoSearch=search.run(prompt)
    llm=OpenAI(temperature=creativity,model_name='gpt-3.5-turbo',openai_api_key=api_key)

    title_template=PromptTemplate(
        input_variables=['subject','DuckDuckGoSearch'],
        template='''Please come up with a creative title for a Youtube video on the topic: {subject}
        Here are some details about this topic {DuckDuckGoSearch}'''
    )
    title_chain=LLMChain(llm=llm,prompt=title_template,verbose=True)
    
    Script_Tempalte=PromptTemplate(
        input_variables=['Title','DuckDuckGoSearch','Duration'],
        template="""Using the information given in triple quotes '''{DuckDuckGoSearch}'''
        Create a Script for a Youtube video on this for me, Title : {Title}
        The video duration must be aroud {Duration} minutes"""
    )
    Script_chain=LLMChain(llm=llm,prompt=Script_Tempalte,verbose=True)

    title=title_chain.run(subject=prompt,DuckDuckGoSearch=DuckDuckGoSearch)
    Script=Script_chain.run(Title=title,DuckDuckGoSearch=DuckDuckGoSearch,Duration=video_length)

    return title,Script,DuckDuckGoSearch