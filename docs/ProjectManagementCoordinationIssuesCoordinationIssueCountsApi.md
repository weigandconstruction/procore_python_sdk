# procore_sdk.ProjectManagementCoordinationIssuesCoordinationIssueCountsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_coordination_issues_status_count_get**](ProjectManagementCoordinationIssuesCoordinationIssueCountsApi.md#rest_v10_coordination_issues_status_count_get) | **GET** /rest/v1.0/coordination_issues/status_count | List Grouped Coordination Issue Status Count


# **rest_v10_coordination_issues_status_count_get**
> List[RestV10CoordinationIssuesStatusCountGet200ResponseInner] rest_v10_coordination_issues_status_count_get(procore_company_id, project_id, filters_group_by=filters_group_by, page=page, per_page=per_page)

List Grouped Coordination Issue Status Count

This endpoint returns the status counts for Coordination Issues in a project. The counts provide information about how the issues are distributed by location and assignee company.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_coordination_issues_status_count_get200_response_inner import RestV10CoordinationIssuesStatusCountGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementCoordinationIssuesCoordinationIssueCountsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    filters_group_by = 'filters_group_by_example' # str | Filter status counts by group_by attribute. (optional)
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Grouped Coordination Issue Status Count
        api_response = api_instance.rest_v10_coordination_issues_status_count_get(procore_company_id, project_id, filters_group_by=filters_group_by, page=page, per_page=per_page)
        print("The response of ProjectManagementCoordinationIssuesCoordinationIssueCountsApi->rest_v10_coordination_issues_status_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementCoordinationIssuesCoordinationIssueCountsApi->rest_v10_coordination_issues_status_count_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **filters_group_by** | **str**| Filter status counts by group_by attribute. | [optional] 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[RestV10CoordinationIssuesStatusCountGet200ResponseInner]**](RestV10CoordinationIssuesStatusCountGet200ResponseInner.md)

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

