# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import Any, Callable, Dict, Generic, List, Optional, TypeVar, Union
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._communication_identity_operations import build_create_request, build_delete_request, build_exchange_teams_user_access_token_request, build_issue_access_token_request, build_revoke_access_tokens_request

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class CommunicationIdentityOperations:
    """CommunicationIdentityOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.communication.identity.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace_async
    async def create(
        self,
        create_token_with_scopes: Optional[List[Union[str, "_models.CommunicationTokenScope"]]] = None,
        **kwargs: Any
    ) -> "_models.CommunicationIdentityAccessTokenResult":
        """Create a new identity, and optionally, an access token.

        Create a new identity, and optionally, an access token.

        :param create_token_with_scopes: Also create access token for the created identity.
        :type create_token_with_scopes: list[str or
         ~azure.communication.identity.models.CommunicationTokenScope]
        :keyword api_version: Api Version. The default value is "2021-10-31-preview". Note that
         overriding this default value may result in unsupported behavior.
        :paramtype api_version: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CommunicationIdentityAccessTokenResult, or the result of cls(response)
        :rtype: ~azure.communication.identity.models.CommunicationIdentityAccessTokenResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.CommunicationIdentityAccessTokenResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2021-10-31-preview")  # type: str
        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _body = _models.CommunicationIdentityCreateRequest(create_token_with_scopes=create_token_with_scopes)
        if _body is not None:
            json = self._serialize.body(_body, 'CommunicationIdentityCreateRequest')
        else:
            json = None

        request = build_create_request(
            api_version=api_version,
            content_type=content_type,
            json=json,
            template_url=self.create.metadata['url'],
        )
        request = _convert_request(request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.CommunicationErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('CommunicationIdentityAccessTokenResult', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create.metadata = {'url': '/identities'}  # type: ignore


    @distributed_trace_async
    async def delete(
        self,
        id: str,
        **kwargs: Any
    ) -> None:
        """Delete the identity, revoke all tokens for the identity and delete all associated data.

        Delete the identity, revoke all tokens for the identity and delete all associated data.

        :param id: Identifier of the identity to be deleted.
        :type id: str
        :keyword api_version: Api Version. The default value is "2021-10-31-preview". Note that
         overriding this default value may result in unsupported behavior.
        :paramtype api_version: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2021-10-31-preview")  # type: str

        
        request = build_delete_request(
            id=id,
            api_version=api_version,
            template_url=self.delete.metadata['url'],
        )
        request = _convert_request(request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.CommunicationErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {'url': '/identities/{id}'}  # type: ignore


    @distributed_trace_async
    async def revoke_access_tokens(
        self,
        id: str,
        **kwargs: Any
    ) -> None:
        """Revoke all access tokens for the specific identity.

        Revoke all access tokens for the specific identity.

        :param id: Identifier of the identity.
        :type id: str
        :keyword api_version: Api Version. The default value is "2021-10-31-preview". Note that
         overriding this default value may result in unsupported behavior.
        :paramtype api_version: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2021-10-31-preview")  # type: str

        
        request = build_revoke_access_tokens_request(
            id=id,
            api_version=api_version,
            template_url=self.revoke_access_tokens.metadata['url'],
        )
        request = _convert_request(request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.CommunicationErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    revoke_access_tokens.metadata = {'url': '/identities/{id}/:revokeAccessTokens'}  # type: ignore


    @distributed_trace_async
    async def exchange_teams_user_access_token(
        self,
        token: str,
        **kwargs: Any
    ) -> "_models.CommunicationIdentityAccessToken":
        """Exchange an AAD access token of a Teams user for a new Communication Identity access token with
        a matching expiration time.

        Exchange an AAD access token of a Teams user for a new Communication Identity access token with
        a matching expiration time.

        :param token: AAD access token of a Teams User to acquire a new Communication Identity access
         token.
        :type token: str
        :keyword api_version: Api Version. The default value is "2021-10-31-preview". Note that
         overriding this default value may result in unsupported behavior.
        :paramtype api_version: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CommunicationIdentityAccessToken, or the result of cls(response)
        :rtype: ~azure.communication.identity.models.CommunicationIdentityAccessToken
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.CommunicationIdentityAccessToken"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2021-10-31-preview")  # type: str
        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _body = _models.TeamsUserAccessTokenRequest(token=token)
        json = self._serialize.body(_body, 'TeamsUserAccessTokenRequest')

        request = build_exchange_teams_user_access_token_request(
            api_version=api_version,
            content_type=content_type,
            json=json,
            template_url=self.exchange_teams_user_access_token.metadata['url'],
        )
        request = _convert_request(request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.CommunicationErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('CommunicationIdentityAccessToken', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    exchange_teams_user_access_token.metadata = {'url': '/teamsUser/:exchangeAccessToken'}  # type: ignore


    @distributed_trace_async
    async def issue_access_token(
        self,
        id: str,
        scopes: List[Union[str, "_models.CommunicationTokenScope"]],
        **kwargs: Any
    ) -> "_models.CommunicationIdentityAccessToken":
        """Issue a new token for an identity.

        Issue a new token for an identity.

        :param id: Identifier of the identity to issue token for.
        :type id: str
        :param scopes: List of scopes attached to the token.
        :type scopes: list[str or ~azure.communication.identity.models.CommunicationTokenScope]
        :keyword api_version: Api Version. The default value is "2021-10-31-preview". Note that
         overriding this default value may result in unsupported behavior.
        :paramtype api_version: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CommunicationIdentityAccessToken, or the result of cls(response)
        :rtype: ~azure.communication.identity.models.CommunicationIdentityAccessToken
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.CommunicationIdentityAccessToken"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2021-10-31-preview")  # type: str
        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _body = _models.CommunicationIdentityAccessTokenRequest(scopes=scopes)
        json = self._serialize.body(_body, 'CommunicationIdentityAccessTokenRequest')

        request = build_issue_access_token_request(
            id=id,
            api_version=api_version,
            content_type=content_type,
            json=json,
            template_url=self.issue_access_token.metadata['url'],
        )
        request = _convert_request(request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.CommunicationErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('CommunicationIdentityAccessToken', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    issue_access_token.metadata = {'url': '/identities/{id}/:issueAccessToken'}  # type: ignore

