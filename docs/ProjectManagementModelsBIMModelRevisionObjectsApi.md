# procore_sdk.ProjectManagementModelsBIMModelRevisionObjectsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_bim_model_revisions_id_objects_get**](ProjectManagementModelsBIMModelRevisionObjectsApi.md#rest_v10_bim_model_revisions_id_objects_get) | **GET** /rest/v1.0/bim_model_revisions/{id}/objects | List BIM Model Revision objects


# **rest_v10_bim_model_revisions_id_objects_get**
> List[RestV10BimPropertyFilesIdObjectsGet200ResponseInner] rest_v10_bim_model_revisions_id_objects_get(procore_company_id, id, project_id, page=page, per_page=per_page, filters_id=filters_id, filters_query=filters_query)

List BIM Model Revision objects

Lists objects for a specific BIM Model Revision.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_bim_property_files_id_objects_get200_response_inner import RestV10BimPropertyFilesIdObjectsGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementModelsBIMModelRevisionObjectsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | BIM Model Revision ID
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_query = 'filters_query_example' # str | Filter item(s) containing query. Searchable fields include Object Value (optional)

    try:
        # List BIM Model Revision objects
        api_response = api_instance.rest_v10_bim_model_revisions_id_objects_get(procore_company_id, id, project_id, page=page, per_page=per_page, filters_id=filters_id, filters_query=filters_query)
        print("The response of ProjectManagementModelsBIMModelRevisionObjectsApi->rest_v10_bim_model_revisions_id_objects_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementModelsBIMModelRevisionObjectsApi->rest_v10_bim_model_revisions_id_objects_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| BIM Model Revision ID | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_id** | [**List[int]**](int.md)| Return item(s) with the specified IDs. | [optional] 
 **filters_query** | **str**| Filter item(s) containing query. Searchable fields include Object Value | [optional] 

### Return type

[**List[RestV10BimPropertyFilesIdObjectsGet200ResponseInner]**](RestV10BimPropertyFilesIdObjectsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | BIM Model Objects listed successfully |  -  |
**400** | Bad Request |  -  |
**401** | User does not have permission to view BIM Model Object |  -  |
**403** | User does not have permission to view BIM Model Object |  -  |
**422** | Unprocessable entity |  -  |
**500** | Unexpected Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

