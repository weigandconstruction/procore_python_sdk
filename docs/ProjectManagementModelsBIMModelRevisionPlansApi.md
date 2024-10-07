# procore_sdk.ProjectManagementModelsBIMModelRevisionPlansApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_bim_model_revision_plans_get**](ProjectManagementModelsBIMModelRevisionPlansApi.md#rest_v10_bim_model_revision_plans_get) | **GET** /rest/v1.0/bim_model_revision_plans | List BIM Model Revision Plans
[**rest_v10_bim_model_revision_plans_id_delete**](ProjectManagementModelsBIMModelRevisionPlansApi.md#rest_v10_bim_model_revision_plans_id_delete) | **DELETE** /rest/v1.0/bim_model_revision_plans/{id} | Delete BIM Model Revision Plan
[**rest_v10_bim_model_revision_plans_id_get**](ProjectManagementModelsBIMModelRevisionPlansApi.md#rest_v10_bim_model_revision_plans_id_get) | **GET** /rest/v1.0/bim_model_revision_plans/{id} | Show BIM Model Revision Plan
[**rest_v10_bim_model_revision_plans_post**](ProjectManagementModelsBIMModelRevisionPlansApi.md#rest_v10_bim_model_revision_plans_post) | **POST** /rest/v1.0/bim_model_revision_plans | Create BIM Model Revision Plan


# **rest_v10_bim_model_revision_plans_get**
> List[RestV10BimModelRevisionPlansGet200ResponseInner] rest_v10_bim_model_revision_plans_get(procore_company_id, project_id, page=page, per_page=per_page, view=view, filters_id=filters_id, filters_bim_plan_id=filters_bim_plan_id, filters_bim_model_revision_id=filters_bim_model_revision_id, filters_bim_level_id=filters_bim_level_id)

List BIM Model Revision Plans

Lists BIM Model Revision Plans associated with the specified Project.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_bim_model_revision_plans_get200_response_inner import RestV10BimModelRevisionPlansGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementModelsBIMModelRevisionPlansApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    view = 'view_example' # str | The compact view contains only ids. The extended view contains the response shown below. The normal view contains 'bim_plan_id' and 'bim_level_id' instead of objects. The default view is normal. (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_bim_plan_id = 56 # int | Filter item(s) with matching BIM Plan ids (optional)
    filters_bim_model_revision_id = 56 # int | Filter item(s) with matching Bim Model Revision ids. (optional)
    filters_bim_level_id = 56 # int | Filter item(s) with matching BIM Level ids (optional)

    try:
        # List BIM Model Revision Plans
        api_response = api_instance.rest_v10_bim_model_revision_plans_get(procore_company_id, project_id, page=page, per_page=per_page, view=view, filters_id=filters_id, filters_bim_plan_id=filters_bim_plan_id, filters_bim_model_revision_id=filters_bim_model_revision_id, filters_bim_level_id=filters_bim_level_id)
        print("The response of ProjectManagementModelsBIMModelRevisionPlansApi->rest_v10_bim_model_revision_plans_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementModelsBIMModelRevisionPlansApi->rest_v10_bim_model_revision_plans_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **view** | **str**| The compact view contains only ids. The extended view contains the response shown below. The normal view contains &#39;bim_plan_id&#39; and &#39;bim_level_id&#39; instead of objects. The default view is normal. | [optional] 
 **filters_id** | [**List[int]**](int.md)| Return item(s) with the specified IDs. | [optional] 
 **filters_bim_plan_id** | **int**| Filter item(s) with matching BIM Plan ids | [optional] 
 **filters_bim_model_revision_id** | **int**| Filter item(s) with matching Bim Model Revision ids. | [optional] 
 **filters_bim_level_id** | **int**| Filter item(s) with matching BIM Level ids | [optional] 

### Return type

[**List[RestV10BimModelRevisionPlansGet200ResponseInner]**](RestV10BimModelRevisionPlansGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | BIM Model Revision Plans listed successfully |  * Per-Page - Number of items retrieved per page <br>  * Total - Total number of items to be retrieved <br>  * Link - Link headers for the first, prev, next, and last link <br>  |
**403** | User does not have permission to view BIM Model Revision Plans |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_bim_model_revision_plans_id_delete**
> rest_v10_bim_model_revision_plans_id_delete(procore_company_id, id, project_id)

Delete BIM Model Revision Plan

Delete a BIM Model Revision Plan from the system.

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
    api_instance = procore_sdk.ProjectManagementModelsBIMModelRevisionPlansApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | BIM Model Revision Plan ID
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Delete BIM Model Revision Plan
        api_instance.rest_v10_bim_model_revision_plans_id_delete(procore_company_id, id, project_id)
    except Exception as e:
        print("Exception when calling ProjectManagementModelsBIMModelRevisionPlansApi->rest_v10_bim_model_revision_plans_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| BIM Model Revision Plan ID | 
 **project_id** | **int**| Unique identifier for the project. | 

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
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_bim_model_revision_plans_id_get**
> RestV10BimModelRevisionPlansGet200ResponseInner rest_v10_bim_model_revision_plans_id_get(procore_company_id, id, project_id, view=view)

Show BIM Model Revision Plan

Return a single BIM Model Revision Plan item.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_bim_model_revision_plans_get200_response_inner import RestV10BimModelRevisionPlansGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementModelsBIMModelRevisionPlansApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | BIM Model Revision Plan ID
    project_id = 56 # int | Unique identifier for the project.
    view = 'view_example' # str | The compact view contains only ids. The extended view contains the response shown below. The normal view contains 'bim_plan_id' and 'bim_level_id' instead of objects. The default view is normal. (optional)

    try:
        # Show BIM Model Revision Plan
        api_response = api_instance.rest_v10_bim_model_revision_plans_id_get(procore_company_id, id, project_id, view=view)
        print("The response of ProjectManagementModelsBIMModelRevisionPlansApi->rest_v10_bim_model_revision_plans_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementModelsBIMModelRevisionPlansApi->rest_v10_bim_model_revision_plans_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| BIM Model Revision Plan ID | 
 **project_id** | **int**| Unique identifier for the project. | 
 **view** | **str**| The compact view contains only ids. The extended view contains the response shown below. The normal view contains &#39;bim_plan_id&#39; and &#39;bim_level_id&#39; instead of objects. The default view is normal. | [optional] 

### Return type

[**RestV10BimModelRevisionPlansGet200ResponseInner**](RestV10BimModelRevisionPlansGet200ResponseInner.md)

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

# **rest_v10_bim_model_revision_plans_post**
> RestV10BimModelRevisionPlansGet200ResponseInner rest_v10_bim_model_revision_plans_post(procore_company_id, body133)

Create BIM Model Revision Plan

Create a relationship between a BIM Model Revision and a BIM Plan.

### Example


```python
import procore_sdk
from procore_sdk.models.body133 import Body133
from procore_sdk.models.rest_v10_bim_model_revision_plans_get200_response_inner import RestV10BimModelRevisionPlansGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementModelsBIMModelRevisionPlansApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    body133 = procore_sdk.Body133() # Body133 | 

    try:
        # Create BIM Model Revision Plan
        api_response = api_instance.rest_v10_bim_model_revision_plans_post(procore_company_id, body133)
        print("The response of ProjectManagementModelsBIMModelRevisionPlansApi->rest_v10_bim_model_revision_plans_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementModelsBIMModelRevisionPlansApi->rest_v10_bim_model_revision_plans_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **body133** | [**Body133**](Body133.md)|  | 

### Return type

[**RestV10BimModelRevisionPlansGet200ResponseInner**](RestV10BimModelRevisionPlansGet200ResponseInner.md)

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

