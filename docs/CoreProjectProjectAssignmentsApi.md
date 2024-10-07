# procore_sdk.CoreProjectProjectAssignmentsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_users_user_id_project_assignments_get**](CoreProjectProjectAssignmentsApi.md#rest_v10_companies_company_id_users_user_id_project_assignments_get) | **GET** /rest/v1.0/companies/{company_id}/users/{user_id}/project_assignments | List Project assignments for a Company User


# **rest_v10_companies_company_id_users_user_id_project_assignments_get**
> List[ProjectAssignmentNormalView] rest_v10_companies_company_id_users_user_id_project_assignments_get(procore_company_id, company_id, user_id, page=page, per_page=per_page, filters_active=filters_active, filters_name=filters_name, filters_by_stage=filters_by_stage, filters_by_type=filters_by_type, filters_by_program=filters_by_program, filters_by_region=filters_by_region, filters_by_status=filters_by_status, sort=sort, direction=direction)

List Project assignments for a Company User

This endpoint returns the current and potential Project assignments for the specified User. This includes Project information, as well as the Permission Template and Roles assigned to a given user when they are assigned on a Project.

### Example


```python
import procore_sdk
from procore_sdk.models.project_assignment_normal_view import ProjectAssignmentNormalView
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
    api_instance = procore_sdk.CoreProjectProjectAssignmentsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    user_id = 56 # int | User ID
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_active = True # bool | If true, returns item(s) with a status of 'active'. (optional)
    filters_name = ['filters_name_example'] # List[str] | Filter item(s) with matching name. (optional)
    filters_by_stage = procore_sdk.RestV11ProjectsGetFiltersByOwnerTypeParameter() # RestV11ProjectsGetFiltersByOwnerTypeParameter | Return item(s) with the specified project stage ID(s). (optional)
    filters_by_type = procore_sdk.RestV11ProjectsGetFiltersByOwnerTypeParameter() # RestV11ProjectsGetFiltersByOwnerTypeParameter | Return item(s) with the specified project type ID(s). (optional)
    filters_by_program = procore_sdk.RestV11ProjectsGetFiltersByOwnerTypeParameter() # RestV11ProjectsGetFiltersByOwnerTypeParameter | Return item(s) with the specified project program ID(s). (optional)
    filters_by_region = procore_sdk.RestV11ProjectsGetFiltersByOwnerTypeParameter() # RestV11ProjectsGetFiltersByOwnerTypeParameter | Return item(s) with the specified project region ID(s). (optional)
    filters_by_status = 'filters_by_status_example' # str | Return item(s) with the specified status value. Must be one of Active, Inactive, or All. (optional)
    sort = 'sort_example' # str | Sort the results by the specified field. (optional)
    direction = 'direction_example' # str | Sort direction. Default is ascending, nulls first. (optional)

    try:
        # List Project assignments for a Company User
        api_response = api_instance.rest_v10_companies_company_id_users_user_id_project_assignments_get(procore_company_id, company_id, user_id, page=page, per_page=per_page, filters_active=filters_active, filters_name=filters_name, filters_by_stage=filters_by_stage, filters_by_type=filters_by_type, filters_by_program=filters_by_program, filters_by_region=filters_by_region, filters_by_status=filters_by_status, sort=sort, direction=direction)
        print("The response of CoreProjectProjectAssignmentsApi->rest_v10_companies_company_id_users_user_id_project_assignments_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectProjectAssignmentsApi->rest_v10_companies_company_id_users_user_id_project_assignments_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **user_id** | **int**| User ID | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_active** | **bool**| If true, returns item(s) with a status of &#39;active&#39;. | [optional] 
 **filters_name** | [**List[str]**](str.md)| Filter item(s) with matching name. | [optional] 
 **filters_by_stage** | [**RestV11ProjectsGetFiltersByOwnerTypeParameter**](.md)| Return item(s) with the specified project stage ID(s). | [optional] 
 **filters_by_type** | [**RestV11ProjectsGetFiltersByOwnerTypeParameter**](.md)| Return item(s) with the specified project type ID(s). | [optional] 
 **filters_by_program** | [**RestV11ProjectsGetFiltersByOwnerTypeParameter**](.md)| Return item(s) with the specified project program ID(s). | [optional] 
 **filters_by_region** | [**RestV11ProjectsGetFiltersByOwnerTypeParameter**](.md)| Return item(s) with the specified project region ID(s). | [optional] 
 **filters_by_status** | **str**| Return item(s) with the specified status value. Must be one of Active, Inactive, or All. | [optional] 
 **sort** | **str**| Sort the results by the specified field. | [optional] 
 **direction** | **str**| Sort direction. Default is ascending, nulls first. | [optional] 

### Return type

[**List[ProjectAssignmentNormalView]**](ProjectAssignmentNormalView.md)

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

