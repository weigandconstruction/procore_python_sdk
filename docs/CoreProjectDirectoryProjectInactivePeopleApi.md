# procore_sdk.CoreProjectDirectoryProjectInactivePeopleApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_people_inactive_get**](CoreProjectDirectoryProjectInactivePeopleApi.md#rest_v10_projects_project_id_people_inactive_get) | **GET** /rest/v1.0/projects/{project_id}/people/inactive | List Inactive Project People


# **rest_v10_projects_project_id_people_inactive_get**
> List[RestV10ProjectsProjectIdPeopleGet200ResponseInner] rest_v10_projects_project_id_people_inactive_get(procore_company_id, project_id, view=view, page=page, per_page=per_page, filters_is_employee=filters_is_employee, filters_reference_users_only=filters_reference_users_only, filters_without_reference_users=filters_without_reference_users, filters_include_company_people=filters_include_company_people, filters_search=filters_search, filters_connected=filters_connected, filters_vendor_id=filters_vendor_id, filters_job_title=filters_job_title, filters_country_code=filters_country_code, filters_state_code=filters_state_code, filters_trade_id=filters_trade_id, filters_permission_template_id=filters_permission_template_id, sort=sort)

List Inactive Project People

Return a list of People associated with a Project. Includes users in the directory and reference users.  See [Filtering on List Actions](https://developers.procore.com/documentation/filtering-on-list-actions) for information on using the filtering capabilities provided by this endpoint.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_people_get200_response_inner import RestV10ProjectsProjectIdPeopleGet200ResponseInner
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
    api_instance = procore_sdk.CoreProjectDirectoryProjectInactivePeopleApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | ID of the project
    view = 'view_example' # str | Specifies which view of the resource to return (which attributes should be present in the response). Users without read permissions to Directory are limited to the normal and extended views. If a valid view is not provided, it will default to normal. (optional)
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_is_employee = True # bool | If true, returns item(s) where `is_employee` value is true. (optional)
    filters_reference_users_only = True # bool | If true, returns only people who are reference users. (optional)
    filters_without_reference_users = True # bool | If true, returns only people who are not reference users. (optional)
    filters_include_company_people = True # bool | If true, returns people in the Company not just the Project. This option only works if the user has permission to create people in the project directory or permission to read from the company directory. (optional)
    filters_search = 'filters_search_example' # str | Returns item(s) matching the specified search query string. (optional)
    filters_connected = True # bool | If true, returns only people who are connected users. If false, returns only people who are not connected users. (optional)
    filters_vendor_id = [56] # List[int] | Return item(s) with the specified Vendor IDs. (optional)
    filters_job_title = 'filters_job_title_example' # str | Returns only people who have the specified job title. (optional)
    filters_country_code = 'filters_country_code_example' # str | Returns only people who have the specified country code. (optional)
    filters_state_code = 'filters_state_code_example' # str | Returns only people who have the specified state code. (optional)
    filters_trade_id = [56] # List[int] | Array of Trade IDs. Returns item(s) with the specified Trade IDs. (optional)
    filters_permission_template_id = [56] # List[int] | Array of Permission Template IDs. Returns item(s) with the specified Permission Template IDs. (optional)
    sort = 'sort_example' # str | Return items with the specified sort (optional)

    try:
        # List Inactive Project People
        api_response = api_instance.rest_v10_projects_project_id_people_inactive_get(procore_company_id, project_id, view=view, page=page, per_page=per_page, filters_is_employee=filters_is_employee, filters_reference_users_only=filters_reference_users_only, filters_without_reference_users=filters_without_reference_users, filters_include_company_people=filters_include_company_people, filters_search=filters_search, filters_connected=filters_connected, filters_vendor_id=filters_vendor_id, filters_job_title=filters_job_title, filters_country_code=filters_country_code, filters_state_code=filters_state_code, filters_trade_id=filters_trade_id, filters_permission_template_id=filters_permission_template_id, sort=sort)
        print("The response of CoreProjectDirectoryProjectInactivePeopleApi->rest_v10_projects_project_id_people_inactive_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectDirectoryProjectInactivePeopleApi->rest_v10_projects_project_id_people_inactive_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| ID of the project | 
 **view** | **str**| Specifies which view of the resource to return (which attributes should be present in the response). Users without read permissions to Directory are limited to the normal and extended views. If a valid view is not provided, it will default to normal. | [optional] 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_is_employee** | **bool**| If true, returns item(s) where &#x60;is_employee&#x60; value is true. | [optional] 
 **filters_reference_users_only** | **bool**| If true, returns only people who are reference users. | [optional] 
 **filters_without_reference_users** | **bool**| If true, returns only people who are not reference users. | [optional] 
 **filters_include_company_people** | **bool**| If true, returns people in the Company not just the Project. This option only works if the user has permission to create people in the project directory or permission to read from the company directory. | [optional] 
 **filters_search** | **str**| Returns item(s) matching the specified search query string. | [optional] 
 **filters_connected** | **bool**| If true, returns only people who are connected users. If false, returns only people who are not connected users. | [optional] 
 **filters_vendor_id** | [**List[int]**](int.md)| Return item(s) with the specified Vendor IDs. | [optional] 
 **filters_job_title** | **str**| Returns only people who have the specified job title. | [optional] 
 **filters_country_code** | **str**| Returns only people who have the specified country code. | [optional] 
 **filters_state_code** | **str**| Returns only people who have the specified state code. | [optional] 
 **filters_trade_id** | [**List[int]**](int.md)| Array of Trade IDs. Returns item(s) with the specified Trade IDs. | [optional] 
 **filters_permission_template_id** | [**List[int]**](int.md)| Array of Permission Template IDs. Returns item(s) with the specified Permission Template IDs. | [optional] 
 **sort** | **str**| Return items with the specified sort | [optional] 

### Return type

[**List[RestV10ProjectsProjectIdPeopleGet200ResponseInner]**](RestV10ProjectsProjectIdPeopleGet200ResponseInner.md)

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

