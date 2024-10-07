# procore_sdk.ConstructionFinancialsCommitmentsRequisitionSubcontractorInvoiceSinglePDFCompilersApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_requisitions_requisition_id_single_pdf_compilers_post**](ConstructionFinancialsCommitmentsRequisitionSubcontractorInvoiceSinglePDFCompilersApi.md#rest_v10_requisitions_requisition_id_single_pdf_compilers_post) | **POST** /rest/v1.0/requisitions/{requisition_id}/single_pdf_compilers | Merges one or more PDFs of a requisition into a single PDF


# **rest_v10_requisitions_requisition_id_single_pdf_compilers_post**
> RestV10RequisitionsRequisitionIdSinglePdfCompilersPost200Response rest_v10_requisitions_requisition_id_single_pdf_compilers_post(procore_company_id, requisition_id, project_id, body22, polling=polling)

Merges one or more PDFs of a requisition into a single PDF

Merges one or more PDFs of a requisition into a single PDF. There are two ways to use this endpoint. First to generate a cover sheet for the requisition. If you would like to receive a polling URL that will follow the job provide the polling option in the query params `polling=true`. If you would like the file emailed to you omit the polling param in the query params. You can use the following request payload as an example  ````json {   \"files\":[     {\"type\": \"cover_sheet\", \"id\": \"\"}   ] } ```` If you would like to include some attachments, you can use the following request payload as an example  ````json {   \"files\": [     {       \"id\": \"\",       \"type\": \"cover_sheet\"     },     {       \"id\": 1234,       \"url\": \"http://example.com/file_1.pdf\",       \"type\": \"prostore_file\"     }   ] } ````

### Example


```python
import procore_sdk
from procore_sdk.models.body22 import Body22
from procore_sdk.models.rest_v10_requisitions_requisition_id_single_pdf_compilers_post200_response import RestV10RequisitionsRequisitionIdSinglePdfCompilersPost200Response
from procore_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.procore.com
# See configuration.py for a list of all supported configuration parameters.
configuration = procore_sdk.Configuration(
    host = "https://api.procore.com"
)


# Enter a context with an instance of the API client
with procore_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = procore_sdk.ConstructionFinancialsCommitmentsRequisitionSubcontractorInvoiceSinglePDFCompilersApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    requisition_id = 56 # int | Requisition (Subcontractor Invoice) ID
    project_id = 56 # int | Unique identifier for the project.
    body22 = procore_sdk.Body22() # Body22 | 
    polling = True # bool | Determines if the PDF is emailed or a job URL is returned (optional)

    try:
        # Merges one or more PDFs of a requisition into a single PDF
        api_response = api_instance.rest_v10_requisitions_requisition_id_single_pdf_compilers_post(procore_company_id, requisition_id, project_id, body22, polling=polling)
        print("The response of ConstructionFinancialsCommitmentsRequisitionSubcontractorInvoiceSinglePDFCompilersApi->rest_v10_requisitions_requisition_id_single_pdf_compilers_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsCommitmentsRequisitionSubcontractorInvoiceSinglePDFCompilersApi->rest_v10_requisitions_requisition_id_single_pdf_compilers_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **requisition_id** | **int**| Requisition (Subcontractor Invoice) ID | 
 **project_id** | **int**| Unique identifier for the project. | 
 **body22** | [**Body22**](Body22.md)|  | 
 **polling** | **bool**| Determines if the PDF is emailed or a job URL is returned | [optional] 

### Return type

[**RestV10RequisitionsRequisitionIdSinglePdfCompilersPost200Response**](RestV10RequisitionsRequisitionIdSinglePdfCompilersPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

