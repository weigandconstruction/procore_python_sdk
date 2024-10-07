# procore_sdk.QualityAndSafetyInspectionsInspectionItemSignaturesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_signature_requests_id_signature_delete**](QualityAndSafetyInspectionsInspectionItemSignaturesApi.md#rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_signature_requests_id_signature_delete) | **DELETE** /rest/v2.0/companies/{company_id}/projects/{project_id}/inspection_items/{item_id}/signature_requests/{id}/signature | Deletes an Inspection Item Signature
[**rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_signature_requests_id_signature_post**](QualityAndSafetyInspectionsInspectionItemSignaturesApi.md#rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_signature_requests_id_signature_post) | **POST** /rest/v2.0/companies/{company_id}/projects/{project_id}/inspection_items/{item_id}/signature_requests/{id}/signature | Creates a Inspection Item Signature Request


# **rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_signature_requests_id_signature_delete**
> rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_signature_requests_id_signature_delete(procore_company_id, company_id, project_id, item_id, id)

Deletes an Inspection Item Signature

Deletes an Inspection Item Signature for a specified Inspection Item Signature Request.

### Example


```python
import procore_sdk
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
    api_instance = procore_sdk.QualityAndSafetyInspectionsInspectionItemSignaturesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 'company_id_example' # str | Unique identifier for the company.
    project_id = 'project_id_example' # str | Unique identifier for the project.
    item_id = 'item_id_example' # str | Unique identifier for the inspection item.
    id = 'id_example' # str | Unique identifier for the inspection item signature request.

    try:
        # Deletes an Inspection Item Signature
        api_instance.rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_signature_requests_id_signature_delete(procore_company_id, company_id, project_id, item_id, id)
    except Exception as e:
        print("Exception when calling QualityAndSafetyInspectionsInspectionItemSignaturesApi->rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_signature_requests_id_signature_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **str**| Unique identifier for the company. | 
 **project_id** | **str**| Unique identifier for the project. | 
 **item_id** | **str**| Unique identifier for the inspection item. | 
 **id** | **str**| Unique identifier for the inspection item signature request. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_signature_requests_id_signature_post**
> RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsIdSignaturePost201Response rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_signature_requests_id_signature_post(procore_company_id, company_id, project_id, item_id, id, rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_signature_requests_id_signature_post_request=rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_signature_requests_id_signature_post_request)

Creates a Inspection Item Signature Request

Creates a Inspection Item Signature Request for a specified Inspection.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_signature_requests_id_signature_post201_response import RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsIdSignaturePost201Response
from procore_sdk.models.rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_signature_requests_id_signature_post_request import RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsIdSignaturePostRequest
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
    api_instance = procore_sdk.QualityAndSafetyInspectionsInspectionItemSignaturesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 'company_id_example' # str | Unique identifier for the company.
    project_id = 'project_id_example' # str | Unique identifier for the project.
    item_id = 'item_id_example' # str | Unique identifier for the inspection item.
    id = 'id_example' # str | Unique identifier for the inspection item signature request.
    rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_signature_requests_id_signature_post_request = procore_sdk.RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsIdSignaturePostRequest() # RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsIdSignaturePostRequest |  (optional)

    try:
        # Creates a Inspection Item Signature Request
        api_response = api_instance.rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_signature_requests_id_signature_post(procore_company_id, company_id, project_id, item_id, id, rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_signature_requests_id_signature_post_request=rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_signature_requests_id_signature_post_request)
        print("The response of QualityAndSafetyInspectionsInspectionItemSignaturesApi->rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_signature_requests_id_signature_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualityAndSafetyInspectionsInspectionItemSignaturesApi->rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_signature_requests_id_signature_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **str**| Unique identifier for the company. | 
 **project_id** | **str**| Unique identifier for the project. | 
 **item_id** | **str**| Unique identifier for the inspection item. | 
 **id** | **str**| Unique identifier for the inspection item signature request. | 
 **rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_signature_requests_id_signature_post_request** | [**RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsIdSignaturePostRequest**](RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsIdSignaturePostRequest.md)|  | [optional] 

### Return type

[**RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsIdSignaturePost201Response**](RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsIdSignaturePost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

