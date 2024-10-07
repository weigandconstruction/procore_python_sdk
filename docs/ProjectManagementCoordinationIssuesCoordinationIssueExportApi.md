# procore_sdk.ProjectManagementCoordinationIssuesCoordinationIssueExportApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_coordination_issues_export_get**](ProjectManagementCoordinationIssuesCoordinationIssueExportApi.md#rest_v10_coordination_issues_export_get) | **GET** /rest/v1.0/coordination_issues/export | Download Coordination Issues


# **rest_v10_coordination_issues_export_get**
> str rest_v10_coordination_issues_export_get(procore_company_id, project_id, export_format, filters_assignee_company_id=filters_assignee_company_id, filters_assignee_id=filters_assignee_id, filters_ids=filters_ids, filters_location_id=filters_location_id, filters_search=filters_search, filters_coordination_issue_file_id=filters_coordination_issue_file_id, filters_status=filters_status, filters_updated_at=filters_updated_at, filters_issue_type=filters_issue_type, filters_priority=filters_priority, filters_trade_id=filters_trade_id, view=view, sort=sort)

Download Coordination Issues

Downloads coordination issues to a file specified by the export format. The items to be exported can be scoped by using filters. BCF export will only export the issues with a snapshot and valid camera data.

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
    api_instance = procore_sdk.ProjectManagementCoordinationIssuesCoordinationIssueExportApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    export_format = 'export_format_example' # str | Export File Format.
    filters_assignee_company_id = [56] # List[int] | Filter item(s) with matching assignee vendor companies. (optional)
    filters_assignee_id = [56] # List[int] | Filter item(s) with matching assignees. (optional)
    filters_ids = [56] # List[int] | Filter item(s) with matching ids. (optional)
    filters_location_id = [56] # List[int] | Filter item(s) with matching locations. (optional)
    filters_search = 'filters_search_example' # str | Filter item(s) with the matching search query. The search is performed on title and issue number. (optional)
    filters_coordination_issue_file_id = [56] # List[int] | Filter item(s) with the exact coordination issue file. (optional)
    filters_status = ['filters_status_example'] # List[str] | Filter item(s) with matching status. (optional)
    filters_updated_at = 'filters_updated_at_example' # str | Filter item(s) within a specific updated at iso8601 datetime range. (optional)
    filters_issue_type = ['filters_issue_type_example'] # List[str] | Filter item(s) with matching issue_type. (optional)
    filters_priority = ['filters_priority_example'] # List[str] | Filter item(s) with matching priority. (optional)
    filters_trade_id = [56] # List[int] | Filter item(s) with matching trades. (optional)
    view = 'view_example' # str | Export View. (optional)
    sort = 'sort_example' # str | Sort item(s) by an attribute. The default sort is ascending. To sort in descending order, prepend the sort value with a hyphen character '-' (optional)

    try:
        # Download Coordination Issues
        api_response = api_instance.rest_v10_coordination_issues_export_get(procore_company_id, project_id, export_format, filters_assignee_company_id=filters_assignee_company_id, filters_assignee_id=filters_assignee_id, filters_ids=filters_ids, filters_location_id=filters_location_id, filters_search=filters_search, filters_coordination_issue_file_id=filters_coordination_issue_file_id, filters_status=filters_status, filters_updated_at=filters_updated_at, filters_issue_type=filters_issue_type, filters_priority=filters_priority, filters_trade_id=filters_trade_id, view=view, sort=sort)
        print("The response of ProjectManagementCoordinationIssuesCoordinationIssueExportApi->rest_v10_coordination_issues_export_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementCoordinationIssuesCoordinationIssueExportApi->rest_v10_coordination_issues_export_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **export_format** | **str**| Export File Format. | 
 **filters_assignee_company_id** | [**List[int]**](int.md)| Filter item(s) with matching assignee vendor companies. | [optional] 
 **filters_assignee_id** | [**List[int]**](int.md)| Filter item(s) with matching assignees. | [optional] 
 **filters_ids** | [**List[int]**](int.md)| Filter item(s) with matching ids. | [optional] 
 **filters_location_id** | [**List[int]**](int.md)| Filter item(s) with matching locations. | [optional] 
 **filters_search** | **str**| Filter item(s) with the matching search query. The search is performed on title and issue number. | [optional] 
 **filters_coordination_issue_file_id** | [**List[int]**](int.md)| Filter item(s) with the exact coordination issue file. | [optional] 
 **filters_status** | [**List[str]**](str.md)| Filter item(s) with matching status. | [optional] 
 **filters_updated_at** | **str**| Filter item(s) within a specific updated at iso8601 datetime range. | [optional] 
 **filters_issue_type** | [**List[str]**](str.md)| Filter item(s) with matching issue_type. | [optional] 
 **filters_priority** | [**List[str]**](str.md)| Filter item(s) with matching priority. | [optional] 
 **filters_trade_id** | [**List[int]**](int.md)| Filter item(s) with matching trades. | [optional] 
 **view** | **str**| Export View. | [optional] 
 **sort** | **str**| Sort item(s) by an attribute. The default sort is ascending. To sort in descending order, prepend the sort value with a hyphen character &#39;-&#39; | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Coordination Issues CSV |  -  |
**202** | Accepted |  -  |
**403** | User does not have permission to export Coordination Issues |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

