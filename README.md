# Personalized Email Generation and Sending System

This project demonstrates a multi-agent AI system designed to generate personalized, insightful emails and then format and send them. It leverages a flexible framework to enable agents to collaborate effectively on this task, maximizing their collective intelligence and capabilities.

## Installation

Ensure you have Python >=3.10 <3.14 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

```bash
pip install -e .
```

### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/toolprac/config/agents.yaml` to define your agents
- Modify `src/toolprac/config/tasks.yaml` to define your tasks
- Modify `src/toolprac/crew.py` to add your own logic, tools and specific args
- Modify `src/toolprac/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart the AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the system, assembling the agents and assigning them tasks as defined in your configuration. You will be prompted to enter a topic for the motivational email. The system will then draft, format, and send the email.

## Understanding Your Crew

The system is composed of two main AI agents:

- **Email_agent**: An expert in providing clear, insightful, and supportive advice. This agent drafts personalized, empathetic emails based on user preferences and a given topic.
- **Email_Formatter_Agent**: An expert in HTML and CSS email design. This agent transforms plain text emails into visually appealing and engaging HTML emails and handles the sending process.

These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve the objective of sending well-crafted advisory emails. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in this system.


