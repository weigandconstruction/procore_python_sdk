# coding: utf-8

"""
    Procore Rest API Documentation

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.0
    Contact: apisupport@procore.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from pydantic import Field, StrictInt, StrictStr
from typing import List, Optional
from typing_extensions import Annotated
from procore_sdk.models.rest_v10_companies_company_id_workflow_permanent_logs_get200_response_inner import RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInner

from procore_sdk.api_client import ApiClient, RequestSerialized
from procore_sdk.api_response import ApiResponse
from procore_sdk.rest import RESTResponseType


class CoreWorkflowsLegacyWorkflowPermanentLogsApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def rest_v10_companies_company_id_workflow_permanent_logs_get(
        self,
        procore_company_id: Annotated[StrictInt, Field(description="Unique company identifier associated with the Procore User Account.")],
        company_id: Annotated[StrictInt, Field(description="Unique identifier for the company.")],
        filters_workflowed_object_type: Annotated[StrictStr, Field(description="Filter log(s) with matching workflowed object type")],
        filters_workflowed_object_id: Annotated[StrictInt, Field(description="Filter log(s) with matching workflowed object id")],
        page: Annotated[Optional[StrictInt], Field(description="Page")] = None,
        per_page: Annotated[Optional[StrictInt], Field(description="Elements per page")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> List[RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInner]:
        """List Workflow Permanent Logs

        Return a list of workflow permanent logs. Any resource using workflow should have log of activities and events related to the workflow.  See [Filtering on List Actions](https://developers.procore.com/documentation/filtering-on-list-actions) for information on using the filtering capabilities provided by this endpoint.

        :param procore_company_id: Unique company identifier associated with the Procore User Account. (required)
        :type procore_company_id: int
        :param company_id: Unique identifier for the company. (required)
        :type company_id: int
        :param filters_workflowed_object_type: Filter log(s) with matching workflowed object type (required)
        :type filters_workflowed_object_type: str
        :param filters_workflowed_object_id: Filter log(s) with matching workflowed object id (required)
        :type filters_workflowed_object_id: int
        :param page: Page
        :type page: int
        :param per_page: Elements per page
        :type per_page: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._rest_v10_companies_company_id_workflow_permanent_logs_get_serialize(
            procore_company_id=procore_company_id,
            company_id=company_id,
            filters_workflowed_object_type=filters_workflowed_object_type,
            filters_workflowed_object_id=filters_workflowed_object_id,
            page=page,
            per_page=per_page,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInner]",
            '400': "RestV10CompaniesCompanyIdWorkflowPermanentLogsGet400Response",
            '401': "RestV10CompaniesCompanyIdWorkflowPermanentLogsGet401Response",
            '403': "RestV10CompaniesCompanyIdWorkflowPermanentLogsGet401Response",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def rest_v10_companies_company_id_workflow_permanent_logs_get_with_http_info(
        self,
        procore_company_id: Annotated[StrictInt, Field(description="Unique company identifier associated with the Procore User Account.")],
        company_id: Annotated[StrictInt, Field(description="Unique identifier for the company.")],
        filters_workflowed_object_type: Annotated[StrictStr, Field(description="Filter log(s) with matching workflowed object type")],
        filters_workflowed_object_id: Annotated[StrictInt, Field(description="Filter log(s) with matching workflowed object id")],
        page: Annotated[Optional[StrictInt], Field(description="Page")] = None,
        per_page: Annotated[Optional[StrictInt], Field(description="Elements per page")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[List[RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInner]]:
        """List Workflow Permanent Logs

        Return a list of workflow permanent logs. Any resource using workflow should have log of activities and events related to the workflow.  See [Filtering on List Actions](https://developers.procore.com/documentation/filtering-on-list-actions) for information on using the filtering capabilities provided by this endpoint.

        :param procore_company_id: Unique company identifier associated with the Procore User Account. (required)
        :type procore_company_id: int
        :param company_id: Unique identifier for the company. (required)
        :type company_id: int
        :param filters_workflowed_object_type: Filter log(s) with matching workflowed object type (required)
        :type filters_workflowed_object_type: str
        :param filters_workflowed_object_id: Filter log(s) with matching workflowed object id (required)
        :type filters_workflowed_object_id: int
        :param page: Page
        :type page: int
        :param per_page: Elements per page
        :type per_page: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._rest_v10_companies_company_id_workflow_permanent_logs_get_serialize(
            procore_company_id=procore_company_id,
            company_id=company_id,
            filters_workflowed_object_type=filters_workflowed_object_type,
            filters_workflowed_object_id=filters_workflowed_object_id,
            page=page,
            per_page=per_page,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInner]",
            '400': "RestV10CompaniesCompanyIdWorkflowPermanentLogsGet400Response",
            '401': "RestV10CompaniesCompanyIdWorkflowPermanentLogsGet401Response",
            '403': "RestV10CompaniesCompanyIdWorkflowPermanentLogsGet401Response",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def rest_v10_companies_company_id_workflow_permanent_logs_get_without_preload_content(
        self,
        procore_company_id: Annotated[StrictInt, Field(description="Unique company identifier associated with the Procore User Account.")],
        company_id: Annotated[StrictInt, Field(description="Unique identifier for the company.")],
        filters_workflowed_object_type: Annotated[StrictStr, Field(description="Filter log(s) with matching workflowed object type")],
        filters_workflowed_object_id: Annotated[StrictInt, Field(description="Filter log(s) with matching workflowed object id")],
        page: Annotated[Optional[StrictInt], Field(description="Page")] = None,
        per_page: Annotated[Optional[StrictInt], Field(description="Elements per page")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """List Workflow Permanent Logs

        Return a list of workflow permanent logs. Any resource using workflow should have log of activities and events related to the workflow.  See [Filtering on List Actions](https://developers.procore.com/documentation/filtering-on-list-actions) for information on using the filtering capabilities provided by this endpoint.

        :param procore_company_id: Unique company identifier associated with the Procore User Account. (required)
        :type procore_company_id: int
        :param company_id: Unique identifier for the company. (required)
        :type company_id: int
        :param filters_workflowed_object_type: Filter log(s) with matching workflowed object type (required)
        :type filters_workflowed_object_type: str
        :param filters_workflowed_object_id: Filter log(s) with matching workflowed object id (required)
        :type filters_workflowed_object_id: int
        :param page: Page
        :type page: int
        :param per_page: Elements per page
        :type per_page: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._rest_v10_companies_company_id_workflow_permanent_logs_get_serialize(
            procore_company_id=procore_company_id,
            company_id=company_id,
            filters_workflowed_object_type=filters_workflowed_object_type,
            filters_workflowed_object_id=filters_workflowed_object_id,
            page=page,
            per_page=per_page,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInner]",
            '400': "RestV10CompaniesCompanyIdWorkflowPermanentLogsGet400Response",
            '401': "RestV10CompaniesCompanyIdWorkflowPermanentLogsGet401Response",
            '403': "RestV10CompaniesCompanyIdWorkflowPermanentLogsGet401Response",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _rest_v10_companies_company_id_workflow_permanent_logs_get_serialize(
        self,
        procore_company_id,
        company_id,
        filters_workflowed_object_type,
        filters_workflowed_object_id,
        page,
        per_page,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if company_id is not None:
            _path_params['company_id'] = company_id
        # process the query parameters
        if page is not None:
            
            _query_params.append(('page', page))
            
        if per_page is not None:
            
            _query_params.append(('per_page', per_page))
            
        if filters_workflowed_object_type is not None:
            
            _query_params.append(('filters[workflowed_object_type]', filters_workflowed_object_type))
            
        if filters_workflowed_object_id is not None:
            
            _query_params.append(('filters[workflowed_object_id]', filters_workflowed_object_id))
            
        # process the header parameters
        if procore_company_id is not None:
            _header_params['Procore-Company-Id'] = procore_company_id
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/rest/v1.0/companies/{company_id}/workflow_permanent_logs',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def rest_v10_projects_project_id_workflow_permanent_logs_get(
        self,
        procore_company_id: Annotated[StrictInt, Field(description="Unique company identifier associated with the Procore User Account.")],
        project_id: Annotated[StrictInt, Field(description="Unique identifier for the project.")],
        filters_workflowed_object_type: Annotated[StrictStr, Field(description="Filter log(s) with matching workflowed object type")],
        filters_workflowed_object_id: Annotated[StrictInt, Field(description="Filter log(s) with matching workflowed object id")],
        page: Annotated[Optional[StrictInt], Field(description="Page")] = None,
        per_page: Annotated[Optional[StrictInt], Field(description="Elements per page")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> List[RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInner]:
        """List Workflow Permanent Logs

        Return a list of workflow permanent logs. Any resource using workflow should have log of activities and events related to the workflow.  See [Filtering on List Actions](https://developers.procore.com/documentation/filtering-on-list-actions) for information on using the filtering capabilities provided by this endpoint.

        :param procore_company_id: Unique company identifier associated with the Procore User Account. (required)
        :type procore_company_id: int
        :param project_id: Unique identifier for the project. (required)
        :type project_id: int
        :param filters_workflowed_object_type: Filter log(s) with matching workflowed object type (required)
        :type filters_workflowed_object_type: str
        :param filters_workflowed_object_id: Filter log(s) with matching workflowed object id (required)
        :type filters_workflowed_object_id: int
        :param page: Page
        :type page: int
        :param per_page: Elements per page
        :type per_page: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._rest_v10_projects_project_id_workflow_permanent_logs_get_serialize(
            procore_company_id=procore_company_id,
            project_id=project_id,
            filters_workflowed_object_type=filters_workflowed_object_type,
            filters_workflowed_object_id=filters_workflowed_object_id,
            page=page,
            per_page=per_page,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInner]",
            '400': "RestV10CompaniesCompanyIdWorkflowPermanentLogsGet400Response",
            '401': "RestV10CompaniesCompanyIdWorkflowPermanentLogsGet401Response",
            '403': "RestV10CompaniesCompanyIdWorkflowPermanentLogsGet401Response",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def rest_v10_projects_project_id_workflow_permanent_logs_get_with_http_info(
        self,
        procore_company_id: Annotated[StrictInt, Field(description="Unique company identifier associated with the Procore User Account.")],
        project_id: Annotated[StrictInt, Field(description="Unique identifier for the project.")],
        filters_workflowed_object_type: Annotated[StrictStr, Field(description="Filter log(s) with matching workflowed object type")],
        filters_workflowed_object_id: Annotated[StrictInt, Field(description="Filter log(s) with matching workflowed object id")],
        page: Annotated[Optional[StrictInt], Field(description="Page")] = None,
        per_page: Annotated[Optional[StrictInt], Field(description="Elements per page")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[List[RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInner]]:
        """List Workflow Permanent Logs

        Return a list of workflow permanent logs. Any resource using workflow should have log of activities and events related to the workflow.  See [Filtering on List Actions](https://developers.procore.com/documentation/filtering-on-list-actions) for information on using the filtering capabilities provided by this endpoint.

        :param procore_company_id: Unique company identifier associated with the Procore User Account. (required)
        :type procore_company_id: int
        :param project_id: Unique identifier for the project. (required)
        :type project_id: int
        :param filters_workflowed_object_type: Filter log(s) with matching workflowed object type (required)
        :type filters_workflowed_object_type: str
        :param filters_workflowed_object_id: Filter log(s) with matching workflowed object id (required)
        :type filters_workflowed_object_id: int
        :param page: Page
        :type page: int
        :param per_page: Elements per page
        :type per_page: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._rest_v10_projects_project_id_workflow_permanent_logs_get_serialize(
            procore_company_id=procore_company_id,
            project_id=project_id,
            filters_workflowed_object_type=filters_workflowed_object_type,
            filters_workflowed_object_id=filters_workflowed_object_id,
            page=page,
            per_page=per_page,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInner]",
            '400': "RestV10CompaniesCompanyIdWorkflowPermanentLogsGet400Response",
            '401': "RestV10CompaniesCompanyIdWorkflowPermanentLogsGet401Response",
            '403': "RestV10CompaniesCompanyIdWorkflowPermanentLogsGet401Response",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def rest_v10_projects_project_id_workflow_permanent_logs_get_without_preload_content(
        self,
        procore_company_id: Annotated[StrictInt, Field(description="Unique company identifier associated with the Procore User Account.")],
        project_id: Annotated[StrictInt, Field(description="Unique identifier for the project.")],
        filters_workflowed_object_type: Annotated[StrictStr, Field(description="Filter log(s) with matching workflowed object type")],
        filters_workflowed_object_id: Annotated[StrictInt, Field(description="Filter log(s) with matching workflowed object id")],
        page: Annotated[Optional[StrictInt], Field(description="Page")] = None,
        per_page: Annotated[Optional[StrictInt], Field(description="Elements per page")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """List Workflow Permanent Logs

        Return a list of workflow permanent logs. Any resource using workflow should have log of activities and events related to the workflow.  See [Filtering on List Actions](https://developers.procore.com/documentation/filtering-on-list-actions) for information on using the filtering capabilities provided by this endpoint.

        :param procore_company_id: Unique company identifier associated with the Procore User Account. (required)
        :type procore_company_id: int
        :param project_id: Unique identifier for the project. (required)
        :type project_id: int
        :param filters_workflowed_object_type: Filter log(s) with matching workflowed object type (required)
        :type filters_workflowed_object_type: str
        :param filters_workflowed_object_id: Filter log(s) with matching workflowed object id (required)
        :type filters_workflowed_object_id: int
        :param page: Page
        :type page: int
        :param per_page: Elements per page
        :type per_page: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._rest_v10_projects_project_id_workflow_permanent_logs_get_serialize(
            procore_company_id=procore_company_id,
            project_id=project_id,
            filters_workflowed_object_type=filters_workflowed_object_type,
            filters_workflowed_object_id=filters_workflowed_object_id,
            page=page,
            per_page=per_page,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInner]",
            '400': "RestV10CompaniesCompanyIdWorkflowPermanentLogsGet400Response",
            '401': "RestV10CompaniesCompanyIdWorkflowPermanentLogsGet401Response",
            '403': "RestV10CompaniesCompanyIdWorkflowPermanentLogsGet401Response",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _rest_v10_projects_project_id_workflow_permanent_logs_get_serialize(
        self,
        procore_company_id,
        project_id,
        filters_workflowed_object_type,
        filters_workflowed_object_id,
        page,
        per_page,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if project_id is not None:
            _path_params['project_id'] = project_id
        # process the query parameters
        if page is not None:
            
            _query_params.append(('page', page))
            
        if per_page is not None:
            
            _query_params.append(('per_page', per_page))
            
        if filters_workflowed_object_type is not None:
            
            _query_params.append(('filters[workflowed_object_type]', filters_workflowed_object_type))
            
        if filters_workflowed_object_id is not None:
            
            _query_params.append(('filters[workflowed_object_id]', filters_workflowed_object_id))
            
        # process the header parameters
        if procore_company_id is not None:
            _header_params['Procore-Company-Id'] = procore_company_id
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/rest/v1.0/projects/{project_id}/workflow_permanent_logs',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


