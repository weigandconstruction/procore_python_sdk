# procore_sdk.CoreProjectProjectToolsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_tools_get**](CoreProjectProjectToolsApi.md#rest_v10_projects_project_id_tools_get) | **GET** /rest/v1.0/projects/{project_id}/tools | List project tools
[**rest_v10_projects_project_id_tools_patch**](CoreProjectProjectToolsApi.md#rest_v10_projects_project_id_tools_patch) | **PATCH** /rest/v1.0/projects/{project_id}/tools | Update project tools
[**rest_v10_tools_get**](CoreProjectProjectToolsApi.md#rest_v10_tools_get) | **GET** /rest/v1.0/tools | List project tools


# **rest_v10_projects_project_id_tools_get**
> List[RestV10ProjectsProjectIdToolsGet200ResponseInner] rest_v10_projects_project_id_tools_get(procore_company_id, project_id, filters_is_active=filters_is_active, for_mobile=for_mobile, include_configurable_generic_tools=include_configurable_generic_tools, page=page, per_page=per_page)

List project tools

Returns all Tools available to the provided Project.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_tools_get200_response_inner import RestV10ProjectsProjectIdToolsGet200ResponseInner
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
    api_instance = procore_sdk.CoreProjectProjectToolsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    filters_is_active = True # bool | Retrieve active or inactive tools. (optional)
    for_mobile = True # bool | Filters tools that Procore's iOS and Android apps support. (optional)
    include_configurable_generic_tools = True # bool | Includes configurable custom tools in the for_mobile view. (optional)
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List project tools
        api_response = api_instance.rest_v10_projects_project_id_tools_get(procore_company_id, project_id, filters_is_active=filters_is_active, for_mobile=for_mobile, include_configurable_generic_tools=include_configurable_generic_tools, page=page, per_page=per_page)
        print("The response of CoreProjectProjectToolsApi->rest_v10_projects_project_id_tools_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectProjectToolsApi->rest_v10_projects_project_id_tools_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **filters_is_active** | **bool**| Retrieve active or inactive tools. | [optional] 
 **for_mobile** | **bool**| Filters tools that Procore&#39;s iOS and Android apps support. | [optional] 
 **include_configurable_generic_tools** | **bool**| Includes configurable custom tools in the for_mobile view. | [optional] 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[RestV10ProjectsProjectIdToolsGet200ResponseInner]**](RestV10ProjectsProjectIdToolsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * Per-Page - Number of items retrieved per page <br>  * Total - Total number of items to be retrieved <br>  * Link - Link headers for the first, prev, next, and last link <br>  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_tools_patch**
> List[RestV10ProjectsProjectIdToolsGet200ResponseInner] rest_v10_projects_project_id_tools_patch(procore_company_id, project_id, rest_v10_projects_project_id_tools_patch_request=rest_v10_projects_project_id_tools_patch_request)

Update project tools

Updates the order and active status of Project Tools.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_tools_get200_response_inner import RestV10ProjectsProjectIdToolsGet200ResponseInner
from procore_sdk.models.rest_v10_projects_project_id_tools_patch_request import RestV10ProjectsProjectIdToolsPatchRequest
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
    api_instance = procore_sdk.CoreProjectProjectToolsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_projects_project_id_tools_patch_request = procore_sdk.RestV10ProjectsProjectIdToolsPatchRequest() # RestV10ProjectsProjectIdToolsPatchRequest |  (optional)

    try:
        # Update project tools
        api_response = api_instance.rest_v10_projects_project_id_tools_patch(procore_company_id, project_id, rest_v10_projects_project_id_tools_patch_request=rest_v10_projects_project_id_tools_patch_request)
        print("The response of CoreProjectProjectToolsApi->rest_v10_projects_project_id_tools_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectProjectToolsApi->rest_v10_projects_project_id_tools_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_projects_project_id_tools_patch_request** | [**RestV10ProjectsProjectIdToolsPatchRequest**](RestV10ProjectsProjectIdToolsPatchRequest.md)|  | [optional] 

### Return type

[**List[RestV10ProjectsProjectIdToolsGet200ResponseInner]**](RestV10ProjectsProjectIdToolsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_tools_get**
> List[RestV10ToolsGet200ResponseInner] rest_v10_tools_get(procore_company_id, project_id, page=page, per_page=per_page)

List project tools

Returns all Tools available to the provided Project.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_tools_get200_response_inner import RestV10ToolsGet200ResponseInner
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
    api_instance = procore_sdk.CoreProjectProjectToolsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List project tools
        api_response = api_instance.rest_v10_tools_get(procore_company_id, project_id, page=page, per_page=per_page)
        print("The response of CoreProjectProjectToolsApi->rest_v10_tools_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectProjectToolsApi->rest_v10_tools_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[RestV10ToolsGet200ResponseInner]**](RestV10ToolsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * Per-Page - Number of items retrieved per page <br>  * Total - Total number of items to be retrieved <br>  * Link - Link headers for the first, prev, next, and last link <br>  |
**404** | Not Found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

