from types import TracebackType

from typing_extensions import Self


class FakeAsyncClient:

    def __init__(self) -> None:
        pass

    async def __aenter__(self) -> Self:
        print("Fake async client initialized.")
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        print("Fake async client exited.")

    async def invoke(self, value: str) -> str:
        return f"Fake async client invoked with value: {value}"
