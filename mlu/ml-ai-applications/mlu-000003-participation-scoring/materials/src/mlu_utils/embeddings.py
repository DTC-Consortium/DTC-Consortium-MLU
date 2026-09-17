"""Bedrock embeddings helper.

Wraps Amazon Nova Multimodal Embeddings as a LangChain Embeddings class so
the notebook can do `from mlu_utils.embeddings import NovaMultimodalEmbeddings`
instead of carrying a 30-line class definition inside the notebook.
"""
import json
from typing import List

from langchain_core.embeddings import Embeddings


class NovaMultimodalEmbeddings(Embeddings):
    """Embeddings via Amazon Nova 2 Multimodal Embeddings on Bedrock."""

    def __init__(
        self,
        client,
        model_id: str = "amazon.nova-2-multimodal-embeddings-v1:0",
        dimension: int = 1024,
    ):
        self.client = client
        self.model_id = model_id
        self.dimension = dimension

    def _embed(self, text: str, purpose: str) -> List[float]:
        body = {
            "taskType": "SINGLE_EMBEDDING",
            "singleEmbeddingParams": {
                "embeddingDimension": self.dimension,
                "embeddingPurpose": purpose,
                "text": {"truncationMode": "END", "value": text},
            },
        }
        response = self.client.invoke_model(modelId=self.model_id, body=json.dumps(body))
        result = json.loads(response["body"].read())
        return result["embeddings"][0]["embedding"]

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        return [self._embed(t, "GENERIC_INDEX") for t in texts]

    def embed_query(self, text: str) -> List[float]:
        return self._embed(text, "GENERIC_RETRIEVAL")
