# procore_sdk.ProjectManagementCoordinationIssuesCoordinationIssueStatusTotalsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_coordination_issues_status_total_get**](ProjectManagementCoordinationIssuesCoordinationIssueStatusTotalsApi.md#rest_v10_coordination_issues_status_total_get) | **GET** /rest/v1.0/coordination_issues/status_total | Show Coordination Issue Count by Status


# **rest_v10_coordination_issues_status_total_get**
> RestV10CoordinationIssuesStatusTotalGet200Response rest_v10_coordination_issues_status_total_get(procore_company_id, project_id)

Show Coordination Issue Count by Status

This endpoint returns the status counts for Coordination Issues in a project. The counts provide information about how the issues are distributed by location and assignee company.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_coordination_issues_status_total_get200_response import RestV10CoordinationIssuesStatusTotalGet200Response
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
    api_instance = procore_sdk.ProjectManagementCoordinationIssuesCoordinationIssueStatusTotalsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Show Coordination Issue Count by Status
        api_response = api_instance.rest_v10_coordination_issues_status_total_get(procore_company_id, project_id)
        print("The response of ProjectManagementCoordinationIssuesCoordinationIssueStatusTotalsApi->rest_v10_coordination_issues_status_total_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementCoordinationIssuesCoordinationIssueStatusTotalsApi->rest_v10_coordination_issues_status_total_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**RestV10CoordinationIssuesStatusTotalGet200Response**](RestV10CoordinationIssuesStatusTotalGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

