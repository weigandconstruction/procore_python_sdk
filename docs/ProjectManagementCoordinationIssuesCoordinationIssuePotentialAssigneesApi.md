# procore_sdk.ProjectManagementCoordinationIssuesCoordinationIssuePotentialAssigneesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_coordination_issues_assignees_get**](ProjectManagementCoordinationIssuesCoordinationIssuePotentialAssigneesApi.md#rest_v10_coordination_issues_assignees_get) | **GET** /rest/v1.0/coordination_issues/assignees | List Coordination Issue Assignable Users


# **rest_v10_coordination_issues_assignees_get**
> List[RestV10CoordinationIssuesGet200ResponseInnerAllOfAssignee] rest_v10_coordination_issues_assignees_get(procore_company_id, project_id, page=page, per_page=per_page)

List Coordination Issue Assignable Users

Lists potential assignees for Coordination Issues. Users who are admin or standard users can be assigned to a Coordination Issue

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_coordination_issues_get200_response_inner_all_of_assignee import RestV10CoordinationIssuesGet200ResponseInnerAllOfAssignee
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
    api_instance = procore_sdk.ProjectManagementCoordinationIssuesCoordinationIssuePotentialAssigneesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Coordination Issue Assignable Users
        api_response = api_instance.rest_v10_coordination_issues_assignees_get(procore_company_id, project_id, page=page, per_page=per_page)
        print("The response of ProjectManagementCoordinationIssuesCoordinationIssuePotentialAssigneesApi->rest_v10_coordination_issues_assignees_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementCoordinationIssuesCoordinationIssuePotentialAssigneesApi->rest_v10_coordination_issues_assignees_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[RestV10CoordinationIssuesGet200ResponseInnerAllOfAssignee]**](RestV10CoordinationIssuesGet200ResponseInnerAllOfAssignee.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Coordination Issue assignees listed successfully |  * Per-Page - Number of items retrieved per page <br>  * Total - Total number of items to be retrieved <br>  * Link - Link headers for the first, prev, next, and last link <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | User does not have permission to view Coordination Issue assignees |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

