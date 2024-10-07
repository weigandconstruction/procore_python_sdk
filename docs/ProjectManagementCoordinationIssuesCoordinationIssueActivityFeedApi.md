# procore_sdk.ProjectManagementCoordinationIssuesCoordinationIssueActivityFeedApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_coordination_issue_activities_feed_get**](ProjectManagementCoordinationIssuesCoordinationIssueActivityFeedApi.md#rest_v10_coordination_issue_activities_feed_get) | **GET** /rest/v1.0/coordination_issue_activities/feed | List Coordination Issue Activity Feed Items


# **rest_v10_coordination_issue_activities_feed_get**
> List[RestV10CoordinationIssueActivitiesFeedGet200ResponseInner] rest_v10_coordination_issue_activities_feed_get(procore_company_id, project_id, page=page, per_page=per_page, filters_id=filters_id, filters_coordination_issue_id=filters_coordination_issue_id, filters_include_deleted=filters_include_deleted)

List Coordination Issue Activity Feed Items

Lists activity feed item in coordination issues associated with the specified project.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_coordination_issue_activities_feed_get200_response_inner import RestV10CoordinationIssueActivitiesFeedGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementCoordinationIssuesCoordinationIssueActivityFeedApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_coordination_issue_id = [56] # List[int] | Filter item(s) with coordination issues. (optional)
    filters_include_deleted = 'filters_include_deleted_example' # str | Use 'only' for only deleted resources. Use 'with' for deleted and undeleted resources. (optional)

    try:
        # List Coordination Issue Activity Feed Items
        api_response = api_instance.rest_v10_coordination_issue_activities_feed_get(procore_company_id, project_id, page=page, per_page=per_page, filters_id=filters_id, filters_coordination_issue_id=filters_coordination_issue_id, filters_include_deleted=filters_include_deleted)
        print("The response of ProjectManagementCoordinationIssuesCoordinationIssueActivityFeedApi->rest_v10_coordination_issue_activities_feed_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementCoordinationIssuesCoordinationIssueActivityFeedApi->rest_v10_coordination_issue_activities_feed_get: %s\n" % e)
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
 **filters_include_deleted** | **str**| Use &#39;only&#39; for only deleted resources. Use &#39;with&#39; for deleted and undeleted resources. | [optional] 

### Return type

[**List[RestV10CoordinationIssueActivitiesFeedGet200ResponseInner]**](RestV10CoordinationIssueActivitiesFeedGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Coordination Issue Activity Feed items listed successfully |  * Per-Page - Number of items retrieved per page <br>  * Total - Total number of items to be retrieved <br>  * Link - Link headers for the first, prev, next, and last link <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

