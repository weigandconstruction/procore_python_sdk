# procore_sdk.ProjectManagementProjectScheduleScheduleResourcesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_resources_get**](ProjectManagementProjectScheduleScheduleResourcesApi.md#rest_v10_resources_get) | **GET** /rest/v1.0/resources | List Resources
[**rest_v10_resources_id_delete**](ProjectManagementProjectScheduleScheduleResourcesApi.md#rest_v10_resources_id_delete) | **DELETE** /rest/v1.0/resources/{id} | Delete resource
[**rest_v10_resources_id_get**](ProjectManagementProjectScheduleScheduleResourcesApi.md#rest_v10_resources_id_get) | **GET** /rest/v1.0/resources/{id} | Show resource
[**rest_v10_resources_id_patch**](ProjectManagementProjectScheduleScheduleResourcesApi.md#rest_v10_resources_id_patch) | **PATCH** /rest/v1.0/resources/{id} | Update resource
[**rest_v10_resources_post**](ProjectManagementProjectScheduleScheduleResourcesApi.md#rest_v10_resources_post) | **POST** /rest/v1.0/resources | Create resource
[**rest_v11_projects_project_id_schedule_resources_get**](ProjectManagementProjectScheduleScheduleResourcesApi.md#rest_v11_projects_project_id_schedule_resources_get) | **GET** /rest/v1.1/projects/{project_id}/schedule/resources | List Resources
[**rest_v11_projects_project_id_schedule_resources_id_delete**](ProjectManagementProjectScheduleScheduleResourcesApi.md#rest_v11_projects_project_id_schedule_resources_id_delete) | **DELETE** /rest/v1.1/projects/{project_id}/schedule/resources/{id} | Delete resource
[**rest_v11_projects_project_id_schedule_resources_id_get**](ProjectManagementProjectScheduleScheduleResourcesApi.md#rest_v11_projects_project_id_schedule_resources_id_get) | **GET** /rest/v1.1/projects/{project_id}/schedule/resources/{id} | Show resource
[**rest_v11_projects_project_id_schedule_resources_id_patch**](ProjectManagementProjectScheduleScheduleResourcesApi.md#rest_v11_projects_project_id_schedule_resources_id_patch) | **PATCH** /rest/v1.1/projects/{project_id}/schedule/resources/{id} | Update resource
[**rest_v11_projects_project_id_schedule_resources_post**](ProjectManagementProjectScheduleScheduleResourcesApi.md#rest_v11_projects_project_id_schedule_resources_post) | **POST** /rest/v1.1/projects/{project_id}/schedule/resources | Create resource


# **rest_v10_resources_get**
> List[Resource2] rest_v10_resources_get(procore_company_id, project_id, page=page, per_page=per_page)

List Resources

Return a list of all resources in a specified Project

### Example


```python
import procore_sdk
from procore_sdk.models.resource2 import Resource2
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
    api_instance = procore_sdk.ProjectManagementProjectScheduleScheduleResourcesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Resources
        api_response = api_instance.rest_v10_resources_get(procore_company_id, project_id, page=page, per_page=per_page)
        print("The response of ProjectManagementProjectScheduleScheduleResourcesApi->rest_v10_resources_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementProjectScheduleScheduleResourcesApi->rest_v10_resources_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[Resource2]**](Resource2.md)

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

# **rest_v10_resources_id_delete**
> rest_v10_resources_id_delete(procore_company_id, id, project_id)

Delete resource

Delete the specified Resource. Note that when a resource is deleted, any assignments to tasks will also be removed.

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
    api_instance = procore_sdk.ProjectManagementProjectScheduleScheduleResourcesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the resource
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Delete resource
        api_instance.rest_v10_resources_id_delete(procore_company_id, id, project_id)
    except Exception as e:
        print("Exception when calling ProjectManagementProjectScheduleScheduleResourcesApi->rest_v10_resources_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the resource | 
 **project_id** | **int**| Unique identifier for the project. | 

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
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_resources_id_get**
> Resource2 rest_v10_resources_id_get(procore_company_id, id, project_id)

Show resource

Show detail on the specified Resource.

### Example


```python
import procore_sdk
from procore_sdk.models.resource2 import Resource2
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
    api_instance = procore_sdk.ProjectManagementProjectScheduleScheduleResourcesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the resource
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Show resource
        api_response = api_instance.rest_v10_resources_id_get(procore_company_id, id, project_id)
        print("The response of ProjectManagementProjectScheduleScheduleResourcesApi->rest_v10_resources_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementProjectScheduleScheduleResourcesApi->rest_v10_resources_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the resource | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**Resource2**](Resource2.md)

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

# **rest_v10_resources_id_patch**
> Resource2 rest_v10_resources_id_patch(procore_company_id, id, body17)

Update resource

Update the specified Resource.

### Example


```python
import procore_sdk
from procore_sdk.models.body17 import Body17
from procore_sdk.models.resource2 import Resource2
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
    api_instance = procore_sdk.ProjectManagementProjectScheduleScheduleResourcesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the resource
    body17 = procore_sdk.Body17() # Body17 | 

    try:
        # Update resource
        api_response = api_instance.rest_v10_resources_id_patch(procore_company_id, id, body17)
        print("The response of ProjectManagementProjectScheduleScheduleResourcesApi->rest_v10_resources_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementProjectScheduleScheduleResourcesApi->rest_v10_resources_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the resource | 
 **body17** | [**Body17**](Body17.md)|  | 

### Return type

[**Resource2**](Resource2.md)

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
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_resources_post**
> Resource2 rest_v10_resources_post(procore_company_id, body17)

Create resource

Create a new Resource associated with the specified Project.

### Example


```python
import procore_sdk
from procore_sdk.models.body17 import Body17
from procore_sdk.models.resource2 import Resource2
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
    api_instance = procore_sdk.ProjectManagementProjectScheduleScheduleResourcesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    body17 = procore_sdk.Body17() # Body17 | 

    try:
        # Create resource
        api_response = api_instance.rest_v10_resources_post(procore_company_id, body17)
        print("The response of ProjectManagementProjectScheduleScheduleResourcesApi->rest_v10_resources_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementProjectScheduleScheduleResourcesApi->rest_v10_resources_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **body17** | [**Body17**](Body17.md)|  | 

### Return type

[**Resource2**](Resource2.md)

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

# **rest_v11_projects_project_id_schedule_resources_get**
> List[Resource] rest_v11_projects_project_id_schedule_resources_get(procore_company_id, project_id, page=page, per_page=per_page, filters_query=filters_query)

List Resources

Return a list of all resources in a specified Project

### Example


```python
import procore_sdk
from procore_sdk.models.resource import Resource
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
    api_instance = procore_sdk.ProjectManagementProjectScheduleScheduleResourcesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_query = 'filters_query_example' # str | Return item(s) containing search query (optional)

    try:
        # List Resources
        api_response = api_instance.rest_v11_projects_project_id_schedule_resources_get(procore_company_id, project_id, page=page, per_page=per_page, filters_query=filters_query)
        print("The response of ProjectManagementProjectScheduleScheduleResourcesApi->rest_v11_projects_project_id_schedule_resources_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementProjectScheduleScheduleResourcesApi->rest_v11_projects_project_id_schedule_resources_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_query** | **str**| Return item(s) containing search query | [optional] 

### Return type

[**List[Resource]**](Resource.md)

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

# **rest_v11_projects_project_id_schedule_resources_id_delete**
> rest_v11_projects_project_id_schedule_resources_id_delete(procore_company_id, project_id, id)

Delete resource

Delete the specified Resource. Note that when a Resource is deleted, any assignments to Tasks will also be removed.

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
    api_instance = procore_sdk.ProjectManagementProjectScheduleScheduleResourcesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | ID of the resource

    try:
        # Delete resource
        api_instance.rest_v11_projects_project_id_schedule_resources_id_delete(procore_company_id, project_id, id)
    except Exception as e:
        print("Exception when calling ProjectManagementProjectScheduleScheduleResourcesApi->rest_v11_projects_project_id_schedule_resources_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| ID of the resource | 

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
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v11_projects_project_id_schedule_resources_id_get**
> Resource rest_v11_projects_project_id_schedule_resources_id_get(procore_company_id, project_id, id)

Show resource

Show detail on the specified Resource.

### Example


```python
import procore_sdk
from procore_sdk.models.resource import Resource
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
    api_instance = procore_sdk.ProjectManagementProjectScheduleScheduleResourcesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | ID of the resource

    try:
        # Show resource
        api_response = api_instance.rest_v11_projects_project_id_schedule_resources_id_get(procore_company_id, project_id, id)
        print("The response of ProjectManagementProjectScheduleScheduleResourcesApi->rest_v11_projects_project_id_schedule_resources_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementProjectScheduleScheduleResourcesApi->rest_v11_projects_project_id_schedule_resources_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| ID of the resource | 

### Return type

[**Resource**](Resource.md)

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

# **rest_v11_projects_project_id_schedule_resources_id_patch**
> Resource rest_v11_projects_project_id_schedule_resources_id_patch(procore_company_id, project_id, id, body17)

Update resource

Update the specified Resource.

### Example


```python
import procore_sdk
from procore_sdk.models.body17 import Body17
from procore_sdk.models.resource import Resource
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
    api_instance = procore_sdk.ProjectManagementProjectScheduleScheduleResourcesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | ID of the resource
    body17 = procore_sdk.Body17() # Body17 | 

    try:
        # Update resource
        api_response = api_instance.rest_v11_projects_project_id_schedule_resources_id_patch(procore_company_id, project_id, id, body17)
        print("The response of ProjectManagementProjectScheduleScheduleResourcesApi->rest_v11_projects_project_id_schedule_resources_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementProjectScheduleScheduleResourcesApi->rest_v11_projects_project_id_schedule_resources_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| ID of the resource | 
 **body17** | [**Body17**](Body17.md)|  | 

### Return type

[**Resource**](Resource.md)

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
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v11_projects_project_id_schedule_resources_post**
> Resource rest_v11_projects_project_id_schedule_resources_post(procore_company_id, project_id, body17)

Create resource

Create a new Resource associated with the specified Project.

### Example


```python
import procore_sdk
from procore_sdk.models.body17 import Body17
from procore_sdk.models.resource import Resource
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
    api_instance = procore_sdk.ProjectManagementProjectScheduleScheduleResourcesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    body17 = procore_sdk.Body17() # Body17 | 

    try:
        # Create resource
        api_response = api_instance.rest_v11_projects_project_id_schedule_resources_post(procore_company_id, project_id, body17)
        print("The response of ProjectManagementProjectScheduleScheduleResourcesApi->rest_v11_projects_project_id_schedule_resources_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementProjectScheduleScheduleResourcesApi->rest_v11_projects_project_id_schedule_resources_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **body17** | [**Body17**](Body17.md)|  | 

### Return type

[**Resource**](Resource.md)

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

