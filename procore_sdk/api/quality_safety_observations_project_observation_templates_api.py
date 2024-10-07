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

from pydantic import Field, StrictInt
from typing import List, Optional
from typing_extensions import Annotated
from procore_sdk.models.project_observation_template1 import ProjectObservationTemplate1
from procore_sdk.models.rest_v10_projects_project_id_observation_templates_bulk_update_patch_request import RestV10ProjectsProjectIdObservationTemplatesBulkUpdatePatchRequest

from procore_sdk.api_client import ApiClient, RequestSerialized
from procore_sdk.api_response import ApiResponse
from procore_sdk.rest import RESTResponseType


class QualitySafetyObservationsProjectObservationTemplatesApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def rest_v10_projects_project_id_observation_templates_bulk_update_patch(
        self,
        procore_company_id: Annotated[StrictInt, Field(description="Unique company identifier associated with the Procore User Account.")],
        project_id: Annotated[StrictInt, Field(description="Unique identifier for the project.")],
        rest_v10_projects_project_id_observation_templates_bulk_update_patch_request: RestV10ProjectsProjectIdObservationTemplatesBulkUpdatePatchRequest,
        observation_template_ids: Annotated[Optional[List[StrictInt]], Field(description="IDs of all Project Observation Templates specified for bulk update")] = None,
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
    ) -> List[ProjectObservationTemplate1]:
        """Bulk Update Project Observation Templates

        Updates multiple Project Observation Templates

        :param procore_company_id: Unique company identifier associated with the Procore User Account. (required)
        :type procore_company_id: int
        :param project_id: Unique identifier for the project. (required)
        :type project_id: int
        :param rest_v10_projects_project_id_observation_templates_bulk_update_patch_request: (required)
        :type rest_v10_projects_project_id_observation_templates_bulk_update_patch_request: RestV10ProjectsProjectIdObservationTemplatesBulkUpdatePatchRequest
        :param observation_template_ids: IDs of all Project Observation Templates specified for bulk update
        :type observation_template_ids: List[int]
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

        _param = self._rest_v10_projects_project_id_observation_templates_bulk_update_patch_serialize(
            procore_company_id=procore_company_id,
            project_id=project_id,
            rest_v10_projects_project_id_observation_templates_bulk_update_patch_request=rest_v10_projects_project_id_observation_templates_bulk_update_patch_request,
            observation_template_ids=observation_template_ids,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[ProjectObservationTemplate1]",
            '400': "RestV10CompaniesCompanyIdWorkflowPermanentLogsGet401Response",
            '401': "RestV10CompaniesCompanyIdWorkflowPermanentLogsGet401Response",
            '403': "RestV10CompaniesCompanyIdWorkflowPermanentLogsGet401Response",
            '404': "RestV10CompaniesCompanyIdWorkflowPermanentLogsGet401Response",
            '422': "RestV10CompaniesCompanyIdWorkflowPermanentLogsGet401Response",
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
    def rest_v10_projects_project_id_observation_templates_bulk_update_patch_with_http_info(
        self,
        procore_company_id: Annotated[StrictInt, Field(description="Unique company identifier associated with the Procore User Account.")],
        project_id: Annotated[StrictInt, Field(description="Unique identifier for the project.")],
        rest_v10_projects_project_id_observation_templates_bulk_update_patch_request: RestV10ProjectsProjectIdObservationTemplatesBulkUpdatePatchRequest,
        observation_template_ids: Annotated[Optional[List[StrictInt]], Field(description="IDs of all Project Observation Templates specified for bulk update")] = None,
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
    ) -> ApiResponse[List[ProjectObservationTemplate1]]:
        """Bulk Update Project Observation Templates

        Updates multiple Project Observation Templates

        :param procore_company_id: Unique company identifier associated with the Procore User Account. (required)
        :type procore_company_id: int
        :param project_id: Unique identifier for the project. (required)
        :type project_id: int
        :param rest_v10_projects_project_id_observation_templates_bulk_update_patch_request: (required)
        :type rest_v10_projects_project_id_observation_templates_bulk_update_patch_request: RestV10ProjectsProjectIdObservationTemplatesBulkUpdatePatchRequest
        :param observation_template_ids: IDs of all Project Observation Templates specified for bulk update
        :type observation_template_ids: List[int]
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

        _param = self._rest_v10_projects_project_id_observation_templates_bulk_update_patch_serialize(
            procore_company_id=procore_company_id,
            project_id=project_id,
            rest_v10_projects_project_id_observation_templates_bulk_update_patch_request=rest_v10_projects_project_id_observation_templates_bulk_update_patch_request,
            observation_template_ids=observation_template_ids,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[ProjectObservationTemplate1]",
            '400': "RestV10CompaniesCompanyIdWorkflowPermanentLogsGet401Response",
            '401': "RestV10CompaniesCompanyIdWorkflowPermanentLogsGet401Response",
            '403': "RestV10CompaniesCompanyIdWorkflowPermanentLogsGet401Response",
            '404': "RestV10CompaniesCompanyIdWorkflowPermanentLogsGet401Response",
            '422': "RestV10CompaniesCompanyIdWorkflowPermanentLogsGet401Response",
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
    def rest_v10_projects_project_id_observation_templates_bulk_update_patch_without_preload_content(
        self,
        procore_company_id: Annotated[StrictInt, Field(description="Unique company identifier associated with the Procore User Account.")],
        project_id: Annotated[StrictInt, Field(description="Unique identifier for the project.")],
        rest_v10_projects_project_id_observation_templates_bulk_update_patch_request: RestV10ProjectsProjectIdObservationTemplatesBulkUpdatePatchRequest,
        observation_template_ids: Annotated[Optional[List[StrictInt]], Field(description="IDs of all Project Observation Templates specified for bulk update")] = None,
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
        """Bulk Update Project Observation Templates

        Updates multiple Project Observation Templates

        :param procore_company_id: Unique company identifier associated with the Procore User Account. (required)
        :type procore_company_id: int
        :param project_id: Unique identifier for the project. (required)
        :type project_id: int
        :param rest_v10_projects_project_id_observation_templates_bulk_update_patch_request: (required)
        :type rest_v10_projects_project_id_observation_templates_bulk_update_patch_request: RestV10ProjectsProjectIdObservationTemplatesBulkUpdatePatchRequest
        :param observation_template_ids: IDs of all Project Observation Templates specified for bulk update
        :type observation_template_ids: List[int]
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

        _param = self._rest_v10_projects_project_id_observation_templates_bulk_update_patch_serialize(
            procore_company_id=procore_company_id,
            project_id=project_id,
            rest_v10_projects_project_id_observation_templates_bulk_update_patch_request=rest_v10_projects_project_id_observation_templates_bulk_update_patch_request,
            observation_template_ids=observation_template_ids,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[ProjectObservationTemplate1]",
            '400': "RestV10CompaniesCompanyIdWorkflowPermanentLogsGet401Response",
            '401': "RestV10CompaniesCompanyIdWorkflowPermanentLogsGet401Response",
            '403': "RestV10CompaniesCompanyIdWorkflowPermanentLogsGet401Response",
            '404': "RestV10CompaniesCompanyIdWorkflowPermanentLogsGet401Response",
            '422': "RestV10CompaniesCompanyIdWorkflowPermanentLogsGet401Response",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _rest_v10_projects_project_id_observation_templates_bulk_update_patch_serialize(
        self,
        procore_company_id,
        project_id,
        rest_v10_projects_project_id_observation_templates_bulk_update_patch_request,
        observation_template_ids,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
            'observation_template_ids': 'csv',
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
        if observation_template_ids is not None:
            
            _query_params.append(('observation_template_ids', observation_template_ids))
            
        # process the header parameters
        if procore_company_id is not None:
            _header_params['Procore-Company-Id'] = procore_company_id
        # process the form parameters
        # process the body parameter
        if rest_v10_projects_project_id_observation_templates_bulk_update_patch_request is not None:
            _body_params = rest_v10_projects_project_id_observation_templates_bulk_update_patch_request


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
        ]

        return self.api_client.param_serialize(
            method='PATCH',
            resource_path='/rest/v1.0/projects/{project_id}/observation_templates/bulk_update',
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


