# procore_sdk.ProjectManagementCoordinationIssuesCoordinationIssueRecycleBinApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_coordination_issues_recycle_bin_get**](ProjectManagementCoordinationIssuesCoordinationIssueRecycleBinApi.md#rest_v10_coordination_issues_recycle_bin_get) | **GET** /rest/v1.0/coordination_issues/recycle_bin | List Coordination Issues in Recycle Bin
[**rest_v10_coordination_issues_recycle_bin_id_get**](ProjectManagementCoordinationIssuesCoordinationIssueRecycleBinApi.md#rest_v10_coordination_issues_recycle_bin_id_get) | **GET** /rest/v1.0/coordination_issues/recycle_bin/{id} | Show Coordination Issue in Recycle Bin
[**rest_v10_coordination_issues_recycle_bin_id_patch**](ProjectManagementCoordinationIssuesCoordinationIssueRecycleBinApi.md#rest_v10_coordination_issues_recycle_bin_id_patch) | **PATCH** /rest/v1.0/coordination_issues/recycle_bin/{id} | Restore Coordination Issue from Recycle Bin


# **rest_v10_coordination_issues_recycle_bin_get**
> List[RestV10CoordinationIssuesGet200ResponseInner] rest_v10_coordination_issues_recycle_bin_get(procore_company_id, project_id, page=page, per_page=per_page, filters_assignee_company_id=filters_assignee_company_id, filters_assignee_id=filters_assignee_id, filters_ids=filters_ids, filters_location_id=filters_location_id, filters_include_sublocations=filters_include_sublocations, filters_search=filters_search, filters_coordination_issue_file_id=filters_coordination_issue_file_id, filters_status=filters_status, filters_updated_at=filters_updated_at, filters_due_date=filters_due_date, filters_created_at=filters_created_at, sort=sort, view=view)

List Coordination Issues in Recycle Bin

Lists all deleted Coordination Issues in the specified project

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_coordination_issues_get200_response_inner import RestV10CoordinationIssuesGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementCoordinationIssuesCoordinationIssueRecycleBinApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_assignee_company_id = [56] # List[int] | Filter item(s) with matching assignee vendor companies. (optional)
    filters_assignee_id = [56] # List[int] | Filter item(s) with matching assignees. (optional)
    filters_ids = [56] # List[int] | Filter item(s) with matching ids. (optional)
    filters_location_id = [56] # List[int] | Filter item(s) with matching locations. (optional)
    filters_include_sublocations = False # bool | Use together with `filters[location_id]`  (optional) (default to False)
    filters_search = 'filters_search_example' # str | Filter item(s) with the matching search query. The search is performed on title and issue number. (optional)
    filters_coordination_issue_file_id = [56] # List[int] | Filter item(s) with the exact coordination issue file. (optional)
    filters_status = ['filters_status_example'] # List[str] | Filter item(s) with matching status. (optional)
    filters_updated_at = 'filters_updated_at_example' # str | Filter item(s) within a specific updated at iso8601 datetime range. (optional)
    filters_due_date = 'filters_due_date_example' # str | Filter item(s) within a specific due date iso8601 date range. (optional)
    filters_created_at = 'filters_created_at_example' # str | Filter item(s) within a specific created at iso8601 datetime range. (optional)
    sort = 'sort_example' # str | Sort item(s) by an attribute. The default sort is ascending. To sort in descending order, prepend the sort value with a hyphen character '-' (optional)
    view = 'view_example' # str | The compact view contains only ids. The normal view is a subset of the response shown below, and does not include attachments, viewpoints, linked items and updated_by The extended view contains the response shown below. The default view is normal. (optional)

    try:
        # List Coordination Issues in Recycle Bin
        api_response = api_instance.rest_v10_coordination_issues_recycle_bin_get(procore_company_id, project_id, page=page, per_page=per_page, filters_assignee_company_id=filters_assignee_company_id, filters_assignee_id=filters_assignee_id, filters_ids=filters_ids, filters_location_id=filters_location_id, filters_include_sublocations=filters_include_sublocations, filters_search=filters_search, filters_coordination_issue_file_id=filters_coordination_issue_file_id, filters_status=filters_status, filters_updated_at=filters_updated_at, filters_due_date=filters_due_date, filters_created_at=filters_created_at, sort=sort, view=view)
        print("The response of ProjectManagementCoordinationIssuesCoordinationIssueRecycleBinApi->rest_v10_coordination_issues_recycle_bin_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementCoordinationIssuesCoordinationIssueRecycleBinApi->rest_v10_coordination_issues_recycle_bin_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_assignee_company_id** | [**List[int]**](int.md)| Filter item(s) with matching assignee vendor companies. | [optional] 
 **filters_assignee_id** | [**List[int]**](int.md)| Filter item(s) with matching assignees. | [optional] 
 **filters_ids** | [**List[int]**](int.md)| Filter item(s) with matching ids. | [optional] 
 **filters_location_id** | [**List[int]**](int.md)| Filter item(s) with matching locations. | [optional] 
 **filters_include_sublocations** | **bool**| Use together with &#x60;filters[location_id]&#x60;  | [optional] [default to False]
 **filters_search** | **str**| Filter item(s) with the matching search query. The search is performed on title and issue number. | [optional] 
 **filters_coordination_issue_file_id** | [**List[int]**](int.md)| Filter item(s) with the exact coordination issue file. | [optional] 
 **filters_status** | [**List[str]**](str.md)| Filter item(s) with matching status. | [optional] 
 **filters_updated_at** | **str**| Filter item(s) within a specific updated at iso8601 datetime range. | [optional] 
 **filters_due_date** | **str**| Filter item(s) within a specific due date iso8601 date range. | [optional] 
 **filters_created_at** | **str**| Filter item(s) within a specific created at iso8601 datetime range. | [optional] 
 **sort** | **str**| Sort item(s) by an attribute. The default sort is ascending. To sort in descending order, prepend the sort value with a hyphen character &#39;-&#39; | [optional] 
 **view** | **str**| The compact view contains only ids. The normal view is a subset of the response shown below, and does not include attachments, viewpoints, linked items and updated_by The extended view contains the response shown below. The default view is normal. | [optional] 

### Return type

[**List[RestV10CoordinationIssuesGet200ResponseInner]**](RestV10CoordinationIssuesGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Coordination Issues listed successfully |  * Per-Page - Number of items retrieved per page <br>  * Total - Total number of items to be retrieved <br>  * Link - Link headers for the first, prev, next, and last link <br>  |
**403** | User does not have permission to view Coordination Issues |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_coordination_issues_recycle_bin_id_get**
> RestV10CoordinationIssuesGet200ResponseInner rest_v10_coordination_issues_recycle_bin_id_get(procore_company_id, id, project_id, view=view)

Show Coordination Issue in Recycle Bin

Return a single Coordination Issue item in Recycle Bin.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_coordination_issues_get200_response_inner import RestV10CoordinationIssuesGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementCoordinationIssuesCoordinationIssueRecycleBinApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | Coordination Issue ID
    project_id = 56 # int | Unique identifier for the project.
    view = 'view_example' # str | The compact view contains only ids. The normal view is a subset of the response shown below, and does not include attachments, viewpoints, linked items and updated_by The extended view contains the response shown below. The default view is normal. (optional)

    try:
        # Show Coordination Issue in Recycle Bin
        api_response = api_instance.rest_v10_coordination_issues_recycle_bin_id_get(procore_company_id, id, project_id, view=view)
        print("The response of ProjectManagementCoordinationIssuesCoordinationIssueRecycleBinApi->rest_v10_coordination_issues_recycle_bin_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementCoordinationIssuesCoordinationIssueRecycleBinApi->rest_v10_coordination_issues_recycle_bin_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| Coordination Issue ID | 
 **project_id** | **int**| Unique identifier for the project. | 
 **view** | **str**| The compact view contains only ids. The normal view is a subset of the response shown below, and does not include attachments, viewpoints, linked items and updated_by The extended view contains the response shown below. The default view is normal. | [optional] 

### Return type

[**RestV10CoordinationIssuesGet200ResponseInner**](RestV10CoordinationIssuesGet200ResponseInner.md)

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

# **rest_v10_coordination_issues_recycle_bin_id_patch**
> rest_v10_coordination_issues_recycle_bin_id_patch(procore_company_id, id, rest_v10_coordination_issues_recycle_bin_id_patch_request)

Restore Coordination Issue from Recycle Bin

Restore Coordination Issue from Recycle Bin

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_coordination_issues_recycle_bin_id_patch_request import RestV10CoordinationIssuesRecycleBinIdPatchRequest
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
    api_instance = procore_sdk.ProjectManagementCoordinationIssuesCoordinationIssueRecycleBinApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | Coordination Issue ID
    rest_v10_coordination_issues_recycle_bin_id_patch_request = procore_sdk.RestV10CoordinationIssuesRecycleBinIdPatchRequest() # RestV10CoordinationIssuesRecycleBinIdPatchRequest | 

    try:
        # Restore Coordination Issue from Recycle Bin
        api_instance.rest_v10_coordination_issues_recycle_bin_id_patch(procore_company_id, id, rest_v10_coordination_issues_recycle_bin_id_patch_request)
    except Exception as e:
        print("Exception when calling ProjectManagementCoordinationIssuesCoordinationIssueRecycleBinApi->rest_v10_coordination_issues_recycle_bin_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| Coordination Issue ID | 
 **rest_v10_coordination_issues_recycle_bin_id_patch_request** | [**RestV10CoordinationIssuesRecycleBinIdPatchRequest**](RestV10CoordinationIssuesRecycleBinIdPatchRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

