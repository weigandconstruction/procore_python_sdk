# procore_sdk.CoreTasksTaskItemCommentsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_projects_project_id_task_item_comments_get**](CoreTasksTaskItemCommentsApi.md#rest_v10_companies_company_id_projects_project_id_task_item_comments_get) | **GET** /rest/v1.0/companies/{company_id}/projects/{project_id}/task_item_comments | List Task Item Comments
[**rest_v10_companies_company_id_projects_project_id_task_item_comments_id_delete**](CoreTasksTaskItemCommentsApi.md#rest_v10_companies_company_id_projects_project_id_task_item_comments_id_delete) | **DELETE** /rest/v1.0/companies/{company_id}/projects/{project_id}/task_item_comments/{id} | Delete a task item comment
[**rest_v10_companies_company_id_projects_project_id_task_item_comments_id_patch**](CoreTasksTaskItemCommentsApi.md#rest_v10_companies_company_id_projects_project_id_task_item_comments_id_patch) | **PATCH** /rest/v1.0/companies/{company_id}/projects/{project_id}/task_item_comments/{id} | Update a task item comment
[**rest_v10_companies_company_id_projects_project_id_task_item_comments_post**](CoreTasksTaskItemCommentsApi.md#rest_v10_companies_company_id_projects_project_id_task_item_comments_post) | **POST** /rest/v1.0/companies/{company_id}/projects/{project_id}/task_item_comments | Create a task item comment


# **rest_v10_companies_company_id_projects_project_id_task_item_comments_get**
> List[RestV10CompaniesCompanyIdProjectsProjectIdTaskItemCommentsGet200ResponseInner] rest_v10_companies_company_id_projects_project_id_task_item_comments_get(procore_company_id, company_id, project_id, filters_task_item_id=filters_task_item_id, filters_created_by_id=filters_created_by_id, page=page, per_page=per_page)

List Task Item Comments

Returns a list of comments associated with the project. Can be filtered by task_item_id and/or created_by_id.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_projects_project_id_task_item_comments_get200_response_inner import RestV10CompaniesCompanyIdProjectsProjectIdTaskItemCommentsGet200ResponseInner
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
    api_instance = procore_sdk.CoreTasksTaskItemCommentsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    project_id = 56 # int | Unique identifier for the project.
    filters_task_item_id = 56 # int | Filter by task_item_id to return comments for only that task_item (optional)
    filters_created_by_id = [56] # List[int] | Returns item(s) created by the specified User IDs. (optional)
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Task Item Comments
        api_response = api_instance.rest_v10_companies_company_id_projects_project_id_task_item_comments_get(procore_company_id, company_id, project_id, filters_task_item_id=filters_task_item_id, filters_created_by_id=filters_created_by_id, page=page, per_page=per_page)
        print("The response of CoreTasksTaskItemCommentsApi->rest_v10_companies_company_id_projects_project_id_task_item_comments_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreTasksTaskItemCommentsApi->rest_v10_companies_company_id_projects_project_id_task_item_comments_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **filters_task_item_id** | **int**| Filter by task_item_id to return comments for only that task_item | [optional] 
 **filters_created_by_id** | [**List[int]**](int.md)| Returns item(s) created by the specified User IDs. | [optional] 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[RestV10CompaniesCompanyIdProjectsProjectIdTaskItemCommentsGet200ResponseInner]**](RestV10CompaniesCompanyIdProjectsProjectIdTaskItemCommentsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Per-Page - Number of items retrieved per page <br>  * Total - Total number of items to be retrieved <br>  * Link - Link headers for the first, prev, next, and last link <br>  |
**403** | User does not have right permissions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_projects_project_id_task_item_comments_id_delete**
> RestV10CompaniesCompanyIdProjectsProjectIdTaskItemCommentsGet200ResponseInner rest_v10_companies_company_id_projects_project_id_task_item_comments_id_delete(procore_company_id, company_id, project_id, id)

Delete a task item comment

Deletes the task item comment with ID supplied in path. Returns an empty body if successful.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_projects_project_id_task_item_comments_get200_response_inner import RestV10CompaniesCompanyIdProjectsProjectIdTaskItemCommentsGet200ResponseInner
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
    api_instance = procore_sdk.CoreTasksTaskItemCommentsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Task Item Comment ID

    try:
        # Delete a task item comment
        api_response = api_instance.rest_v10_companies_company_id_projects_project_id_task_item_comments_id_delete(procore_company_id, company_id, project_id, id)
        print("The response of CoreTasksTaskItemCommentsApi->rest_v10_companies_company_id_projects_project_id_task_item_comments_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreTasksTaskItemCommentsApi->rest_v10_companies_company_id_projects_project_id_task_item_comments_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Task Item Comment ID | 

### Return type

[**RestV10CompaniesCompanyIdProjectsProjectIdTaskItemCommentsGet200ResponseInner**](RestV10CompaniesCompanyIdProjectsProjectIdTaskItemCommentsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_projects_project_id_task_item_comments_id_patch**
> RestV10CompaniesCompanyIdProjectsProjectIdTaskItemCommentsGet200ResponseInner rest_v10_companies_company_id_projects_project_id_task_item_comments_id_patch(procore_company_id, company_id, project_id, id, rest_v10_companies_company_id_projects_project_id_task_item_comments_id_patch_request)

Update a task item comment

Updates the task item comment with ID supplied in path. Returns the updated comment.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_projects_project_id_task_item_comments_get200_response_inner import RestV10CompaniesCompanyIdProjectsProjectIdTaskItemCommentsGet200ResponseInner
from procore_sdk.models.rest_v10_companies_company_id_projects_project_id_task_item_comments_id_patch_request import RestV10CompaniesCompanyIdProjectsProjectIdTaskItemCommentsIdPatchRequest
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
    api_instance = procore_sdk.CoreTasksTaskItemCommentsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Task Item Comment ID
    rest_v10_companies_company_id_projects_project_id_task_item_comments_id_patch_request = procore_sdk.RestV10CompaniesCompanyIdProjectsProjectIdTaskItemCommentsIdPatchRequest() # RestV10CompaniesCompanyIdProjectsProjectIdTaskItemCommentsIdPatchRequest | 

    try:
        # Update a task item comment
        api_response = api_instance.rest_v10_companies_company_id_projects_project_id_task_item_comments_id_patch(procore_company_id, company_id, project_id, id, rest_v10_companies_company_id_projects_project_id_task_item_comments_id_patch_request)
        print("The response of CoreTasksTaskItemCommentsApi->rest_v10_companies_company_id_projects_project_id_task_item_comments_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreTasksTaskItemCommentsApi->rest_v10_companies_company_id_projects_project_id_task_item_comments_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Task Item Comment ID | 
 **rest_v10_companies_company_id_projects_project_id_task_item_comments_id_patch_request** | [**RestV10CompaniesCompanyIdProjectsProjectIdTaskItemCommentsIdPatchRequest**](RestV10CompaniesCompanyIdProjectsProjectIdTaskItemCommentsIdPatchRequest.md)|  | 

### Return type

[**RestV10CompaniesCompanyIdProjectsProjectIdTaskItemCommentsGet200ResponseInner**](RestV10CompaniesCompanyIdProjectsProjectIdTaskItemCommentsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_projects_project_id_task_item_comments_post**
> RestV10CompaniesCompanyIdProjectsProjectIdTaskItemCommentsGet200ResponseInner rest_v10_companies_company_id_projects_project_id_task_item_comments_post(procore_company_id, company_id, project_id, rest_v10_companies_company_id_projects_project_id_task_item_comments_post_request)

Create a task item comment

Create a new task item comment for a given task_item_id and created_by_id

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_projects_project_id_task_item_comments_get200_response_inner import RestV10CompaniesCompanyIdProjectsProjectIdTaskItemCommentsGet200ResponseInner
from procore_sdk.models.rest_v10_companies_company_id_projects_project_id_task_item_comments_post_request import RestV10CompaniesCompanyIdProjectsProjectIdTaskItemCommentsPostRequest
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
    api_instance = procore_sdk.CoreTasksTaskItemCommentsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_companies_company_id_projects_project_id_task_item_comments_post_request = procore_sdk.RestV10CompaniesCompanyIdProjectsProjectIdTaskItemCommentsPostRequest() # RestV10CompaniesCompanyIdProjectsProjectIdTaskItemCommentsPostRequest | 

    try:
        # Create a task item comment
        api_response = api_instance.rest_v10_companies_company_id_projects_project_id_task_item_comments_post(procore_company_id, company_id, project_id, rest_v10_companies_company_id_projects_project_id_task_item_comments_post_request)
        print("The response of CoreTasksTaskItemCommentsApi->rest_v10_companies_company_id_projects_project_id_task_item_comments_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreTasksTaskItemCommentsApi->rest_v10_companies_company_id_projects_project_id_task_item_comments_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_companies_company_id_projects_project_id_task_item_comments_post_request** | [**RestV10CompaniesCompanyIdProjectsProjectIdTaskItemCommentsPostRequest**](RestV10CompaniesCompanyIdProjectsProjectIdTaskItemCommentsPostRequest.md)|  | 

### Return type

[**RestV10CompaniesCompanyIdProjectsProjectIdTaskItemCommentsGet200ResponseInner**](RestV10CompaniesCompanyIdProjectsProjectIdTaskItemCommentsGet200ResponseInner.md)

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
**422** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

