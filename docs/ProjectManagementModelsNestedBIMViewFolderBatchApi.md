# procore_sdk.ProjectManagementModelsNestedBIMViewFolderBatchApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_nested_bim_view_folders_batch_post**](ProjectManagementModelsNestedBIMViewFolderBatchApi.md#rest_v10_nested_bim_view_folders_batch_post) | **POST** /rest/v1.0/nested_bim_view_folders/batch | Create a batch of BIM View Folder by path


# **rest_v10_nested_bim_view_folders_batch_post**
> NestedBIMViewFolderBatchCreateResponse rest_v10_nested_bim_view_folders_batch_post(procore_company_id, body60)

Create a batch of BIM View Folder by path

Creates a batch of nested BIM folders as per path provided. If the folder corresponding to a path exists, the folder at the lowest level is returned.

### Example


```python
import procore_sdk
from procore_sdk.models.body60 import Body60
from procore_sdk.models.nested_bim_view_folder_batch_create_response import NestedBIMViewFolderBatchCreateResponse
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
    api_instance = procore_sdk.ProjectManagementModelsNestedBIMViewFolderBatchApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    body60 = procore_sdk.Body60() # Body60 | 

    try:
        # Create a batch of BIM View Folder by path
        api_response = api_instance.rest_v10_nested_bim_view_folders_batch_post(procore_company_id, body60)
        print("The response of ProjectManagementModelsNestedBIMViewFolderBatchApi->rest_v10_nested_bim_view_folders_batch_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementModelsNestedBIMViewFolderBatchApi->rest_v10_nested_bim_view_folders_batch_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **body60** | [**Body60**](Body60.md)|  | 

### Return type

[**NestedBIMViewFolderBatchCreateResponse**](NestedBIMViewFolderBatchCreateResponse.md)

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

