from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type

class FileReadInput(BaseModel):
    """Input for reading a file."""
    file_path: str = Field(..., description="The path to the file to read.")

class FileReadTool(BaseTool):
    name: str = "Read File Content"
    description: str = "Reads the entire content of a specified file."
    args_schema: Type[BaseModel] = FileReadInput

    def _run(self, file_path: str) -> str:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            return f"Successfully read content from '{file_path}'.\n\n{content}"
        except FileNotFoundError:
            return f"Error: The file '{file_path}' was not found."
        except Exception as e:
            return f"An error occurred while reading the file: {str(e)}"