import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    timeout=30
)


def create_simple_tasks(description):
    if not client.api_key:
        return ["Error: The GEMINI_API_KEY is not configured."]

    try:
        prompt = f"""Desglosa la siguiente tarea compleja en una lista de 3 a 5 subtareas simples y accionables.
Tarea: {description}

Formato de respuesta:
- Subtarea 1
- Subtarea 2
- Subtarea 3
- etc.

Responde solo con la lista de subtareas, una por linea, empezando cada linea con un guion.
"""

        params = {
            "model": "gemini-3.5-flash-lite",
            "messages": [
                {
                    "role": "system",
                    "content": "Eres un asistente experto en gestion de tareas que ayuda a dividir tareas complejas en pasos simples y accionables.",
                },
                {"role": "user", "content": prompt},
            ],
            "max_tokens": 300,
        }

        response = client.chat.completions.create(**params)
        content = response.choices[0].message.content.strip()

        subtasks = []
        for line in content.split("\n"):
            line = line.strip()
            if line.startswith("-"):
                subtask = line[1:].strip()
                if subtask:
                    subtasks.append(subtask)

        return subtasks if subtasks else ["Error: We can not find any task."]

    except Exception as e:
        return [f"Error: We can not connect to the AI service ({e})."]