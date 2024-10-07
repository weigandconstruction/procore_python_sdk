# procore_sdk.ProjectManagementCoordinationIssuesCoordinationIssueProcoreItemAssociationsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_coordination_issues_coordination_issue_id_procore_item_associations_id_delete**](ProjectManagementCoordinationIssuesCoordinationIssueProcoreItemAssociationsApi.md#rest_v10_coordination_issues_coordination_issue_id_procore_item_associations_id_delete) | **DELETE** /rest/v1.0/coordination_issues/{coordination_issue_id}/procore_item_associations/{id} | Delete Procore Item Association
[**rest_v10_coordination_issues_coordination_issue_id_procore_item_associations_post**](ProjectManagementCoordinationIssuesCoordinationIssueProcoreItemAssociationsApi.md#rest_v10_coordination_issues_coordination_issue_id_procore_item_associations_post) | **POST** /rest/v1.0/coordination_issues/{coordination_issue_id}/procore_item_associations | Create Procore Item Association


# **rest_v10_coordination_issues_coordination_issue_id_procore_item_associations_id_delete**
> rest_v10_coordination_issues_coordination_issue_id_procore_item_associations_id_delete(procore_company_id, coordination_issue_id, id, project_id, item_type)

Delete Procore Item Association

Delete the association between Coordination Issue and Procore item

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
    api_instance = procore_sdk.ProjectManagementCoordinationIssuesCoordinationIssueProcoreItemAssociationsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    coordination_issue_id = 56 # int | Coordination Issue ID
    id = 56 # int | Procore Item Association ID
    project_id = 56 # int | Unique identifier for the project.
    item_type = 'item_type_example' # str | Type of Procore item

    try:
        # Delete Procore Item Association
        api_instance.rest_v10_coordination_issues_coordination_issue_id_procore_item_associations_id_delete(procore_company_id, coordination_issue_id, id, project_id, item_type)
    except Exception as e:
        print("Exception when calling ProjectManagementCoordinationIssuesCoordinationIssueProcoreItemAssociationsApi->rest_v10_coordination_issues_coordination_issue_id_procore_item_associations_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **coordination_issue_id** | **int**| Coordination Issue ID | 
 **id** | **int**| Procore Item Association ID | 
 **project_id** | **int**| Unique identifier for the project. | 
 **item_type** | **str**| Type of Procore item | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_coordination_issues_coordination_issue_id_procore_item_associations_post**
> RestV10CoordinationIssuesGet200ResponseInnerAllOfLinkedProcoreItemsInner rest_v10_coordination_issues_coordination_issue_id_procore_item_associations_post(procore_company_id, coordination_issue_id, body108)

Create Procore Item Association

CoordinationIssue can be associated with other procore items. This API endpoint creates that association. The extended view provides what is shown below. The normal view is the same as the extended view but excludes subject and title in item_data. The compact view returns coordination_issue_id, item_id, and item_type only. The default view is normal.

### Example


```python
import procore_sdk
from procore_sdk.models.body108 import Body108
from procore_sdk.models.rest_v10_coordination_issues_get200_response_inner_all_of_linked_procore_items_inner import RestV10CoordinationIssuesGet200ResponseInnerAllOfLinkedProcoreItemsInner
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
    api_instance = procore_sdk.ProjectManagementCoordinationIssuesCoordinationIssueProcoreItemAssociationsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    coordination_issue_id = 56 # int | Coordination Issue ID
    body108 = procore_sdk.Body108() # Body108 | 

    try:
        # Create Procore Item Association
        api_response = api_instance.rest_v10_coordination_issues_coordination_issue_id_procore_item_associations_post(procore_company_id, coordination_issue_id, body108)
        print("The response of ProjectManagementCoordinationIssuesCoordinationIssueProcoreItemAssociationsApi->rest_v10_coordination_issues_coordination_issue_id_procore_item_associations_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementCoordinationIssuesCoordinationIssueProcoreItemAssociationsApi->rest_v10_coordination_issues_coordination_issue_id_procore_item_associations_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **coordination_issue_id** | **int**| Coordination Issue ID | 
 **body108** | [**Body108**](Body108.md)|  | 

### Return type

[**RestV10CoordinationIssuesGet200ResponseInnerAllOfLinkedProcoreItemsInner**](RestV10CoordinationIssuesGet200ResponseInnerAllOfLinkedProcoreItemsInner.md)

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
**404** | Not Found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

