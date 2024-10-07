# procore_sdk.ProjectManagementProjectScheduleLookaheadsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_schedule_lookaheads_get**](ProjectManagementProjectScheduleLookaheadsApi.md#rest_v10_projects_project_id_schedule_lookaheads_get) | **GET** /rest/v1.0/projects/{project_id}/schedule/lookaheads | List Lookaheads
[**rest_v10_projects_project_id_schedule_lookaheads_id_delete**](ProjectManagementProjectScheduleLookaheadsApi.md#rest_v10_projects_project_id_schedule_lookaheads_id_delete) | **DELETE** /rest/v1.0/projects/{project_id}/schedule/lookaheads/{id} | Delete Lookahead
[**rest_v10_projects_project_id_schedule_lookaheads_id_get**](ProjectManagementProjectScheduleLookaheadsApi.md#rest_v10_projects_project_id_schedule_lookaheads_id_get) | **GET** /rest/v1.0/projects/{project_id}/schedule/lookaheads/{id} | Show Lookahead
[**rest_v10_projects_project_id_schedule_lookaheads_post**](ProjectManagementProjectScheduleLookaheadsApi.md#rest_v10_projects_project_id_schedule_lookaheads_post) | **POST** /rest/v1.0/projects/{project_id}/schedule/lookaheads | Create Lookahead
[**rest_v11_projects_project_id_schedule_lookaheads_get**](ProjectManagementProjectScheduleLookaheadsApi.md#rest_v11_projects_project_id_schedule_lookaheads_get) | **GET** /rest/v1.1/projects/{project_id}/schedule/lookaheads | List Lookaheads
[**rest_v11_projects_project_id_schedule_lookaheads_id_delete**](ProjectManagementProjectScheduleLookaheadsApi.md#rest_v11_projects_project_id_schedule_lookaheads_id_delete) | **DELETE** /rest/v1.1/projects/{project_id}/schedule/lookaheads/{id} | Delete Lookahead
[**rest_v11_projects_project_id_schedule_lookaheads_id_get**](ProjectManagementProjectScheduleLookaheadsApi.md#rest_v11_projects_project_id_schedule_lookaheads_id_get) | **GET** /rest/v1.1/projects/{project_id}/schedule/lookaheads/{id} | Show Lookahead
[**rest_v11_projects_project_id_schedule_lookaheads_post**](ProjectManagementProjectScheduleLookaheadsApi.md#rest_v11_projects_project_id_schedule_lookaheads_post) | **POST** /rest/v1.1/projects/{project_id}/schedule/lookaheads | Create Lookahead


# **rest_v10_projects_project_id_schedule_lookaheads_get**
> List[RestV11ProjectsProjectIdScheduleLookaheadsGet200ResponseInner] rest_v10_projects_project_id_schedule_lookaheads_get(procore_company_id, project_id)

List Lookaheads

Returns all Lookaheads for the project.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v11_projects_project_id_schedule_lookaheads_get200_response_inner import RestV11ProjectsProjectIdScheduleLookaheadsGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementProjectScheduleLookaheadsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.

    try:
        # List Lookaheads
        api_response = api_instance.rest_v10_projects_project_id_schedule_lookaheads_get(procore_company_id, project_id)
        print("The response of ProjectManagementProjectScheduleLookaheadsApi->rest_v10_projects_project_id_schedule_lookaheads_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementProjectScheduleLookaheadsApi->rest_v10_projects_project_id_schedule_lookaheads_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**List[RestV11ProjectsProjectIdScheduleLookaheadsGet200ResponseInner]**](RestV11ProjectsProjectIdScheduleLookaheadsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | User does not have right permissions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_schedule_lookaheads_id_delete**
> rest_v10_projects_project_id_schedule_lookaheads_id_delete(procore_company_id, project_id, id)

Delete Lookahead

Deletes a single Lookahead.

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
    api_instance = procore_sdk.ProjectManagementProjectScheduleLookaheadsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Lookahead ID

    try:
        # Delete Lookahead
        api_instance.rest_v10_projects_project_id_schedule_lookaheads_id_delete(procore_company_id, project_id, id)
    except Exception as e:
        print("Exception when calling ProjectManagementProjectScheduleLookaheadsApi->rest_v10_projects_project_id_schedule_lookaheads_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Lookahead ID | 

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
**204** | The lookahead was deleted |  -  |
**403** | User does not have right permissions |  -  |
**404** | Not found |  -  |
**422** | Unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_schedule_lookaheads_id_get**
> RestV11ProjectsProjectIdScheduleLookaheadsIdGet200Response rest_v10_projects_project_id_schedule_lookaheads_id_get(procore_company_id, project_id, id)

Show Lookahead

Returns single Lookahead.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v11_projects_project_id_schedule_lookaheads_id_get200_response import RestV11ProjectsProjectIdScheduleLookaheadsIdGet200Response
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
    api_instance = procore_sdk.ProjectManagementProjectScheduleLookaheadsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Lookahead ID

    try:
        # Show Lookahead
        api_response = api_instance.rest_v10_projects_project_id_schedule_lookaheads_id_get(procore_company_id, project_id, id)
        print("The response of ProjectManagementProjectScheduleLookaheadsApi->rest_v10_projects_project_id_schedule_lookaheads_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementProjectScheduleLookaheadsApi->rest_v10_projects_project_id_schedule_lookaheads_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Lookahead ID | 

### Return type

[**RestV11ProjectsProjectIdScheduleLookaheadsIdGet200Response**](RestV11ProjectsProjectIdScheduleLookaheadsIdGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | User does not have right permissions |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_schedule_lookaheads_post**
> RestV11ProjectsProjectIdScheduleLookaheadsGet200ResponseInner rest_v10_projects_project_id_schedule_lookaheads_post(procore_company_id, project_id, rest_v10_projects_project_id_schedule_lookaheads_post_request)

Create Lookahead

Create a new Lookahead for the project

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_schedule_lookaheads_post_request import RestV10ProjectsProjectIdScheduleLookaheadsPostRequest
from procore_sdk.models.rest_v11_projects_project_id_schedule_lookaheads_get200_response_inner import RestV11ProjectsProjectIdScheduleLookaheadsGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementProjectScheduleLookaheadsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_projects_project_id_schedule_lookaheads_post_request = procore_sdk.RestV10ProjectsProjectIdScheduleLookaheadsPostRequest() # RestV10ProjectsProjectIdScheduleLookaheadsPostRequest | 

    try:
        # Create Lookahead
        api_response = api_instance.rest_v10_projects_project_id_schedule_lookaheads_post(procore_company_id, project_id, rest_v10_projects_project_id_schedule_lookaheads_post_request)
        print("The response of ProjectManagementProjectScheduleLookaheadsApi->rest_v10_projects_project_id_schedule_lookaheads_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementProjectScheduleLookaheadsApi->rest_v10_projects_project_id_schedule_lookaheads_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_projects_project_id_schedule_lookaheads_post_request** | [**RestV10ProjectsProjectIdScheduleLookaheadsPostRequest**](RestV10ProjectsProjectIdScheduleLookaheadsPostRequest.md)|  | 

### Return type

[**RestV11ProjectsProjectIdScheduleLookaheadsGet200ResponseInner**](RestV11ProjectsProjectIdScheduleLookaheadsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**403** | User does not have right permissions |  -  |
**422** | Unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v11_projects_project_id_schedule_lookaheads_get**
> List[RestV11ProjectsProjectIdScheduleLookaheadsGet200ResponseInner] rest_v11_projects_project_id_schedule_lookaheads_get(procore_company_id, project_id)

List Lookaheads

Returns all Lookaheads for the project.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v11_projects_project_id_schedule_lookaheads_get200_response_inner import RestV11ProjectsProjectIdScheduleLookaheadsGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementProjectScheduleLookaheadsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.

    try:
        # List Lookaheads
        api_response = api_instance.rest_v11_projects_project_id_schedule_lookaheads_get(procore_company_id, project_id)
        print("The response of ProjectManagementProjectScheduleLookaheadsApi->rest_v11_projects_project_id_schedule_lookaheads_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementProjectScheduleLookaheadsApi->rest_v11_projects_project_id_schedule_lookaheads_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**List[RestV11ProjectsProjectIdScheduleLookaheadsGet200ResponseInner]**](RestV11ProjectsProjectIdScheduleLookaheadsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | User does not have right permissions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v11_projects_project_id_schedule_lookaheads_id_delete**
> rest_v11_projects_project_id_schedule_lookaheads_id_delete(procore_company_id, project_id, id)

Delete Lookahead

Deletes a single Lookahead.

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
    api_instance = procore_sdk.ProjectManagementProjectScheduleLookaheadsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Lookahead ID

    try:
        # Delete Lookahead
        api_instance.rest_v11_projects_project_id_schedule_lookaheads_id_delete(procore_company_id, project_id, id)
    except Exception as e:
        print("Exception when calling ProjectManagementProjectScheduleLookaheadsApi->rest_v11_projects_project_id_schedule_lookaheads_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Lookahead ID | 

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
**204** | The lookahead was deleted |  -  |
**403** | User does not have right permissions |  -  |
**404** | Not found |  -  |
**422** | Unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v11_projects_project_id_schedule_lookaheads_id_get**
> RestV11ProjectsProjectIdScheduleLookaheadsIdGet200Response rest_v11_projects_project_id_schedule_lookaheads_id_get(procore_company_id, project_id, id)

Show Lookahead

Returns single Lookahead.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v11_projects_project_id_schedule_lookaheads_id_get200_response import RestV11ProjectsProjectIdScheduleLookaheadsIdGet200Response
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
    api_instance = procore_sdk.ProjectManagementProjectScheduleLookaheadsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Lookahead ID

    try:
        # Show Lookahead
        api_response = api_instance.rest_v11_projects_project_id_schedule_lookaheads_id_get(procore_company_id, project_id, id)
        print("The response of ProjectManagementProjectScheduleLookaheadsApi->rest_v11_projects_project_id_schedule_lookaheads_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementProjectScheduleLookaheadsApi->rest_v11_projects_project_id_schedule_lookaheads_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Lookahead ID | 

### Return type

[**RestV11ProjectsProjectIdScheduleLookaheadsIdGet200Response**](RestV11ProjectsProjectIdScheduleLookaheadsIdGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | User does not have right permissions |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v11_projects_project_id_schedule_lookaheads_post**
> RestV11ProjectsProjectIdScheduleLookaheadsGet200ResponseInner rest_v11_projects_project_id_schedule_lookaheads_post(procore_company_id, project_id, rest_v11_projects_project_id_schedule_lookaheads_post_request)

Create Lookahead

Create a new Lookahead for the project

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v11_projects_project_id_schedule_lookaheads_get200_response_inner import RestV11ProjectsProjectIdScheduleLookaheadsGet200ResponseInner
from procore_sdk.models.rest_v11_projects_project_id_schedule_lookaheads_post_request import RestV11ProjectsProjectIdScheduleLookaheadsPostRequest
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
    api_instance = procore_sdk.ProjectManagementProjectScheduleLookaheadsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rest_v11_projects_project_id_schedule_lookaheads_post_request = procore_sdk.RestV11ProjectsProjectIdScheduleLookaheadsPostRequest() # RestV11ProjectsProjectIdScheduleLookaheadsPostRequest | 

    try:
        # Create Lookahead
        api_response = api_instance.rest_v11_projects_project_id_schedule_lookaheads_post(procore_company_id, project_id, rest_v11_projects_project_id_schedule_lookaheads_post_request)
        print("The response of ProjectManagementProjectScheduleLookaheadsApi->rest_v11_projects_project_id_schedule_lookaheads_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementProjectScheduleLookaheadsApi->rest_v11_projects_project_id_schedule_lookaheads_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v11_projects_project_id_schedule_lookaheads_post_request** | [**RestV11ProjectsProjectIdScheduleLookaheadsPostRequest**](RestV11ProjectsProjectIdScheduleLookaheadsPostRequest.md)|  | 

### Return type

[**RestV11ProjectsProjectIdScheduleLookaheadsGet200ResponseInner**](RestV11ProjectsProjectIdScheduleLookaheadsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**403** | User does not have right permissions |  -  |
**422** | Unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

