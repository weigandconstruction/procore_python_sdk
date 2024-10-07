# procore_sdk.QualitySafetyInspectionsInspectionUsersApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v11_projects_project_id_checklist_users_get**](QualitySafetyInspectionsInspectionUsersApi.md#rest_v11_projects_project_id_checklist_users_get) | **GET** /rest/v1.1/projects/{project_id}/checklist/users | List Inspection Users


# **rest_v11_projects_project_id_checklist_users_get**
> List[InspectionUser] rest_v11_projects_project_id_checklist_users_get(procore_company_id, project_id, page=page, per_page=per_page, filters_vendor_id=filters_vendor_id, filters_potential_assignee=filters_potential_assignee, filters_potential_distribution_member=filters_potential_distribution_member, filters_potential_point_of_contact=filters_potential_point_of_contact, sort=sort)

List Inspection Users

Returns a list of Inspection Users for a given project

### Example


```python
import procore_sdk
from procore_sdk.models.inspection_user import InspectionUser
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
    api_instance = procore_sdk.QualitySafetyInspectionsInspectionUsersApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_vendor_id = 56 # int | Return item(s) with the specified Vendor ID. (optional)
    filters_potential_assignee = True # bool | Returns item(s) with the that can be potential inspection assignees. (optional)
    filters_potential_distribution_member = True # bool | Returns item(s) that can be potential distribution members. (optional)
    filters_potential_point_of_contact = True # bool | Returns item(s) with the that can be potential inspection points of contact. (optional)
    sort = 'sort_example' # str | Direction of sorting param (name) is in desc order of full name (optional)

    try:
        # List Inspection Users
        api_response = api_instance.rest_v11_projects_project_id_checklist_users_get(procore_company_id, project_id, page=page, per_page=per_page, filters_vendor_id=filters_vendor_id, filters_potential_assignee=filters_potential_assignee, filters_potential_distribution_member=filters_potential_distribution_member, filters_potential_point_of_contact=filters_potential_point_of_contact, sort=sort)
        print("The response of QualitySafetyInspectionsInspectionUsersApi->rest_v11_projects_project_id_checklist_users_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsInspectionUsersApi->rest_v11_projects_project_id_checklist_users_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_vendor_id** | **int**| Return item(s) with the specified Vendor ID. | [optional] 
 **filters_potential_assignee** | **bool**| Returns item(s) with the that can be potential inspection assignees. | [optional] 
 **filters_potential_distribution_member** | **bool**| Returns item(s) that can be potential distribution members. | [optional] 
 **filters_potential_point_of_contact** | **bool**| Returns item(s) with the that can be potential inspection points of contact. | [optional] 
 **sort** | **str**| Direction of sorting param (name) is in desc order of full name | [optional] 

### Return type

[**List[InspectionUser]**](InspectionUser.md)

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

