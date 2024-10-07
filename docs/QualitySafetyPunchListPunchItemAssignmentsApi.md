# procore_sdk.QualitySafetyPunchListPunchItemAssignmentsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_punch_item_assignments_id_get**](QualitySafetyPunchListPunchItemAssignmentsApi.md#rest_v10_projects_project_id_punch_item_assignments_id_get) | **GET** /rest/v1.0/projects/{project_id}/punch_item_assignments/{id} | Show Punch Assignment
[**rest_v10_projects_project_id_punch_item_assignments_id_patch**](QualitySafetyPunchListPunchItemAssignmentsApi.md#rest_v10_projects_project_id_punch_item_assignments_id_patch) | **PATCH** /rest/v1.0/projects/{project_id}/punch_item_assignments/{id} | Update Punch Item Assignment


# **rest_v10_projects_project_id_punch_item_assignments_id_get**
> RestV10ProjectsProjectIdPunchItemAssignmentsIdGet200Response rest_v10_projects_project_id_punch_item_assignments_id_get(procore_company_id, id, project_id)

Show Punch Assignment

Returns single Punch Item Assignment.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_punch_item_assignments_id_get200_response import RestV10ProjectsProjectIdPunchItemAssignmentsIdGet200Response
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
    api_instance = procore_sdk.QualitySafetyPunchListPunchItemAssignmentsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the Punch Item Assignment
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Show Punch Assignment
        api_response = api_instance.rest_v10_projects_project_id_punch_item_assignments_id_get(procore_company_id, id, project_id)
        print("The response of QualitySafetyPunchListPunchItemAssignmentsApi->rest_v10_projects_project_id_punch_item_assignments_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyPunchListPunchItemAssignmentsApi->rest_v10_projects_project_id_punch_item_assignments_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the Punch Item Assignment | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**RestV10ProjectsProjectIdPunchItemAssignmentsIdGet200Response**](RestV10ProjectsProjectIdPunchItemAssignmentsIdGet200Response.md)

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
**403** | User does not have right permissions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_punch_item_assignments_id_patch**
> RestV10ProjectsProjectIdPunchItemAssignmentsIdGet200Response rest_v10_projects_project_id_punch_item_assignments_id_patch(procore_company_id, id, project_id, rest_v10_projects_project_id_punch_item_assignments_id_patch_request)

Update Punch Item Assignment

Update single Punch Item Assignment.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_punch_item_assignments_id_get200_response import RestV10ProjectsProjectIdPunchItemAssignmentsIdGet200Response
from procore_sdk.models.rest_v10_projects_project_id_punch_item_assignments_id_patch_request import RestV10ProjectsProjectIdPunchItemAssignmentsIdPatchRequest
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
    api_instance = procore_sdk.QualitySafetyPunchListPunchItemAssignmentsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the Punch Item Assignment
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_projects_project_id_punch_item_assignments_id_patch_request = procore_sdk.RestV10ProjectsProjectIdPunchItemAssignmentsIdPatchRequest() # RestV10ProjectsProjectIdPunchItemAssignmentsIdPatchRequest | 

    try:
        # Update Punch Item Assignment
        api_response = api_instance.rest_v10_projects_project_id_punch_item_assignments_id_patch(procore_company_id, id, project_id, rest_v10_projects_project_id_punch_item_assignments_id_patch_request)
        print("The response of QualitySafetyPunchListPunchItemAssignmentsApi->rest_v10_projects_project_id_punch_item_assignments_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyPunchListPunchItemAssignmentsApi->rest_v10_projects_project_id_punch_item_assignments_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the Punch Item Assignment | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_projects_project_id_punch_item_assignments_id_patch_request** | [**RestV10ProjectsProjectIdPunchItemAssignmentsIdPatchRequest**](RestV10ProjectsProjectIdPunchItemAssignmentsIdPatchRequest.md)|  | 

### Return type

[**RestV10ProjectsProjectIdPunchItemAssignmentsIdGet200Response**](RestV10ProjectsProjectIdPunchItemAssignmentsIdGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Can not update due to errors |  -  |
**401** | Unauthorized |  -  |
**403** | User does not have right permissions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

