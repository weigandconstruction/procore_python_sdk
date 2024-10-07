# procore_sdk.CoreOpenItemsOpenItemsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_open_items_all_get**](CoreOpenItemsOpenItemsApi.md#rest_v10_open_items_all_get) | **GET** /rest/v1.0/open_items/all | Get Open Items Statistics
[**rest_v10_open_items_mine_get**](CoreOpenItemsOpenItemsApi.md#rest_v10_open_items_mine_get) | **GET** /rest/v1.0/open_items/mine | Get Open Items Statistics


# **rest_v10_open_items_all_get**
> RestV10OpenItemsAllGet200Response rest_v10_open_items_all_get(procore_company_id, project_id, tool_name=tool_name)

Get Open Items Statistics

Return open items statistics for a project (all users)

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_open_items_all_get200_response import RestV10OpenItemsAllGet200Response
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
    api_instance = procore_sdk.CoreOpenItemsOpenItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    tool_name = 'tool_name_example' # str |  (optional)

    try:
        # Get Open Items Statistics
        api_response = api_instance.rest_v10_open_items_all_get(procore_company_id, project_id, tool_name=tool_name)
        print("The response of CoreOpenItemsOpenItemsApi->rest_v10_open_items_all_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreOpenItemsOpenItemsApi->rest_v10_open_items_all_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **tool_name** | **str**|  | [optional] 

### Return type

[**RestV10OpenItemsAllGet200Response**](RestV10OpenItemsAllGet200Response.md)

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_open_items_mine_get**
> RestV10OpenItemsAllGet200Response rest_v10_open_items_mine_get(procore_company_id, project_id, tool_name=tool_name)

Get Open Items Statistics

Return open items statistics for a project (current user)

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_open_items_all_get200_response import RestV10OpenItemsAllGet200Response
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
    api_instance = procore_sdk.CoreOpenItemsOpenItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    tool_name = 'tool_name_example' # str |  (optional)

    try:
        # Get Open Items Statistics
        api_response = api_instance.rest_v10_open_items_mine_get(procore_company_id, project_id, tool_name=tool_name)
        print("The response of CoreOpenItemsOpenItemsApi->rest_v10_open_items_mine_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreOpenItemsOpenItemsApi->rest_v10_open_items_mine_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **tool_name** | **str**|  | [optional] 

### Return type

[**RestV10OpenItemsAllGet200Response**](RestV10OpenItemsAllGet200Response.md)

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

