"""
Module for the Web API service. This can be used to create a web API,
which uses an underlying web app to register endpoints and serve the app on
the specified host and port. It can be used to present functionality behind
specified endpoints, which can be called by clients to interact with the
service.
"""

from types import TracebackType
from typing import Union, Callable, Any
from typing_extensions import Self
from flask import Response
from src.app import WebApp, WebAppConfig


class WebAPI:
    """
    Base Web API service, which contains the run method to start the web API
    and requires implementations to add endpoint handlers to the web app.
    """

    def __init__(self) -> None:
        self._app = WebApp(
            config=WebAppConfig(
                host="0.0.0.0",
                port=12345,
                threads=4,
                connection_limit=100,
            )
        )
        self._endpoint_handlers: dict[
            str, tuple[list[str], str, Callable[..., Any]]
        ] = {
            "homepage": (["GET"], "/", self._create_homepage),
        }

    def __enter__(self) -> Self:
        """
        Method to enter the context manager.

        :return: The web API service.
        :rtype: Self
        """
        return self

    def __exit__(
        self,
        exc_type: Union[type[BaseException], None],
        exc_val: Union[BaseException, None],
        exc_tb: Union[TracebackType, None],
    ) -> None:
        """
        Method to exit the context manager.

        :param exc_type: The exception type.
        :type exc_type: Union[type[BaseException], None]
        :param exc_val: The exception value.
        :type exc_val: Union[BaseException, None]
        :param exc_tb: The exception traceback.
        :type exc_tb: Union[TracebackType, None]
        """

    def run(self) -> None:
        """
        Run the web API. This method adds the endpoint handlers to the web app
        and starts the server.
        """
        for name, (
            methods,
            endpoint,
            handler,
        ) in self._endpoint_handlers.items():
            self._app.add_endpoint(
                endpoint,
                name,
                handler,
                methods,
            )

        self._app.run()

    def _create_homepage(self, params: dict[str, Any]) -> Response:
        """
        Handler for creating the Flask API homepage. This is a GET request,
        which does not require any data to be passed in the request and simply
        returns a welcome message.

        :param params: The request parameters.
        :type params: dict[str, Any]
        :return: The response.
        :rtype: Response
        """
        _ = params
        return Response(
            "<h1> Hello, welcome to the Flask API homepage! </h1>", 200
        )
