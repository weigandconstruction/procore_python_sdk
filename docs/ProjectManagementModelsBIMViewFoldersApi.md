# procore_sdk.ProjectManagementModelsBIMViewFoldersApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_bim_view_folders_get**](ProjectManagementModelsBIMViewFoldersApi.md#rest_v10_bim_view_folders_get) | **GET** /rest/v1.0/bim_view_folders | List BIM View Folders
[**rest_v10_bim_view_folders_post**](ProjectManagementModelsBIMViewFoldersApi.md#rest_v10_bim_view_folders_post) | **POST** /rest/v1.0/bim_view_folders | Create BIM View Folder


# **rest_v10_bim_view_folders_get**
> List[RestV10NestedBimViewFoldersPost200Response] rest_v10_bim_view_folders_get(procore_company_id, project_id, page=page, per_page=per_page, filters_id=filters_id, filters_bim_file_id=filters_bim_file_id, filters_parent_id=filters_parent_id)

List BIM View Folders

Lists BIM View Folders associated with the specified Project.

### Example


```python
import procore_sdk
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
    api_instance = procore_sdk.ProjectManagementModelsBIMViewFoldersApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_bim_file_id = 56 # int | Filter item(s) with matching BIM File ids (optional)
    filters_parent_id = 56 # int | Filter item(s) with matching parent_id (optional)

    try:
        # List BIM View Folders
        api_response = api_instance.rest_v10_bim_view_folders_get(procore_company_id, project_id, page=page, per_page=per_page, filters_id=filters_id, filters_bim_file_id=filters_bim_file_id, filters_parent_id=filters_parent_id)
        print("The response of ProjectManagementModelsBIMViewFoldersApi->rest_v10_bim_view_folders_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementModelsBIMViewFoldersApi->rest_v10_bim_view_folders_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_id** | [**List[int]**](int.md)| Return item(s) with the specified IDs. | [optional] 
 **filters_bim_file_id** | **int**| Filter item(s) with matching BIM File ids | [optional] 
 **filters_parent_id** | **int**| Filter item(s) with matching parent_id | [optional] 

### Return type

[**List[RestV10NestedBimViewFoldersPost200Response]**](RestV10NestedBimViewFoldersPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | BIM View Folders listed successfully |  * Per-Page - Number of items retrieved per page <br>  * Total - Total number of items to be retrieved <br>  * Link - Link headers for the first, prev, next, and last link <br>  |
**403** | User does not have permission to view BIM View Folders |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_bim_view_folders_post**
> RestV10NestedBimViewFoldersPost200Response rest_v10_bim_view_folders_post(procore_company_id, body124)

Create BIM View Folder

Create BIM View Folder

### Example


```python
import procore_sdk
from procore_sdk.models.body124 import Body124
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
    api_instance = procore_sdk.ProjectManagementModelsBIMViewFoldersApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    body124 = procore_sdk.Body124() # Body124 | 

    try:
        # Create BIM View Folder
        api_response = api_instance.rest_v10_bim_view_folders_post(procore_company_id, body124)
        print("The response of ProjectManagementModelsBIMViewFoldersApi->rest_v10_bim_view_folders_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementModelsBIMViewFoldersApi->rest_v10_bim_view_folders_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **body124** | [**Body124**](Body124.md)|  | 

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
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

