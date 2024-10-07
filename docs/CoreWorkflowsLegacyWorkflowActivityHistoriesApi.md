# procore_sdk.CoreWorkflowsLegacyWorkflowActivityHistoriesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_workflow_activity_histories_get**](CoreWorkflowsLegacyWorkflowActivityHistoriesApi.md#rest_v10_workflow_activity_histories_get) | **GET** /rest/v1.0/workflow_activity_histories | List Workflow Activity Histories
[**rest_v10_workflow_activity_histories_id_get**](CoreWorkflowsLegacyWorkflowActivityHistoriesApi.md#rest_v10_workflow_activity_histories_id_get) | **GET** /rest/v1.0/workflow_activity_histories/{id} | Show Workflow Activity History
[**rest_v10_workflow_activity_histories_post**](CoreWorkflowsLegacyWorkflowActivityHistoriesApi.md#rest_v10_workflow_activity_histories_post) | **POST** /rest/v1.0/workflow_activity_histories | Create Workflow Activity History


# **rest_v10_workflow_activity_histories_get**
> List[RestV10WorkflowActivityHistoriesGet200ResponseInner] rest_v10_workflow_activity_histories_get(procore_company_id, workflow_instance_id, company_id, page=page, per_page=per_page)

List Workflow Activity Histories

Return a list of activities performed for a workflow instance.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_workflow_activity_histories_get200_response_inner import RestV10WorkflowActivityHistoriesGet200ResponseInner
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
    api_instance = procore_sdk.CoreWorkflowsLegacyWorkflowActivityHistoriesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    workflow_instance_id = 56 # int | Workflow Instance ID
    company_id = 56 # int | Unique identifier for the company.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Workflow Activity Histories
        api_response = api_instance.rest_v10_workflow_activity_histories_get(procore_company_id, workflow_instance_id, company_id, page=page, per_page=per_page)
        print("The response of CoreWorkflowsLegacyWorkflowActivityHistoriesApi->rest_v10_workflow_activity_histories_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreWorkflowsLegacyWorkflowActivityHistoriesApi->rest_v10_workflow_activity_histories_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **workflow_instance_id** | **int**| Workflow Instance ID | 
 **company_id** | **int**| Unique identifier for the company. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[RestV10WorkflowActivityHistoriesGet200ResponseInner]**](RestV10WorkflowActivityHistoriesGet200ResponseInner.md)

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
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_workflow_activity_histories_id_get**
> RestV10WorkflowActivityHistoriesGet200ResponseInner rest_v10_workflow_activity_histories_id_get(procore_company_id, id, workflow_instance_id, company_id)

Show Workflow Activity History

Get information about a Workflow Activity History

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_workflow_activity_histories_get200_response_inner import RestV10WorkflowActivityHistoriesGet200ResponseInner
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
    api_instance = procore_sdk.CoreWorkflowsLegacyWorkflowActivityHistoriesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID
    workflow_instance_id = 56 # int | Workflow Instance ID
    company_id = 56 # int | Unique identifier for the company.

    try:
        # Show Workflow Activity History
        api_response = api_instance.rest_v10_workflow_activity_histories_id_get(procore_company_id, id, workflow_instance_id, company_id)
        print("The response of CoreWorkflowsLegacyWorkflowActivityHistoriesApi->rest_v10_workflow_activity_histories_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreWorkflowsLegacyWorkflowActivityHistoriesApi->rest_v10_workflow_activity_histories_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID | 
 **workflow_instance_id** | **int**| Workflow Instance ID | 
 **company_id** | **int**| Unique identifier for the company. | 

### Return type

[**RestV10WorkflowActivityHistoriesGet200ResponseInner**](RestV10WorkflowActivityHistoriesGet200ResponseInner.md)

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

# **rest_v10_workflow_activity_histories_post**
> RestV10WorkflowActivityHistoriesGet200ResponseInner rest_v10_workflow_activity_histories_post(procore_company_id, workflow_instance_id, company_id, rest_v10_workflow_activity_histories_post_request)

Create Workflow Activity History

Perform a workflow activity. Workflows Instances transition between states when all required activities have been performed.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_workflow_activity_histories_get200_response_inner import RestV10WorkflowActivityHistoriesGet200ResponseInner
from procore_sdk.models.rest_v10_workflow_activity_histories_post_request import RestV10WorkflowActivityHistoriesPostRequest
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
    api_instance = procore_sdk.CoreWorkflowsLegacyWorkflowActivityHistoriesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    workflow_instance_id = 56 # int | Workflow Instance ID
    company_id = 56 # int | Unique identifier for the company.
    rest_v10_workflow_activity_histories_post_request = procore_sdk.RestV10WorkflowActivityHistoriesPostRequest() # RestV10WorkflowActivityHistoriesPostRequest | 

    try:
        # Create Workflow Activity History
        api_response = api_instance.rest_v10_workflow_activity_histories_post(procore_company_id, workflow_instance_id, company_id, rest_v10_workflow_activity_histories_post_request)
        print("The response of CoreWorkflowsLegacyWorkflowActivityHistoriesApi->rest_v10_workflow_activity_histories_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreWorkflowsLegacyWorkflowActivityHistoriesApi->rest_v10_workflow_activity_histories_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **workflow_instance_id** | **int**| Workflow Instance ID | 
 **company_id** | **int**| Unique identifier for the company. | 
 **rest_v10_workflow_activity_histories_post_request** | [**RestV10WorkflowActivityHistoriesPostRequest**](RestV10WorkflowActivityHistoriesPostRequest.md)|  | 

### Return type

[**RestV10WorkflowActivityHistoriesGet200ResponseInner**](RestV10WorkflowActivityHistoriesGet200ResponseInner.md)

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

