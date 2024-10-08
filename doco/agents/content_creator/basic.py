"Basic agent for Content Creating"
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from doco.prompts.content import PERSONA_PROMPT, BLOG_PUBLICATION_GUIDANCE
from doco.agents.config import AgentConfig
from doco.agents.base import BaseAgent


class ContentCreator(BaseAgent):
    content_creator_config = AgentConfig().content_creator

    def __init__(self): 
        super().__init__(provider=self.content_creator_config['provider'], 
                         llm_config=self.content_creator_config['llm_config'], 
                         tools=[], 
                         system_prompt=PERSONA_PROMPT, 
                         instruction=BLOG_PUBLICATION_GUIDANCE)

    def _build_agent(self, llm, tools: list, system_prompt: str, instruction: str):
        """Create an agent's core: allowing function callings and prompting"""
        prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "{system_prompt}\n{tool_names}\n{instruction}"
                ),
                MessagesPlaceholder(variable_name="messages"),
            ]
        )
        prompt = prompt.partial(system_prompt=system_prompt)
        prompt = prompt.partial(tool_names=", ".join([tool.name for tool in tools]))
        prompt = prompt.partial(instruction=instruction)
        return prompt | llm.bind_tools(tools)