# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from msrest import Serializer

from .. import models as _models
from .._vendor import _convert_request, _format_url_section

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Optional, TypeVar
    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False
# fmt: off

def build_query_pipeline_runs_by_workspace_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = kwargs.pop('api_version', "2020-12-01")  # type: str
    content_type = kwargs.pop('content_type', None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/queryPipelineRuns')

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_get_pipeline_run_request(
    run_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = kwargs.pop('api_version', "2020-12-01")  # type: str

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/pipelineruns/{runId}')
    path_format_arguments = {
        "runId": _SERIALIZER.url("run_id", run_id, 'str'),
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


def build_query_activity_runs_request(
    pipeline_name,  # type: str
    run_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = kwargs.pop('api_version', "2020-12-01")  # type: str
    content_type = kwargs.pop('content_type', None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/pipelines/{pipelineName}/pipelineruns/{runId}/queryActivityruns')
    path_format_arguments = {
        "pipelineName": _SERIALIZER.url("pipeline_name", pipeline_name, 'str', max_length=260, min_length=1, pattern=r'^[A-Za-z0-9_][^<>*#.%&:\\+?/]*$'),
        "runId": _SERIALIZER.url("run_id", run_id, 'str'),
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
        method="POST",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_cancel_pipeline_run_request(
    run_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = kwargs.pop('api_version', "2020-12-01")  # type: str
    is_recursive = kwargs.pop('is_recursive', None)  # type: Optional[bool]

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/pipelineruns/{runId}/cancel')
    path_format_arguments = {
        "runId": _SERIALIZER.url("run_id", run_id, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if is_recursive is not None:
        query_parameters['isRecursive'] = _SERIALIZER.query("is_recursive", is_recursive, 'bool')
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )

# fmt: on
class PipelineRunOperations(object):
    """PipelineRunOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.synapse.artifacts.models
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
    def query_pipeline_runs_by_workspace(
        self,
        filter_parameters,  # type: "_models.RunFilterParameters"
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.PipelineRunsQueryResponse"
        """Query pipeline runs in the workspace based on input filter conditions.

        :param filter_parameters: Parameters to filter the pipeline run.
        :type filter_parameters: ~azure.synapse.artifacts.models.RunFilterParameters
        :keyword api_version: Api Version. The default value is "2020-12-01". Note that overriding this
         default value may result in unsupported behavior.
        :paramtype api_version: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PipelineRunsQueryResponse, or the result of cls(response)
        :rtype: ~azure.synapse.artifacts.models.PipelineRunsQueryResponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.PipelineRunsQueryResponse"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2020-12-01")  # type: str
        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(filter_parameters, 'RunFilterParameters')

        request = build_query_pipeline_runs_by_workspace_request(
            api_version=api_version,
            content_type=content_type,
            json=_json,
            template_url=self.query_pipeline_runs_by_workspace.metadata['url'],
        )
        request = _convert_request(request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.CloudErrorAutoGenerated, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('PipelineRunsQueryResponse', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    query_pipeline_runs_by_workspace.metadata = {'url': '/queryPipelineRuns'}  # type: ignore


    @distributed_trace
    def get_pipeline_run(
        self,
        run_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.PipelineRun"
        """Get a pipeline run by its run ID.

        :param run_id: The pipeline run identifier.
        :type run_id: str
        :keyword api_version: Api Version. The default value is "2020-12-01". Note that overriding this
         default value may result in unsupported behavior.
        :paramtype api_version: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PipelineRun, or the result of cls(response)
        :rtype: ~azure.synapse.artifacts.models.PipelineRun
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.PipelineRun"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2020-12-01")  # type: str

        
        request = build_get_pipeline_run_request(
            run_id=run_id,
            api_version=api_version,
            template_url=self.get_pipeline_run.metadata['url'],
        )
        request = _convert_request(request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.CloudErrorAutoGenerated, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('PipelineRun', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_pipeline_run.metadata = {'url': '/pipelineruns/{runId}'}  # type: ignore


    @distributed_trace
    def query_activity_runs(
        self,
        pipeline_name,  # type: str
        run_id,  # type: str
        filter_parameters,  # type: "_models.RunFilterParameters"
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.ActivityRunsQueryResponse"
        """Query activity runs based on input filter conditions.

        :param pipeline_name: The pipeline name.
        :type pipeline_name: str
        :param run_id: The pipeline run identifier.
        :type run_id: str
        :param filter_parameters: Parameters to filter the activity runs.
        :type filter_parameters: ~azure.synapse.artifacts.models.RunFilterParameters
        :keyword api_version: Api Version. The default value is "2020-12-01". Note that overriding this
         default value may result in unsupported behavior.
        :paramtype api_version: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ActivityRunsQueryResponse, or the result of cls(response)
        :rtype: ~azure.synapse.artifacts.models.ActivityRunsQueryResponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ActivityRunsQueryResponse"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2020-12-01")  # type: str
        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(filter_parameters, 'RunFilterParameters')

        request = build_query_activity_runs_request(
            pipeline_name=pipeline_name,
            run_id=run_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            template_url=self.query_activity_runs.metadata['url'],
        )
        request = _convert_request(request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.CloudErrorAutoGenerated, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('ActivityRunsQueryResponse', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    query_activity_runs.metadata = {'url': '/pipelines/{pipelineName}/pipelineruns/{runId}/queryActivityruns'}  # type: ignore


    @distributed_trace
    def cancel_pipeline_run(
        self,
        run_id,  # type: str
        is_recursive=None,  # type: Optional[bool]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Cancel a pipeline run by its run ID.

        :param run_id: The pipeline run identifier.
        :type run_id: str
        :param is_recursive: If true, cancel all the Child pipelines that are triggered by the current
         pipeline.
        :type is_recursive: bool
        :keyword api_version: Api Version. The default value is "2020-12-01". Note that overriding this
         default value may result in unsupported behavior.
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

        api_version = kwargs.pop('api_version', "2020-12-01")  # type: str

        
        request = build_cancel_pipeline_run_request(
            run_id=run_id,
            api_version=api_version,
            is_recursive=is_recursive,
            template_url=self.cancel_pipeline_run.metadata['url'],
        )
        request = _convert_request(request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.CloudErrorAutoGenerated, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    cancel_pipeline_run.metadata = {'url': '/pipelineruns/{runId}/cancel'}  # type: ignore

