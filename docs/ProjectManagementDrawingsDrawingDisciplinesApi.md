# procore_sdk.ProjectManagementDrawingsDrawingDisciplinesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_drawing_disciplines_get**](ProjectManagementDrawingsDrawingDisciplinesApi.md#rest_v10_projects_project_id_drawing_disciplines_get) | **GET** /rest/v1.0/projects/{project_id}/drawing_disciplines | List Drawing Disciplines
[**rest_v10_projects_project_id_drawing_disciplines_id_patch**](ProjectManagementDrawingsDrawingDisciplinesApi.md#rest_v10_projects_project_id_drawing_disciplines_id_patch) | **PATCH** /rest/v1.0/projects/{project_id}/drawing_disciplines/{id} | Update drawing discipline
[**rest_v10_projects_project_id_drawing_disciplines_id_put**](ProjectManagementDrawingsDrawingDisciplinesApi.md#rest_v10_projects_project_id_drawing_disciplines_id_put) | **PUT** /rest/v1.0/projects/{project_id}/drawing_disciplines/{id} | Update drawing discipline
[**rest_v11_projects_project_id_drawing_disciplines_get**](ProjectManagementDrawingsDrawingDisciplinesApi.md#rest_v11_projects_project_id_drawing_disciplines_get) | **GET** /rest/v1.1/projects/{project_id}/drawing_disciplines | List Drawing Disciplines
[**rest_v11_projects_project_id_drawing_disciplines_id_patch**](ProjectManagementDrawingsDrawingDisciplinesApi.md#rest_v11_projects_project_id_drawing_disciplines_id_patch) | **PATCH** /rest/v1.1/projects/{project_id}/drawing_disciplines/{id} | Update drawing discipline


# **rest_v10_projects_project_id_drawing_disciplines_get**
> List[RestV11ProjectsProjectIdDrawingDisciplinesGet200ResponseInner] rest_v10_projects_project_id_drawing_disciplines_get(procore_company_id, project_id)

List Drawing Disciplines

List of Drawing Disciplines

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v11_projects_project_id_drawing_disciplines_get200_response_inner import RestV11ProjectsProjectIdDrawingDisciplinesGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementDrawingsDrawingDisciplinesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.

    try:
        # List Drawing Disciplines
        api_response = api_instance.rest_v10_projects_project_id_drawing_disciplines_get(procore_company_id, project_id)
        print("The response of ProjectManagementDrawingsDrawingDisciplinesApi->rest_v10_projects_project_id_drawing_disciplines_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementDrawingsDrawingDisciplinesApi->rest_v10_projects_project_id_drawing_disciplines_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**List[RestV11ProjectsProjectIdDrawingDisciplinesGet200ResponseInner]**](RestV11ProjectsProjectIdDrawingDisciplinesGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_drawing_disciplines_id_patch**
> RestV11ProjectsProjectIdDrawingDisciplinesIdPatch200Response rest_v10_projects_project_id_drawing_disciplines_id_patch(procore_company_id, project_id, id, rest_v11_projects_project_id_drawing_disciplines_id_patch_request=rest_v11_projects_project_id_drawing_disciplines_id_patch_request)

Update drawing discipline

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v11_projects_project_id_drawing_disciplines_id_patch200_response import RestV11ProjectsProjectIdDrawingDisciplinesIdPatch200Response
from procore_sdk.models.rest_v11_projects_project_id_drawing_disciplines_id_patch_request import RestV11ProjectsProjectIdDrawingDisciplinesIdPatchRequest
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
    api_instance = procore_sdk.ProjectManagementDrawingsDrawingDisciplinesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | ID of the discipline to update
    rest_v11_projects_project_id_drawing_disciplines_id_patch_request = procore_sdk.RestV11ProjectsProjectIdDrawingDisciplinesIdPatchRequest() # RestV11ProjectsProjectIdDrawingDisciplinesIdPatchRequest |  (optional)

    try:
        # Update drawing discipline
        api_response = api_instance.rest_v10_projects_project_id_drawing_disciplines_id_patch(procore_company_id, project_id, id, rest_v11_projects_project_id_drawing_disciplines_id_patch_request=rest_v11_projects_project_id_drawing_disciplines_id_patch_request)
        print("The response of ProjectManagementDrawingsDrawingDisciplinesApi->rest_v10_projects_project_id_drawing_disciplines_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementDrawingsDrawingDisciplinesApi->rest_v10_projects_project_id_drawing_disciplines_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| ID of the discipline to update | 
 **rest_v11_projects_project_id_drawing_disciplines_id_patch_request** | [**RestV11ProjectsProjectIdDrawingDisciplinesIdPatchRequest**](RestV11ProjectsProjectIdDrawingDisciplinesIdPatchRequest.md)|  | [optional] 

### Return type

[**RestV11ProjectsProjectIdDrawingDisciplinesIdPatch200Response**](RestV11ProjectsProjectIdDrawingDisciplinesIdPatch200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_drawing_disciplines_id_put**
> RestV10ProjectsProjectIdDrawingDisciplinesIdPut200Response rest_v10_projects_project_id_drawing_disciplines_id_put(procore_company_id, project_id, id, name)

Update drawing discipline

This is a deprecated endpoint.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_drawing_disciplines_id_put200_response import RestV10ProjectsProjectIdDrawingDisciplinesIdPut200Response
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
    api_instance = procore_sdk.ProjectManagementDrawingsDrawingDisciplinesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | ID of the discipline to update
    name = 'name_example' # str | New name for the Drawing Discipline

    try:
        # Update drawing discipline
        api_response = api_instance.rest_v10_projects_project_id_drawing_disciplines_id_put(procore_company_id, project_id, id, name)
        print("The response of ProjectManagementDrawingsDrawingDisciplinesApi->rest_v10_projects_project_id_drawing_disciplines_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementDrawingsDrawingDisciplinesApi->rest_v10_projects_project_id_drawing_disciplines_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| ID of the discipline to update | 
 **name** | **str**| New name for the Drawing Discipline | 

### Return type

[**RestV10ProjectsProjectIdDrawingDisciplinesIdPut200Response**](RestV10ProjectsProjectIdDrawingDisciplinesIdPut200Response.md)

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

# **rest_v11_projects_project_id_drawing_disciplines_get**
> List[RestV11ProjectsProjectIdDrawingDisciplinesGet200ResponseInner] rest_v11_projects_project_id_drawing_disciplines_get(procore_company_id, project_id, filters_id=filters_id, view=view, page=page, per_page=per_page)

List Drawing Disciplines

List of Drawing Disciplines

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v11_projects_project_id_drawing_disciplines_get200_response_inner import RestV11ProjectsProjectIdDrawingDisciplinesGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementDrawingsDrawingDisciplinesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    filters_id = [56] # List[int] | Filter by Drawing Disciplines ID To request specific drawing discipline ids add `filters[id]=[1,2,3]` to filters (optional)
    view = 'view_example' # str | Specify response schema view (optional)
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Drawing Disciplines
        api_response = api_instance.rest_v11_projects_project_id_drawing_disciplines_get(procore_company_id, project_id, filters_id=filters_id, view=view, page=page, per_page=per_page)
        print("The response of ProjectManagementDrawingsDrawingDisciplinesApi->rest_v11_projects_project_id_drawing_disciplines_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementDrawingsDrawingDisciplinesApi->rest_v11_projects_project_id_drawing_disciplines_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **filters_id** | [**List[int]**](int.md)| Filter by Drawing Disciplines ID To request specific drawing discipline ids add &#x60;filters[id]&#x3D;[1,2,3]&#x60; to filters | [optional] 
 **view** | **str**| Specify response schema view | [optional] 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[RestV11ProjectsProjectIdDrawingDisciplinesGet200ResponseInner]**](RestV11ProjectsProjectIdDrawingDisciplinesGet200ResponseInner.md)

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

# **rest_v11_projects_project_id_drawing_disciplines_id_patch**
> RestV11ProjectsProjectIdDrawingDisciplinesIdPatch200Response rest_v11_projects_project_id_drawing_disciplines_id_patch(procore_company_id, project_id, id, rest_v11_projects_project_id_drawing_disciplines_id_patch_request=rest_v11_projects_project_id_drawing_disciplines_id_patch_request)

Update drawing discipline

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v11_projects_project_id_drawing_disciplines_id_patch200_response import RestV11ProjectsProjectIdDrawingDisciplinesIdPatch200Response
from procore_sdk.models.rest_v11_projects_project_id_drawing_disciplines_id_patch_request import RestV11ProjectsProjectIdDrawingDisciplinesIdPatchRequest
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
    api_instance = procore_sdk.ProjectManagementDrawingsDrawingDisciplinesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | ID of the discipline to update
    rest_v11_projects_project_id_drawing_disciplines_id_patch_request = procore_sdk.RestV11ProjectsProjectIdDrawingDisciplinesIdPatchRequest() # RestV11ProjectsProjectIdDrawingDisciplinesIdPatchRequest |  (optional)

    try:
        # Update drawing discipline
        api_response = api_instance.rest_v11_projects_project_id_drawing_disciplines_id_patch(procore_company_id, project_id, id, rest_v11_projects_project_id_drawing_disciplines_id_patch_request=rest_v11_projects_project_id_drawing_disciplines_id_patch_request)
        print("The response of ProjectManagementDrawingsDrawingDisciplinesApi->rest_v11_projects_project_id_drawing_disciplines_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementDrawingsDrawingDisciplinesApi->rest_v11_projects_project_id_drawing_disciplines_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| ID of the discipline to update | 
 **rest_v11_projects_project_id_drawing_disciplines_id_patch_request** | [**RestV11ProjectsProjectIdDrawingDisciplinesIdPatchRequest**](RestV11ProjectsProjectIdDrawingDisciplinesIdPatchRequest.md)|  | [optional] 

### Return type

[**RestV11ProjectsProjectIdDrawingDisciplinesIdPatch200Response**](RestV11ProjectsProjectIdDrawingDisciplinesIdPatch200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

