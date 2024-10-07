# procore_sdk.ProjectManagementCoordinationIssuesCoordinationIssueStatusChangesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_coordination_issues_id_status_changes_get**](ProjectManagementCoordinationIssuesCoordinationIssueStatusChangesApi.md#rest_v10_coordination_issues_id_status_changes_get) | **GET** /rest/v1.0/coordination_issues/{id}/status_changes | List status change history for a Coordination Issue


# **rest_v10_coordination_issues_id_status_changes_get**
> List[RestV10CoordinationIssuesIdStatusChangesGet200ResponseInner] rest_v10_coordination_issues_id_status_changes_get(procore_company_id, id, project_id, view=view, page=page, per_page=per_page)

List status change history for a Coordination Issue

This endpoint returns the status change history for the specified CoordinationIssue. The status change history is sorted by most recent first.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_coordination_issues_id_status_changes_get200_response_inner import RestV10CoordinationIssuesIdStatusChangesGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementCoordinationIssuesCoordinationIssueStatusChangesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | Coordination Issue ID
    project_id = 56 # int | Unique identifier for the project.
    view = 'view_example' # str | The extended view provides what is shown below. The normal view is the same as the extended view but excludes attribute created_by, linked_rfi and linked_observation_item. The compact view returns ids only. The default view is normal. Both linked_rfi or linked_observation_item can be empty objects, or at most one of them is populated. (optional)
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List status change history for a Coordination Issue
        api_response = api_instance.rest_v10_coordination_issues_id_status_changes_get(procore_company_id, id, project_id, view=view, page=page, per_page=per_page)
        print("The response of ProjectManagementCoordinationIssuesCoordinationIssueStatusChangesApi->rest_v10_coordination_issues_id_status_changes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementCoordinationIssuesCoordinationIssueStatusChangesApi->rest_v10_coordination_issues_id_status_changes_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| Coordination Issue ID | 
 **project_id** | **int**| Unique identifier for the project. | 
 **view** | **str**| The extended view provides what is shown below. The normal view is the same as the extended view but excludes attribute created_by, linked_rfi and linked_observation_item. The compact view returns ids only. The default view is normal. Both linked_rfi or linked_observation_item can be empty objects, or at most one of them is populated. | [optional] 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[RestV10CoordinationIssuesIdStatusChangesGet200ResponseInner]**](RestV10CoordinationIssuesIdStatusChangesGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Per-Page - Number of items retrieved per page <br>  * Total - Total number of items to be retrieved <br>  * Link - Link headers for the first, prev, next, and last link <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

