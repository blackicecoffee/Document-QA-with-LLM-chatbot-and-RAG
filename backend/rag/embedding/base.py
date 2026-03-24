from abc import ABC, abstractmethod
from typing import Any, List

import numpy as np

class BaseEmbedding(ABC):
    @abstractmethod
    def embed(self, query: str) -> np.array[float]:
        """
        Generate vector embedding for query
        
        :param query: input string
        :type query: str
        :return: vector embedding for query
        :rtype: np.array[float]
        """