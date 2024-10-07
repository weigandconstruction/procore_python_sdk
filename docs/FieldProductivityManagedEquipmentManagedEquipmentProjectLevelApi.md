# procore_sdk.FieldProductivityManagedEquipmentManagedEquipmentProjectLevelApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_managed_equipment_get**](FieldProductivityManagedEquipmentManagedEquipmentProjectLevelApi.md#rest_v10_projects_project_id_managed_equipment_get) | **GET** /rest/v1.0/projects/{project_id}/managed_equipment | List all equipment
[**rest_v10_projects_project_id_managed_equipment_id_delete**](FieldProductivityManagedEquipmentManagedEquipmentProjectLevelApi.md#rest_v10_projects_project_id_managed_equipment_id_delete) | **DELETE** /rest/v1.0/projects/{project_id}/managed_equipment/{id} | Delete an equipment
[**rest_v10_projects_project_id_managed_equipment_id_get**](FieldProductivityManagedEquipmentManagedEquipmentProjectLevelApi.md#rest_v10_projects_project_id_managed_equipment_id_get) | **GET** /rest/v1.0/projects/{project_id}/managed_equipment/{id} | Show equipment
[**rest_v10_projects_project_id_managed_equipment_id_patch**](FieldProductivityManagedEquipmentManagedEquipmentProjectLevelApi.md#rest_v10_projects_project_id_managed_equipment_id_patch) | **PATCH** /rest/v1.0/projects/{project_id}/managed_equipment/{id} | Update an equipment
[**rest_v10_projects_project_id_managed_equipment_id_restore_patch**](FieldProductivityManagedEquipmentManagedEquipmentProjectLevelApi.md#rest_v10_projects_project_id_managed_equipment_id_restore_patch) | **PATCH** /rest/v1.0/projects/{project_id}/managed_equipment/{id}/restore | Restoring an equipment
[**rest_v10_projects_project_id_managed_equipment_ids_get**](FieldProductivityManagedEquipmentManagedEquipmentProjectLevelApi.md#rest_v10_projects_project_id_managed_equipment_ids_get) | **GET** /rest/v1.0/projects/{project_id}/managed_equipment/ids | List all project equipment IDs
[**rest_v10_projects_project_id_managed_equipment_post**](FieldProductivityManagedEquipmentManagedEquipmentProjectLevelApi.md#rest_v10_projects_project_id_managed_equipment_post) | **POST** /rest/v1.0/projects/{project_id}/managed_equipment | Create a new equipment
[**rest_v10_projects_project_id_managed_equipment_search_post**](FieldProductivityManagedEquipmentManagedEquipmentProjectLevelApi.md#rest_v10_projects_project_id_managed_equipment_search_post) | **POST** /rest/v1.0/projects/{project_id}/managed_equipment/search | Search all equipment


# **rest_v10_projects_project_id_managed_equipment_get**
> List[RestV10ProjectsProjectIdManagedEquipmentGet200ResponseInner] rest_v10_projects_project_id_managed_equipment_get(procore_company_id, project_id, page=page, per_page=per_page, filters_updated_at=filters_updated_at, filters_managed_equipment_id=filters_managed_equipment_id, filters_managed_equipment_category_id=filters_managed_equipment_category_id, filters_managed_equipment_type_id=filters_managed_equipment_type_id, filters_managed_equipment_make_id=filters_managed_equipment_make_id, filters_managed_equipment_model_id=filters_managed_equipment_model_id, filters_company_visible=filters_company_visible, filters_current_project_id=filters_current_project_id, filters_year=filters_year, filters_status=filters_status, filters_last_service_date=filters_last_service_date, filters_next_service_date=filters_next_service_date, filters_onsite=filters_onsite, filters_offsite=filters_offsite, filters_ownership=filters_ownership, filters_vendor_id=filters_vendor_id, filters_induction_status=filters_induction_status)

List all equipment

Return a list of all equipment with details for a specified project.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_managed_equipment_get200_response_inner import RestV10ProjectsProjectIdManagedEquipmentGet200ResponseInner
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
    api_instance = procore_sdk.FieldProductivityManagedEquipmentManagedEquipmentProjectLevelApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_managed_equipment_id = 56 # int | Return item(s) with the specified Managed Equipment ID. (optional)
    filters_managed_equipment_category_id = 56 # int | Return item(s) with the specified Managed Equipment Category ID. (optional)
    filters_managed_equipment_type_id = 56 # int | Return item(s) with the specified Managed Equipment Type ID. (optional)
    filters_managed_equipment_make_id = 56 # int | Return item(s) with the specified Managed Equipment Make ID. (optional)
    filters_managed_equipment_model_id = 56 # int | Return item(s) with the specified Managed Equipment Model ID. (optional)
    filters_company_visible = True # bool | If true, return item(s) with 'company visible' status. (optional)
    filters_current_project_id = 56 # int | Return item(s) with the specified current project ID. (optional)
    filters_year = 56 # int | Return item(s) with the specified year. (optional)
    filters_status = ['filters_status_example'] # List[str] | Returns item(s) matching the specified status value. (optional)
    filters_last_service_date = 'filters_last_service_date_example' # str | Return item(s) with a last service date within the specified ISO 8601 datetime range. (optional)
    filters_next_service_date = 'filters_next_service_date_example' # str | Return item(s) with a next service date within the specified ISO 8601 datetime range. (optional)
    filters_onsite = ['filters_onsite_example'] # List[str] | Onsite Dates. Returns item(s) with the specified range of onsite dates. (optional)
    filters_offsite = ['filters_offsite_example'] # List[str] | Offsite Dates. Returns item(s) with the specified range of offsite dates. (optional)
    filters_ownership = 'filters_ownership_example' # str | Returns only item(s) with the specified ownership value. Must be one of Owned, Rented, or Sub. (optional)
    filters_vendor_id = 56 # int | Return item(s) with the specified Vendor ID. (optional)
    filters_induction_status = False # bool | Returns item(s) with the specified inudction status. (optional) (default to False)

    try:
        # List all equipment
        api_response = api_instance.rest_v10_projects_project_id_managed_equipment_get(procore_company_id, project_id, page=page, per_page=per_page, filters_updated_at=filters_updated_at, filters_managed_equipment_id=filters_managed_equipment_id, filters_managed_equipment_category_id=filters_managed_equipment_category_id, filters_managed_equipment_type_id=filters_managed_equipment_type_id, filters_managed_equipment_make_id=filters_managed_equipment_make_id, filters_managed_equipment_model_id=filters_managed_equipment_model_id, filters_company_visible=filters_company_visible, filters_current_project_id=filters_current_project_id, filters_year=filters_year, filters_status=filters_status, filters_last_service_date=filters_last_service_date, filters_next_service_date=filters_next_service_date, filters_onsite=filters_onsite, filters_offsite=filters_offsite, filters_ownership=filters_ownership, filters_vendor_id=filters_vendor_id, filters_induction_status=filters_induction_status)
        print("The response of FieldProductivityManagedEquipmentManagedEquipmentProjectLevelApi->rest_v10_projects_project_id_managed_equipment_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityManagedEquipmentManagedEquipmentProjectLevelApi->rest_v10_projects_project_id_managed_equipment_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_managed_equipment_id** | **int**| Return item(s) with the specified Managed Equipment ID. | [optional] 
 **filters_managed_equipment_category_id** | **int**| Return item(s) with the specified Managed Equipment Category ID. | [optional] 
 **filters_managed_equipment_type_id** | **int**| Return item(s) with the specified Managed Equipment Type ID. | [optional] 
 **filters_managed_equipment_make_id** | **int**| Return item(s) with the specified Managed Equipment Make ID. | [optional] 
 **filters_managed_equipment_model_id** | **int**| Return item(s) with the specified Managed Equipment Model ID. | [optional] 
 **filters_company_visible** | **bool**| If true, return item(s) with &#39;company visible&#39; status. | [optional] 
 **filters_current_project_id** | **int**| Return item(s) with the specified current project ID. | [optional] 
 **filters_year** | **int**| Return item(s) with the specified year. | [optional] 
 **filters_status** | [**List[str]**](str.md)| Returns item(s) matching the specified status value. | [optional] 
 **filters_last_service_date** | **str**| Return item(s) with a last service date within the specified ISO 8601 datetime range. | [optional] 
 **filters_next_service_date** | **str**| Return item(s) with a next service date within the specified ISO 8601 datetime range. | [optional] 
 **filters_onsite** | [**List[str]**](str.md)| Onsite Dates. Returns item(s) with the specified range of onsite dates. | [optional] 
 **filters_offsite** | [**List[str]**](str.md)| Offsite Dates. Returns item(s) with the specified range of offsite dates. | [optional] 
 **filters_ownership** | **str**| Returns only item(s) with the specified ownership value. Must be one of Owned, Rented, or Sub. | [optional] 
 **filters_vendor_id** | **int**| Return item(s) with the specified Vendor ID. | [optional] 
 **filters_induction_status** | **bool**| Returns item(s) with the specified inudction status. | [optional] [default to False]

### Return type

[**List[RestV10ProjectsProjectIdManagedEquipmentGet200ResponseInner]**](RestV10ProjectsProjectIdManagedEquipmentGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Per-Page - Number of items retrieved per page <br>  * Total - Total number of items to be retrieved <br>  * Link - Link headers for the first, prev, next, and last link <br>  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_managed_equipment_id_delete**
> RestV10ProjectsProjectIdManagedEquipmentGet200ResponseInner rest_v10_projects_project_id_managed_equipment_id_delete(procore_company_id, project_id, id)

Delete an equipment

Deleting an equipment associated with the specified project.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_managed_equipment_get200_response_inner import RestV10ProjectsProjectIdManagedEquipmentGet200ResponseInner
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
    api_instance = procore_sdk.FieldProductivityManagedEquipmentManagedEquipmentProjectLevelApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Id of the equipment

    try:
        # Delete an equipment
        api_response = api_instance.rest_v10_projects_project_id_managed_equipment_id_delete(procore_company_id, project_id, id)
        print("The response of FieldProductivityManagedEquipmentManagedEquipmentProjectLevelApi->rest_v10_projects_project_id_managed_equipment_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityManagedEquipmentManagedEquipmentProjectLevelApi->rest_v10_projects_project_id_managed_equipment_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Id of the equipment | 

### Return type

[**RestV10ProjectsProjectIdManagedEquipmentGet200ResponseInner**](RestV10ProjectsProjectIdManagedEquipmentGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Equipment deleted |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_managed_equipment_id_get**
> RestV10ProjectsProjectIdManagedEquipmentGet200ResponseInner rest_v10_projects_project_id_managed_equipment_id_get(procore_company_id, project_id, id)

Show equipment

Return equipment detailed information.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_managed_equipment_get200_response_inner import RestV10ProjectsProjectIdManagedEquipmentGet200ResponseInner
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
    api_instance = procore_sdk.FieldProductivityManagedEquipmentManagedEquipmentProjectLevelApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | ID

    try:
        # Show equipment
        api_response = api_instance.rest_v10_projects_project_id_managed_equipment_id_get(procore_company_id, project_id, id)
        print("The response of FieldProductivityManagedEquipmentManagedEquipmentProjectLevelApi->rest_v10_projects_project_id_managed_equipment_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityManagedEquipmentManagedEquipmentProjectLevelApi->rest_v10_projects_project_id_managed_equipment_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| ID | 

### Return type

[**RestV10ProjectsProjectIdManagedEquipmentGet200ResponseInner**](RestV10ProjectsProjectIdManagedEquipmentGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_managed_equipment_id_patch**
> RestV10ProjectsProjectIdManagedEquipmentGet200ResponseInner rest_v10_projects_project_id_managed_equipment_id_patch(procore_company_id, project_id, id, managed_equipment_body)

Update an equipment

Updating an equipment associated with the specified project.

### Example


```python
import procore_sdk
from procore_sdk.models.managed_equipment_body import ManagedEquipmentBody
from procore_sdk.models.rest_v10_projects_project_id_managed_equipment_get200_response_inner import RestV10ProjectsProjectIdManagedEquipmentGet200ResponseInner
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
    api_instance = procore_sdk.FieldProductivityManagedEquipmentManagedEquipmentProjectLevelApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Id of the equipment
    managed_equipment_body = procore_sdk.ManagedEquipmentBody() # ManagedEquipmentBody | 

    try:
        # Update an equipment
        api_response = api_instance.rest_v10_projects_project_id_managed_equipment_id_patch(procore_company_id, project_id, id, managed_equipment_body)
        print("The response of FieldProductivityManagedEquipmentManagedEquipmentProjectLevelApi->rest_v10_projects_project_id_managed_equipment_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityManagedEquipmentManagedEquipmentProjectLevelApi->rest_v10_projects_project_id_managed_equipment_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Id of the equipment | 
 **managed_equipment_body** | [**ManagedEquipmentBody**](ManagedEquipmentBody.md)|  | 

### Return type

[**RestV10ProjectsProjectIdManagedEquipmentGet200ResponseInner**](RestV10ProjectsProjectIdManagedEquipmentGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Equipment updated |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**422** | Error updating an equipment |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_managed_equipment_id_restore_patch**
> RestV10ProjectsProjectIdManagedEquipmentGet200ResponseInner rest_v10_projects_project_id_managed_equipment_id_restore_patch(procore_company_id, project_id, id, managed_equipment_body)

Restoring an equipment

Restoring an equipment associated with the specified project.

### Example


```python
import procore_sdk
from procore_sdk.models.managed_equipment_body import ManagedEquipmentBody
from procore_sdk.models.rest_v10_projects_project_id_managed_equipment_get200_response_inner import RestV10ProjectsProjectIdManagedEquipmentGet200ResponseInner
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
    api_instance = procore_sdk.FieldProductivityManagedEquipmentManagedEquipmentProjectLevelApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Id of the equipment
    managed_equipment_body = procore_sdk.ManagedEquipmentBody() # ManagedEquipmentBody | 

    try:
        # Restoring an equipment
        api_response = api_instance.rest_v10_projects_project_id_managed_equipment_id_restore_patch(procore_company_id, project_id, id, managed_equipment_body)
        print("The response of FieldProductivityManagedEquipmentManagedEquipmentProjectLevelApi->rest_v10_projects_project_id_managed_equipment_id_restore_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityManagedEquipmentManagedEquipmentProjectLevelApi->rest_v10_projects_project_id_managed_equipment_id_restore_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Id of the equipment | 
 **managed_equipment_body** | [**ManagedEquipmentBody**](ManagedEquipmentBody.md)|  | 

### Return type

[**RestV10ProjectsProjectIdManagedEquipmentGet200ResponseInner**](RestV10ProjectsProjectIdManagedEquipmentGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Equipment restore |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**422** | Error restoring an equipment |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_managed_equipment_ids_get**
> List[int] rest_v10_projects_project_id_managed_equipment_ids_get(procore_company_id, project_id, page=page, per_page=per_page, filters_updated_at=filters_updated_at)

List all project equipment IDs

Return a list of all equipment IDs with details for a specified project.

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
    api_instance = procore_sdk.FieldProductivityManagedEquipmentManagedEquipmentProjectLevelApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)

    try:
        # List all project equipment IDs
        api_response = api_instance.rest_v10_projects_project_id_managed_equipment_ids_get(procore_company_id, project_id, page=page, per_page=per_page, filters_updated_at=filters_updated_at)
        print("The response of FieldProductivityManagedEquipmentManagedEquipmentProjectLevelApi->rest_v10_projects_project_id_managed_equipment_ids_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityManagedEquipmentManagedEquipmentProjectLevelApi->rest_v10_projects_project_id_managed_equipment_ids_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 

### Return type

**List[int]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Per-Page - Number of items retrieved per page <br>  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_managed_equipment_post**
> RestV10ProjectsProjectIdManagedEquipmentGet200ResponseInner rest_v10_projects_project_id_managed_equipment_post(procore_company_id, project_id, managed_equipment_body)

Create a new equipment

Create a new equipment associated with the specified project.

### Example


```python
import procore_sdk
from procore_sdk.models.managed_equipment_body import ManagedEquipmentBody
from procore_sdk.models.rest_v10_projects_project_id_managed_equipment_get200_response_inner import RestV10ProjectsProjectIdManagedEquipmentGet200ResponseInner
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
    api_instance = procore_sdk.FieldProductivityManagedEquipmentManagedEquipmentProjectLevelApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    managed_equipment_body = procore_sdk.ManagedEquipmentBody() # ManagedEquipmentBody | 

    try:
        # Create a new equipment
        api_response = api_instance.rest_v10_projects_project_id_managed_equipment_post(procore_company_id, project_id, managed_equipment_body)
        print("The response of FieldProductivityManagedEquipmentManagedEquipmentProjectLevelApi->rest_v10_projects_project_id_managed_equipment_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityManagedEquipmentManagedEquipmentProjectLevelApi->rest_v10_projects_project_id_managed_equipment_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **managed_equipment_body** | [**ManagedEquipmentBody**](ManagedEquipmentBody.md)|  | 

### Return type

[**RestV10ProjectsProjectIdManagedEquipmentGet200ResponseInner**](RestV10ProjectsProjectIdManagedEquipmentGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Equipment Created Succesfully |  -  |
**403** | Forbidden |  -  |
**422** | Error creating an equipment |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_managed_equipment_search_post**
> List[RestV10ProjectsProjectIdManagedEquipmentGet200ResponseInner] rest_v10_projects_project_id_managed_equipment_search_post(procore_company_id, project_id, page=page, per_page=per_page, filters_updated_at=filters_updated_at, filters_managed_equipment_id=filters_managed_equipment_id, filters_managed_equipment_category_id=filters_managed_equipment_category_id, filters_managed_equipment_type_id=filters_managed_equipment_type_id, filters_managed_equipment_make_id=filters_managed_equipment_make_id, filters_managed_equipment_model_id=filters_managed_equipment_model_id, filters_company_visible=filters_company_visible, filters_current_project_id=filters_current_project_id, filters_year=filters_year, filters_status=filters_status, filters_last_service_date=filters_last_service_date, filters_next_service_date=filters_next_service_date, search_keyword=search_keyword, filters_onsite=filters_onsite, filters_offsite=filters_offsite, filters_ownership=filters_ownership, filters_vendor_id=filters_vendor_id, filters_induction_status=filters_induction_status)

Search all equipment

Return a list of all searched equipment with details for a specified project.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_managed_equipment_get200_response_inner import RestV10ProjectsProjectIdManagedEquipmentGet200ResponseInner
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
    api_instance = procore_sdk.FieldProductivityManagedEquipmentManagedEquipmentProjectLevelApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_managed_equipment_id = 56 # int | Return item(s) with the specified Managed Equipment ID. (optional)
    filters_managed_equipment_category_id = 56 # int | Return item(s) with the specified Managed Equipment Category ID. (optional)
    filters_managed_equipment_type_id = 56 # int | Return item(s) with the specified Managed Equipment Type ID. (optional)
    filters_managed_equipment_make_id = 56 # int | Return item(s) with the specified Managed Equipment Make ID. (optional)
    filters_managed_equipment_model_id = 56 # int | Return item(s) with the specified Managed Equipment Model ID. (optional)
    filters_company_visible = True # bool | If true, return item(s) with 'company visible' status. (optional)
    filters_current_project_id = 56 # int | Return item(s) with the specified current project ID. (optional)
    filters_year = 56 # int | Return item(s) with the specified year. (optional)
    filters_status = ['filters_status_example'] # List[str] | Returns item(s) matching the specified status value. (optional)
    filters_last_service_date = 'filters_last_service_date_example' # str | Return item(s) with a last service date within the specified ISO 8601 datetime range. (optional)
    filters_next_service_date = 'filters_next_service_date_example' # str | Return item(s) with a next service date within the specified ISO 8601 datetime range. (optional)
    search_keyword = 'search_keyword_example' # str | Search keyword to search Project Managed Equipment. (optional)
    filters_onsite = ['filters_onsite_example'] # List[str] | Onsite Dates. Returns item(s) with the specified range of onsite dates. (optional)
    filters_offsite = ['filters_offsite_example'] # List[str] | Offsite Dates. Returns item(s) with the specified range of offsite dates. (optional)
    filters_ownership = 'filters_ownership_example' # str | Returns only item(s) with the specified ownership value. Must be one of Owned, Rented, or Sub. (optional)
    filters_vendor_id = 56 # int | Return item(s) with the specified Vendor ID. (optional)
    filters_induction_status = False # bool | Returns item(s) with the specified inudction status. (optional) (default to False)

    try:
        # Search all equipment
        api_response = api_instance.rest_v10_projects_project_id_managed_equipment_search_post(procore_company_id, project_id, page=page, per_page=per_page, filters_updated_at=filters_updated_at, filters_managed_equipment_id=filters_managed_equipment_id, filters_managed_equipment_category_id=filters_managed_equipment_category_id, filters_managed_equipment_type_id=filters_managed_equipment_type_id, filters_managed_equipment_make_id=filters_managed_equipment_make_id, filters_managed_equipment_model_id=filters_managed_equipment_model_id, filters_company_visible=filters_company_visible, filters_current_project_id=filters_current_project_id, filters_year=filters_year, filters_status=filters_status, filters_last_service_date=filters_last_service_date, filters_next_service_date=filters_next_service_date, search_keyword=search_keyword, filters_onsite=filters_onsite, filters_offsite=filters_offsite, filters_ownership=filters_ownership, filters_vendor_id=filters_vendor_id, filters_induction_status=filters_induction_status)
        print("The response of FieldProductivityManagedEquipmentManagedEquipmentProjectLevelApi->rest_v10_projects_project_id_managed_equipment_search_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityManagedEquipmentManagedEquipmentProjectLevelApi->rest_v10_projects_project_id_managed_equipment_search_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_managed_equipment_id** | **int**| Return item(s) with the specified Managed Equipment ID. | [optional] 
 **filters_managed_equipment_category_id** | **int**| Return item(s) with the specified Managed Equipment Category ID. | [optional] 
 **filters_managed_equipment_type_id** | **int**| Return item(s) with the specified Managed Equipment Type ID. | [optional] 
 **filters_managed_equipment_make_id** | **int**| Return item(s) with the specified Managed Equipment Make ID. | [optional] 
 **filters_managed_equipment_model_id** | **int**| Return item(s) with the specified Managed Equipment Model ID. | [optional] 
 **filters_company_visible** | **bool**| If true, return item(s) with &#39;company visible&#39; status. | [optional] 
 **filters_current_project_id** | **int**| Return item(s) with the specified current project ID. | [optional] 
 **filters_year** | **int**| Return item(s) with the specified year. | [optional] 
 **filters_status** | [**List[str]**](str.md)| Returns item(s) matching the specified status value. | [optional] 
 **filters_last_service_date** | **str**| Return item(s) with a last service date within the specified ISO 8601 datetime range. | [optional] 
 **filters_next_service_date** | **str**| Return item(s) with a next service date within the specified ISO 8601 datetime range. | [optional] 
 **search_keyword** | **str**| Search keyword to search Project Managed Equipment. | [optional] 
 **filters_onsite** | [**List[str]**](str.md)| Onsite Dates. Returns item(s) with the specified range of onsite dates. | [optional] 
 **filters_offsite** | [**List[str]**](str.md)| Offsite Dates. Returns item(s) with the specified range of offsite dates. | [optional] 
 **filters_ownership** | **str**| Returns only item(s) with the specified ownership value. Must be one of Owned, Rented, or Sub. | [optional] 
 **filters_vendor_id** | **int**| Return item(s) with the specified Vendor ID. | [optional] 
 **filters_induction_status** | **bool**| Returns item(s) with the specified inudction status. | [optional] [default to False]

### Return type

[**List[RestV10ProjectsProjectIdManagedEquipmentGet200ResponseInner]**](RestV10ProjectsProjectIdManagedEquipmentGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Per-Page - Number of items retrieved per page <br>  * Total - Total number of items to be retrieved <br>  * Link - Link headers for the first, prev, next, and last link <br>  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

