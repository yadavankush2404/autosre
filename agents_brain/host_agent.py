import redis
import json
# from openai import OpenAI
from langchain_groq import ChatGroq
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_core.prompts import ChatPromptTemplate
from tools import search_runbook, execute_remediation
from dotenv import load_dotenv
import os

load_dotenv()



# 1. Setup Agent
llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0)
tools = [search_runbook, execute_remediation]

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an Autonomous SRE Agent. When an incident occurs: 1. Search Runbook. 2. Ask user for approval. 3. Execute fix."),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}"),
])

agent = create_openai_tools_agent(llm, tools, prompt)
executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# 2. Redis Monitor Loop
r = redis.Redis(host='localhost', port=6379, decode_responses=True)
p = r.pubsub()
p.subscribe('incidents')

print("SRE Host Agent is watching Redis 'incidents' channel...")

for message in p.listen():
    if message['type'] == 'message':
        data = json.loads(message['data'])
        print(f"\n[ALERT] Incident detected in {data['service']}!")
        
        # Trigger the Reasoning Chain
        user_input = f"Incident Report: {data['details']}. Error Code: {data['error_code']}. Resolve this."
        
        executor.invoke({"input": user_input})