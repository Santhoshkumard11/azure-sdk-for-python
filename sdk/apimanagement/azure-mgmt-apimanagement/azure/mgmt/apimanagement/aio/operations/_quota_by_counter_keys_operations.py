# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import Any, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._quota_by_counter_keys_operations import build_list_by_service_request, build_update_request
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class QuotaByCounterKeysOperations:
    """QuotaByCounterKeysOperations async operations.

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

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace_async
    async def list_by_service(
        self,
        resource_group_name: str,
        service_name: str,
        quota_counter_key: str,
        **kwargs: Any
    ) -> "_models.QuotaCounterCollection":
        """Lists a collection of current quota counter periods associated with the counter-key configured
        in the policy on the specified service instance. The api does not support paging yet.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param service_name: The name of the API Management service.
        :type service_name: str
        :param quota_counter_key: Quota counter key identifier.This is the result of expression defined
         in counter-key attribute of the quota-by-key policy.For Example, if you specify
         counter-key="boo" in the policy, then it’s accessible by "boo" counter key. But if it’s defined
         as counter-key="@("b"+"a")" then it will be accessible by "ba" key.
        :type quota_counter_key: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: QuotaCounterCollection, or the result of cls(response)
        :rtype: ~api_management_client.models.QuotaCounterCollection
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.QuotaCounterCollection"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_list_by_service_request(
            resource_group_name=resource_group_name,
            service_name=service_name,
            quota_counter_key=quota_counter_key,
            subscription_id=self._config.subscription_id,
            template_url=self.list_by_service.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('QuotaCounterCollection', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    list_by_service.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/quotas/{quotaCounterKey}'}  # type: ignore


    @distributed_trace_async
    async def update(
        self,
        resource_group_name: str,
        service_name: str,
        quota_counter_key: str,
        parameters: "_models.QuotaCounterValueUpdateContract",
        **kwargs: Any
    ) -> "_models.QuotaCounterCollection":
        """Updates all the quota counter values specified with the existing quota counter key to a value
        in the specified service instance. This should be used for reset of the quota counter values.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param service_name: The name of the API Management service.
        :type service_name: str
        :param quota_counter_key: Quota counter key identifier.This is the result of expression defined
         in counter-key attribute of the quota-by-key policy.For Example, if you specify
         counter-key="boo" in the policy, then it’s accessible by "boo" counter key. But if it’s defined
         as counter-key="@("b"+"a")" then it will be accessible by "ba" key.
        :type quota_counter_key: str
        :param parameters: The value of the quota counter to be applied to all quota counter periods.
        :type parameters: ~api_management_client.models.QuotaCounterValueUpdateContract
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: QuotaCounterCollection, or the result of cls(response)
        :rtype: ~api_management_client.models.QuotaCounterCollection
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.QuotaCounterCollection"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(parameters, 'QuotaCounterValueUpdateContract')

        request = build_update_request(
            resource_group_name=resource_group_name,
            service_name=service_name,
            quota_counter_key=quota_counter_key,
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
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('QuotaCounterCollection', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/quotas/{quotaCounterKey}'}  # type: ignore

