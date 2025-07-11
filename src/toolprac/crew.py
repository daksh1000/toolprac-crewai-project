from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from .tools.custom_tool import SendEmailTool
from .tools.file_read_tool import FileReadTool
from typing import List

@CrewBase
class Toolprac():
    """Toolprac crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def Email_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['Email_agent'], # type: ignore[index]
            tools = [FileReadTool()],
            verbose=True
        )

    @agent
    def Email_Formatter_Agent(self) -> Agent:
        return Agent(
            config=self.agents_config['Email_Formatter_Agent'], # type: ignore[index]
            tools = [SendEmailTool()],
            verbose=True
        )

    
    @task
    def draft_advisory_email(self) -> Task:
        return Task(
            config=self.tasks_config['draft_advisory_email'], # type: ignore[index]
            agent=self.Email_agent()
        )

    @task
    def format_and_send_email(self) -> Task:
        return Task(
            config=self.tasks_config['format_and_send_email'], # type: ignore[index]
            agent=self.Email_Formatter_Agent()
        )

    

    @crew
    def crew(self) -> Crew:
        """Creates the Toolprac crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
        
