"""
Module for the Web API service. This can be used to create a web API,
which uses an underlying web app to register endpoints and serve the app on
the specified host and port. It can be used to present functionality behind
specified endpoints, which can be called by clients to interact with the
service.
"""

from typing import Callable, Any

from flask import Response

from src.base_api import BaseWebAPI


class WebAPI(BaseWebAPI):
    """
    Base Web API service, which contains the run method to start the web API
    and requires implementations to add endpoint handlers to the web app.
    """

    def __init__(self) -> None:
        super().__init__(
            host="0.0.0.0",
            port=12345,
        )

    @property
    def _endpoint_handlers(
        self,
    ) -> dict[str, tuple[list[str], str, Callable[..., Any]]]:
        """
        Property to get the endpoint handlers. This should be implemented by
        subclasses to provide the actual endpoint handlers.

        :return: The endpoint handlers.
        :rtype: dict[str, tuple[list[str], str, Callable[..., Any]]]
        """
        return {
            "homepage": (["GET"], "/", self._create_homepage),
        }

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
