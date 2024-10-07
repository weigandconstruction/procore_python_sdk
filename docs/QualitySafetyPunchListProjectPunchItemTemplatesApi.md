# procore_sdk.QualitySafetyPunchListProjectPunchItemTemplatesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_punch_item_templates_get**](QualitySafetyPunchListProjectPunchItemTemplatesApi.md#rest_v10_projects_project_id_punch_item_templates_get) | **GET** /rest/v1.0/projects/{project_id}/punch_item_templates | List Project Punch Item Templates


# **rest_v10_projects_project_id_punch_item_templates_get**
> List[ProjectPunchItemTemplates] rest_v10_projects_project_id_punch_item_templates_get(procore_company_id, project_id, filters_id=filters_id, filters_active=filters_active, filters_updated_at=filters_updated_at, page=page, per_page=per_page)

List Project Punch Item Templates

Return a list of all Project Punch Item Templates associated with a Project.

### Example


```python
import procore_sdk
from procore_sdk.models.project_punch_item_templates import ProjectPunchItemTemplates
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
    api_instance = procore_sdk.QualitySafetyPunchListProjectPunchItemTemplatesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_active = True # bool | If true, returns item(s) with a status of 'active'. (optional)
    filters_updated_at = 'filters_updated_at_example' # str | Return item(s) within a specific updated at iso8601 datetime range (optional)
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Project Punch Item Templates
        api_response = api_instance.rest_v10_projects_project_id_punch_item_templates_get(procore_company_id, project_id, filters_id=filters_id, filters_active=filters_active, filters_updated_at=filters_updated_at, page=page, per_page=per_page)
        print("The response of QualitySafetyPunchListProjectPunchItemTemplatesApi->rest_v10_projects_project_id_punch_item_templates_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyPunchListProjectPunchItemTemplatesApi->rest_v10_projects_project_id_punch_item_templates_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **filters_id** | [**List[int]**](int.md)| Return item(s) with the specified IDs. | [optional] 
 **filters_active** | **bool**| If true, returns item(s) with a status of &#39;active&#39;. | [optional] 
 **filters_updated_at** | **str**| Return item(s) within a specific updated at iso8601 datetime range | [optional] 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[ProjectPunchItemTemplates]**](ProjectPunchItemTemplates.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Per-Page - Number of items retrieved per page <br>  * Total - Total number of items to be retrieved <br>  * Link - Link headers for the first, prev, next, and last link <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

