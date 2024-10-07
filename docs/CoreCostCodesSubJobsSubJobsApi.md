# procore_sdk.CoreCostCodesSubJobsSubJobsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_sub_jobs_get**](CoreCostCodesSubJobsSubJobsApi.md#rest_v10_sub_jobs_get) | **GET** /rest/v1.0/sub_jobs | List Sub Jobs
[**rest_v10_sub_jobs_id_delete**](CoreCostCodesSubJobsSubJobsApi.md#rest_v10_sub_jobs_id_delete) | **DELETE** /rest/v1.0/sub_jobs/{id} | Delete Sub Job
[**rest_v10_sub_jobs_id_get**](CoreCostCodesSubJobsSubJobsApi.md#rest_v10_sub_jobs_id_get) | **GET** /rest/v1.0/sub_jobs/{id} | Show Sub Job
[**rest_v10_sub_jobs_id_patch**](CoreCostCodesSubJobsSubJobsApi.md#rest_v10_sub_jobs_id_patch) | **PATCH** /rest/v1.0/sub_jobs/{id} | Update Sub Job
[**rest_v10_sub_jobs_post**](CoreCostCodesSubJobsSubJobsApi.md#rest_v10_sub_jobs_post) | **POST** /rest/v1.0/sub_jobs | Create Sub Job
[**rest_v10_sub_jobs_sync_patch**](CoreCostCodesSubJobsSubJobsApi.md#rest_v10_sub_jobs_sync_patch) | **PATCH** /rest/v1.0/sub_jobs/sync | Sync Sub Jobs


# **rest_v10_sub_jobs_get**
> List[RestV10SubJobsGet200ResponseInner] rest_v10_sub_jobs_get(procore_company_id, project_id, page=page, per_page=per_page)

List Sub Jobs

Return a list of all Sub Jobs in a specified Project.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_sub_jobs_get200_response_inner import RestV10SubJobsGet200ResponseInner
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
    api_instance = procore_sdk.CoreCostCodesSubJobsSubJobsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Sub Jobs
        api_response = api_instance.rest_v10_sub_jobs_get(procore_company_id, project_id, page=page, per_page=per_page)
        print("The response of CoreCostCodesSubJobsSubJobsApi->rest_v10_sub_jobs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCostCodesSubJobsSubJobsApi->rest_v10_sub_jobs_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[RestV10SubJobsGet200ResponseInner]**](RestV10SubJobsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Per-Page - Number of items retrieved per page <br>  * Total - Total number of items to be retrieved <br>  * Link - Link headers for the first, prev, next, and last link <br>  |
**403** | User does not have right permissions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_sub_jobs_id_delete**
> rest_v10_sub_jobs_id_delete(procore_company_id, id, project_id)

Delete Sub Job

Delete a specified Sub Job. Deprecation Note: Please find the replacement endpoint in the Work Breakdown Structure documents. This endpoint will be replaced with the Delete Project Segment Item Endpoint.

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
    api_instance = procore_sdk.CoreCostCodesSubJobsSubJobsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Delete Sub Job
        api_instance.rest_v10_sub_jobs_id_delete(procore_company_id, id, project_id)
    except Exception as e:
        print("Exception when calling CoreCostCodesSubJobsSubJobsApi->rest_v10_sub_jobs_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_sub_jobs_id_get**
> RestV10SubJobsGet200ResponseInner rest_v10_sub_jobs_id_get(procore_company_id, id, project_id)

Show Sub Job

Return a specified Sub Jobs in a specified Project.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_sub_jobs_get200_response_inner import RestV10SubJobsGet200ResponseInner
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
    api_instance = procore_sdk.CoreCostCodesSubJobsSubJobsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Show Sub Job
        api_response = api_instance.rest_v10_sub_jobs_id_get(procore_company_id, id, project_id)
        print("The response of CoreCostCodesSubJobsSubJobsApi->rest_v10_sub_jobs_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCostCodesSubJobsSubJobsApi->rest_v10_sub_jobs_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**RestV10SubJobsGet200ResponseInner**](RestV10SubJobsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_sub_jobs_id_patch**
> RestV10SubJobsGet200ResponseInner rest_v10_sub_jobs_id_patch(procore_company_id, id, sub_job_body)

Update Sub Job

Update a specified Sub Job.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_sub_jobs_get200_response_inner import RestV10SubJobsGet200ResponseInner
from procore_sdk.models.sub_job_body import SubJobBody
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
    api_instance = procore_sdk.CoreCostCodesSubJobsSubJobsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID
    sub_job_body = procore_sdk.SubJobBody() # SubJobBody | 

    try:
        # Update Sub Job
        api_response = api_instance.rest_v10_sub_jobs_id_patch(procore_company_id, id, sub_job_body)
        print("The response of CoreCostCodesSubJobsSubJobsApi->rest_v10_sub_jobs_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCostCodesSubJobsSubJobsApi->rest_v10_sub_jobs_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID | 
 **sub_job_body** | [**SubJobBody**](SubJobBody.md)|  | 

### Return type

[**RestV10SubJobsGet200ResponseInner**](RestV10SubJobsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_sub_jobs_post**
> RestV10SubJobsGet200ResponseInner rest_v10_sub_jobs_post(procore_company_id, sub_job_body)

Create Sub Job

Create a new Sub Job.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_sub_jobs_get200_response_inner import RestV10SubJobsGet200ResponseInner
from procore_sdk.models.sub_job_body import SubJobBody
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
    api_instance = procore_sdk.CoreCostCodesSubJobsSubJobsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    sub_job_body = procore_sdk.SubJobBody() # SubJobBody | 

    try:
        # Create Sub Job
        api_response = api_instance.rest_v10_sub_jobs_post(procore_company_id, sub_job_body)
        print("The response of CoreCostCodesSubJobsSubJobsApi->rest_v10_sub_jobs_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCostCodesSubJobsSubJobsApi->rest_v10_sub_jobs_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **sub_job_body** | [**SubJobBody**](SubJobBody.md)|  | 

### Return type

[**RestV10SubJobsGet200ResponseInner**](RestV10SubJobsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Can not create Sub Job due to errors. |  -  |
**403** | User does not have right permissions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_sub_jobs_sync_patch**
> RestV10SubJobsSyncPatch200Response rest_v10_sub_jobs_sync_patch(procore_company_id, project_id, sub_job_sync_body)

Sync Sub Jobs

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_sub_jobs_sync_patch200_response import RestV10SubJobsSyncPatch200Response
from procore_sdk.models.sub_job_sync_body import SubJobSyncBody
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
    api_instance = procore_sdk.CoreCostCodesSubJobsSubJobsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    sub_job_sync_body = procore_sdk.SubJobSyncBody() # SubJobSyncBody | 

    try:
        # Sync Sub Jobs
        api_response = api_instance.rest_v10_sub_jobs_sync_patch(procore_company_id, project_id, sub_job_sync_body)
        print("The response of CoreCostCodesSubJobsSubJobsApi->rest_v10_sub_jobs_sync_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCostCodesSubJobsSubJobsApi->rest_v10_sub_jobs_sync_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **sub_job_sync_body** | [**SubJobSyncBody**](SubJobSyncBody.md)|  | 

### Return type

[**RestV10SubJobsSyncPatch200Response**](RestV10SubJobsSyncPatch200Response.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

