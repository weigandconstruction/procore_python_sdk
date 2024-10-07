# procore_sdk.ProjectManagementModelsBIMPropertyFileObjectsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_bim_property_files_id_objects_get**](ProjectManagementModelsBIMPropertyFileObjectsApi.md#rest_v10_bim_property_files_id_objects_get) | **GET** /rest/v1.0/bim_property_files/{id}/objects | List BIM Property File Objects


# **rest_v10_bim_property_files_id_objects_get**
> List[RestV10BimPropertyFilesIdObjectsGet200ResponseInner] rest_v10_bim_property_files_id_objects_get(procore_company_id, id, project_id, page=page, per_page=per_page, object_search_id=object_search_id, filters_id=filters_id, filters_query=filters_query)

List BIM Property File Objects

Lists objects from a specific BIM Property File. A BIM Property File is a resource that represents a 3d-model database. For models published to the Models tool, the property file id can be found in [BIM Model Revision](https://developers.procore.com/reference/rest/v1/bim-model-revisions?version=1.0#show-bim-model-revision) object\\_definition -> id. For models uploaded and extracted with Procore Documents, the property file id can be found in [BIM File Extraction](https://developers.procore.com/reference/rest/v1/bim-file-extractions?version=1.0#show-bim-file-extraction) extraction\\_items -> artifact -> properties -> id.

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
    api_instance = procore_sdk.ProjectManagementModelsBIMPropertyFileObjectsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | BIM Property File ID.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    object_search_id = 56 # int | Object search id (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_query = 'filters_query_example' # str | Filter item(s) containing query. Searchable fields include Object Value (optional)

    try:
        # List BIM Property File Objects
        api_response = api_instance.rest_v10_bim_property_files_id_objects_get(procore_company_id, id, project_id, page=page, per_page=per_page, object_search_id=object_search_id, filters_id=filters_id, filters_query=filters_query)
        print("The response of ProjectManagementModelsBIMPropertyFileObjectsApi->rest_v10_bim_property_files_id_objects_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementModelsBIMPropertyFileObjectsApi->rest_v10_bim_property_files_id_objects_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| BIM Property File ID. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **object_search_id** | **int**| Object search id | [optional] 
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
**200** | BIM Property File Objects listed successfully |  -  |
**400** | Bad Request |  -  |
**401** | User does not have permission to view BIM Property File Object |  -  |
**403** | User does not have permission to view BIM Property File Object |  -  |
**422** | Unprocessable entity |  -  |
**500** | Unexpected Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

