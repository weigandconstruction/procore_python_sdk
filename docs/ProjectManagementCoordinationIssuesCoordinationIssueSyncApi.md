# procore_sdk.ProjectManagementCoordinationIssuesCoordinationIssueSyncApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_coordination_issues_bulk_delete_post**](ProjectManagementCoordinationIssuesCoordinationIssueSyncApi.md#rest_v10_coordination_issues_bulk_delete_post) | **POST** /rest/v1.0/coordination_issues/bulk_delete | Delete Bulk Coordination Issues
[**rest_v10_coordination_issues_sync_patch**](ProjectManagementCoordinationIssuesCoordinationIssueSyncApi.md#rest_v10_coordination_issues_sync_patch) | **PATCH** /rest/v1.0/coordination_issues/sync | Create and Update Bulk Coordination Issues


# **rest_v10_coordination_issues_bulk_delete_post**
> CoordinationIssueSyncResponse1 rest_v10_coordination_issues_bulk_delete_post(procore_company_id, body107)

Delete Bulk Coordination Issues

This endpoint is used to delete a batch of CoordinationIssues.

### Example


```python
import procore_sdk
from procore_sdk.models.body107 import Body107
from procore_sdk.models.coordination_issue_sync_response1 import CoordinationIssueSyncResponse1
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
    api_instance = procore_sdk.ProjectManagementCoordinationIssuesCoordinationIssueSyncApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    body107 = procore_sdk.Body107() # Body107 | 

    try:
        # Delete Bulk Coordination Issues
        api_response = api_instance.rest_v10_coordination_issues_bulk_delete_post(procore_company_id, body107)
        print("The response of ProjectManagementCoordinationIssuesCoordinationIssueSyncApi->rest_v10_coordination_issues_bulk_delete_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementCoordinationIssuesCoordinationIssueSyncApi->rest_v10_coordination_issues_bulk_delete_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **body107** | [**Body107**](Body107.md)|  | 

### Return type

[**CoordinationIssueSyncResponse1**](CoordinationIssueSyncResponse1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_coordination_issues_sync_patch**
> CoordinationIssueSyncResponse rest_v10_coordination_issues_sync_patch(procore_company_id, body106)

Create and Update Bulk Coordination Issues

This endpoint is used to create and update a batch of CoordinationIssues. See [Using Sync Actions](/documentation/using-sync-actions) for additional information.  If an 'id' attribute is present in any payload item, that item is processed for 'update'. Only title, description, due_date, location_id, assignee_id, issue_type, priority, and trade_id can be updated using this endpoint.

### Example


```python
import procore_sdk
from procore_sdk.models.body106 import Body106
from procore_sdk.models.coordination_issue_sync_response import CoordinationIssueSyncResponse
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
    api_instance = procore_sdk.ProjectManagementCoordinationIssuesCoordinationIssueSyncApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    body106 = procore_sdk.Body106() # Body106 | 

    try:
        # Create and Update Bulk Coordination Issues
        api_response = api_instance.rest_v10_coordination_issues_sync_patch(procore_company_id, body106)
        print("The response of ProjectManagementCoordinationIssuesCoordinationIssueSyncApi->rest_v10_coordination_issues_sync_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementCoordinationIssuesCoordinationIssueSyncApi->rest_v10_coordination_issues_sync_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **body106** | [**Body106**](Body106.md)|  | 

### Return type

[**CoordinationIssueSyncResponse**](CoordinationIssueSyncResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

