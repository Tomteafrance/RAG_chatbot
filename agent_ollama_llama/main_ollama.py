from __future__ import annotations
from typing import Optional, Union
from langchain_community.llms import Ollama
from crewai import Agent, Task, Crew, Process

# Create a new agent 
model = Ollama(model = 'llama3')

# Agent 1 : Email Classifier 
email = "nigerian prince sending some gold"

# Create a task
classifier = Agent(
    role = "email classifier",
    goal = "accurately classify emails based on their importance, email one of these rating : important, casual, or spam",
    backstory = "You are an AI assistant whose only job is to classify emails accurately and honestly. DO not be afraid to give emails bad rating if they are not important. Your job is to help the user manage their inbox.",
    verbose = True,
    allow_delegation = False, 
    llm = model
)

# Agent 2 : Responder

responder = Agent(
    role = "email responder",
    goal = "Based on the importance of the email, write a concise and simple response. If the email is rated 'important' write a formal response, if the email is rated 'casual' write a casual response and if the email is rated 'spam' ignore the email. no matter what, be very cocnise.",
    backstory = "You are an AI assistant whose only job is to write short responses to emails based on their importance. The importance will be provided to you by the 'classifier' agent.",
    verbose = True,
    allow_delegation = False,
    llm = model
)

classify_email = Task(
    description = f"Classify the email '{email}'",
    agent = classifier,
    expected_output = "One of these three options : 'important', 'casual', or 'spam'",
)

respond_to_email = Task(
    description = f"Respond to the email: '{email}' based on the importance provided by the 'classifier' agent.",
    agent = responder,
    expected_output = "a very concise response to the email based on the importance provided by the 'classifier' agent.",
)

crew = Crew(
    agents = [classifier, responder],
    tasks = [classify_email, respond_to_email],
    verbose = 2,
    process = Process.sequential
)

output = crew.kickoff()
print(output)