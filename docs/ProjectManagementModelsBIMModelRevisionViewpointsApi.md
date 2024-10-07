# procore_sdk.ProjectManagementModelsBIMModelRevisionViewpointsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_bim_model_revision_viewpoints_get**](ProjectManagementModelsBIMModelRevisionViewpointsApi.md#rest_v10_bim_model_revision_viewpoints_get) | **GET** /rest/v1.0/bim_model_revision_viewpoints | List BIM Model Revision Viewpoints


# **rest_v10_bim_model_revision_viewpoints_get**
> List[RestV10BimModelRevisionViewpointsGet200ResponseInner] rest_v10_bim_model_revision_viewpoints_get(procore_company_id, project_id, filters_id=filters_id, filters_bim_model_revision_id=filters_bim_model_revision_id, filters_updated_at=filters_updated_at, filters_primary=filters_primary, view=view, viewpoint_format=viewpoint_format, page=page, per_page=per_page)

List BIM Model Revision Viewpoints

List BIM Model Revision Viewpoints associated to a BIM model revision

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_bim_model_revision_viewpoints_get200_response_inner import RestV10BimModelRevisionViewpointsGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementModelsBIMModelRevisionViewpointsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_bim_model_revision_id = 56 # int | Filter item(s) with matching Bim Model Revision ids. (optional)
    filters_updated_at = 'filters_updated_at_example' # str | Filter item(s) within a specific updated at iso8601 datetime range. (optional)
    filters_primary = True # bool | Filter items by primary flag (optional)
    view = 'view_example' # str | The compact view contains only ids. The extended view contains the response shown below. The normal view contains bim_viewpoint_id instead of object. The default view is normal. (optional)
    viewpoint_format = 'viewpoint_format_example' # str | Specify viewpoint data format. This parameter functions only when the query parameter view is 'extended' The default format returns the viewpoint content as saved. The procore format returns the viewpoint content converted to Procore format. If a valid conversion is not possible, empty viewpoint is returned. (optional)
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List BIM Model Revision Viewpoints
        api_response = api_instance.rest_v10_bim_model_revision_viewpoints_get(procore_company_id, project_id, filters_id=filters_id, filters_bim_model_revision_id=filters_bim_model_revision_id, filters_updated_at=filters_updated_at, filters_primary=filters_primary, view=view, viewpoint_format=viewpoint_format, page=page, per_page=per_page)
        print("The response of ProjectManagementModelsBIMModelRevisionViewpointsApi->rest_v10_bim_model_revision_viewpoints_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementModelsBIMModelRevisionViewpointsApi->rest_v10_bim_model_revision_viewpoints_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **filters_id** | [**List[int]**](int.md)| Return item(s) with the specified IDs. | [optional] 
 **filters_bim_model_revision_id** | **int**| Filter item(s) with matching Bim Model Revision ids. | [optional] 
 **filters_updated_at** | **str**| Filter item(s) within a specific updated at iso8601 datetime range. | [optional] 
 **filters_primary** | **bool**| Filter items by primary flag | [optional] 
 **view** | **str**| The compact view contains only ids. The extended view contains the response shown below. The normal view contains bim_viewpoint_id instead of object. The default view is normal. | [optional] 
 **viewpoint_format** | **str**| Specify viewpoint data format. This parameter functions only when the query parameter view is &#39;extended&#39; The default format returns the viewpoint content as saved. The procore format returns the viewpoint content converted to Procore format. If a valid conversion is not possible, empty viewpoint is returned. | [optional] 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[RestV10BimModelRevisionViewpointsGet200ResponseInner]**](RestV10BimModelRevisionViewpointsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | BIM Model Revision Viewpoints listed successfully |  * Per-Page - Number of items retrieved per page <br>  * Total - Total number of items to be retrieved <br>  * Link - Link headers for the first, prev, next, and last link <br>  |
**403** | User does not have permission to view BIM Model Revision Viewpoints |  -  |
**404** | Not Found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

