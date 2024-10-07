# procore_sdk.ProjectManagementModelsBIMViewpointAssociationsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_bim_viewpoints_bim_viewpoint_id_associations_delete**](ProjectManagementModelsBIMViewpointAssociationsApi.md#rest_v10_bim_viewpoints_bim_viewpoint_id_associations_delete) | **DELETE** /rest/v1.0/bim_viewpoints/{bim_viewpoint_id}/associations | Delete Viewpoint and Procore Item association
[**rest_v10_bim_viewpoints_bim_viewpoint_id_associations_post**](ProjectManagementModelsBIMViewpointAssociationsApi.md#rest_v10_bim_viewpoints_bim_viewpoint_id_associations_post) | **POST** /rest/v1.0/bim_viewpoints/{bim_viewpoint_id}/associations | Create Viewpoint and Procore Item association


# **rest_v10_bim_viewpoints_bim_viewpoint_id_associations_delete**
> rest_v10_bim_viewpoints_bim_viewpoint_id_associations_delete(procore_company_id, bim_viewpoint_id, project_id, item_id, item_type)

Delete Viewpoint and Procore Item association

Delete the association between a BIM Viewpoint and a procore item.

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
    api_instance = procore_sdk.ProjectManagementModelsBIMViewpointAssociationsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    bim_viewpoint_id = 56 # int | BIM Viewpoint ID
    project_id = 56 # int | Unique identifier for the project.
    item_id = 56 # int | Procore Item ID
    item_type = 'item_type_example' # str | Procore Item Type

    try:
        # Delete Viewpoint and Procore Item association
        api_instance.rest_v10_bim_viewpoints_bim_viewpoint_id_associations_delete(procore_company_id, bim_viewpoint_id, project_id, item_id, item_type)
    except Exception as e:
        print("Exception when calling ProjectManagementModelsBIMViewpointAssociationsApi->rest_v10_bim_viewpoints_bim_viewpoint_id_associations_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **bim_viewpoint_id** | **int**| BIM Viewpoint ID | 
 **project_id** | **int**| Unique identifier for the project. | 
 **item_id** | **int**| Procore Item ID | 
 **item_type** | **str**| Procore Item Type | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_bim_viewpoints_bim_viewpoint_id_associations_post**
> rest_v10_bim_viewpoints_bim_viewpoint_id_associations_post(procore_company_id, bim_viewpoint_id, body123)

Create Viewpoint and Procore Item association

A BIM Viewpoint can be associated with other procore items. This API endpoint creates that association.

### Example


```python
import procore_sdk
from procore_sdk.models.body123 import Body123
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
    api_instance = procore_sdk.ProjectManagementModelsBIMViewpointAssociationsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    bim_viewpoint_id = 56 # int | BIM Viewpoint ID
    body123 = procore_sdk.Body123() # Body123 | 

    try:
        # Create Viewpoint and Procore Item association
        api_instance.rest_v10_bim_viewpoints_bim_viewpoint_id_associations_post(procore_company_id, bim_viewpoint_id, body123)
    except Exception as e:
        print("Exception when calling ProjectManagementModelsBIMViewpointAssociationsApi->rest_v10_bim_viewpoints_bim_viewpoint_id_associations_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **bim_viewpoint_id** | **int**| BIM Viewpoint ID | 
 **body123** | [**Body123**](Body123.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

