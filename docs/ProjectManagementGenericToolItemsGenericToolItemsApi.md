# procore_sdk.ProjectManagementGenericToolItemsGenericToolItemsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_generic_tool_items_id_get**](ProjectManagementGenericToolItemsGenericToolItemsApi.md#rest_v10_generic_tool_items_id_get) | **GET** /rest/v1.0/generic_tool_items/{id} | Show Generic Tool Item


# **rest_v10_generic_tool_items_id_get**
> GenericToolItem rest_v10_generic_tool_items_id_get(procore_company_id, project_id, id)

Show Generic Tool Item

Get the details of a single Generic Tool Item

### Example


```python
import procore_sdk
from procore_sdk.models.generic_tool_item import GenericToolItem
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
    api_instance = procore_sdk.ProjectManagementGenericToolItemsGenericToolItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Generic Tool Item ID

    try:
        # Show Generic Tool Item
        api_response = api_instance.rest_v10_generic_tool_items_id_get(procore_company_id, project_id, id)
        print("The response of ProjectManagementGenericToolItemsGenericToolItemsApi->rest_v10_generic_tool_items_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementGenericToolItemsGenericToolItemsApi->rest_v10_generic_tool_items_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Generic Tool Item ID | 

### Return type

[**GenericToolItem**](GenericToolItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

