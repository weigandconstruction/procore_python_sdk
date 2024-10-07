# procore_sdk.ProjectManagementCoordinationIssuesCoordinationIssueAssignmentApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_coordination_issues_coordination_issue_id_assignments_post**](ProjectManagementCoordinationIssuesCoordinationIssueAssignmentApi.md#rest_v10_coordination_issues_coordination_issue_id_assignments_post) | **POST** /rest/v1.0/coordination_issues/{coordination_issue_id}/assignments | Create Coordination Issue Assignment


# **rest_v10_coordination_issues_coordination_issue_id_assignments_post**
> RestV10CoordinationIssuesCoordinationIssueIdAssignmentsPost201Response rest_v10_coordination_issues_coordination_issue_id_assignments_post(procore_company_id, coordination_issue_id, rest_v10_coordination_issues_coordination_issue_id_assignments_post_request)

Create Coordination Issue Assignment

Create a Coordination Issue Assignment, which executes a series of actions that updates coordination issue assignee_id and creates an instance of CoordinationIssueActivity.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_coordination_issues_coordination_issue_id_assignments_post201_response import RestV10CoordinationIssuesCoordinationIssueIdAssignmentsPost201Response
from procore_sdk.models.rest_v10_coordination_issues_coordination_issue_id_assignments_post_request import RestV10CoordinationIssuesCoordinationIssueIdAssignmentsPostRequest
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
    api_instance = procore_sdk.ProjectManagementCoordinationIssuesCoordinationIssueAssignmentApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    coordination_issue_id = 56 # int | Coordination Issue ID
    rest_v10_coordination_issues_coordination_issue_id_assignments_post_request = procore_sdk.RestV10CoordinationIssuesCoordinationIssueIdAssignmentsPostRequest() # RestV10CoordinationIssuesCoordinationIssueIdAssignmentsPostRequest | 

    try:
        # Create Coordination Issue Assignment
        api_response = api_instance.rest_v10_coordination_issues_coordination_issue_id_assignments_post(procore_company_id, coordination_issue_id, rest_v10_coordination_issues_coordination_issue_id_assignments_post_request)
        print("The response of ProjectManagementCoordinationIssuesCoordinationIssueAssignmentApi->rest_v10_coordination_issues_coordination_issue_id_assignments_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementCoordinationIssuesCoordinationIssueAssignmentApi->rest_v10_coordination_issues_coordination_issue_id_assignments_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **coordination_issue_id** | **int**| Coordination Issue ID | 
 **rest_v10_coordination_issues_coordination_issue_id_assignments_post_request** | [**RestV10CoordinationIssuesCoordinationIssueIdAssignmentsPostRequest**](RestV10CoordinationIssuesCoordinationIssueIdAssignmentsPostRequest.md)|  | 

### Return type

[**RestV10CoordinationIssuesCoordinationIssueIdAssignmentsPost201Response**](RestV10CoordinationIssuesCoordinationIssueIdAssignmentsPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

