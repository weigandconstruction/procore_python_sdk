# procore_sdk.ProjectManagementDrawingsDrawingAreasApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_drawing_areas_get**](ProjectManagementDrawingsDrawingAreasApi.md#rest_v10_projects_project_id_drawing_areas_get) | **GET** /rest/v1.0/projects/{project_id}/drawing_areas | List drawing areas
[**rest_v10_projects_project_id_drawing_areas_post**](ProjectManagementDrawingsDrawingAreasApi.md#rest_v10_projects_project_id_drawing_areas_post) | **POST** /rest/v1.0/projects/{project_id}/drawing_areas | Create drawing area
[**rest_v11_projects_project_id_drawing_areas_get**](ProjectManagementDrawingsDrawingAreasApi.md#rest_v11_projects_project_id_drawing_areas_get) | **GET** /rest/v1.1/projects/{project_id}/drawing_areas | List drawing areas
[**rest_v11_projects_project_id_drawing_areas_post**](ProjectManagementDrawingsDrawingAreasApi.md#rest_v11_projects_project_id_drawing_areas_post) | **POST** /rest/v1.1/projects/{project_id}/drawing_areas | Create drawing area


# **rest_v10_projects_project_id_drawing_areas_get**
> List[DrawingArea1] rest_v10_projects_project_id_drawing_areas_get(procore_company_id, project_id, page=page, per_page=per_page)

List drawing areas

Returns a list of all Drawing Areas in the specified Project.

### Example


```python
import procore_sdk
from procore_sdk.models.drawing_area1 import DrawingArea1
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
    api_instance = procore_sdk.ProjectManagementDrawingsDrawingAreasApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List drawing areas
        api_response = api_instance.rest_v10_projects_project_id_drawing_areas_get(procore_company_id, project_id, page=page, per_page=per_page)
        print("The response of ProjectManagementDrawingsDrawingAreasApi->rest_v10_projects_project_id_drawing_areas_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementDrawingsDrawingAreasApi->rest_v10_projects_project_id_drawing_areas_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[DrawingArea1]**](DrawingArea1.md)

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

# **rest_v10_projects_project_id_drawing_areas_post**
> RestV11ProjectsProjectIdDrawingAreasPost201Response rest_v10_projects_project_id_drawing_areas_post(procore_company_id, project_id, body91)

Create drawing area

Create a new Drawing Area in the specified Project.

### Example


```python
import procore_sdk
from procore_sdk.models.body91 import Body91
from procore_sdk.models.rest_v11_projects_project_id_drawing_areas_post201_response import RestV11ProjectsProjectIdDrawingAreasPost201Response
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
    api_instance = procore_sdk.ProjectManagementDrawingsDrawingAreasApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    body91 = procore_sdk.Body91() # Body91 | 

    try:
        # Create drawing area
        api_response = api_instance.rest_v10_projects_project_id_drawing_areas_post(procore_company_id, project_id, body91)
        print("The response of ProjectManagementDrawingsDrawingAreasApi->rest_v10_projects_project_id_drawing_areas_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementDrawingsDrawingAreasApi->rest_v10_projects_project_id_drawing_areas_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **body91** | [**Body91**](Body91.md)|  | 

### Return type

[**RestV11ProjectsProjectIdDrawingAreasPost201Response**](RestV11ProjectsProjectIdDrawingAreasPost201Response.md)

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

# **rest_v11_projects_project_id_drawing_areas_get**
> List[DrawingArea] rest_v11_projects_project_id_drawing_areas_get(procore_company_id, project_id, page=page, per_page=per_page, filters_id=filters_id, view=view)

List drawing areas

Returns a list of all Drawing Areas in the specified Project.

### Example


```python
import procore_sdk
from procore_sdk.models.drawing_area import DrawingArea
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
    api_instance = procore_sdk.ProjectManagementDrawingsDrawingAreasApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_id = [56] # List[int] | Filter by Drawing Areas ID To request specific drawing area ids add `filters[id]=[1,2,3]` to filters (optional)
    view = 'view_example' # str | Specify response schema view (optional)

    try:
        # List drawing areas
        api_response = api_instance.rest_v11_projects_project_id_drawing_areas_get(procore_company_id, project_id, page=page, per_page=per_page, filters_id=filters_id, view=view)
        print("The response of ProjectManagementDrawingsDrawingAreasApi->rest_v11_projects_project_id_drawing_areas_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementDrawingsDrawingAreasApi->rest_v11_projects_project_id_drawing_areas_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_id** | [**List[int]**](int.md)| Filter by Drawing Areas ID To request specific drawing area ids add &#x60;filters[id]&#x3D;[1,2,3]&#x60; to filters | [optional] 
 **view** | **str**| Specify response schema view | [optional] 

### Return type

[**List[DrawingArea]**](DrawingArea.md)

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

# **rest_v11_projects_project_id_drawing_areas_post**
> RestV11ProjectsProjectIdDrawingAreasPost201Response rest_v11_projects_project_id_drawing_areas_post(procore_company_id, project_id, body90)

Create drawing area

Create a new Drawing Area in the specified Project.

### Example


```python
import procore_sdk
from procore_sdk.models.body90 import Body90
from procore_sdk.models.rest_v11_projects_project_id_drawing_areas_post201_response import RestV11ProjectsProjectIdDrawingAreasPost201Response
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
    api_instance = procore_sdk.ProjectManagementDrawingsDrawingAreasApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    body90 = procore_sdk.Body90() # Body90 | 

    try:
        # Create drawing area
        api_response = api_instance.rest_v11_projects_project_id_drawing_areas_post(procore_company_id, project_id, body90)
        print("The response of ProjectManagementDrawingsDrawingAreasApi->rest_v11_projects_project_id_drawing_areas_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementDrawingsDrawingAreasApi->rest_v11_projects_project_id_drawing_areas_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **body90** | [**Body90**](Body90.md)|  | 

### Return type

[**RestV11ProjectsProjectIdDrawingAreasPost201Response**](RestV11ProjectsProjectIdDrawingAreasPost201Response.md)

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

