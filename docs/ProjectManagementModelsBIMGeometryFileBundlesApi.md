# procore_sdk.ProjectManagementModelsBIMGeometryFileBundlesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_bim_geometry_file_bundles_id_get**](ProjectManagementModelsBIMGeometryFileBundlesApi.md#rest_v10_bim_geometry_file_bundles_id_get) | **GET** /rest/v1.0/bim_geometry_file_bundles/{id} | Show BIM Geometry File Bundle
[**rest_v10_bim_geometry_file_bundles_post**](ProjectManagementModelsBIMGeometryFileBundlesApi.md#rest_v10_bim_geometry_file_bundles_post) | **POST** /rest/v1.0/bim_geometry_file_bundles | Create BIM Geometry File Bundle


# **rest_v10_bim_geometry_file_bundles_id_get**
> RestV10BimGeometryFileBundlesIdGet200Response rest_v10_bim_geometry_file_bundles_id_get(procore_company_id, id, project_id, view=view)

Show BIM Geometry File Bundle

Return BIM Geometry File Bundle details.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_bim_geometry_file_bundles_id_get200_response import RestV10BimGeometryFileBundlesIdGet200Response
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
    api_instance = procore_sdk.ProjectManagementModelsBIMGeometryFileBundlesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | BIM Geometry File Bundle ID
    project_id = 56 # int | Unique identifier for the project.
    view = 'view_example' # str | The compact view contains only ids. The extended view contains the response shown below. The normal view contains ids instead of objects for each file object. The default view is normal. (optional)

    try:
        # Show BIM Geometry File Bundle
        api_response = api_instance.rest_v10_bim_geometry_file_bundles_id_get(procore_company_id, id, project_id, view=view)
        print("The response of ProjectManagementModelsBIMGeometryFileBundlesApi->rest_v10_bim_geometry_file_bundles_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementModelsBIMGeometryFileBundlesApi->rest_v10_bim_geometry_file_bundles_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| BIM Geometry File Bundle ID | 
 **project_id** | **int**| Unique identifier for the project. | 
 **view** | **str**| The compact view contains only ids. The extended view contains the response shown below. The normal view contains ids instead of objects for each file object. The default view is normal. | [optional] 

### Return type

[**RestV10BimGeometryFileBundlesIdGet200Response**](RestV10BimGeometryFileBundlesIdGet200Response.md)

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
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_bim_geometry_file_bundles_post**
> RestV10BimGeometryFileBundlesPost201Response rest_v10_bim_geometry_file_bundles_post(procore_company_id, body139)

Create BIM Geometry File Bundle

Create a BIM Geometry File Bundle in a Project

### Example


```python
import procore_sdk
from procore_sdk.models.body139 import Body139
from procore_sdk.models.rest_v10_bim_geometry_file_bundles_post201_response import RestV10BimGeometryFileBundlesPost201Response
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
    api_instance = procore_sdk.ProjectManagementModelsBIMGeometryFileBundlesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    body139 = procore_sdk.Body139() # Body139 | 

    try:
        # Create BIM Geometry File Bundle
        api_response = api_instance.rest_v10_bim_geometry_file_bundles_post(procore_company_id, body139)
        print("The response of ProjectManagementModelsBIMGeometryFileBundlesApi->rest_v10_bim_geometry_file_bundles_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementModelsBIMGeometryFileBundlesApi->rest_v10_bim_geometry_file_bundles_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **body139** | [**Body139**](Body139.md)|  | 

### Return type

[**RestV10BimGeometryFileBundlesPost201Response**](RestV10BimGeometryFileBundlesPost201Response.md)

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

