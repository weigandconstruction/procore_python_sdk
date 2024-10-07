# procore_sdk.ProjectManagementProjectScheduleLookaheadTasksApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_schedule_lookahead_tasks_id_delete**](ProjectManagementProjectScheduleLookaheadTasksApi.md#rest_v10_projects_project_id_schedule_lookahead_tasks_id_delete) | **DELETE** /rest/v1.0/projects/{project_id}/schedule/lookahead_tasks/{id} | Delete Lookahead Task
[**rest_v10_projects_project_id_schedule_lookahead_tasks_id_patch**](ProjectManagementProjectScheduleLookaheadTasksApi.md#rest_v10_projects_project_id_schedule_lookahead_tasks_id_patch) | **PATCH** /rest/v1.0/projects/{project_id}/schedule/lookahead_tasks/{id} | Update Lookahead Task
[**rest_v10_projects_project_id_schedule_lookahead_tasks_post**](ProjectManagementProjectScheduleLookaheadTasksApi.md#rest_v10_projects_project_id_schedule_lookahead_tasks_post) | **POST** /rest/v1.0/projects/{project_id}/schedule/lookahead_tasks | Create Lookahead Task


# **rest_v10_projects_project_id_schedule_lookahead_tasks_id_delete**
> rest_v10_projects_project_id_schedule_lookahead_tasks_id_delete(procore_company_id, project_id, id)

Delete Lookahead Task

Delete a Lookahead Task from the project schedule

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
    api_instance = procore_sdk.ProjectManagementProjectScheduleLookaheadTasksApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Lookahead Task ID

    try:
        # Delete Lookahead Task
        api_instance.rest_v10_projects_project_id_schedule_lookahead_tasks_id_delete(procore_company_id, project_id, id)
    except Exception as e:
        print("Exception when calling ProjectManagementProjectScheduleLookaheadTasksApi->rest_v10_projects_project_id_schedule_lookahead_tasks_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Lookahead Task ID | 

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
**200** | Deleted |  -  |
**403** | User does not have right permissions |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_schedule_lookahead_tasks_id_patch**
> RestV10ProjectsProjectIdScheduleLookaheadTasksPost201Response rest_v10_projects_project_id_schedule_lookahead_tasks_id_patch(procore_company_id, project_id, id, rest_v10_projects_project_id_schedule_lookahead_tasks_post_request)

Update Lookahead Task

Update a Lookahead Task for the project schedule

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_schedule_lookahead_tasks_post201_response import RestV10ProjectsProjectIdScheduleLookaheadTasksPost201Response
from procore_sdk.models.rest_v10_projects_project_id_schedule_lookahead_tasks_post_request import RestV10ProjectsProjectIdScheduleLookaheadTasksPostRequest
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
    api_instance = procore_sdk.ProjectManagementProjectScheduleLookaheadTasksApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Lookahead Task ID
    rest_v10_projects_project_id_schedule_lookahead_tasks_post_request = procore_sdk.RestV10ProjectsProjectIdScheduleLookaheadTasksPostRequest() # RestV10ProjectsProjectIdScheduleLookaheadTasksPostRequest | 

    try:
        # Update Lookahead Task
        api_response = api_instance.rest_v10_projects_project_id_schedule_lookahead_tasks_id_patch(procore_company_id, project_id, id, rest_v10_projects_project_id_schedule_lookahead_tasks_post_request)
        print("The response of ProjectManagementProjectScheduleLookaheadTasksApi->rest_v10_projects_project_id_schedule_lookahead_tasks_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementProjectScheduleLookaheadTasksApi->rest_v10_projects_project_id_schedule_lookahead_tasks_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Lookahead Task ID | 
 **rest_v10_projects_project_id_schedule_lookahead_tasks_post_request** | [**RestV10ProjectsProjectIdScheduleLookaheadTasksPostRequest**](RestV10ProjectsProjectIdScheduleLookaheadTasksPostRequest.md)|  | 

### Return type

[**RestV10ProjectsProjectIdScheduleLookaheadTasksPost201Response**](RestV10ProjectsProjectIdScheduleLookaheadTasksPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated |  -  |
**403** | User does not have right permissions |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_schedule_lookahead_tasks_post**
> RestV10ProjectsProjectIdScheduleLookaheadTasksPost201Response rest_v10_projects_project_id_schedule_lookahead_tasks_post(procore_company_id, project_id, rest_v10_projects_project_id_schedule_lookahead_tasks_post_request)

Create Lookahead Task

Create new Lookahead Task for the project schedule

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_schedule_lookahead_tasks_post201_response import RestV10ProjectsProjectIdScheduleLookaheadTasksPost201Response
from procore_sdk.models.rest_v10_projects_project_id_schedule_lookahead_tasks_post_request import RestV10ProjectsProjectIdScheduleLookaheadTasksPostRequest
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
    api_instance = procore_sdk.ProjectManagementProjectScheduleLookaheadTasksApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_projects_project_id_schedule_lookahead_tasks_post_request = procore_sdk.RestV10ProjectsProjectIdScheduleLookaheadTasksPostRequest() # RestV10ProjectsProjectIdScheduleLookaheadTasksPostRequest | 

    try:
        # Create Lookahead Task
        api_response = api_instance.rest_v10_projects_project_id_schedule_lookahead_tasks_post(procore_company_id, project_id, rest_v10_projects_project_id_schedule_lookahead_tasks_post_request)
        print("The response of ProjectManagementProjectScheduleLookaheadTasksApi->rest_v10_projects_project_id_schedule_lookahead_tasks_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementProjectScheduleLookaheadTasksApi->rest_v10_projects_project_id_schedule_lookahead_tasks_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_projects_project_id_schedule_lookahead_tasks_post_request** | [**RestV10ProjectsProjectIdScheduleLookaheadTasksPostRequest**](RestV10ProjectsProjectIdScheduleLookaheadTasksPostRequest.md)|  | 

### Return type

[**RestV10ProjectsProjectIdScheduleLookaheadTasksPost201Response**](RestV10ProjectsProjectIdScheduleLookaheadTasksPost201Response.md)

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
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

