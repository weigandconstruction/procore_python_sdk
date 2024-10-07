# procore_sdk.ProjectManagementModelsBIMViewpointsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_bim_viewpoints_id_get**](ProjectManagementModelsBIMViewpointsApi.md#rest_v10_bim_viewpoints_id_get) | **GET** /rest/v1.0/bim_viewpoints/{id} | Show BIM Viewpoint
[**rest_v10_bim_viewpoints_post**](ProjectManagementModelsBIMViewpointsApi.md#rest_v10_bim_viewpoints_post) | **POST** /rest/v1.0/bim_viewpoints | Create a BIM Viewpoint


# **rest_v10_bim_viewpoints_id_get**
> RestV10BimViewpointsPost201Response rest_v10_bim_viewpoints_id_get(procore_company_id, id, project_id)

Show BIM Viewpoint

Return a single BIM Viewpoint

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_bim_viewpoints_post201_response import RestV10BimViewpointsPost201Response
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
    api_instance = procore_sdk.ProjectManagementModelsBIMViewpointsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Show BIM Viewpoint
        api_response = api_instance.rest_v10_bim_viewpoints_id_get(procore_company_id, id, project_id)
        print("The response of ProjectManagementModelsBIMViewpointsApi->rest_v10_bim_viewpoints_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementModelsBIMViewpointsApi->rest_v10_bim_viewpoints_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**RestV10BimViewpointsPost201Response**](RestV10BimViewpointsPost201Response.md)

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
**404** | Not Found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_bim_viewpoints_post**
> RestV10BimViewpointsPost201Response rest_v10_bim_viewpoints_post(procore_company_id, body121)

Create a BIM Viewpoint

Create a BIM Viewpoint

### Example


```python
import procore_sdk
from procore_sdk.models.body121 import Body121
from procore_sdk.models.rest_v10_bim_viewpoints_post201_response import RestV10BimViewpointsPost201Response
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
    api_instance = procore_sdk.ProjectManagementModelsBIMViewpointsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    body121 = procore_sdk.Body121() # Body121 | 

    try:
        # Create a BIM Viewpoint
        api_response = api_instance.rest_v10_bim_viewpoints_post(procore_company_id, body121)
        print("The response of ProjectManagementModelsBIMViewpointsApi->rest_v10_bim_viewpoints_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementModelsBIMViewpointsApi->rest_v10_bim_viewpoints_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **body121** | [**Body121**](Body121.md)|  | 

### Return type

[**RestV10BimViewpointsPost201Response**](RestV10BimViewpointsPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

