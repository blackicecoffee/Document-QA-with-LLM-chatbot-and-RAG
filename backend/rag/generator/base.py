from abc import ABC, abstractmethod

from typing import Optional, Any

class BaseGenerator(ABC):
    def __init__(self, system_prompt: str, llm_model: str, provider: Optional[str]):
        self.system_prompt = system_prompt
        self.llm_model = llm_model
        self.provider = provider

    @abstractmethod
    def generate(self, query: str, context: Any) -> Any:
        """
        Generate response
        
        :param query: user's query
        :type query: str
        :param context: Retrieved context
        :type context: Any
        :return: response
        :rtype: Any
        """