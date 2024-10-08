"Supervisor re-direct users to interact with appropriate agent."

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from doco.prompts.supervisor import SYSTEM_PROMPT
from doco.io.response import routeResponse
from doco.io._graph import options, members
from doco.agents.config import AgentConfig
from doco.agents.base import BaseAgent


class Supervisor(BaseAgent): 
    supervisor_config = AgentConfig().supervisor
    def __init__(self): 
        super().__init__(provider=self.supervisor_config['provider'], 
                llm_config=self.supervisor_config['llm_config'], 
                tools=[], 
                system_prompt=SYSTEM_PROMPT, 
                instruction="")
        

    def _build_agent(self, llm, tools: list, system_prompt: str, instruction: str):
        prompt = ChatPromptTemplate.from_messages(
                [
                    ("system", system_prompt),
                    MessagesPlaceholder(variable_name="messages"),
                    (
                        "system",
                        "Given the conversation above, who should act next?"
                        " Or should we FINISH? Select one of: {options}",
                    ),
                ]
            ).partial(options=str(options), members=", ".join(members))

        return prompt | llm.with_structured_output(routeResponse)
        