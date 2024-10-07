# procore_sdk.CoreLocalFilesLocalFilesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_local_files_uuid_get**](CoreLocalFilesLocalFilesApi.md#rest_v10_local_files_uuid_get) | **GET** /rest/v1.0/local_files/{uuid} | Get file by its UUID


# **rest_v10_local_files_uuid_get**
> bytearray rest_v10_local_files_uuid_get(procore_company_id, uuid)

Get file by its UUID

Get binary file content(from the local disk) or redirect to the File service(on remote storage).

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
    api_instance = procore_sdk.CoreLocalFilesLocalFilesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    uuid = 'uuid_example' # str | UUID of the file

    try:
        # Get file by its UUID
        api_response = api_instance.rest_v10_local_files_uuid_get(procore_company_id, uuid)
        print("The response of CoreLocalFilesLocalFilesApi->rest_v10_local_files_uuid_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreLocalFilesLocalFilesApi->rest_v10_local_files_uuid_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **uuid** | **str**| UUID of the file | 

### Return type

**bytearray**

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
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

