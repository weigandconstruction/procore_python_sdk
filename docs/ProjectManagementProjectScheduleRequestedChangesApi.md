# procore_sdk.ProjectManagementProjectScheduleRequestedChangesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_requested_changes_get**](ProjectManagementProjectScheduleRequestedChangesApi.md#rest_v10_requested_changes_get) | **GET** /rest/v1.0/requested_changes | List Requested Changes
[**rest_v10_requested_changes_post**](ProjectManagementProjectScheduleRequestedChangesApi.md#rest_v10_requested_changes_post) | **POST** /rest/v1.0/requested_changes | Creates Requested Change
[**rest_v10_requested_changes_review_patch**](ProjectManagementProjectScheduleRequestedChangesApi.md#rest_v10_requested_changes_review_patch) | **PATCH** /rest/v1.0/requested_changes/review | Review Requested Changes


# **rest_v10_requested_changes_get**
> RestV10RequestedChangesGet200Response rest_v10_requested_changes_get(procore_company_id, project_id, task_id=task_id, view=view, page=page, per_page=per_page)

List Requested Changes

List all Requested Changes of a Task.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_requested_changes_get200_response import RestV10RequestedChangesGet200Response
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
    api_instance = procore_sdk.ProjectManagementProjectScheduleRequestedChangesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    task_id = 56 # int | The task for which all requested changes will be retrieved. (optional)
    view = 'view_example' # str | The `with_task` view includes an additional task data for correspondent requested changes (optional)
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Requested Changes
        api_response = api_instance.rest_v10_requested_changes_get(procore_company_id, project_id, task_id=task_id, view=view, page=page, per_page=per_page)
        print("The response of ProjectManagementProjectScheduleRequestedChangesApi->rest_v10_requested_changes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementProjectScheduleRequestedChangesApi->rest_v10_requested_changes_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **task_id** | **int**| The task for which all requested changes will be retrieved. | [optional] 
 **view** | **str**| The &#x60;with_task&#x60; view includes an additional task data for correspondent requested changes | [optional] 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**RestV10RequestedChangesGet200Response**](RestV10RequestedChangesGet200Response.md)

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

# **rest_v10_requested_changes_post**
> RestV11ProjectsProjectIdScheduleRequestedChangesGet200ResponseInner rest_v10_requested_changes_post(procore_company_id, project_id, task_id, rest_v11_projects_project_id_schedule_tasks_task_id_requested_changes_post_request)

Creates Requested Change

Creates a requested changes for a Task.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v11_projects_project_id_schedule_requested_changes_get200_response_inner import RestV11ProjectsProjectIdScheduleRequestedChangesGet200ResponseInner
from procore_sdk.models.rest_v11_projects_project_id_schedule_tasks_task_id_requested_changes_post_request import RestV11ProjectsProjectIdScheduleTasksTaskIdRequestedChangesPostRequest
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
    api_instance = procore_sdk.ProjectManagementProjectScheduleRequestedChangesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    task_id = 56 # int | The task for which requested changes will be added to.
    rest_v11_projects_project_id_schedule_tasks_task_id_requested_changes_post_request = procore_sdk.RestV11ProjectsProjectIdScheduleTasksTaskIdRequestedChangesPostRequest() # RestV11ProjectsProjectIdScheduleTasksTaskIdRequestedChangesPostRequest | 

    try:
        # Creates Requested Change
        api_response = api_instance.rest_v10_requested_changes_post(procore_company_id, project_id, task_id, rest_v11_projects_project_id_schedule_tasks_task_id_requested_changes_post_request)
        print("The response of ProjectManagementProjectScheduleRequestedChangesApi->rest_v10_requested_changes_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementProjectScheduleRequestedChangesApi->rest_v10_requested_changes_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **task_id** | **int**| The task for which requested changes will be added to. | 
 **rest_v11_projects_project_id_schedule_tasks_task_id_requested_changes_post_request** | [**RestV11ProjectsProjectIdScheduleTasksTaskIdRequestedChangesPostRequest**](RestV11ProjectsProjectIdScheduleTasksTaskIdRequestedChangesPostRequest.md)|  | 

### Return type

[**RestV11ProjectsProjectIdScheduleRequestedChangesGet200ResponseInner**](RestV11ProjectsProjectIdScheduleRequestedChangesGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_requested_changes_review_patch**
> List[RestV11ProjectsProjectIdScheduleRequestedChangesReviewPatch200ResponseInner] rest_v10_requested_changes_review_patch(procore_company_id, project_id, rest_v11_projects_project_id_schedule_requested_changes_review_patch_request)

Review Requested Changes

Review Requested Changes for Tasks.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v11_projects_project_id_schedule_requested_changes_review_patch200_response_inner import RestV11ProjectsProjectIdScheduleRequestedChangesReviewPatch200ResponseInner
from procore_sdk.models.rest_v11_projects_project_id_schedule_requested_changes_review_patch_request import RestV11ProjectsProjectIdScheduleRequestedChangesReviewPatchRequest
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
    api_instance = procore_sdk.ProjectManagementProjectScheduleRequestedChangesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rest_v11_projects_project_id_schedule_requested_changes_review_patch_request = procore_sdk.RestV11ProjectsProjectIdScheduleRequestedChangesReviewPatchRequest() # RestV11ProjectsProjectIdScheduleRequestedChangesReviewPatchRequest | 

    try:
        # Review Requested Changes
        api_response = api_instance.rest_v10_requested_changes_review_patch(procore_company_id, project_id, rest_v11_projects_project_id_schedule_requested_changes_review_patch_request)
        print("The response of ProjectManagementProjectScheduleRequestedChangesApi->rest_v10_requested_changes_review_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementProjectScheduleRequestedChangesApi->rest_v10_requested_changes_review_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v11_projects_project_id_schedule_requested_changes_review_patch_request** | [**RestV11ProjectsProjectIdScheduleRequestedChangesReviewPatchRequest**](RestV11ProjectsProjectIdScheduleRequestedChangesReviewPatchRequest.md)|  | 

### Return type

[**List[RestV11ProjectsProjectIdScheduleRequestedChangesReviewPatch200ResponseInner]**](RestV11ProjectsProjectIdScheduleRequestedChangesReviewPatch200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

