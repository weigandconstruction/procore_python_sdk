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

from pydantic import Field, StrictBool, StrictInt
from typing import Optional
from typing_extensions import Annotated
from procore_sdk.models.body22 import Body22
from procore_sdk.models.rest_v10_requisitions_requisition_id_single_pdf_compilers_post200_response import RestV10RequisitionsRequisitionIdSinglePdfCompilersPost200Response

from procore_sdk.api_client import ApiClient, RequestSerialized
from procore_sdk.api_response import ApiResponse
from procore_sdk.rest import RESTResponseType


class ConstructionFinancialsCommitmentsRequisitionSubcontractorInvoiceSinglePDFCompilersApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def rest_v10_requisitions_requisition_id_single_pdf_compilers_post(
        self,
        procore_company_id: Annotated[StrictInt, Field(description="Unique company identifier associated with the Procore User Account.")],
        requisition_id: Annotated[StrictInt, Field(description="Requisition (Subcontractor Invoice) ID")],
        project_id: Annotated[StrictInt, Field(description="Unique identifier for the project.")],
        body22: Body22,
        polling: Annotated[Optional[StrictBool], Field(description="Determines if the PDF is emailed or a job URL is returned")] = None,
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
    ) -> RestV10RequisitionsRequisitionIdSinglePdfCompilersPost200Response:
        """Merges one or more PDFs of a requisition into a single PDF

        Merges one or more PDFs of a requisition into a single PDF. There are two ways to use this endpoint. First to generate a cover sheet for the requisition. If you would like to receive a polling URL that will follow the job provide the polling option in the query params `polling=true`. If you would like the file emailed to you omit the polling param in the query params. You can use the following request payload as an example  ````json {   \"files\":[     {\"type\": \"cover_sheet\", \"id\": \"\"}   ] } ```` If you would like to include some attachments, you can use the following request payload as an example  ````json {   \"files\": [     {       \"id\": \"\",       \"type\": \"cover_sheet\"     },     {       \"id\": 1234,       \"url\": \"http://example.com/file_1.pdf\",       \"type\": \"prostore_file\"     }   ] } ````

        :param procore_company_id: Unique company identifier associated with the Procore User Account. (required)
        :type procore_company_id: int
        :param requisition_id: Requisition (Subcontractor Invoice) ID (required)
        :type requisition_id: int
        :param project_id: Unique identifier for the project. (required)
        :type project_id: int
        :param body22: (required)
        :type body22: Body22
        :param polling: Determines if the PDF is emailed or a job URL is returned
        :type polling: bool
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

        _param = self._rest_v10_requisitions_requisition_id_single_pdf_compilers_post_serialize(
            procore_company_id=procore_company_id,
            requisition_id=requisition_id,
            project_id=project_id,
            body22=body22,
            polling=polling,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "RestV10RequisitionsRequisitionIdSinglePdfCompilersPost200Response",
            '400': "RestV10CompaniesCompanyIdWorkflowPermanentLogsGet401Response",
            '401': "RestV10CompaniesCompanyIdWorkflowPermanentLogsGet401Response",
            '403': "RestV10CompaniesCompanyIdWorkflowPermanentLogsGet401Response",
            '404': "RestV10WorkOrderContractsWorkOrderContractIdSubcontractorScheduleOfValuesStatusPatch404Response",
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
    def rest_v10_requisitions_requisition_id_single_pdf_compilers_post_with_http_info(
        self,
        procore_company_id: Annotated[StrictInt, Field(description="Unique company identifier associated with the Procore User Account.")],
        requisition_id: Annotated[StrictInt, Field(description="Requisition (Subcontractor Invoice) ID")],
        project_id: Annotated[StrictInt, Field(description="Unique identifier for the project.")],
        body22: Body22,
        polling: Annotated[Optional[StrictBool], Field(description="Determines if the PDF is emailed or a job URL is returned")] = None,
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
    ) -> ApiResponse[RestV10RequisitionsRequisitionIdSinglePdfCompilersPost200Response]:
        """Merges one or more PDFs of a requisition into a single PDF

        Merges one or more PDFs of a requisition into a single PDF. There are two ways to use this endpoint. First to generate a cover sheet for the requisition. If you would like to receive a polling URL that will follow the job provide the polling option in the query params `polling=true`. If you would like the file emailed to you omit the polling param in the query params. You can use the following request payload as an example  ````json {   \"files\":[     {\"type\": \"cover_sheet\", \"id\": \"\"}   ] } ```` If you would like to include some attachments, you can use the following request payload as an example  ````json {   \"files\": [     {       \"id\": \"\",       \"type\": \"cover_sheet\"     },     {       \"id\": 1234,       \"url\": \"http://example.com/file_1.pdf\",       \"type\": \"prostore_file\"     }   ] } ````

        :param procore_company_id: Unique company identifier associated with the Procore User Account. (required)
        :type procore_company_id: int
        :param requisition_id: Requisition (Subcontractor Invoice) ID (required)
        :type requisition_id: int
        :param project_id: Unique identifier for the project. (required)
        :type project_id: int
        :param body22: (required)
        :type body22: Body22
        :param polling: Determines if the PDF is emailed or a job URL is returned
        :type polling: bool
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

        _param = self._rest_v10_requisitions_requisition_id_single_pdf_compilers_post_serialize(
            procore_company_id=procore_company_id,
            requisition_id=requisition_id,
            project_id=project_id,
            body22=body22,
            polling=polling,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "RestV10RequisitionsRequisitionIdSinglePdfCompilersPost200Response",
            '400': "RestV10CompaniesCompanyIdWorkflowPermanentLogsGet401Response",
            '401': "RestV10CompaniesCompanyIdWorkflowPermanentLogsGet401Response",
            '403': "RestV10CompaniesCompanyIdWorkflowPermanentLogsGet401Response",
            '404': "RestV10WorkOrderContractsWorkOrderContractIdSubcontractorScheduleOfValuesStatusPatch404Response",
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
    def rest_v10_requisitions_requisition_id_single_pdf_compilers_post_without_preload_content(
        self,
        procore_company_id: Annotated[StrictInt, Field(description="Unique company identifier associated with the Procore User Account.")],
        requisition_id: Annotated[StrictInt, Field(description="Requisition (Subcontractor Invoice) ID")],
        project_id: Annotated[StrictInt, Field(description="Unique identifier for the project.")],
        body22: Body22,
        polling: Annotated[Optional[StrictBool], Field(description="Determines if the PDF is emailed or a job URL is returned")] = None,
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
        """Merges one or more PDFs of a requisition into a single PDF

        Merges one or more PDFs of a requisition into a single PDF. There are two ways to use this endpoint. First to generate a cover sheet for the requisition. If you would like to receive a polling URL that will follow the job provide the polling option in the query params `polling=true`. If you would like the file emailed to you omit the polling param in the query params. You can use the following request payload as an example  ````json {   \"files\":[     {\"type\": \"cover_sheet\", \"id\": \"\"}   ] } ```` If you would like to include some attachments, you can use the following request payload as an example  ````json {   \"files\": [     {       \"id\": \"\",       \"type\": \"cover_sheet\"     },     {       \"id\": 1234,       \"url\": \"http://example.com/file_1.pdf\",       \"type\": \"prostore_file\"     }   ] } ````

        :param procore_company_id: Unique company identifier associated with the Procore User Account. (required)
        :type procore_company_id: int
        :param requisition_id: Requisition (Subcontractor Invoice) ID (required)
        :type requisition_id: int
        :param project_id: Unique identifier for the project. (required)
        :type project_id: int
        :param body22: (required)
        :type body22: Body22
        :param polling: Determines if the PDF is emailed or a job URL is returned
        :type polling: bool
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

        _param = self._rest_v10_requisitions_requisition_id_single_pdf_compilers_post_serialize(
            procore_company_id=procore_company_id,
            requisition_id=requisition_id,
            project_id=project_id,
            body22=body22,
            polling=polling,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "RestV10RequisitionsRequisitionIdSinglePdfCompilersPost200Response",
            '400': "RestV10CompaniesCompanyIdWorkflowPermanentLogsGet401Response",
            '401': "RestV10CompaniesCompanyIdWorkflowPermanentLogsGet401Response",
            '403': "RestV10CompaniesCompanyIdWorkflowPermanentLogsGet401Response",
            '404': "RestV10WorkOrderContractsWorkOrderContractIdSubcontractorScheduleOfValuesStatusPatch404Response",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _rest_v10_requisitions_requisition_id_single_pdf_compilers_post_serialize(
        self,
        procore_company_id,
        requisition_id,
        project_id,
        body22,
        polling,
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
        if requisition_id is not None:
            _path_params['requisition_id'] = requisition_id
        # process the query parameters
        if polling is not None:
            
            _query_params.append(('polling', polling))
            
        if project_id is not None:
            
            _query_params.append(('project_id', project_id))
            
        # process the header parameters
        if procore_company_id is not None:
            _header_params['Procore-Company-Id'] = procore_company_id
        # process the form parameters
        # process the body parameter
        if body22 is not None:
            _body_params = body22


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
            method='POST',
            resource_path='/rest/v1.0/requisitions/{requisition_id}/single_pdf_compilers',
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


