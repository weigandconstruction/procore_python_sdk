# procore_sdk.ProjectManagementEmailCommunicationsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_communications_id_get**](ProjectManagementEmailCommunicationsApi.md#rest_v10_communications_id_get) | **GET** /rest/v1.0/communications/{id} | Show Communication


# **rest_v10_communications_id_get**
> RestV10CommunicationsIdGet200Response rest_v10_communications_id_get(procore_company_id, project_id, id)

Show Communication

Shows detailed information around a single email communication

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_communications_id_get200_response import RestV10CommunicationsIdGet200Response
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
    api_instance = procore_sdk.ProjectManagementEmailCommunicationsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Communication ID

    try:
        # Show Communication
        api_response = api_instance.rest_v10_communications_id_get(procore_company_id, project_id, id)
        print("The response of ProjectManagementEmailCommunicationsApi->rest_v10_communications_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementEmailCommunicationsApi->rest_v10_communications_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Communication ID | 

### Return type

[**RestV10CommunicationsIdGet200Response**](RestV10CommunicationsIdGet200Response.md)

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

