# Toolprac Crew

Welcome to the Toolprac Crew project, powered by [crewAI](https://crewai.com). This project demonstrates a multi-agent AI system designed to generate personalized, insightful emails and then format and send them. It leverages the powerful and flexible framework provided by crewAI to enable agents to collaborate effectively on this task, maximizing their collective intelligence and capabilities.

## Installation

Ensure you have Python >=3.10 <3.14 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/toolprac/config/agents.yaml` to define your agents
- Modify `src/toolprac/config/tasks.yaml` to define your tasks
- Modify `src/toolprac/crew.py` to add your own logic, tools and specific args
- Modify `src/toolprac/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the Toolprac Crew, assembling the agents and assigning them tasks as defined in your configuration. You will be prompted to enter a topic for the motivational email. The crew will then draft, format, and send the email.

## Understanding Your Crew

The Toolprac Crew is composed of two main AI agents:

- **Email_agent**: An expert in providing clear, insightful, and supportive advice. This agent drafts personalized, empathetic emails based on user preferences and a given topic.
- **Email_Formatter_Agent**: An expert in HTML and CSS email design. This agent transforms plain text emails into visually appealing and engaging HTML emails and handles the sending process.

These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve the objective of sending well-crafted advisory emails. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the Toolprac Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
