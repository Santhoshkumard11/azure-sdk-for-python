# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import Any, AsyncIterable, Callable, Dict, Generic, Optional, TypeVar, Union
import warnings

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.polling import AsyncLROPoller, AsyncNoPolling, AsyncPollingMethod
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.async_arm_polling import AsyncARMPolling

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._resource_groups_operations import build_check_existence_request, build_create_or_update_request, build_delete_request_initial, build_export_template_request, build_get_request, build_list_request, build_update_request
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class ResourceGroupsOperations:
    """ResourceGroupsOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.resource.resources.v2019_03_01.models
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
    async def check_existence(
        self,
        resource_group_name: str,
        **kwargs: Any
    ) -> bool:
        """Checks whether a resource group exists.

        :param resource_group_name: The name of the resource group to check. The name is case
         insensitive.
        :type resource_group_name: str
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

        
        request = build_check_existence_request(
            resource_group_name=resource_group_name,
            subscription_id=self._config.subscription_id,
            template_url=self.check_existence.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204, 404]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})
        return 200 <= response.status_code <= 299

    check_existence.metadata = {'url': '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}'}  # type: ignore


    @distributed_trace_async
    async def create_or_update(
        self,
        resource_group_name: str,
        parameters: "_models.ResourceGroup",
        **kwargs: Any
    ) -> "_models.ResourceGroup":
        """Creates or updates a resource group.

        :param resource_group_name: The name of the resource group to create or update. Can include
         alphanumeric, underscore, parentheses, hyphen, period (except at end), and Unicode characters
         that match the allowed characters.
        :type resource_group_name: str
        :param parameters: Parameters supplied to the create or update a resource group.
        :type parameters: ~azure.mgmt.resource.resources.v2019_03_01.models.ResourceGroup
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ResourceGroup, or the result of cls(response)
        :rtype: ~azure.mgmt.resource.resources.v2019_03_01.models.ResourceGroup
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ResourceGroup"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(parameters, 'ResourceGroup')

        request = build_create_or_update_request(
            resource_group_name=resource_group_name,
            subscription_id=self._config.subscription_id,
            content_type=content_type,
            json=_json,
            template_url=self.create_or_update.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize('ResourceGroup', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('ResourceGroup', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_or_update.metadata = {'url': '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}'}  # type: ignore


    async def _delete_initial(
        self,
        resource_group_name: str,
        **kwargs: Any
    ) -> None:
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_delete_request_initial(
            resource_group_name=resource_group_name,
            subscription_id=self._config.subscription_id,
            template_url=self._delete_initial.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    _delete_initial.metadata = {'url': '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}'}  # type: ignore


    @distributed_trace_async
    async def begin_delete(
        self,
        resource_group_name: str,
        **kwargs: Any
    ) -> AsyncLROPoller[None]:
        """Deletes a resource group.

        When you delete a resource group, all of its resources are also deleted. Deleting a resource
        group deletes all of its template deployments and currently stored operations.

        :param resource_group_name: The name of the resource group to delete. The name is case
         insensitive.
        :type resource_group_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either None or the result of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[None]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        polling = kwargs.pop('polling', True)  # type: Union[bool, azure.core.polling.AsyncPollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        cont_token = kwargs.pop('continuation_token', None)  # type: Optional[str]
        if cont_token is None:
            raw_result = await self._delete_initial(
                resource_group_name=resource_group_name,
                cls=lambda x,y,z: x,
                **kwargs
            )
        kwargs.pop('error_map', None)

        def get_long_running_output(pipeline_response):
            if cls:
                return cls(pipeline_response, None, {})


        if polling is True: polling_method = AsyncARMPolling(lro_delay, **kwargs)
        elif polling is False: polling_method = AsyncNoPolling()
        else: polling_method = polling
        if cont_token:
            return AsyncLROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output
            )
        else:
            return AsyncLROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}'}  # type: ignore

    @distributed_trace_async
    async def get(
        self,
        resource_group_name: str,
        **kwargs: Any
    ) -> "_models.ResourceGroup":
        """Gets a resource group.

        :param resource_group_name: The name of the resource group to get. The name is case
         insensitive.
        :type resource_group_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ResourceGroup, or the result of cls(response)
        :rtype: ~azure.mgmt.resource.resources.v2019_03_01.models.ResourceGroup
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ResourceGroup"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_get_request(
            resource_group_name=resource_group_name,
            subscription_id=self._config.subscription_id,
            template_url=self.get.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ResourceGroup', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}'}  # type: ignore


    @distributed_trace_async
    async def update(
        self,
        resource_group_name: str,
        parameters: "_models.ResourceGroupPatchable",
        **kwargs: Any
    ) -> "_models.ResourceGroup":
        """Updates a resource group.

        Resource groups can be updated through a simple PATCH operation to a group address. The format
        of the request is the same as that for creating a resource group. If a field is unspecified,
        the current value is retained.

        :param resource_group_name: The name of the resource group to update. The name is case
         insensitive.
        :type resource_group_name: str
        :param parameters: Parameters supplied to update a resource group.
        :type parameters: ~azure.mgmt.resource.resources.v2019_03_01.models.ResourceGroupPatchable
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ResourceGroup, or the result of cls(response)
        :rtype: ~azure.mgmt.resource.resources.v2019_03_01.models.ResourceGroup
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ResourceGroup"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(parameters, 'ResourceGroupPatchable')

        request = build_update_request(
            resource_group_name=resource_group_name,
            subscription_id=self._config.subscription_id,
            content_type=content_type,
            json=_json,
            template_url=self.update.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ResourceGroup', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    update.metadata = {'url': '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}'}  # type: ignore


    @distributed_trace_async
    async def export_template(
        self,
        resource_group_name: str,
        parameters: "_models.ExportTemplateRequest",
        **kwargs: Any
    ) -> "_models.ResourceGroupExportResult":
        """Captures the specified resource group as a template.

        :param resource_group_name: The name of the resource group to export as a template.
        :type resource_group_name: str
        :param parameters: Parameters for exporting the template.
        :type parameters: ~azure.mgmt.resource.resources.v2019_03_01.models.ExportTemplateRequest
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ResourceGroupExportResult, or the result of cls(response)
        :rtype: ~azure.mgmt.resource.resources.v2019_03_01.models.ResourceGroupExportResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ResourceGroupExportResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(parameters, 'ExportTemplateRequest')

        request = build_export_template_request(
            resource_group_name=resource_group_name,
            subscription_id=self._config.subscription_id,
            content_type=content_type,
            json=_json,
            template_url=self.export_template.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ResourceGroupExportResult', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    export_template.metadata = {'url': '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/exportTemplate'}  # type: ignore


    @distributed_trace
    def list(
        self,
        filter: Optional[str] = None,
        top: Optional[int] = None,
        **kwargs: Any
    ) -> AsyncIterable["_models.ResourceGroupListResult"]:
        """Gets all the resource groups for a subscription.

        :param filter: The filter to apply on the operation.:code:`<br>`:code:`<br>`You can filter by
         tag names and values. For example, to filter for a tag name and value, use $filter=tagName eq
         'tag1' and tagValue eq 'Value1'.
        :type filter: str
        :param top: The number of results to return. If null is passed, returns all resource groups.
        :type top: int
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either ResourceGroupListResult or the result of
         cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.resource.resources.v2019_03_01.models.ResourceGroupListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ResourceGroupListResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_request(
                    subscription_id=self._config.subscription_id,
                    filter=filter,
                    top=top,
                    template_url=self.list.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                
                request = build_list_request(
                    subscription_id=self._config.subscription_id,
                    filter=filter,
                    top=top,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("ResourceGroupListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response


        return AsyncItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': '/subscriptions/{subscriptionId}/resourcegroups'}  # type: ignore
