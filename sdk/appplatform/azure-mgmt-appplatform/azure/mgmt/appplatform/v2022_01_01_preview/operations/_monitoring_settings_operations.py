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
from azure.core.polling import LROPoller, NoPolling, PollingMethod
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.arm_polling import ARMPolling
from msrest import Serializer

from .. import models as _models
from .._vendor import _convert_request, _format_url_section
T = TypeVar('T')
JSONType = Any
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False

def build_get_request(
    subscription_id: str,
    resource_group_name: str,
    service_name: str,
    **kwargs: Any
) -> HttpRequest:
    api_version = "2022-01-01-preview"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AppPlatform/Spring/{serviceName}/monitoringSettings/default')
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str'),
        "serviceName": _SERIALIZER.url("service_name", service_name, 'str'),
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


def build_update_put_request_initial(
    subscription_id: str,
    resource_group_name: str,
    service_name: str,
    *,
    json: JSONType = None,
    content: Any = None,
    **kwargs: Any
) -> HttpRequest:
    content_type = kwargs.pop('content_type', None)  # type: Optional[str]

    api_version = "2022-01-01-preview"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AppPlatform/Spring/{serviceName}/monitoringSettings/default')
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str'),
        "serviceName": _SERIALIZER.url("service_name", service_name, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        json=json,
        content=content,
        **kwargs
    )


def build_update_patch_request_initial(
    subscription_id: str,
    resource_group_name: str,
    service_name: str,
    *,
    json: JSONType = None,
    content: Any = None,
    **kwargs: Any
) -> HttpRequest:
    content_type = kwargs.pop('content_type', None)  # type: Optional[str]

    api_version = "2022-01-01-preview"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AppPlatform/Spring/{serviceName}/monitoringSettings/default')
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str'),
        "serviceName": _SERIALIZER.url("service_name", service_name, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PATCH",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        json=json,
        content=content,
        **kwargs
    )

class MonitoringSettingsOperations(object):
    """MonitoringSettingsOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.appplatform.v2022_01_01_preview.models
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
    def get(
        self,
        resource_group_name: str,
        service_name: str,
        **kwargs: Any
    ) -> "_models.MonitoringSettingResource":
        """Get the Monitoring Setting and its properties.

        :param resource_group_name: The name of the resource group that contains the resource. You can
         obtain this value from the Azure Resource Manager API or the portal.
        :type resource_group_name: str
        :param service_name: The name of the Service resource.
        :type service_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MonitoringSettingResource, or the result of cls(response)
        :rtype: ~azure.mgmt.appplatform.v2022_01_01_preview.models.MonitoringSettingResource
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.MonitoringSettingResource"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_get_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            service_name=service_name,
            template_url=self.get.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MonitoringSettingResource', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AppPlatform/Spring/{serviceName}/monitoringSettings/default'}  # type: ignore


    def _update_put_initial(
        self,
        resource_group_name: str,
        service_name: str,
        monitoring_setting_resource: "_models.MonitoringSettingResource",
        **kwargs: Any
    ) -> "_models.MonitoringSettingResource":
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.MonitoringSettingResource"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(monitoring_setting_resource, 'MonitoringSettingResource')

        request = build_update_put_request_initial(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            service_name=service_name,
            content_type=content_type,
            json=_json,
            template_url=self._update_put_initial.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize('MonitoringSettingResource', pipeline_response)

        if response.status_code == 202:
            deserialized = self._deserialize('MonitoringSettingResource', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    _update_put_initial.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AppPlatform/Spring/{serviceName}/monitoringSettings/default'}  # type: ignore


    @distributed_trace
    def begin_update_put(
        self,
        resource_group_name: str,
        service_name: str,
        monitoring_setting_resource: "_models.MonitoringSettingResource",
        **kwargs: Any
    ) -> LROPoller["_models.MonitoringSettingResource"]:
        """Update the Monitoring Setting.

        :param resource_group_name: The name of the resource group that contains the resource. You can
         obtain this value from the Azure Resource Manager API or the portal.
        :type resource_group_name: str
        :param service_name: The name of the Service resource.
        :type service_name: str
        :param monitoring_setting_resource: Parameters for the update operation.
        :type monitoring_setting_resource:
         ~azure.mgmt.appplatform.v2022_01_01_preview.models.MonitoringSettingResource
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be ARMPolling. Pass in False for this
         operation to not poll, or pass in your own initialized polling object for a personal polling
         strategy.
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of LROPoller that returns either MonitoringSettingResource or the result
         of cls(response)
        :rtype:
         ~azure.core.polling.LROPoller[~azure.mgmt.appplatform.v2022_01_01_preview.models.MonitoringSettingResource]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]
        polling = kwargs.pop('polling', True)  # type: Union[bool, azure.core.polling.PollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.MonitoringSettingResource"]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        cont_token = kwargs.pop('continuation_token', None)  # type: Optional[str]
        if cont_token is None:
            raw_result = self._update_put_initial(
                resource_group_name=resource_group_name,
                service_name=service_name,
                monitoring_setting_resource=monitoring_setting_resource,
                content_type=content_type,
                cls=lambda x,y,z: x,
                **kwargs
            )
        kwargs.pop('error_map', None)

        def get_long_running_output(pipeline_response):
            response = pipeline_response.http_response
            deserialized = self._deserialize('MonitoringSettingResource', pipeline_response)
            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized


        if polling is True: polling_method = ARMPolling(lro_delay, lro_options={'final-state-via': 'azure-async-operation'}, **kwargs)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        if cont_token:
            return LROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output
            )
        else:
            return LROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_update_put.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AppPlatform/Spring/{serviceName}/monitoringSettings/default'}  # type: ignore

    def _update_patch_initial(
        self,
        resource_group_name: str,
        service_name: str,
        monitoring_setting_resource: "_models.MonitoringSettingResource",
        **kwargs: Any
    ) -> "_models.MonitoringSettingResource":
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.MonitoringSettingResource"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(monitoring_setting_resource, 'MonitoringSettingResource')

        request = build_update_patch_request_initial(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            service_name=service_name,
            content_type=content_type,
            json=_json,
            template_url=self._update_patch_initial.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize('MonitoringSettingResource', pipeline_response)

        if response.status_code == 202:
            deserialized = self._deserialize('MonitoringSettingResource', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    _update_patch_initial.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AppPlatform/Spring/{serviceName}/monitoringSettings/default'}  # type: ignore


    @distributed_trace
    def begin_update_patch(
        self,
        resource_group_name: str,
        service_name: str,
        monitoring_setting_resource: "_models.MonitoringSettingResource",
        **kwargs: Any
    ) -> LROPoller["_models.MonitoringSettingResource"]:
        """Update the Monitoring Setting.

        :param resource_group_name: The name of the resource group that contains the resource. You can
         obtain this value from the Azure Resource Manager API or the portal.
        :type resource_group_name: str
        :param service_name: The name of the Service resource.
        :type service_name: str
        :param monitoring_setting_resource: Parameters for the update operation.
        :type monitoring_setting_resource:
         ~azure.mgmt.appplatform.v2022_01_01_preview.models.MonitoringSettingResource
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be ARMPolling. Pass in False for this
         operation to not poll, or pass in your own initialized polling object for a personal polling
         strategy.
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of LROPoller that returns either MonitoringSettingResource or the result
         of cls(response)
        :rtype:
         ~azure.core.polling.LROPoller[~azure.mgmt.appplatform.v2022_01_01_preview.models.MonitoringSettingResource]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]
        polling = kwargs.pop('polling', True)  # type: Union[bool, azure.core.polling.PollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.MonitoringSettingResource"]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        cont_token = kwargs.pop('continuation_token', None)  # type: Optional[str]
        if cont_token is None:
            raw_result = self._update_patch_initial(
                resource_group_name=resource_group_name,
                service_name=service_name,
                monitoring_setting_resource=monitoring_setting_resource,
                content_type=content_type,
                cls=lambda x,y,z: x,
                **kwargs
            )
        kwargs.pop('error_map', None)

        def get_long_running_output(pipeline_response):
            response = pipeline_response.http_response
            deserialized = self._deserialize('MonitoringSettingResource', pipeline_response)
            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized


        if polling is True: polling_method = ARMPolling(lro_delay, lro_options={'final-state-via': 'azure-async-operation'}, **kwargs)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        if cont_token:
            return LROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output
            )
        else:
            return LROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_update_patch.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AppPlatform/Spring/{serviceName}/monitoringSettings/default'}  # type: ignore
