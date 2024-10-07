# procore_sdk.CoreWorkflowsLegacyWorkflowInstancesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_workflow_instances_get**](CoreWorkflowsLegacyWorkflowInstancesApi.md#rest_v10_workflow_instances_get) | **GET** /rest/v1.0/workflow_instances | List Workflow Instances
[**rest_v10_workflow_instances_id_get**](CoreWorkflowsLegacyWorkflowInstancesApi.md#rest_v10_workflow_instances_id_get) | **GET** /rest/v1.0/workflow_instances/{id} | Show Workflow Instance


# **rest_v10_workflow_instances_get**
> List[RestV10WorkflowInstancesGet200ResponseInner] rest_v10_workflow_instances_get(procore_company_id, company_id, filters_workflowed_object_id=filters_workflowed_object_id, filters_workflowed_object_type=filters_workflowed_object_type, page=page, per_page=per_page)

List Workflow Instances

Return a list of workflow instances for a workflow. Any resource using workflow should have a workflow instance.  See [Filtering on List Actions](https://developers.procore.com/documentation/filtering-on-list-actions) for information on using the filtering capabilities provided by this endpoint.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_workflow_instances_get200_response_inner import RestV10WorkflowInstancesGet200ResponseInner
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
    api_instance = procore_sdk.CoreWorkflowsLegacyWorkflowInstancesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    filters_workflowed_object_id = 56 # int | Return items for a specific workflow object. (optional)
    filters_workflowed_object_type = 'filters_workflowed_object_type_example' # str | Return items for a specific workflow object type. (optional)
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Workflow Instances
        api_response = api_instance.rest_v10_workflow_instances_get(procore_company_id, company_id, filters_workflowed_object_id=filters_workflowed_object_id, filters_workflowed_object_type=filters_workflowed_object_type, page=page, per_page=per_page)
        print("The response of CoreWorkflowsLegacyWorkflowInstancesApi->rest_v10_workflow_instances_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreWorkflowsLegacyWorkflowInstancesApi->rest_v10_workflow_instances_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **filters_workflowed_object_id** | **int**| Return items for a specific workflow object. | [optional] 
 **filters_workflowed_object_type** | **str**| Return items for a specific workflow object type. | [optional] 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[RestV10WorkflowInstancesGet200ResponseInner]**](RestV10WorkflowInstancesGet200ResponseInner.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_workflow_instances_id_get**
> RestV10WorkflowInstancesGet200ResponseInner rest_v10_workflow_instances_id_get(procore_company_id, company_id, id)

Show Workflow Instance

Get information about a Workflow Instance

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_workflow_instances_get200_response_inner import RestV10WorkflowInstancesGet200ResponseInner
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
    api_instance = procore_sdk.CoreWorkflowsLegacyWorkflowInstancesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | ID

    try:
        # Show Workflow Instance
        api_response = api_instance.rest_v10_workflow_instances_id_get(procore_company_id, company_id, id)
        print("The response of CoreWorkflowsLegacyWorkflowInstancesApi->rest_v10_workflow_instances_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreWorkflowsLegacyWorkflowInstancesApi->rest_v10_workflow_instances_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| ID | 

### Return type

[**RestV10WorkflowInstancesGet200ResponseInner**](RestV10WorkflowInstancesGet200ResponseInner.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

