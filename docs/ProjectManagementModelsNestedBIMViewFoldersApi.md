# procore_sdk.ProjectManagementModelsNestedBIMViewFoldersApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_nested_bim_view_folders_post**](ProjectManagementModelsNestedBIMViewFoldersApi.md#rest_v10_nested_bim_view_folders_post) | **POST** /rest/v1.0/nested_bim_view_folders | Create or find BIM View Folder by path


# **rest_v10_nested_bim_view_folders_post**
> RestV10NestedBimViewFoldersPost200Response rest_v10_nested_bim_view_folders_post(procore_company_id, body59)

Create or find BIM View Folder by path

Creates or returns the last view folder for the array of path provided.

### Example


```python
import procore_sdk
from procore_sdk.models.body59 import Body59
from procore_sdk.models.rest_v10_nested_bim_view_folders_post200_response import RestV10NestedBimViewFoldersPost200Response
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
    api_instance = procore_sdk.ProjectManagementModelsNestedBIMViewFoldersApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    body59 = procore_sdk.Body59() # Body59 | 

    try:
        # Create or find BIM View Folder by path
        api_response = api_instance.rest_v10_nested_bim_view_folders_post(procore_company_id, body59)
        print("The response of ProjectManagementModelsNestedBIMViewFoldersApi->rest_v10_nested_bim_view_folders_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementModelsNestedBIMViewFoldersApi->rest_v10_nested_bim_view_folders_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **body59** | [**Body59**](Body59.md)|  | 

### Return type

[**RestV10NestedBimViewFoldersPost200Response**](RestV10NestedBimViewFoldersPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Found |  -  |
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

