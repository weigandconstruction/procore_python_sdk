# procore_sdk.QualitySafetyInspectionsChecklistItemTypesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_checklist_item_types_get**](QualitySafetyInspectionsChecklistItemTypesApi.md#rest_v10_checklist_item_types_get) | **GET** /rest/v1.0/checklist/item_types | List Available Checklist Item Types
[**rest_v10_checklist_item_types_id_get**](QualitySafetyInspectionsChecklistItemTypesApi.md#rest_v10_checklist_item_types_id_get) | **GET** /rest/v1.0/checklist/item_types/{id} | Show Checklist Item Type


# **rest_v10_checklist_item_types_get**
> List[ChecklistItemType] rest_v10_checklist_item_types_get(procore_company_id, project_id, company_id, page=page, per_page=per_page)

List Available Checklist Item Types

Lists available Checklist Item Types  NOTE: Though both query parameters are marked as required below, only one of the two needs to be passed in (i.e., if you pass in a project_id then you do not need to also pass in a company_id, and vice versa).

### Example


```python
import procore_sdk
from procore_sdk.models.checklist_item_type import ChecklistItemType
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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistItemTypesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    company_id = 56 # int | Unique identifier for the company.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Available Checklist Item Types
        api_response = api_instance.rest_v10_checklist_item_types_get(procore_company_id, project_id, company_id, page=page, per_page=per_page)
        print("The response of QualitySafetyInspectionsChecklistItemTypesApi->rest_v10_checklist_item_types_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistItemTypesApi->rest_v10_checklist_item_types_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[ChecklistItemType]**](ChecklistItemType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Per-Page - Number of items retrieved per page <br>  * Total - Total number of items to be retrieved <br>  * Link - Link headers for the first, prev, next, and last link <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_checklist_item_types_id_get**
> ChecklistItemType rest_v10_checklist_item_types_id_get(procore_company_id, project_id, company_id, id)

Show Checklist Item Type

Retrieves specific Checklist Item Type  NOTE: Though both query parameters are marked as required below, only one of the two needs to be passed in (i.e., if you pass in a project_id then you do not need to also pass in a company_id, and vice versa).

### Example


```python
import procore_sdk
from procore_sdk.models.checklist_item_type import ChecklistItemType
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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistItemTypesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | Item Type ID

    try:
        # Show Checklist Item Type
        api_response = api_instance.rest_v10_checklist_item_types_id_get(procore_company_id, project_id, company_id, id)
        print("The response of QualitySafetyInspectionsChecklistItemTypesApi->rest_v10_checklist_item_types_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistItemTypesApi->rest_v10_checklist_item_types_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| Item Type ID | 

### Return type

[**ChecklistItemType**](ChecklistItemType.md)

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

