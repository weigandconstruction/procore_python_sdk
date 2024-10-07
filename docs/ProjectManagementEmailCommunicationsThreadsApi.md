# procore_sdk.ProjectManagementEmailCommunicationsThreadsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_communications_communication_id_threads_get**](ProjectManagementEmailCommunicationsThreadsApi.md#rest_v10_communications_communication_id_threads_get) | **GET** /rest/v1.0/communications/{communication_id}/threads | List Communication Threads
[**rest_v10_communications_communication_id_threads_id_get**](ProjectManagementEmailCommunicationsThreadsApi.md#rest_v10_communications_communication_id_threads_id_get) | **GET** /rest/v1.0/communications/{communication_id}/threads/{id} | Show Communication Thread


# **rest_v10_communications_communication_id_threads_get**
> RestV10CommunicationsCommunicationIdThreadsGet200Response rest_v10_communications_communication_id_threads_get(procore_company_id, project_id, communication_id)

List Communication Threads

Return a list of email communication threads.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_communications_communication_id_threads_get200_response import RestV10CommunicationsCommunicationIdThreadsGet200Response
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
    api_instance = procore_sdk.ProjectManagementEmailCommunicationsThreadsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    communication_id = 56 # int | Communication ID

    try:
        # List Communication Threads
        api_response = api_instance.rest_v10_communications_communication_id_threads_get(procore_company_id, project_id, communication_id)
        print("The response of ProjectManagementEmailCommunicationsThreadsApi->rest_v10_communications_communication_id_threads_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementEmailCommunicationsThreadsApi->rest_v10_communications_communication_id_threads_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **communication_id** | **int**| Communication ID | 

### Return type

[**RestV10CommunicationsCommunicationIdThreadsGet200Response**](RestV10CommunicationsCommunicationIdThreadsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_communications_communication_id_threads_id_get**
> RestV10CommunicationsCommunicationIdThreadsIdGet200Response rest_v10_communications_communication_id_threads_id_get(procore_company_id, project_id, communication_id, id)

Show Communication Thread

Shows detailed information for a specific email communication thread

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_communications_communication_id_threads_id_get200_response import RestV10CommunicationsCommunicationIdThreadsIdGet200Response
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
    api_instance = procore_sdk.ProjectManagementEmailCommunicationsThreadsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    communication_id = 56 # int | Communication ID
    id = 56 # int | Communication Thread ID

    try:
        # Show Communication Thread
        api_response = api_instance.rest_v10_communications_communication_id_threads_id_get(procore_company_id, project_id, communication_id, id)
        print("The response of ProjectManagementEmailCommunicationsThreadsApi->rest_v10_communications_communication_id_threads_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementEmailCommunicationsThreadsApi->rest_v10_communications_communication_id_threads_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **communication_id** | **int**| Communication ID | 
 **id** | **int**| Communication Thread ID | 

### Return type

[**RestV10CommunicationsCommunicationIdThreadsIdGet200Response**](RestV10CommunicationsCommunicationIdThreadsIdGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

