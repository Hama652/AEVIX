"""Tokenizer-facing base contracts without implementing tokenization."""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field
from typing import Protocol, runtime_checkable


@dataclass(slots=True, frozen=True)
class TokenizerMetadata:
    """Metadata for a tokenizer family."""

    name: str
    vocabulary_size: int = 0
    special_tokens: tuple[str, ...] = ()
    metadata: dict[str, str] = field(default_factory=dict)


@runtime_checkable
class TokenizerProtocol(Protocol):
    """Minimal tokenizer contract for future language-model work."""

    def encode(self, text: str) -> list[int]:
        """Encode text into token ids."""

    def decode(self, token_ids: Sequence[int]) -> str:
        """Decode token ids into text."""

    @property
    def vocab_size(self) -> int:
        """Return the tokenizer vocabulary size."""
