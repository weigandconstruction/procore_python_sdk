# procore_sdk.QualitySafetyInspectionsChecklistsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_checklist_lists_get**](QualitySafetyInspectionsChecklistsApi.md#rest_v10_checklist_lists_get) | **GET** /rest/v1.0/checklist/lists | List Checklists
[**rest_v10_checklist_lists_id_delete**](QualitySafetyInspectionsChecklistsApi.md#rest_v10_checklist_lists_id_delete) | **DELETE** /rest/v1.0/checklist/lists/{id} | Delete Checklist
[**rest_v10_checklist_lists_id_get**](QualitySafetyInspectionsChecklistsApi.md#rest_v10_checklist_lists_id_get) | **GET** /rest/v1.0/checklist/lists/{id} | Show Checklist
[**rest_v10_checklist_lists_id_patch**](QualitySafetyInspectionsChecklistsApi.md#rest_v10_checklist_lists_id_patch) | **PATCH** /rest/v1.0/checklist/lists/{id} | Update Checklist
[**rest_v10_checklist_lists_post**](QualitySafetyInspectionsChecklistsApi.md#rest_v10_checklist_lists_post) | **POST** /rest/v1.0/checklist/lists | Create Checklist
[**rest_v10_projects_project_id_checklist_lists_get**](QualitySafetyInspectionsChecklistsApi.md#rest_v10_projects_project_id_checklist_lists_get) | **GET** /rest/v1.0/projects/{project_id}/checklist/lists | List Checklists (Inspections)
[**rest_v10_projects_project_id_checklist_lists_grouped_index_get**](QualitySafetyInspectionsChecklistsApi.md#rest_v10_projects_project_id_checklist_lists_grouped_index_get) | **GET** /rest/v1.0/projects/{project_id}/checklist/lists/grouped_index | List Grouped Checklists (Inspections)
[**rest_v10_projects_project_id_checklist_lists_id_delete**](QualitySafetyInspectionsChecklistsApi.md#rest_v10_projects_project_id_checklist_lists_id_delete) | **DELETE** /rest/v1.0/projects/{project_id}/checklist/lists/{id} | Delete Checklist (Inspection)
[**rest_v10_projects_project_id_checklist_lists_id_get**](QualitySafetyInspectionsChecklistsApi.md#rest_v10_projects_project_id_checklist_lists_id_get) | **GET** /rest/v1.0/projects/{project_id}/checklist/lists/{id} | Show Checklist (Inspection)
[**rest_v10_projects_project_id_checklist_lists_id_patch**](QualitySafetyInspectionsChecklistsApi.md#rest_v10_projects_project_id_checklist_lists_id_patch) | **PATCH** /rest/v1.0/projects/{project_id}/checklist/lists/{id} | Update Checklist (Inspection)
[**rest_v10_projects_project_id_checklist_lists_id_send_email_post**](QualitySafetyInspectionsChecklistsApi.md#rest_v10_projects_project_id_checklist_lists_id_send_email_post) | **POST** /rest/v1.0/projects/{project_id}/checklist/lists/{id}/send_email | Send Checklist (Inspection) Email
[**rest_v10_projects_project_id_checklist_lists_post**](QualitySafetyInspectionsChecklistsApi.md#rest_v10_projects_project_id_checklist_lists_post) | **POST** /rest/v1.0/projects/{project_id}/checklist/lists | Create Checklist (Inspection)
[**rest_v10_projects_project_id_recycle_bin_checklist_lists_get**](QualitySafetyInspectionsChecklistsApi.md#rest_v10_projects_project_id_recycle_bin_checklist_lists_get) | **GET** /rest/v1.0/projects/{project_id}/recycle_bin/checklist/lists | List Recycled Checklists (Inspections)
[**rest_v10_projects_project_id_recycle_bin_checklist_lists_grouped_index_get**](QualitySafetyInspectionsChecklistsApi.md#rest_v10_projects_project_id_recycle_bin_checklist_lists_grouped_index_get) | **GET** /rest/v1.0/projects/{project_id}/recycle_bin/checklist/lists/grouped_index | List Grouped Recycled Checklists (Inspections)
[**rest_v10_projects_project_id_recycle_bin_checklist_lists_id_get**](QualitySafetyInspectionsChecklistsApi.md#rest_v10_projects_project_id_recycle_bin_checklist_lists_id_get) | **GET** /rest/v1.0/projects/{project_id}/recycle_bin/checklist/lists/{id} | Show Recycled Checklist (Inspection)
[**rest_v10_projects_project_id_recycle_bin_checklist_lists_id_restore_patch**](QualitySafetyInspectionsChecklistsApi.md#rest_v10_projects_project_id_recycle_bin_checklist_lists_id_restore_patch) | **PATCH** /rest/v1.0/projects/{project_id}/recycle_bin/checklist/lists/{id}/restore | Restore Deleted Checklist (Inspection)
[**rest_v11_projects_project_id_checklist_lists_id_delete**](QualitySafetyInspectionsChecklistsApi.md#rest_v11_projects_project_id_checklist_lists_id_delete) | **DELETE** /rest/v1.1/projects/{project_id}/checklist/lists/{id} | Delete Checklist (Inspection)
[**rest_v11_projects_project_id_checklist_lists_id_patch**](QualitySafetyInspectionsChecklistsApi.md#rest_v11_projects_project_id_checklist_lists_id_patch) | **PATCH** /rest/v1.1/projects/{project_id}/checklist/lists/{id} | Update Checklist (Inspection)
[**rest_v11_projects_project_id_checklist_lists_post**](QualitySafetyInspectionsChecklistsApi.md#rest_v11_projects_project_id_checklist_lists_post) | **POST** /rest/v1.1/projects/{project_id}/checklist/lists | Create Checklist (Inspection)
[**rest_v11_projects_project_id_recycle_bin_checklist_lists_id_restore_patch**](QualitySafetyInspectionsChecklistsApi.md#rest_v11_projects_project_id_recycle_bin_checklist_lists_id_restore_patch) | **PATCH** /rest/v1.1/projects/{project_id}/recycle_bin/checklist/lists/{id}/restore | Restore Deleted Checklist (Inspection)


# **rest_v10_checklist_lists_get**
> List[RestV10ChecklistListsGet200ResponseInner] rest_v10_checklist_lists_get(procore_company_id, project_id, filters_view=filters_view, filters_inspection_type_id=filters_inspection_type_id, filters_point_of_contact_id=filters_point_of_contact_id, filters_inspector_id=filters_inspector_id, filters_list_template_id=filters_list_template_id, filters_location_id=filters_location_id, filters_spec_section_id=filters_spec_section_id, filters_responsible_contractor_id=filters_responsible_contractor_id, filters_status=filters_status, filters_trade_id=filters_trade_id, filters_search=filters_search, filters_due_at=filters_due_at, filters_created_at=filters_created_at, filters_updated_at=filters_updated_at)

List Checklists

Lists Checklist (Inspections) in a specified Project grouped by a specified attribute. By default the Checklists are grouped by template. See [Filtering on List Actions](https://developers.procore.com/documentation/filtering-on-list-actions) for information on using the filtering capabilities provided by this endpoint.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_checklist_lists_get200_response_inner import RestV10ChecklistListsGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    filters_view = 'filters_view_example' # str | If 'recycle', return deleted Checklists. (optional)
    filters_inspection_type_id = [56] # List[int] | Array of Inspection Type IDs. Return item(s) associated with the specified Inspection Type IDs. (optional)
    filters_point_of_contact_id = [56] # List[int] | Array of User IDs. Return item(s) where the specified User IDs are the point of contact. (optional)
    filters_inspector_id = [56] # List[int] | Array of User IDs. Return item(s) where the specified User IDs are inspectors. (optional)
    filters_list_template_id = [56] # List[int] | Array of Checklist Template IDs. Return item(s) associated with the specified Checklist Template IDs. (optional)
    filters_location_id = 56 # int | Filters by specific location (Note: Use *either* this or location_id_with_sublocations, but not both) (optional)
    filters_spec_section_id = [56] # List[int] | Array of Specification Section IDs. Return item(s) associated to the specified Specification Section IDs. (optional)
    filters_responsible_contractor_id = [56] # List[int] | Array of Vendor IDs. Return item(s) where the specified Vendor IDs are the responsible contractor. (optional)
    filters_status = ['filters_status_example'] # List[str] | Returns item(s) matching the specified status value. (optional)
    filters_trade_id = 56 # int | Trade ID (optional)
    filters_search = 'filters_search_example' # str | Returns item(s) matching the specified search query string. (optional)
    filters_due_at = '2013-10-20T19:20:30+01:00' # datetime | Return item(s) due within the specified date range. (optional)
    filters_created_at = '2013-10-20' # date | Return item(s) created within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)

    try:
        # List Checklists
        api_response = api_instance.rest_v10_checklist_lists_get(procore_company_id, project_id, filters_view=filters_view, filters_inspection_type_id=filters_inspection_type_id, filters_point_of_contact_id=filters_point_of_contact_id, filters_inspector_id=filters_inspector_id, filters_list_template_id=filters_list_template_id, filters_location_id=filters_location_id, filters_spec_section_id=filters_spec_section_id, filters_responsible_contractor_id=filters_responsible_contractor_id, filters_status=filters_status, filters_trade_id=filters_trade_id, filters_search=filters_search, filters_due_at=filters_due_at, filters_created_at=filters_created_at, filters_updated_at=filters_updated_at)
        print("The response of QualitySafetyInspectionsChecklistsApi->rest_v10_checklist_lists_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistsApi->rest_v10_checklist_lists_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **filters_view** | **str**| If &#39;recycle&#39;, return deleted Checklists. | [optional] 
 **filters_inspection_type_id** | [**List[int]**](int.md)| Array of Inspection Type IDs. Return item(s) associated with the specified Inspection Type IDs. | [optional] 
 **filters_point_of_contact_id** | [**List[int]**](int.md)| Array of User IDs. Return item(s) where the specified User IDs are the point of contact. | [optional] 
 **filters_inspector_id** | [**List[int]**](int.md)| Array of User IDs. Return item(s) where the specified User IDs are inspectors. | [optional] 
 **filters_list_template_id** | [**List[int]**](int.md)| Array of Checklist Template IDs. Return item(s) associated with the specified Checklist Template IDs. | [optional] 
 **filters_location_id** | **int**| Filters by specific location (Note: Use *either* this or location_id_with_sublocations, but not both) | [optional] 
 **filters_spec_section_id** | [**List[int]**](int.md)| Array of Specification Section IDs. Return item(s) associated to the specified Specification Section IDs. | [optional] 
 **filters_responsible_contractor_id** | [**List[int]**](int.md)| Array of Vendor IDs. Return item(s) where the specified Vendor IDs are the responsible contractor. | [optional] 
 **filters_status** | [**List[str]**](str.md)| Returns item(s) matching the specified status value. | [optional] 
 **filters_trade_id** | **int**| Trade ID | [optional] 
 **filters_search** | **str**| Returns item(s) matching the specified search query string. | [optional] 
 **filters_due_at** | **datetime**| Return item(s) due within the specified date range. | [optional] 
 **filters_created_at** | **date**| Return item(s) created within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 

### Return type

[**List[RestV10ChecklistListsGet200ResponseInner]**](RestV10ChecklistListsGet200ResponseInner.md)

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

# **rest_v10_checklist_lists_id_delete**
> rest_v10_checklist_lists_id_delete(procore_company_id, id, project_id)

Delete Checklist

Deletes Inspection Checklist in a specified Project.

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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | Checklist ID
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Delete Checklist
        api_instance.rest_v10_checklist_lists_id_delete(procore_company_id, id, project_id)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistsApi->rest_v10_checklist_lists_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| Checklist ID | 
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

# **rest_v10_checklist_lists_id_get**
> Checklist3 rest_v10_checklist_lists_id_get(procore_company_id, id, project_id)

Show Checklist

Retrieves Inspection Checklist in a specified Project.

### Example


```python
import procore_sdk
from procore_sdk.models.checklist3 import Checklist3
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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | Checklist ID
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Show Checklist
        api_response = api_instance.rest_v10_checklist_lists_id_get(procore_company_id, id, project_id)
        print("The response of QualitySafetyInspectionsChecklistsApi->rest_v10_checklist_lists_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistsApi->rest_v10_checklist_lists_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| Checklist ID | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**Checklist3**](Checklist3.md)

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

# **rest_v10_checklist_lists_id_patch**
> Checklist3 rest_v10_checklist_lists_id_patch(procore_company_id, id, checklist_body1, run_configurable_validations=run_configurable_validations)

Update Checklist

Updates Inspection Checklist in a specified Project.

### Example


```python
import procore_sdk
from procore_sdk.models.checklist3 import Checklist3
from procore_sdk.models.checklist_body1 import ChecklistBody1
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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | Checklist ID
    checklist_body1 = procore_sdk.ChecklistBody1() # ChecklistBody1 | 
    run_configurable_validations = False # bool | If true, validations are run for the corresponding Configurable Field Set. (optional) (default to False)

    try:
        # Update Checklist
        api_response = api_instance.rest_v10_checklist_lists_id_patch(procore_company_id, id, checklist_body1, run_configurable_validations=run_configurable_validations)
        print("The response of QualitySafetyInspectionsChecklistsApi->rest_v10_checklist_lists_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistsApi->rest_v10_checklist_lists_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| Checklist ID | 
 **checklist_body1** | [**ChecklistBody1**](ChecklistBody1.md)|  | 
 **run_configurable_validations** | **bool**| If true, validations are run for the corresponding Configurable Field Set. | [optional] [default to False]

### Return type

[**Checklist3**](Checklist3.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_checklist_lists_post**
> Checklist3 rest_v10_checklist_lists_post(procore_company_id, checklist_body, run_configurable_validations=run_configurable_validations)

Create Checklist

Creates Inspection Checklist in a specified Project.

### Example


```python
import procore_sdk
from procore_sdk.models.checklist3 import Checklist3
from procore_sdk.models.checklist_body import ChecklistBody
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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    checklist_body = procore_sdk.ChecklistBody() # ChecklistBody | 
    run_configurable_validations = False # bool | If true, validations are run for the corresponding Configurable Field Set. (optional) (default to False)

    try:
        # Create Checklist
        api_response = api_instance.rest_v10_checklist_lists_post(procore_company_id, checklist_body, run_configurable_validations=run_configurable_validations)
        print("The response of QualitySafetyInspectionsChecklistsApi->rest_v10_checklist_lists_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistsApi->rest_v10_checklist_lists_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **checklist_body** | [**ChecklistBody**](ChecklistBody.md)|  | 
 **run_configurable_validations** | **bool**| If true, validations are run for the corresponding Configurable Field Set. | [optional] [default to False]

### Return type

[**Checklist3**](Checklist3.md)

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

# **rest_v10_projects_project_id_checklist_lists_get**
> List[Checklist5] rest_v10_projects_project_id_checklist_lists_get(procore_company_id, project_id, page=page, per_page=per_page, filters_id=filters_id, filters_inspection_date=filters_inspection_date, filters_inspection_type_id=filters_inspection_type_id, filters_inspector_id=filters_inspector_id, filters_template_id=filters_template_id, filters_location_id=filters_location_id, filters_managed_equipment_id=filters_managed_equipment_id, filters_point_of_contact_id=filters_point_of_contact_id, filters_spec_section_id=filters_spec_section_id, filters_responsible_contractor_id=filters_responsible_contractor_id, filters_closed_by_id=filters_closed_by_id, filters_status=filters_status, filters_trade_id=filters_trade_id, filters_query=filters_query, filters_due_at=filters_due_at, filters_created_at=filters_created_at, filters_updated_at=filters_updated_at, filters_closed_at=filters_closed_at, sort=sort)

List Checklists (Inspections)

Lists Checklist (Inspections) in a specified Project. See [Filtering on List Actions](https://developers.procore.com/documentation/filtering-on-list-actions) for information on using the filtering capabilities provided by this endpoint.

### Example


```python
import procore_sdk
from procore_sdk.models.checklist5 import Checklist5
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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_inspection_date = '2013-10-20' # date | Return item(s) with inspection date within the specified ISO 8601 date range. (optional)
    filters_inspection_type_id = [56] # List[int] | Array of Inspection Type IDs. Return item(s) associated with the specified Inspection Type IDs. (optional)
    filters_inspector_id = [56] # List[int] | Array of User IDs. Return item(s) where the specified User IDs are inspectors. (optional)
    filters_template_id = ['filters_template_id_example'] # List[str] | Array of Checklist Template IDs. Return item(s) associated to the specified Checklist Template IDs. (optional)
    filters_location_id = [56] # List[int] | Location ID. Returns item(s) with the specified Location ID or a range of Location IDs. (optional)
    filters_managed_equipment_id = 56 # int | Return item(s) with the specified Managed Equipment ID. (optional)
    filters_point_of_contact_id = [56] # List[int] | Array of User IDs. Return item(s) where the specified User IDs are the point of contact. (optional)
    filters_spec_section_id = [56] # List[int] | Array of Specification Section IDs. Return item(s) associated to the specified Specification Section IDs. (optional)
    filters_responsible_contractor_id = [56] # List[int] | Array of Vendor IDs. Return item(s) where the specified Vendor IDs are the responsible contractor. (optional)
    filters_closed_by_id = [56] # List[int] | Array of User IDs. Return item(s) closed by the specified User ID. (optional)
    filters_status = 56 # int | Return item(s) with the specified statuses (optional)
    filters_trade_id = 56 # int | Trade ID (optional)
    filters_query = 'filters_query_example' # str | Return item(s) containing search query (optional)
    filters_due_at = '2013-10-20T19:20:30+01:00' # datetime | Return item(s) due within the specified date range. (optional)
    filters_created_at = '2013-10-20' # date | Return item(s) created within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_closed_at = '2013-10-20' # date | Returns item(s) closed within the specified ISO 8601 datetime range. (optional)
    sort = 'sort_example' # str |  (optional)

    try:
        # List Checklists (Inspections)
        api_response = api_instance.rest_v10_projects_project_id_checklist_lists_get(procore_company_id, project_id, page=page, per_page=per_page, filters_id=filters_id, filters_inspection_date=filters_inspection_date, filters_inspection_type_id=filters_inspection_type_id, filters_inspector_id=filters_inspector_id, filters_template_id=filters_template_id, filters_location_id=filters_location_id, filters_managed_equipment_id=filters_managed_equipment_id, filters_point_of_contact_id=filters_point_of_contact_id, filters_spec_section_id=filters_spec_section_id, filters_responsible_contractor_id=filters_responsible_contractor_id, filters_closed_by_id=filters_closed_by_id, filters_status=filters_status, filters_trade_id=filters_trade_id, filters_query=filters_query, filters_due_at=filters_due_at, filters_created_at=filters_created_at, filters_updated_at=filters_updated_at, filters_closed_at=filters_closed_at, sort=sort)
        print("The response of QualitySafetyInspectionsChecklistsApi->rest_v10_projects_project_id_checklist_lists_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistsApi->rest_v10_projects_project_id_checklist_lists_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_id** | [**List[int]**](int.md)| Return item(s) with the specified IDs. | [optional] 
 **filters_inspection_date** | **date**| Return item(s) with inspection date within the specified ISO 8601 date range. | [optional] 
 **filters_inspection_type_id** | [**List[int]**](int.md)| Array of Inspection Type IDs. Return item(s) associated with the specified Inspection Type IDs. | [optional] 
 **filters_inspector_id** | [**List[int]**](int.md)| Array of User IDs. Return item(s) where the specified User IDs are inspectors. | [optional] 
 **filters_template_id** | [**List[str]**](str.md)| Array of Checklist Template IDs. Return item(s) associated to the specified Checklist Template IDs. | [optional] 
 **filters_location_id** | [**List[int]**](int.md)| Location ID. Returns item(s) with the specified Location ID or a range of Location IDs. | [optional] 
 **filters_managed_equipment_id** | **int**| Return item(s) with the specified Managed Equipment ID. | [optional] 
 **filters_point_of_contact_id** | [**List[int]**](int.md)| Array of User IDs. Return item(s) where the specified User IDs are the point of contact. | [optional] 
 **filters_spec_section_id** | [**List[int]**](int.md)| Array of Specification Section IDs. Return item(s) associated to the specified Specification Section IDs. | [optional] 
 **filters_responsible_contractor_id** | [**List[int]**](int.md)| Array of Vendor IDs. Return item(s) where the specified Vendor IDs are the responsible contractor. | [optional] 
 **filters_closed_by_id** | [**List[int]**](int.md)| Array of User IDs. Return item(s) closed by the specified User ID. | [optional] 
 **filters_status** | **int**| Return item(s) with the specified statuses | [optional] 
 **filters_trade_id** | **int**| Trade ID | [optional] 
 **filters_query** | **str**| Return item(s) containing search query | [optional] 
 **filters_due_at** | **datetime**| Return item(s) due within the specified date range. | [optional] 
 **filters_created_at** | **date**| Return item(s) created within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_closed_at** | **date**| Returns item(s) closed within the specified ISO 8601 datetime range. | [optional] 
 **sort** | **str**|  | [optional] 

### Return type

[**List[Checklist5]**](Checklist5.md)

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
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_checklist_lists_grouped_index_get**
> List[ChecklistListGroup] rest_v10_projects_project_id_checklist_lists_grouped_index_get(procore_company_id, project_id, page=page, per_page=per_page, filters_id=filters_id, filters_inspection_date=filters_inspection_date, filters_inspection_type_id=filters_inspection_type_id, filters_inspector_id=filters_inspector_id, filters_list_template_id=filters_list_template_id, filters_location_id=filters_location_id, filters_managed_equipment_id=filters_managed_equipment_id, filters_point_of_contact_id=filters_point_of_contact_id, filters_spec_section_id=filters_spec_section_id, filters_responsible_contractor_id=filters_responsible_contractor_id, filters_closed_by_id=filters_closed_by_id, filters_status=filters_status, filters_trade_id=filters_trade_id, filters_query=filters_query, filters_due_at=filters_due_at, filters_created_at=filters_created_at, filters_updated_at=filters_updated_at, filters_closed_at=filters_closed_at, sort=sort, group_by=group_by)

List Grouped Checklists (Inspections)

Lists Grouped Checklist (Inspections) in a specified Project. See [Filtering on List Actions](https://developers.procore.com/documentation/filtering-on-list-actions) for information on using the filtering capabilities provided by this endpoint.

### Example


```python
import procore_sdk
from procore_sdk.models.checklist_list_group import ChecklistListGroup
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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_inspection_date = '2013-10-20' # date | Return item(s) with inspection date within the specified ISO 8601 date range. (optional)
    filters_inspection_type_id = [56] # List[int] | Array of Inspection Type IDs. Return item(s) associated with the specified Inspection Type IDs. (optional)
    filters_inspector_id = [56] # List[int] | Array of User IDs. Return item(s) where the specified User IDs are inspectors. (optional)
    filters_list_template_id = [56] # List[int] | Array of Checklist Template IDs. Return item(s) associated with the specified Checklist Template IDs. (optional)
    filters_location_id = [56] # List[int] | Location ID. Returns item(s) with the specified Location ID or a range of Location IDs. (optional)
    filters_managed_equipment_id = 56 # int | Return item(s) with the specified Managed Equipment ID. (optional)
    filters_point_of_contact_id = [56] # List[int] | Array of User IDs. Return item(s) where the specified User IDs are the point of contact. (optional)
    filters_spec_section_id = [56] # List[int] | Array of Specification Section IDs. Return item(s) associated to the specified Specification Section IDs. (optional)
    filters_responsible_contractor_id = [56] # List[int] | Array of Vendor IDs. Return item(s) where the specified Vendor IDs are the responsible contractor. (optional)
    filters_closed_by_id = [56] # List[int] | Array of User IDs. Return item(s) closed by the specified User ID. (optional)
    filters_status = 56 # int | Return item(s) with the specified statuses (optional)
    filters_trade_id = 56 # int | Trade ID (optional)
    filters_query = 'filters_query_example' # str | Return item(s) containing search query (optional)
    filters_due_at = '2013-10-20T19:20:30+01:00' # datetime | Return item(s) due within the specified date range. (optional)
    filters_created_at = '2013-10-20' # date | Return item(s) created within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_closed_at = '2013-10-20' # date | Returns item(s) closed within the specified ISO 8601 datetime range. (optional)
    sort = 'sort_example' # str |  (optional)
    group_by = 'group_by_example' # str |  (optional)

    try:
        # List Grouped Checklists (Inspections)
        api_response = api_instance.rest_v10_projects_project_id_checklist_lists_grouped_index_get(procore_company_id, project_id, page=page, per_page=per_page, filters_id=filters_id, filters_inspection_date=filters_inspection_date, filters_inspection_type_id=filters_inspection_type_id, filters_inspector_id=filters_inspector_id, filters_list_template_id=filters_list_template_id, filters_location_id=filters_location_id, filters_managed_equipment_id=filters_managed_equipment_id, filters_point_of_contact_id=filters_point_of_contact_id, filters_spec_section_id=filters_spec_section_id, filters_responsible_contractor_id=filters_responsible_contractor_id, filters_closed_by_id=filters_closed_by_id, filters_status=filters_status, filters_trade_id=filters_trade_id, filters_query=filters_query, filters_due_at=filters_due_at, filters_created_at=filters_created_at, filters_updated_at=filters_updated_at, filters_closed_at=filters_closed_at, sort=sort, group_by=group_by)
        print("The response of QualitySafetyInspectionsChecklistsApi->rest_v10_projects_project_id_checklist_lists_grouped_index_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistsApi->rest_v10_projects_project_id_checklist_lists_grouped_index_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_id** | [**List[int]**](int.md)| Return item(s) with the specified IDs. | [optional] 
 **filters_inspection_date** | **date**| Return item(s) with inspection date within the specified ISO 8601 date range. | [optional] 
 **filters_inspection_type_id** | [**List[int]**](int.md)| Array of Inspection Type IDs. Return item(s) associated with the specified Inspection Type IDs. | [optional] 
 **filters_inspector_id** | [**List[int]**](int.md)| Array of User IDs. Return item(s) where the specified User IDs are inspectors. | [optional] 
 **filters_list_template_id** | [**List[int]**](int.md)| Array of Checklist Template IDs. Return item(s) associated with the specified Checklist Template IDs. | [optional] 
 **filters_location_id** | [**List[int]**](int.md)| Location ID. Returns item(s) with the specified Location ID or a range of Location IDs. | [optional] 
 **filters_managed_equipment_id** | **int**| Return item(s) with the specified Managed Equipment ID. | [optional] 
 **filters_point_of_contact_id** | [**List[int]**](int.md)| Array of User IDs. Return item(s) where the specified User IDs are the point of contact. | [optional] 
 **filters_spec_section_id** | [**List[int]**](int.md)| Array of Specification Section IDs. Return item(s) associated to the specified Specification Section IDs. | [optional] 
 **filters_responsible_contractor_id** | [**List[int]**](int.md)| Array of Vendor IDs. Return item(s) where the specified Vendor IDs are the responsible contractor. | [optional] 
 **filters_closed_by_id** | [**List[int]**](int.md)| Array of User IDs. Return item(s) closed by the specified User ID. | [optional] 
 **filters_status** | **int**| Return item(s) with the specified statuses | [optional] 
 **filters_trade_id** | **int**| Trade ID | [optional] 
 **filters_query** | **str**| Return item(s) containing search query | [optional] 
 **filters_due_at** | **datetime**| Return item(s) due within the specified date range. | [optional] 
 **filters_created_at** | **date**| Return item(s) created within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_closed_at** | **date**| Returns item(s) closed within the specified ISO 8601 datetime range. | [optional] 
 **sort** | **str**|  | [optional] 
 **group_by** | **str**|  | [optional] 

### Return type

[**List[ChecklistListGroup]**](ChecklistListGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Per-Page - Number of items retrieved per page <br>  * Total - Total number of items to be retrieved <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_checklist_lists_id_delete**
> rest_v10_projects_project_id_checklist_lists_id_delete(procore_company_id, id, project_id)

Delete Checklist (Inspection)

Deletes specified Checklist (Inspection)

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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | Checklist ID
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Delete Checklist (Inspection)
        api_instance.rest_v10_projects_project_id_checklist_lists_id_delete(procore_company_id, id, project_id)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistsApi->rest_v10_projects_project_id_checklist_lists_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| Checklist ID | 
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
**404** | Not Found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_checklist_lists_id_get**
> Checklist5 rest_v10_projects_project_id_checklist_lists_id_get(procore_company_id, id, project_id)

Show Checklist (Inspection)

Returns the specified Checklist (Inspection)

### Example


```python
import procore_sdk
from procore_sdk.models.checklist5 import Checklist5
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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | Checklist ID
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Show Checklist (Inspection)
        api_response = api_instance.rest_v10_projects_project_id_checklist_lists_id_get(procore_company_id, id, project_id)
        print("The response of QualitySafetyInspectionsChecklistsApi->rest_v10_projects_project_id_checklist_lists_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistsApi->rest_v10_projects_project_id_checklist_lists_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| Checklist ID | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**Checklist5**](Checklist5.md)

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

# **rest_v10_projects_project_id_checklist_lists_id_patch**
> Checklist5 rest_v10_projects_project_id_checklist_lists_id_patch(procore_company_id, id, project_id, rest_v10_projects_project_id_checklist_lists_id_patch_request, run_configurable_validations=run_configurable_validations)

Update Checklist (Inspection)

Updates a specified Checklist (Inspection)

### Example


```python
import procore_sdk
from procore_sdk.models.checklist5 import Checklist5
from procore_sdk.models.rest_v10_projects_project_id_checklist_lists_id_patch_request import RestV10ProjectsProjectIdChecklistListsIdPatchRequest
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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | Checklist ID
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_projects_project_id_checklist_lists_id_patch_request = procore_sdk.RestV10ProjectsProjectIdChecklistListsIdPatchRequest() # RestV10ProjectsProjectIdChecklistListsIdPatchRequest | 
    run_configurable_validations = False # bool | If true, validations are run for the corresponding Configurable Field Set. (optional) (default to False)

    try:
        # Update Checklist (Inspection)
        api_response = api_instance.rest_v10_projects_project_id_checklist_lists_id_patch(procore_company_id, id, project_id, rest_v10_projects_project_id_checklist_lists_id_patch_request, run_configurable_validations=run_configurable_validations)
        print("The response of QualitySafetyInspectionsChecklistsApi->rest_v10_projects_project_id_checklist_lists_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistsApi->rest_v10_projects_project_id_checklist_lists_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| Checklist ID | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_projects_project_id_checklist_lists_id_patch_request** | [**RestV10ProjectsProjectIdChecklistListsIdPatchRequest**](RestV10ProjectsProjectIdChecklistListsIdPatchRequest.md)|  | 
 **run_configurable_validations** | **bool**| If true, validations are run for the corresponding Configurable Field Set. | [optional] [default to False]

### Return type

[**Checklist5**](Checklist5.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_checklist_lists_id_send_email_post**
> rest_v10_projects_project_id_checklist_lists_id_send_email_post(procore_company_id, id, project_id, body111)

Send Checklist (Inspection) Email

Send an email for a Checklist (Inspection) in a Project.

### Example


```python
import procore_sdk
from procore_sdk.models.body111 import Body111
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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | Checklist ID
    project_id = 56 # int | Unique identifier for the project.
    body111 = procore_sdk.Body111() # Body111 | 

    try:
        # Send Checklist (Inspection) Email
        api_instance.rest_v10_projects_project_id_checklist_lists_id_send_email_post(procore_company_id, id, project_id, body111)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistsApi->rest_v10_projects_project_id_checklist_lists_id_send_email_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| Checklist ID | 
 **project_id** | **int**| Unique identifier for the project. | 
 **body111** | [**Body111**](Body111.md)|  | 

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
**204** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_checklist_lists_post**
> Checklist5 rest_v10_projects_project_id_checklist_lists_post(procore_company_id, project_id, rest_v10_projects_project_id_checklist_lists_post_request, run_configurable_validations=run_configurable_validations)

Create Checklist (Inspection)

Creates an instance of Inspection in a given Project

### Example


```python
import procore_sdk
from procore_sdk.models.checklist5 import Checklist5
from procore_sdk.models.rest_v10_projects_project_id_checklist_lists_post_request import RestV10ProjectsProjectIdChecklistListsPostRequest
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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_projects_project_id_checklist_lists_post_request = procore_sdk.RestV10ProjectsProjectIdChecklistListsPostRequest() # RestV10ProjectsProjectIdChecklistListsPostRequest | 
    run_configurable_validations = False # bool | If true, validations are run for the corresponding Configurable Field Set. (optional) (default to False)

    try:
        # Create Checklist (Inspection)
        api_response = api_instance.rest_v10_projects_project_id_checklist_lists_post(procore_company_id, project_id, rest_v10_projects_project_id_checklist_lists_post_request, run_configurable_validations=run_configurable_validations)
        print("The response of QualitySafetyInspectionsChecklistsApi->rest_v10_projects_project_id_checklist_lists_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistsApi->rest_v10_projects_project_id_checklist_lists_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_projects_project_id_checklist_lists_post_request** | [**RestV10ProjectsProjectIdChecklistListsPostRequest**](RestV10ProjectsProjectIdChecklistListsPostRequest.md)|  | 
 **run_configurable_validations** | **bool**| If true, validations are run for the corresponding Configurable Field Set. | [optional] [default to False]

### Return type

[**Checklist5**](Checklist5.md)

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
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_recycle_bin_checklist_lists_get**
> List[Checklist5] rest_v10_projects_project_id_recycle_bin_checklist_lists_get(procore_company_id, project_id, page=page, per_page=per_page, filters_id=filters_id, filters_inspection_date=filters_inspection_date, filters_inspection_type_id=filters_inspection_type_id, filters_inspector_id=filters_inspector_id, filters_template_id=filters_template_id, filters_location_id=filters_location_id, filters_managed_equipment_id=filters_managed_equipment_id, filters_point_of_contact_id=filters_point_of_contact_id, filters_spec_section_id=filters_spec_section_id, filters_responsible_contractor_id=filters_responsible_contractor_id, filters_closed_by_id=filters_closed_by_id, filters_status=filters_status, filters_trade_id=filters_trade_id, filters_query=filters_query, filters_due_at=filters_due_at, filters_created_at=filters_created_at, filters_updated_at=filters_updated_at, filters_closed_at=filters_closed_at, sort=sort)

List Recycled Checklists (Inspections)

Lists Recycled Checklist (Inspections) in a specified Project. See [Filtering on List Actions](https://developers.procore.com/documentation/filtering-on-list-actions) for information on using the filtering capabilities provided by this endpoint.

### Example


```python
import procore_sdk
from procore_sdk.models.checklist5 import Checklist5
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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_inspection_date = '2013-10-20' # date | Return item(s) with inspection date within the specified ISO 8601 date range. (optional)
    filters_inspection_type_id = [56] # List[int] | Array of Inspection Type IDs. Return item(s) associated with the specified Inspection Type IDs. (optional)
    filters_inspector_id = [56] # List[int] | Array of User IDs. Return item(s) where the specified User IDs are inspectors. (optional)
    filters_template_id = ['filters_template_id_example'] # List[str] | Array of Checklist Template IDs. Return item(s) associated to the specified Checklist Template IDs. (optional)
    filters_location_id = [56] # List[int] | Location ID. Returns item(s) with the specified Location ID or a range of Location IDs. (optional)
    filters_managed_equipment_id = 56 # int | Return item(s) with the specified Managed Equipment ID. (optional)
    filters_point_of_contact_id = [56] # List[int] | Array of User IDs. Return item(s) where the specified User IDs are the point of contact. (optional)
    filters_spec_section_id = [56] # List[int] | Array of Specification Section IDs. Return item(s) associated to the specified Specification Section IDs. (optional)
    filters_responsible_contractor_id = [56] # List[int] | Array of Vendor IDs. Return item(s) where the specified Vendor IDs are the responsible contractor. (optional)
    filters_closed_by_id = [56] # List[int] | Array of User IDs. Return item(s) closed by the specified User ID. (optional)
    filters_status = 56 # int | Return item(s) with the specified statuses (optional)
    filters_trade_id = 56 # int | Trade ID (optional)
    filters_query = 'filters_query_example' # str | Return item(s) containing search query (optional)
    filters_due_at = '2013-10-20T19:20:30+01:00' # datetime | Return item(s) due within the specified date range. (optional)
    filters_created_at = '2013-10-20' # date | Return item(s) created within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_closed_at = '2013-10-20' # date | Returns item(s) closed within the specified ISO 8601 datetime range. (optional)
    sort = 'sort_example' # str |  (optional)

    try:
        # List Recycled Checklists (Inspections)
        api_response = api_instance.rest_v10_projects_project_id_recycle_bin_checklist_lists_get(procore_company_id, project_id, page=page, per_page=per_page, filters_id=filters_id, filters_inspection_date=filters_inspection_date, filters_inspection_type_id=filters_inspection_type_id, filters_inspector_id=filters_inspector_id, filters_template_id=filters_template_id, filters_location_id=filters_location_id, filters_managed_equipment_id=filters_managed_equipment_id, filters_point_of_contact_id=filters_point_of_contact_id, filters_spec_section_id=filters_spec_section_id, filters_responsible_contractor_id=filters_responsible_contractor_id, filters_closed_by_id=filters_closed_by_id, filters_status=filters_status, filters_trade_id=filters_trade_id, filters_query=filters_query, filters_due_at=filters_due_at, filters_created_at=filters_created_at, filters_updated_at=filters_updated_at, filters_closed_at=filters_closed_at, sort=sort)
        print("The response of QualitySafetyInspectionsChecklistsApi->rest_v10_projects_project_id_recycle_bin_checklist_lists_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistsApi->rest_v10_projects_project_id_recycle_bin_checklist_lists_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_id** | [**List[int]**](int.md)| Return item(s) with the specified IDs. | [optional] 
 **filters_inspection_date** | **date**| Return item(s) with inspection date within the specified ISO 8601 date range. | [optional] 
 **filters_inspection_type_id** | [**List[int]**](int.md)| Array of Inspection Type IDs. Return item(s) associated with the specified Inspection Type IDs. | [optional] 
 **filters_inspector_id** | [**List[int]**](int.md)| Array of User IDs. Return item(s) where the specified User IDs are inspectors. | [optional] 
 **filters_template_id** | [**List[str]**](str.md)| Array of Checklist Template IDs. Return item(s) associated to the specified Checklist Template IDs. | [optional] 
 **filters_location_id** | [**List[int]**](int.md)| Location ID. Returns item(s) with the specified Location ID or a range of Location IDs. | [optional] 
 **filters_managed_equipment_id** | **int**| Return item(s) with the specified Managed Equipment ID. | [optional] 
 **filters_point_of_contact_id** | [**List[int]**](int.md)| Array of User IDs. Return item(s) where the specified User IDs are the point of contact. | [optional] 
 **filters_spec_section_id** | [**List[int]**](int.md)| Array of Specification Section IDs. Return item(s) associated to the specified Specification Section IDs. | [optional] 
 **filters_responsible_contractor_id** | [**List[int]**](int.md)| Array of Vendor IDs. Return item(s) where the specified Vendor IDs are the responsible contractor. | [optional] 
 **filters_closed_by_id** | [**List[int]**](int.md)| Array of User IDs. Return item(s) closed by the specified User ID. | [optional] 
 **filters_status** | **int**| Return item(s) with the specified statuses | [optional] 
 **filters_trade_id** | **int**| Trade ID | [optional] 
 **filters_query** | **str**| Return item(s) containing search query | [optional] 
 **filters_due_at** | **datetime**| Return item(s) due within the specified date range. | [optional] 
 **filters_created_at** | **date**| Return item(s) created within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_closed_at** | **date**| Returns item(s) closed within the specified ISO 8601 datetime range. | [optional] 
 **sort** | **str**|  | [optional] 

### Return type

[**List[Checklist5]**](Checklist5.md)

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
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_recycle_bin_checklist_lists_grouped_index_get**
> List[ChecklistListGroup] rest_v10_projects_project_id_recycle_bin_checklist_lists_grouped_index_get(procore_company_id, project_id, page=page, per_page=per_page, filters_id=filters_id, filters_inspection_date=filters_inspection_date, filters_inspection_type_id=filters_inspection_type_id, filters_inspector_id=filters_inspector_id, filters_list_template_id=filters_list_template_id, filters_location_id=filters_location_id, filters_managed_equipment_id=filters_managed_equipment_id, filters_point_of_contact_id=filters_point_of_contact_id, filters_spec_section_id=filters_spec_section_id, filters_responsible_contractor_id=filters_responsible_contractor_id, filters_closed_by_id=filters_closed_by_id, filters_status=filters_status, filters_trade_id=filters_trade_id, filters_query=filters_query, filters_due_at=filters_due_at, filters_created_at=filters_created_at, filters_updated_at=filters_updated_at, filters_closed_at=filters_closed_at, sort=sort, group_by=group_by)

List Grouped Recycled Checklists (Inspections)

Lists Recycled Checklist (Inspections) in a specified Project grouped by a specified attribute. By default the Checklists are grouped by template. See [Filtering on List Actions](https://developers.procore.com/documentation/filtering-on-list-actions) for information on using the filtering capabilities provided by this endpoint.

### Example


```python
import procore_sdk
from procore_sdk.models.checklist_list_group import ChecklistListGroup
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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_inspection_date = '2013-10-20' # date | Return item(s) with inspection date within the specified ISO 8601 date range. (optional)
    filters_inspection_type_id = [56] # List[int] | Array of Inspection Type IDs. Return item(s) associated with the specified Inspection Type IDs. (optional)
    filters_inspector_id = [56] # List[int] | Array of User IDs. Return item(s) where the specified User IDs are inspectors. (optional)
    filters_list_template_id = [56] # List[int] | Array of Checklist Template IDs. Return item(s) associated with the specified Checklist Template IDs. (optional)
    filters_location_id = [56] # List[int] | Location ID. Returns item(s) with the specified Location ID or a range of Location IDs. (optional)
    filters_managed_equipment_id = 56 # int | Return item(s) with the specified Managed Equipment ID. (optional)
    filters_point_of_contact_id = [56] # List[int] | Array of User IDs. Return item(s) where the specified User IDs are the point of contact. (optional)
    filters_spec_section_id = [56] # List[int] | Array of Specification Section IDs. Return item(s) associated to the specified Specification Section IDs. (optional)
    filters_responsible_contractor_id = [56] # List[int] | Array of Vendor IDs. Return item(s) where the specified Vendor IDs are the responsible contractor. (optional)
    filters_closed_by_id = [56] # List[int] | Array of User IDs. Return item(s) closed by the specified User ID. (optional)
    filters_status = 56 # int | Return item(s) with the specified statuses (optional)
    filters_trade_id = 56 # int | Trade ID (optional)
    filters_query = 'filters_query_example' # str | Return item(s) containing search query (optional)
    filters_due_at = '2013-10-20T19:20:30+01:00' # datetime | Return item(s) due within the specified date range. (optional)
    filters_created_at = '2013-10-20' # date | Return item(s) created within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_closed_at = '2013-10-20' # date | Returns item(s) closed within the specified ISO 8601 datetime range. (optional)
    sort = 'sort_example' # str |  (optional)
    group_by = 'group_by_example' # str |  (optional)

    try:
        # List Grouped Recycled Checklists (Inspections)
        api_response = api_instance.rest_v10_projects_project_id_recycle_bin_checklist_lists_grouped_index_get(procore_company_id, project_id, page=page, per_page=per_page, filters_id=filters_id, filters_inspection_date=filters_inspection_date, filters_inspection_type_id=filters_inspection_type_id, filters_inspector_id=filters_inspector_id, filters_list_template_id=filters_list_template_id, filters_location_id=filters_location_id, filters_managed_equipment_id=filters_managed_equipment_id, filters_point_of_contact_id=filters_point_of_contact_id, filters_spec_section_id=filters_spec_section_id, filters_responsible_contractor_id=filters_responsible_contractor_id, filters_closed_by_id=filters_closed_by_id, filters_status=filters_status, filters_trade_id=filters_trade_id, filters_query=filters_query, filters_due_at=filters_due_at, filters_created_at=filters_created_at, filters_updated_at=filters_updated_at, filters_closed_at=filters_closed_at, sort=sort, group_by=group_by)
        print("The response of QualitySafetyInspectionsChecklistsApi->rest_v10_projects_project_id_recycle_bin_checklist_lists_grouped_index_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistsApi->rest_v10_projects_project_id_recycle_bin_checklist_lists_grouped_index_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_id** | [**List[int]**](int.md)| Return item(s) with the specified IDs. | [optional] 
 **filters_inspection_date** | **date**| Return item(s) with inspection date within the specified ISO 8601 date range. | [optional] 
 **filters_inspection_type_id** | [**List[int]**](int.md)| Array of Inspection Type IDs. Return item(s) associated with the specified Inspection Type IDs. | [optional] 
 **filters_inspector_id** | [**List[int]**](int.md)| Array of User IDs. Return item(s) where the specified User IDs are inspectors. | [optional] 
 **filters_list_template_id** | [**List[int]**](int.md)| Array of Checklist Template IDs. Return item(s) associated with the specified Checklist Template IDs. | [optional] 
 **filters_location_id** | [**List[int]**](int.md)| Location ID. Returns item(s) with the specified Location ID or a range of Location IDs. | [optional] 
 **filters_managed_equipment_id** | **int**| Return item(s) with the specified Managed Equipment ID. | [optional] 
 **filters_point_of_contact_id** | [**List[int]**](int.md)| Array of User IDs. Return item(s) where the specified User IDs are the point of contact. | [optional] 
 **filters_spec_section_id** | [**List[int]**](int.md)| Array of Specification Section IDs. Return item(s) associated to the specified Specification Section IDs. | [optional] 
 **filters_responsible_contractor_id** | [**List[int]**](int.md)| Array of Vendor IDs. Return item(s) where the specified Vendor IDs are the responsible contractor. | [optional] 
 **filters_closed_by_id** | [**List[int]**](int.md)| Array of User IDs. Return item(s) closed by the specified User ID. | [optional] 
 **filters_status** | **int**| Return item(s) with the specified statuses | [optional] 
 **filters_trade_id** | **int**| Trade ID | [optional] 
 **filters_query** | **str**| Return item(s) containing search query | [optional] 
 **filters_due_at** | **datetime**| Return item(s) due within the specified date range. | [optional] 
 **filters_created_at** | **date**| Return item(s) created within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_closed_at** | **date**| Returns item(s) closed within the specified ISO 8601 datetime range. | [optional] 
 **sort** | **str**|  | [optional] 
 **group_by** | **str**|  | [optional] 

### Return type

[**List[ChecklistListGroup]**](ChecklistListGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Per-Page - Number of items retrieved per page <br>  * Total - Total number of items to be retrieved <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_recycle_bin_checklist_lists_id_get**
> Checklist5 rest_v10_projects_project_id_recycle_bin_checklist_lists_id_get(procore_company_id, id, project_id)

Show Recycled Checklist (Inspection)

Returns the specified Recycled Checklist (Inspection)

### Example


```python
import procore_sdk
from procore_sdk.models.checklist5 import Checklist5
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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | Checklist ID
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Show Recycled Checklist (Inspection)
        api_response = api_instance.rest_v10_projects_project_id_recycle_bin_checklist_lists_id_get(procore_company_id, id, project_id)
        print("The response of QualitySafetyInspectionsChecklistsApi->rest_v10_projects_project_id_recycle_bin_checklist_lists_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistsApi->rest_v10_projects_project_id_recycle_bin_checklist_lists_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| Checklist ID | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**Checklist5**](Checklist5.md)

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_recycle_bin_checklist_lists_id_restore_patch**
> rest_v10_projects_project_id_recycle_bin_checklist_lists_id_restore_patch(procore_company_id, id, project_id)

Restore Deleted Checklist (Inspection)

Restores a specified deleted Checklist (Inspection)

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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | Checklist ID
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Restore Deleted Checklist (Inspection)
        api_instance.rest_v10_projects_project_id_recycle_bin_checklist_lists_id_restore_patch(procore_company_id, id, project_id)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistsApi->rest_v10_projects_project_id_recycle_bin_checklist_lists_id_restore_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| Checklist ID | 
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
**404** | Not Found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v11_projects_project_id_checklist_lists_id_delete**
> rest_v11_projects_project_id_checklist_lists_id_delete(procore_company_id, id, project_id)

Delete Checklist (Inspection)

Deletes specified Checklist (Inspection)

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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | Checklist ID
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Delete Checklist (Inspection)
        api_instance.rest_v11_projects_project_id_checklist_lists_id_delete(procore_company_id, id, project_id)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistsApi->rest_v11_projects_project_id_checklist_lists_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| Checklist ID | 
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
**404** | Not Found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v11_projects_project_id_checklist_lists_id_patch**
> Checklist rest_v11_projects_project_id_checklist_lists_id_patch(procore_company_id, id, project_id, rest_v11_projects_project_id_checklist_lists_id_patch_request, run_configurable_validations=run_configurable_validations)

Update Checklist (Inspection)

Updates a specified Checklist (Inspection)

### Example


```python
import procore_sdk
from procore_sdk.models.checklist import Checklist
from procore_sdk.models.rest_v11_projects_project_id_checklist_lists_id_patch_request import RestV11ProjectsProjectIdChecklistListsIdPatchRequest
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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | Checklist ID
    project_id = 56 # int | Unique identifier for the project.
    rest_v11_projects_project_id_checklist_lists_id_patch_request = procore_sdk.RestV11ProjectsProjectIdChecklistListsIdPatchRequest() # RestV11ProjectsProjectIdChecklistListsIdPatchRequest | 
    run_configurable_validations = False # bool | If true, validations are run for the corresponding Configurable Field Set. (optional) (default to False)

    try:
        # Update Checklist (Inspection)
        api_response = api_instance.rest_v11_projects_project_id_checklist_lists_id_patch(procore_company_id, id, project_id, rest_v11_projects_project_id_checklist_lists_id_patch_request, run_configurable_validations=run_configurable_validations)
        print("The response of QualitySafetyInspectionsChecklistsApi->rest_v11_projects_project_id_checklist_lists_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistsApi->rest_v11_projects_project_id_checklist_lists_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| Checklist ID | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v11_projects_project_id_checklist_lists_id_patch_request** | [**RestV11ProjectsProjectIdChecklistListsIdPatchRequest**](RestV11ProjectsProjectIdChecklistListsIdPatchRequest.md)|  | 
 **run_configurable_validations** | **bool**| If true, validations are run for the corresponding Configurable Field Set. | [optional] [default to False]

### Return type

[**Checklist**](Checklist.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v11_projects_project_id_checklist_lists_post**
> Checklist rest_v11_projects_project_id_checklist_lists_post(procore_company_id, project_id, rest_v11_projects_project_id_checklist_lists_post_request, run_configurable_validations=run_configurable_validations)

Create Checklist (Inspection)

Creates an instance of Inspection in a given Project

### Example


```python
import procore_sdk
from procore_sdk.models.checklist import Checklist
from procore_sdk.models.rest_v11_projects_project_id_checklist_lists_post_request import RestV11ProjectsProjectIdChecklistListsPostRequest
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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rest_v11_projects_project_id_checklist_lists_post_request = procore_sdk.RestV11ProjectsProjectIdChecklistListsPostRequest() # RestV11ProjectsProjectIdChecklistListsPostRequest | 
    run_configurable_validations = False # bool | If true, validations are run for the corresponding Configurable Field Set. (optional) (default to False)

    try:
        # Create Checklist (Inspection)
        api_response = api_instance.rest_v11_projects_project_id_checklist_lists_post(procore_company_id, project_id, rest_v11_projects_project_id_checklist_lists_post_request, run_configurable_validations=run_configurable_validations)
        print("The response of QualitySafetyInspectionsChecklistsApi->rest_v11_projects_project_id_checklist_lists_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistsApi->rest_v11_projects_project_id_checklist_lists_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v11_projects_project_id_checklist_lists_post_request** | [**RestV11ProjectsProjectIdChecklistListsPostRequest**](RestV11ProjectsProjectIdChecklistListsPostRequest.md)|  | 
 **run_configurable_validations** | **bool**| If true, validations are run for the corresponding Configurable Field Set. | [optional] [default to False]

### Return type

[**Checklist**](Checklist.md)

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
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v11_projects_project_id_recycle_bin_checklist_lists_id_restore_patch**
> rest_v11_projects_project_id_recycle_bin_checklist_lists_id_restore_patch(procore_company_id, id, project_id)

Restore Deleted Checklist (Inspection)

Restores a specified deleted Checklist (Inspection)

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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | Checklist ID
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Restore Deleted Checklist (Inspection)
        api_instance.rest_v11_projects_project_id_recycle_bin_checklist_lists_id_restore_patch(procore_company_id, id, project_id)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistsApi->rest_v11_projects_project_id_recycle_bin_checklist_lists_id_restore_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| Checklist ID | 
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
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

