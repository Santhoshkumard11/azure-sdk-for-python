# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import Any, Callable, Dict, Generic, Optional, TypeVar, Union
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.mgmt.core.exceptions import ARMErrorFormat
from msrest import Serializer

from .. import models as _models
from .._vendor import _convert_request, _format_url_section
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False

def build_list_by_notification_request(
    resource_group_name: str,
    service_name: str,
    notification_name: Union[str, "_models.NotificationName"],
    subscription_id: str,
    **kwargs: Any
) -> HttpRequest:
    api_version = "2021-08-01"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/notifications/{notificationName}/recipientEmails')
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str'),
        "serviceName": _SERIALIZER.url("service_name", service_name, 'str', max_length=50, min_length=1, pattern=r'^[a-zA-Z](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?$'),
        "notificationName": _SERIALIZER.url("notification_name", notification_name, 'str'),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_check_entity_exists_request(
    resource_group_name: str,
    service_name: str,
    notification_name: Union[str, "_models.NotificationName"],
    email: str,
    subscription_id: str,
    **kwargs: Any
) -> HttpRequest:
    api_version = "2021-08-01"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/notifications/{notificationName}/recipientEmails/{email}')
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str'),
        "serviceName": _SERIALIZER.url("service_name", service_name, 'str', max_length=50, min_length=1, pattern=r'^[a-zA-Z](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?$'),
        "notificationName": _SERIALIZER.url("notification_name", notification_name, 'str'),
        "email": _SERIALIZER.url("email", email, 'str'),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="HEAD",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_create_or_update_request(
    resource_group_name: str,
    service_name: str,
    notification_name: Union[str, "_models.NotificationName"],
    email: str,
    subscription_id: str,
    **kwargs: Any
) -> HttpRequest:
    api_version = "2021-08-01"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/notifications/{notificationName}/recipientEmails/{email}')
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str'),
        "serviceName": _SERIALIZER.url("service_name", service_name, 'str', max_length=50, min_length=1, pattern=r'^[a-zA-Z](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?$'),
        "notificationName": _SERIALIZER.url("notification_name", notification_name, 'str'),
        "email": _SERIALIZER.url("email", email, 'str'),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_delete_request(
    resource_group_name: str,
    service_name: str,
    notification_name: Union[str, "_models.NotificationName"],
    email: str,
    subscription_id: str,
    **kwargs: Any
) -> HttpRequest:
    api_version = "2021-08-01"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/notifications/{notificationName}/recipientEmails/{email}')
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str'),
        "serviceName": _SERIALIZER.url("service_name", service_name, 'str', max_length=50, min_length=1, pattern=r'^[a-zA-Z](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?$'),
        "notificationName": _SERIALIZER.url("notification_name", notification_name, 'str'),
        "email": _SERIALIZER.url("email", email, 'str'),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="DELETE",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )

class NotificationRecipientEmailOperations(object):
    """NotificationRecipientEmailOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~api_management_client.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace
    def list_by_notification(
        self,
        resource_group_name: str,
        service_name: str,
        notification_name: Union[str, "_models.NotificationName"],
        **kwargs: Any
    ) -> "_models.RecipientEmailCollection":
        """Gets the list of the Notification Recipient Emails subscribed to a notification.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param service_name: The name of the API Management service.
        :type service_name: str
        :param notification_name: Notification Name Identifier.
        :type notification_name: str or ~api_management_client.models.NotificationName
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: RecipientEmailCollection, or the result of cls(response)
        :rtype: ~api_management_client.models.RecipientEmailCollection
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.RecipientEmailCollection"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_list_by_notification_request(
            resource_group_name=resource_group_name,
            service_name=service_name,
            notification_name=notification_name,
            subscription_id=self._config.subscription_id,
            template_url=self.list_by_notification.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('RecipientEmailCollection', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    list_by_notification.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/notifications/{notificationName}/recipientEmails'}  # type: ignore


    @distributed_trace
    def check_entity_exists(
        self,
        resource_group_name: str,
        service_name: str,
        notification_name: Union[str, "_models.NotificationName"],
        email: str,
        **kwargs: Any
    ) -> bool:
        """Determine if Notification Recipient Email subscribed to the notification.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param service_name: The name of the API Management service.
        :type service_name: str
        :param notification_name: Notification Name Identifier.
        :type notification_name: str or ~api_management_client.models.NotificationName
        :param email: Email identifier.
        :type email: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: bool, or the result of cls(response)
        :rtype: bool
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_check_entity_exists_request(
            resource_group_name=resource_group_name,
            service_name=service_name,
            notification_name=notification_name,
            email=email,
            subscription_id=self._config.subscription_id,
            template_url=self.check_entity_exists.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204, 404]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})
        return 200 <= response.status_code <= 299

    check_entity_exists.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/notifications/{notificationName}/recipientEmails/{email}'}  # type: ignore


    @distributed_trace
    def create_or_update(
        self,
        resource_group_name: str,
        service_name: str,
        notification_name: Union[str, "_models.NotificationName"],
        email: str,
        **kwargs: Any
    ) -> "_models.RecipientEmailContract":
        """Adds the Email address to the list of Recipients for the Notification.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param service_name: The name of the API Management service.
        :type service_name: str
        :param notification_name: Notification Name Identifier.
        :type notification_name: str or ~api_management_client.models.NotificationName
        :param email: Email identifier.
        :type email: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: RecipientEmailContract, or the result of cls(response)
        :rtype: ~api_management_client.models.RecipientEmailContract
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.RecipientEmailContract"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_create_or_update_request(
            resource_group_name=resource_group_name,
            service_name=service_name,
            notification_name=notification_name,
            email=email,
            subscription_id=self._config.subscription_id,
            template_url=self.create_or_update.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize('RecipientEmailContract', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('RecipientEmailContract', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_or_update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/notifications/{notificationName}/recipientEmails/{email}'}  # type: ignore


    @distributed_trace
    def delete(
        self,
        resource_group_name: str,
        service_name: str,
        notification_name: Union[str, "_models.NotificationName"],
        email: str,
        **kwargs: Any
    ) -> None:
        """Removes the email from the list of Notification.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param service_name: The name of the API Management service.
        :type service_name: str
        :param notification_name: Notification Name Identifier.
        :type notification_name: str or ~api_management_client.models.NotificationName
        :param email: Email identifier.
        :type email: str
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

        
        request = build_delete_request(
            resource_group_name=resource_group_name,
            service_name=service_name,
            notification_name=notification_name,
            email=email,
            subscription_id=self._config.subscription_id,
            template_url=self.delete.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/notifications/{notificationName}/recipientEmails/{email}'}  # type: ignore

