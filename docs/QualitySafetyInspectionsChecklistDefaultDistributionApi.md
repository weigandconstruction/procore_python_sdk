# procore_sdk.QualitySafetyInspectionsChecklistDefaultDistributionApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_checklist_default_distribution_get**](QualitySafetyInspectionsChecklistDefaultDistributionApi.md#rest_v10_checklist_default_distribution_get) | **GET** /rest/v1.0/checklist/default_distribution | List Default Distribution Members


# **rest_v10_checklist_default_distribution_get**
> List[RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy] rest_v10_checklist_default_distribution_get(procore_company_id, project_id, page=page, per_page=per_page, vendor_id=vendor_id)

List Default Distribution Members

Returns a collection of Users that are on the Inspections Default Distribution list. x-deprecated-at: 1644250224 deprecated: true

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_work_logs_get200_response_inner_created_by import RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy
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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistDefaultDistributionApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    vendor_id = 56 # int | Vendor ID (optional)

    try:
        # List Default Distribution Members
        api_response = api_instance.rest_v10_checklist_default_distribution_get(procore_company_id, project_id, page=page, per_page=per_page, vendor_id=vendor_id)
        print("The response of QualitySafetyInspectionsChecklistDefaultDistributionApi->rest_v10_checklist_default_distribution_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistDefaultDistributionApi->rest_v10_checklist_default_distribution_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **vendor_id** | **int**| Vendor ID | [optional] 

### Return type

[**List[RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy]**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

