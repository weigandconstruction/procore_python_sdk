# procore_sdk.ProjectManagementModelsBIMModelChangeHistoryApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_bim_models_id_change_history_get**](ProjectManagementModelsBIMModelChangeHistoryApi.md#rest_v10_bim_models_id_change_history_get) | **GET** /rest/v1.0/bim_models/{id}/change_history | List BIM Model Change History


# **rest_v10_bim_models_id_change_history_get**
> List[RestV10ProjectsProjectIdTimeAndMaterialEntriesIdChangeHistoryGet304Response] rest_v10_bim_models_id_change_history_get(procore_company_id, id, project_id, page=page, per_page=per_page, view=view)

List BIM Model Change History

This is a deprecated endpoint. This endpoint returns the change history for the specified BimModel. The change history is sorted by most recent first.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_time_and_material_entries_id_change_history_get304_response import RestV10ProjectsProjectIdTimeAndMaterialEntriesIdChangeHistoryGet304Response
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
    api_instance = procore_sdk.ProjectManagementModelsBIMModelChangeHistoryApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | BIM Model ID
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    view = 'view_example' # str | The extended view provides what is shown below. The normal view is the same as the extended view but excludes attribute created_by. The compact view returns ids only. The default view is normal. (optional)

    try:
        # List BIM Model Change History
        api_response = api_instance.rest_v10_bim_models_id_change_history_get(procore_company_id, id, project_id, page=page, per_page=per_page, view=view)
        print("The response of ProjectManagementModelsBIMModelChangeHistoryApi->rest_v10_bim_models_id_change_history_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementModelsBIMModelChangeHistoryApi->rest_v10_bim_models_id_change_history_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| BIM Model ID | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **view** | **str**| The extended view provides what is shown below. The normal view is the same as the extended view but excludes attribute created_by. The compact view returns ids only. The default view is normal. | [optional] 

### Return type

[**List[RestV10ProjectsProjectIdTimeAndMaterialEntriesIdChangeHistoryGet304Response]**](RestV10ProjectsProjectIdTimeAndMaterialEntriesIdChangeHistoryGet304Response.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

