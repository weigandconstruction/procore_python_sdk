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
from typing import List
from typing_extensions import Annotated
from procore_sdk.models.checklist_alternative_response_set_full import ChecklistAlternativeResponseSetFull

from procore_sdk.api_client import ApiClient, RequestSerialized
from procore_sdk.api_response import ApiResponse
from procore_sdk.rest import RESTResponseType


class QualitySafetyInspectionsAlternativeResponseSetsApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def rest_v10_companies_company_id_checklist_alternative_response_sets_get(
        self,
        procore_company_id: Annotated[StrictInt, Field(description="Unique company identifier associated with the Procore User Account.")],
        company_id: Annotated[StrictInt, Field(description="Unique identifier for the company.")],
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
    ) -> List[ChecklistAlternativeResponseSetFull]:
        """List Alternative Response Sets

        Lists Alternative Response Sets for a specified Company.

        :param procore_company_id: Unique company identifier associated with the Procore User Account. (required)
        :type procore_company_id: int
        :param company_id: Unique identifier for the company. (required)
        :type company_id: int
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

        _param = self._rest_v10_companies_company_id_checklist_alternative_response_sets_get_serialize(
            procore_company_id=procore_company_id,
            company_id=company_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[ChecklistAlternativeResponseSetFull]",
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
    def rest_v10_companies_company_id_checklist_alternative_response_sets_get_with_http_info(
        self,
        procore_company_id: Annotated[StrictInt, Field(description="Unique company identifier associated with the Procore User Account.")],
        company_id: Annotated[StrictInt, Field(description="Unique identifier for the company.")],
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
    ) -> ApiResponse[List[ChecklistAlternativeResponseSetFull]]:
        """List Alternative Response Sets

        Lists Alternative Response Sets for a specified Company.

        :param procore_company_id: Unique company identifier associated with the Procore User Account. (required)
        :type procore_company_id: int
        :param company_id: Unique identifier for the company. (required)
        :type company_id: int
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

        _param = self._rest_v10_companies_company_id_checklist_alternative_response_sets_get_serialize(
            procore_company_id=procore_company_id,
            company_id=company_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[ChecklistAlternativeResponseSetFull]",
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
    def rest_v10_companies_company_id_checklist_alternative_response_sets_get_without_preload_content(
        self,
        procore_company_id: Annotated[StrictInt, Field(description="Unique company identifier associated with the Procore User Account.")],
        company_id: Annotated[StrictInt, Field(description="Unique identifier for the company.")],
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
        """List Alternative Response Sets

        Lists Alternative Response Sets for a specified Company.

        :param procore_company_id: Unique company identifier associated with the Procore User Account. (required)
        :type procore_company_id: int
        :param company_id: Unique identifier for the company. (required)
        :type company_id: int
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

        _param = self._rest_v10_companies_company_id_checklist_alternative_response_sets_get_serialize(
            procore_company_id=procore_company_id,
            company_id=company_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[ChecklistAlternativeResponseSetFull]",
            '401': "RestV10CompaniesCompanyIdWorkflowPermanentLogsGet401Response",
            '403': "RestV10CompaniesCompanyIdWorkflowPermanentLogsGet401Response",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _rest_v10_companies_company_id_checklist_alternative_response_sets_get_serialize(
        self,
        procore_company_id,
        company_id,
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
            resource_path='/rest/v1.0/companies/{company_id}/checklist/alternative_response_sets',
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
    def rest_v10_companies_company_id_checklist_alternative_response_sets_id_get(
        self,
        procore_company_id: Annotated[StrictInt, Field(description="Unique company identifier associated with the Procore User Account.")],
        id: Annotated[StrictInt, Field(description="Alternative Response Set ID")],
        company_id: Annotated[StrictInt, Field(description="Unique identifier for the company.")],
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
    ) -> ChecklistAlternativeResponseSetFull:
        """Show Alternative Response Set

        Returns a specified Alternative Response Set. The set includes alternative terms to represent conforming and deficient item responses, e.g. \"Safe\" instead of \"Pass\" for an item with an internal status of \"yes\". The global attribute indicates whether a response set has been provided by Procore.

        :param procore_company_id: Unique company identifier associated with the Procore User Account. (required)
        :type procore_company_id: int
        :param id: Alternative Response Set ID (required)
        :type id: int
        :param company_id: Unique identifier for the company. (required)
        :type company_id: int
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

        _param = self._rest_v10_companies_company_id_checklist_alternative_response_sets_id_get_serialize(
            procore_company_id=procore_company_id,
            id=id,
            company_id=company_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ChecklistAlternativeResponseSetFull",
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
    def rest_v10_companies_company_id_checklist_alternative_response_sets_id_get_with_http_info(
        self,
        procore_company_id: Annotated[StrictInt, Field(description="Unique company identifier associated with the Procore User Account.")],
        id: Annotated[StrictInt, Field(description="Alternative Response Set ID")],
        company_id: Annotated[StrictInt, Field(description="Unique identifier for the company.")],
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
    ) -> ApiResponse[ChecklistAlternativeResponseSetFull]:
        """Show Alternative Response Set

        Returns a specified Alternative Response Set. The set includes alternative terms to represent conforming and deficient item responses, e.g. \"Safe\" instead of \"Pass\" for an item with an internal status of \"yes\". The global attribute indicates whether a response set has been provided by Procore.

        :param procore_company_id: Unique company identifier associated with the Procore User Account. (required)
        :type procore_company_id: int
        :param id: Alternative Response Set ID (required)
        :type id: int
        :param company_id: Unique identifier for the company. (required)
        :type company_id: int
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

        _param = self._rest_v10_companies_company_id_checklist_alternative_response_sets_id_get_serialize(
            procore_company_id=procore_company_id,
            id=id,
            company_id=company_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ChecklistAlternativeResponseSetFull",
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
    def rest_v10_companies_company_id_checklist_alternative_response_sets_id_get_without_preload_content(
        self,
        procore_company_id: Annotated[StrictInt, Field(description="Unique company identifier associated with the Procore User Account.")],
        id: Annotated[StrictInt, Field(description="Alternative Response Set ID")],
        company_id: Annotated[StrictInt, Field(description="Unique identifier for the company.")],
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
        """Show Alternative Response Set

        Returns a specified Alternative Response Set. The set includes alternative terms to represent conforming and deficient item responses, e.g. \"Safe\" instead of \"Pass\" for an item with an internal status of \"yes\". The global attribute indicates whether a response set has been provided by Procore.

        :param procore_company_id: Unique company identifier associated with the Procore User Account. (required)
        :type procore_company_id: int
        :param id: Alternative Response Set ID (required)
        :type id: int
        :param company_id: Unique identifier for the company. (required)
        :type company_id: int
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

        _param = self._rest_v10_companies_company_id_checklist_alternative_response_sets_id_get_serialize(
            procore_company_id=procore_company_id,
            id=id,
            company_id=company_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ChecklistAlternativeResponseSetFull",
            '401': "RestV10CompaniesCompanyIdWorkflowPermanentLogsGet401Response",
            '403': "RestV10CompaniesCompanyIdWorkflowPermanentLogsGet401Response",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _rest_v10_companies_company_id_checklist_alternative_response_sets_id_get_serialize(
        self,
        procore_company_id,
        id,
        company_id,
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
        if id is not None:
            _path_params['id'] = id
        if company_id is not None:
            _path_params['company_id'] = company_id
        # process the query parameters
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
            resource_path='/rest/v1.0/companies/{company_id}/checklist/alternative_response_sets/{id}',
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


