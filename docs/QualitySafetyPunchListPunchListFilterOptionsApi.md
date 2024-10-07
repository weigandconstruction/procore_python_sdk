# procore_sdk.QualitySafetyPunchListPunchListFilterOptionsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_punch_list_assignees_get**](QualitySafetyPunchListPunchListFilterOptionsApi.md#rest_v10_projects_project_id_punch_list_assignees_get) | **GET** /rest/v1.0/projects/{project_id}/punch_list/assignees | List of Punch List Assignee Filter Options
[**rest_v10_projects_project_id_punch_list_vendors_get**](QualitySafetyPunchListPunchListFilterOptionsApi.md#rest_v10_projects_project_id_punch_list_vendors_get) | **GET** /rest/v1.0/projects/{project_id}/punch_list/vendors | List of Punch List Vendor Filter Options


# **rest_v10_projects_project_id_punch_list_assignees_get**
> RestV10ProjectsProjectIdPunchListAssigneesGet200Response rest_v10_projects_project_id_punch_list_assignees_get(procore_company_id, project_id)

List of Punch List Assignee Filter Options

Returns assignees associated to the Punch List

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_punch_list_assignees_get200_response import RestV10ProjectsProjectIdPunchListAssigneesGet200Response
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
    api_instance = procore_sdk.QualitySafetyPunchListPunchListFilterOptionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.

    try:
        # List of Punch List Assignee Filter Options
        api_response = api_instance.rest_v10_projects_project_id_punch_list_assignees_get(procore_company_id, project_id)
        print("The response of QualitySafetyPunchListPunchListFilterOptionsApi->rest_v10_projects_project_id_punch_list_assignees_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyPunchListPunchListFilterOptionsApi->rest_v10_projects_project_id_punch_list_assignees_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**RestV10ProjectsProjectIdPunchListAssigneesGet200Response**](RestV10ProjectsProjectIdPunchListAssigneesGet200Response.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_punch_list_vendors_get**
> RestV10ProjectsProjectIdPunchListAssigneesGet200Response rest_v10_projects_project_id_punch_list_vendors_get(procore_company_id, project_id)

List of Punch List Vendor Filter Options

Returns vendors associated to the Punch List

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_punch_list_assignees_get200_response import RestV10ProjectsProjectIdPunchListAssigneesGet200Response
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
    api_instance = procore_sdk.QualitySafetyPunchListPunchListFilterOptionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.

    try:
        # List of Punch List Vendor Filter Options
        api_response = api_instance.rest_v10_projects_project_id_punch_list_vendors_get(procore_company_id, project_id)
        print("The response of QualitySafetyPunchListPunchListFilterOptionsApi->rest_v10_projects_project_id_punch_list_vendors_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyPunchListPunchListFilterOptionsApi->rest_v10_projects_project_id_punch_list_vendors_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**RestV10ProjectsProjectIdPunchListAssigneesGet200Response**](RestV10ProjectsProjectIdPunchListAssigneesGet200Response.md)

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

