# procore_sdk.ProjectManagementCoordinationIssuesCoordinationIssueActivitiesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_coordination_issue_activities_get**](ProjectManagementCoordinationIssuesCoordinationIssueActivitiesApi.md#rest_v10_coordination_issue_activities_get) | **GET** /rest/v1.0/coordination_issue_activities | List Coordination Issue Activities


# **rest_v10_coordination_issue_activities_get**
> List[RestV10CoordinationIssueActivitiesGet200ResponseInner] rest_v10_coordination_issue_activities_get(procore_company_id, project_id, page=page, per_page=per_page, filters_id=filters_id, filters_coordination_issue_id=filters_coordination_issue_id, view=view, filters_include_deleted=filters_include_deleted)

List Coordination Issue Activities

Lists activities in coordination issues associated with the specified project.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_coordination_issue_activities_get200_response_inner import RestV10CoordinationIssueActivitiesGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementCoordinationIssuesCoordinationIssueActivitiesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_coordination_issue_id = [56] # List[int] | Filter item(s) with coordination issues. (optional)
    view = 'view_example' # str | The compact view contains only ids. The extended view contains the response shown below. The normal view contains all attributes in extended view except activity_details. The default view is normal. (optional)
    filters_include_deleted = 'filters_include_deleted_example' # str | Use 'only' for only deleted resources. Use 'with' for deleted and undeleted resources. (optional)

    try:
        # List Coordination Issue Activities
        api_response = api_instance.rest_v10_coordination_issue_activities_get(procore_company_id, project_id, page=page, per_page=per_page, filters_id=filters_id, filters_coordination_issue_id=filters_coordination_issue_id, view=view, filters_include_deleted=filters_include_deleted)
        print("The response of ProjectManagementCoordinationIssuesCoordinationIssueActivitiesApi->rest_v10_coordination_issue_activities_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementCoordinationIssuesCoordinationIssueActivitiesApi->rest_v10_coordination_issue_activities_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_id** | [**List[int]**](int.md)| Return item(s) with the specified IDs. | [optional] 
 **filters_coordination_issue_id** | [**List[int]**](int.md)| Filter item(s) with coordination issues. | [optional] 
 **view** | **str**| The compact view contains only ids. The extended view contains the response shown below. The normal view contains all attributes in extended view except activity_details. The default view is normal. | [optional] 
 **filters_include_deleted** | **str**| Use &#39;only&#39; for only deleted resources. Use &#39;with&#39; for deleted and undeleted resources. | [optional] 

### Return type

[**List[RestV10CoordinationIssueActivitiesGet200ResponseInner]**](RestV10CoordinationIssueActivitiesGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Coordination Issue Activities listed successfully |  * Per-Page - Number of items retrieved per page <br>  * Total - Total number of items to be retrieved <br>  * Link - Link headers for the first, prev, next, and last link <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

