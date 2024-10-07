# procore_sdk.FieldProductivityManagedEquipmentManagedEquipmentCompanyLevelApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_managed_equipment_bulk_destroy_delete**](FieldProductivityManagedEquipmentManagedEquipmentCompanyLevelApi.md#rest_v10_companies_company_id_managed_equipment_bulk_destroy_delete) | **DELETE** /rest/v1.0/companies/{company_id}/managed_equipment/bulk_destroy | Bulk Delete Managed Equipment
[**rest_v10_companies_company_id_managed_equipment_bulk_restore_patch**](FieldProductivityManagedEquipmentManagedEquipmentCompanyLevelApi.md#rest_v10_companies_company_id_managed_equipment_bulk_restore_patch) | **PATCH** /rest/v1.0/companies/{company_id}/managed_equipment/bulk_restore | Bulk Retrieve Managed Equipment
[**rest_v10_companies_company_id_managed_equipment_get**](FieldProductivityManagedEquipmentManagedEquipmentCompanyLevelApi.md#rest_v10_companies_company_id_managed_equipment_get) | **GET** /rest/v1.0/companies/{company_id}/managed_equipment | List all Equipment
[**rest_v10_companies_company_id_managed_equipment_id_change_history_get**](FieldProductivityManagedEquipmentManagedEquipmentCompanyLevelApi.md#rest_v10_companies_company_id_managed_equipment_id_change_history_get) | **GET** /rest/v1.0/companies/{company_id}/managed_equipment/{id}/change_history | Show Equipment Change History
[**rest_v10_companies_company_id_managed_equipment_id_delete**](FieldProductivityManagedEquipmentManagedEquipmentCompanyLevelApi.md#rest_v10_companies_company_id_managed_equipment_id_delete) | **DELETE** /rest/v1.0/companies/{company_id}/managed_equipment/{id} | Delete Equipment
[**rest_v10_companies_company_id_managed_equipment_id_get**](FieldProductivityManagedEquipmentManagedEquipmentCompanyLevelApi.md#rest_v10_companies_company_id_managed_equipment_id_get) | **GET** /rest/v1.0/companies/{company_id}/managed_equipment/{id} | Show Equipment
[**rest_v10_companies_company_id_managed_equipment_id_patch**](FieldProductivityManagedEquipmentManagedEquipmentCompanyLevelApi.md#rest_v10_companies_company_id_managed_equipment_id_patch) | **PATCH** /rest/v1.0/companies/{company_id}/managed_equipment/{id} | Update Equipment
[**rest_v10_companies_company_id_managed_equipment_id_restore_patch**](FieldProductivityManagedEquipmentManagedEquipmentCompanyLevelApi.md#rest_v10_companies_company_id_managed_equipment_id_restore_patch) | **PATCH** /rest/v1.0/companies/{company_id}/managed_equipment/{id}/restore | Retrieve Equipment
[**rest_v10_companies_company_id_managed_equipment_id_update_deleted_equipment_serial_number_patch**](FieldProductivityManagedEquipmentManagedEquipmentCompanyLevelApi.md#rest_v10_companies_company_id_managed_equipment_id_update_deleted_equipment_serial_number_patch) | **PATCH** /rest/v1.0/companies/{company_id}/managed_equipment/{id}/update_deleted_equipment_serial_number | Update Deleted Equipment Serial Number
[**rest_v10_companies_company_id_managed_equipment_post**](FieldProductivityManagedEquipmentManagedEquipmentCompanyLevelApi.md#rest_v10_companies_company_id_managed_equipment_post) | **POST** /rest/v1.0/companies/{company_id}/managed_equipment | Create Equipment
[**rest_v10_companies_company_id_managed_equipment_query_post**](FieldProductivityManagedEquipmentManagedEquipmentCompanyLevelApi.md#rest_v10_companies_company_id_managed_equipment_query_post) | **POST** /rest/v1.0/companies/{company_id}/managed_equipment/query | Search all equipment
[**rest_v10_companies_company_id_managed_equipment_setup_managed_equipment_dependents_post**](FieldProductivityManagedEquipmentManagedEquipmentCompanyLevelApi.md#rest_v10_companies_company_id_managed_equipment_setup_managed_equipment_dependents_post) | **POST** /rest/v1.0/companies/{company_id}/managed_equipment/setup_managed_equipment_dependents | Setup Managed Equipment Taxonomy
[**rest_v10_companies_company_id_managed_equipment_user_permissions_get**](FieldProductivityManagedEquipmentManagedEquipmentCompanyLevelApi.md#rest_v10_companies_company_id_managed_equipment_user_permissions_get) | **GET** /rest/v1.0/companies/{company_id}/managed_equipment/user_permissions | List all Company Managed Equipment User Permissions
[**rest_v10_companies_company_id_managed_equipment_user_permissions_patch**](FieldProductivityManagedEquipmentManagedEquipmentCompanyLevelApi.md#rest_v10_companies_company_id_managed_equipment_user_permissions_patch) | **PATCH** /rest/v1.0/companies/{company_id}/managed_equipment/user_permissions | Update User Permission


# **rest_v10_companies_company_id_managed_equipment_bulk_destroy_delete**
> List[RestV10ProjectsProjectIdManagedEquipmentGet200ResponseInner] rest_v10_companies_company_id_managed_equipment_bulk_destroy_delete(procore_company_id, company_id, rest_v10_companies_company_id_managed_equipment_bulk_destroy_delete_request)

Bulk Delete Managed Equipment

Delete multiple Managed Equipment with one request.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_managed_equipment_bulk_destroy_delete_request import RestV10CompaniesCompanyIdManagedEquipmentBulkDestroyDeleteRequest
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
    api_instance = procore_sdk.FieldProductivityManagedEquipmentManagedEquipmentCompanyLevelApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    rest_v10_companies_company_id_managed_equipment_bulk_destroy_delete_request = procore_sdk.RestV10CompaniesCompanyIdManagedEquipmentBulkDestroyDeleteRequest() # RestV10CompaniesCompanyIdManagedEquipmentBulkDestroyDeleteRequest | 

    try:
        # Bulk Delete Managed Equipment
        api_response = api_instance.rest_v10_companies_company_id_managed_equipment_bulk_destroy_delete(procore_company_id, company_id, rest_v10_companies_company_id_managed_equipment_bulk_destroy_delete_request)
        print("The response of FieldProductivityManagedEquipmentManagedEquipmentCompanyLevelApi->rest_v10_companies_company_id_managed_equipment_bulk_destroy_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityManagedEquipmentManagedEquipmentCompanyLevelApi->rest_v10_companies_company_id_managed_equipment_bulk_destroy_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **rest_v10_companies_company_id_managed_equipment_bulk_destroy_delete_request** | [**RestV10CompaniesCompanyIdManagedEquipmentBulkDestroyDeleteRequest**](RestV10CompaniesCompanyIdManagedEquipmentBulkDestroyDeleteRequest.md)|  | 

### Return type

[**List[RestV10ProjectsProjectIdManagedEquipmentGet200ResponseInner]**](RestV10ProjectsProjectIdManagedEquipmentGet200ResponseInner.md)

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
**422** | Unprocessable Entity |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_managed_equipment_bulk_restore_patch**
> List[RestV10ProjectsProjectIdManagedEquipmentGet200ResponseInner] rest_v10_companies_company_id_managed_equipment_bulk_restore_patch(procore_company_id, company_id, rest_v10_companies_company_id_managed_equipment_bulk_restore_patch_request)

Bulk Retrieve Managed Equipment

Restore multiple Managed Equipment with one request.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_managed_equipment_bulk_restore_patch_request import RestV10CompaniesCompanyIdManagedEquipmentBulkRestorePatchRequest
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
    api_instance = procore_sdk.FieldProductivityManagedEquipmentManagedEquipmentCompanyLevelApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    rest_v10_companies_company_id_managed_equipment_bulk_restore_patch_request = procore_sdk.RestV10CompaniesCompanyIdManagedEquipmentBulkRestorePatchRequest() # RestV10CompaniesCompanyIdManagedEquipmentBulkRestorePatchRequest | 

    try:
        # Bulk Retrieve Managed Equipment
        api_response = api_instance.rest_v10_companies_company_id_managed_equipment_bulk_restore_patch(procore_company_id, company_id, rest_v10_companies_company_id_managed_equipment_bulk_restore_patch_request)
        print("The response of FieldProductivityManagedEquipmentManagedEquipmentCompanyLevelApi->rest_v10_companies_company_id_managed_equipment_bulk_restore_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityManagedEquipmentManagedEquipmentCompanyLevelApi->rest_v10_companies_company_id_managed_equipment_bulk_restore_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **rest_v10_companies_company_id_managed_equipment_bulk_restore_patch_request** | [**RestV10CompaniesCompanyIdManagedEquipmentBulkRestorePatchRequest**](RestV10CompaniesCompanyIdManagedEquipmentBulkRestorePatchRequest.md)|  | 

### Return type

[**List[RestV10ProjectsProjectIdManagedEquipmentGet200ResponseInner]**](RestV10ProjectsProjectIdManagedEquipmentGet200ResponseInner.md)

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
**422** | Unprocessable Entity |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_managed_equipment_get**
> List[RestV10ProjectsProjectIdManagedEquipmentGet200ResponseInner] rest_v10_companies_company_id_managed_equipment_get(procore_company_id, company_id, page=page, per_page=per_page, filters_updated_at=filters_updated_at, filters_managed_equipment_id=filters_managed_equipment_id, filters_managed_equipment_category_id=filters_managed_equipment_category_id, filters_managed_equipment_type_id=filters_managed_equipment_type_id, filters_managed_equipment_make_id=filters_managed_equipment_make_id, filters_managed_equipment_model_id=filters_managed_equipment_model_id, filters_company_visible=filters_company_visible, filters_current_project_id=filters_current_project_id, filters_year=filters_year, filters_status=filters_status, filters_last_service_date=filters_last_service_date, filters_next_service_date=filters_next_service_date)

List all Equipment

Return a list of all Equipment with details for a specified company.

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
    api_instance = procore_sdk.FieldProductivityManagedEquipmentManagedEquipmentCompanyLevelApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
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

    try:
        # List all Equipment
        api_response = api_instance.rest_v10_companies_company_id_managed_equipment_get(procore_company_id, company_id, page=page, per_page=per_page, filters_updated_at=filters_updated_at, filters_managed_equipment_id=filters_managed_equipment_id, filters_managed_equipment_category_id=filters_managed_equipment_category_id, filters_managed_equipment_type_id=filters_managed_equipment_type_id, filters_managed_equipment_make_id=filters_managed_equipment_make_id, filters_managed_equipment_model_id=filters_managed_equipment_model_id, filters_company_visible=filters_company_visible, filters_current_project_id=filters_current_project_id, filters_year=filters_year, filters_status=filters_status, filters_last_service_date=filters_last_service_date, filters_next_service_date=filters_next_service_date)
        print("The response of FieldProductivityManagedEquipmentManagedEquipmentCompanyLevelApi->rest_v10_companies_company_id_managed_equipment_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityManagedEquipmentManagedEquipmentCompanyLevelApi->rest_v10_companies_company_id_managed_equipment_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
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

# **rest_v10_companies_company_id_managed_equipment_id_change_history_get**
> ManagedEquipmentChangeHistory rest_v10_companies_company_id_managed_equipment_id_change_history_get(procore_company_id, company_id, id)

Show Equipment Change History

Return Equipment change history detailed information.

### Example


```python
import procore_sdk
from procore_sdk.models.managed_equipment_change_history import ManagedEquipmentChangeHistory
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
    api_instance = procore_sdk.FieldProductivityManagedEquipmentManagedEquipmentCompanyLevelApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | ID

    try:
        # Show Equipment Change History
        api_response = api_instance.rest_v10_companies_company_id_managed_equipment_id_change_history_get(procore_company_id, company_id, id)
        print("The response of FieldProductivityManagedEquipmentManagedEquipmentCompanyLevelApi->rest_v10_companies_company_id_managed_equipment_id_change_history_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityManagedEquipmentManagedEquipmentCompanyLevelApi->rest_v10_companies_company_id_managed_equipment_id_change_history_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| ID | 

### Return type

[**ManagedEquipmentChangeHistory**](ManagedEquipmentChangeHistory.md)

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

# **rest_v10_companies_company_id_managed_equipment_id_delete**
> RestV10ProjectsProjectIdManagedEquipmentGet200ResponseInner rest_v10_companies_company_id_managed_equipment_id_delete(procore_company_id, company_id, id)

Delete Equipment

Deleting a piece of Equipment

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
    api_instance = procore_sdk.FieldProductivityManagedEquipmentManagedEquipmentCompanyLevelApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | Id of the Equipment

    try:
        # Delete Equipment
        api_response = api_instance.rest_v10_companies_company_id_managed_equipment_id_delete(procore_company_id, company_id, id)
        print("The response of FieldProductivityManagedEquipmentManagedEquipmentCompanyLevelApi->rest_v10_companies_company_id_managed_equipment_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityManagedEquipmentManagedEquipmentCompanyLevelApi->rest_v10_companies_company_id_managed_equipment_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| Id of the Equipment | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_managed_equipment_id_get**
> RestV10ProjectsProjectIdManagedEquipmentGet200ResponseInner rest_v10_companies_company_id_managed_equipment_id_get(procore_company_id, company_id, id)

Show Equipment

Return Equipment detailed information.

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
    api_instance = procore_sdk.FieldProductivityManagedEquipmentManagedEquipmentCompanyLevelApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | ID

    try:
        # Show Equipment
        api_response = api_instance.rest_v10_companies_company_id_managed_equipment_id_get(procore_company_id, company_id, id)
        print("The response of FieldProductivityManagedEquipmentManagedEquipmentCompanyLevelApi->rest_v10_companies_company_id_managed_equipment_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityManagedEquipmentManagedEquipmentCompanyLevelApi->rest_v10_companies_company_id_managed_equipment_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
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

# **rest_v10_companies_company_id_managed_equipment_id_patch**
> RestV10ProjectsProjectIdManagedEquipmentGet200ResponseInner rest_v10_companies_company_id_managed_equipment_id_patch(procore_company_id, company_id, id, managed_equipment_body)

Update Equipment

Updating a piece of Equipment

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
    api_instance = procore_sdk.FieldProductivityManagedEquipmentManagedEquipmentCompanyLevelApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | Id of the Equipment
    managed_equipment_body = procore_sdk.ManagedEquipmentBody() # ManagedEquipmentBody | 

    try:
        # Update Equipment
        api_response = api_instance.rest_v10_companies_company_id_managed_equipment_id_patch(procore_company_id, company_id, id, managed_equipment_body)
        print("The response of FieldProductivityManagedEquipmentManagedEquipmentCompanyLevelApi->rest_v10_companies_company_id_managed_equipment_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityManagedEquipmentManagedEquipmentCompanyLevelApi->rest_v10_companies_company_id_managed_equipment_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| Id of the Equipment | 
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
**422** | Error updating a piece of Equipment |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_managed_equipment_id_restore_patch**
> RestV10ProjectsProjectIdManagedEquipmentGet200ResponseInner rest_v10_companies_company_id_managed_equipment_id_restore_patch(procore_company_id, company_id, id, managed_equipment_body)

Retrieve Equipment

Restore a piece of Equipment

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
    api_instance = procore_sdk.FieldProductivityManagedEquipmentManagedEquipmentCompanyLevelApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | Id of the Equipment
    managed_equipment_body = procore_sdk.ManagedEquipmentBody() # ManagedEquipmentBody | 

    try:
        # Retrieve Equipment
        api_response = api_instance.rest_v10_companies_company_id_managed_equipment_id_restore_patch(procore_company_id, company_id, id, managed_equipment_body)
        print("The response of FieldProductivityManagedEquipmentManagedEquipmentCompanyLevelApi->rest_v10_companies_company_id_managed_equipment_id_restore_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityManagedEquipmentManagedEquipmentCompanyLevelApi->rest_v10_companies_company_id_managed_equipment_id_restore_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| Id of the Equipment | 
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
**200** | Equipment restored |  -  |
**422** | Error restoring a piece of Equipment |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_managed_equipment_id_update_deleted_equipment_serial_number_patch**
> RestV10ProjectsProjectIdManagedEquipmentGet200ResponseInner rest_v10_companies_company_id_managed_equipment_id_update_deleted_equipment_serial_number_patch(procore_company_id, company_id, id, managed_equipment_serial_number_update_body)

Update Deleted Equipment Serial Number

Update a serial number for a deleted piece of Equipment

### Example


```python
import procore_sdk
from procore_sdk.models.managed_equipment_serial_number_update_body import ManagedEquipmentSerialNumberUpdateBody
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
    api_instance = procore_sdk.FieldProductivityManagedEquipmentManagedEquipmentCompanyLevelApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | Id of the Equipment
    managed_equipment_serial_number_update_body = procore_sdk.ManagedEquipmentSerialNumberUpdateBody() # ManagedEquipmentSerialNumberUpdateBody | 

    try:
        # Update Deleted Equipment Serial Number
        api_response = api_instance.rest_v10_companies_company_id_managed_equipment_id_update_deleted_equipment_serial_number_patch(procore_company_id, company_id, id, managed_equipment_serial_number_update_body)
        print("The response of FieldProductivityManagedEquipmentManagedEquipmentCompanyLevelApi->rest_v10_companies_company_id_managed_equipment_id_update_deleted_equipment_serial_number_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityManagedEquipmentManagedEquipmentCompanyLevelApi->rest_v10_companies_company_id_managed_equipment_id_update_deleted_equipment_serial_number_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| Id of the Equipment | 
 **managed_equipment_serial_number_update_body** | [**ManagedEquipmentSerialNumberUpdateBody**](ManagedEquipmentSerialNumberUpdateBody.md)|  | 

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
**200** | Equipment serial number updated |  -  |
**422** | Error updating serial number for a deleted piece of Equipment |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_managed_equipment_post**
> RestV10ProjectsProjectIdManagedEquipmentGet200ResponseInner rest_v10_companies_company_id_managed_equipment_post(procore_company_id, company_id, managed_equipment_body)

Create Equipment

Create a new Equipment associated with the specified company.

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
    api_instance = procore_sdk.FieldProductivityManagedEquipmentManagedEquipmentCompanyLevelApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    managed_equipment_body = procore_sdk.ManagedEquipmentBody() # ManagedEquipmentBody | 

    try:
        # Create Equipment
        api_response = api_instance.rest_v10_companies_company_id_managed_equipment_post(procore_company_id, company_id, managed_equipment_body)
        print("The response of FieldProductivityManagedEquipmentManagedEquipmentCompanyLevelApi->rest_v10_companies_company_id_managed_equipment_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityManagedEquipmentManagedEquipmentCompanyLevelApi->rest_v10_companies_company_id_managed_equipment_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
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
**422** | Error creating a piece Equipment |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_managed_equipment_query_post**
> List[RestV10ProjectsProjectIdManagedEquipmentGet200ResponseInner] rest_v10_companies_company_id_managed_equipment_query_post(procore_company_id, company_id, page=page, per_page=per_page, filters_updated_at=filters_updated_at, filters_managed_equipment_id=filters_managed_equipment_id, filters_managed_equipment_category_id=filters_managed_equipment_category_id, filters_managed_equipment_type_id=filters_managed_equipment_type_id, filters_managed_equipment_make_id=filters_managed_equipment_make_id, filters_managed_equipment_model_id=filters_managed_equipment_model_id, filters_company_visible=filters_company_visible, filters_current_project_id=filters_current_project_id, filters_year=filters_year, filters_status=filters_status, filters_last_service_date=filters_last_service_date, filters_next_service_date=filters_next_service_date, search_keyword=search_keyword)

Search all equipment

Return a list of all searched equipment with details for a specified company.

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
    api_instance = procore_sdk.FieldProductivityManagedEquipmentManagedEquipmentCompanyLevelApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
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

    try:
        # Search all equipment
        api_response = api_instance.rest_v10_companies_company_id_managed_equipment_query_post(procore_company_id, company_id, page=page, per_page=per_page, filters_updated_at=filters_updated_at, filters_managed_equipment_id=filters_managed_equipment_id, filters_managed_equipment_category_id=filters_managed_equipment_category_id, filters_managed_equipment_type_id=filters_managed_equipment_type_id, filters_managed_equipment_make_id=filters_managed_equipment_make_id, filters_managed_equipment_model_id=filters_managed_equipment_model_id, filters_company_visible=filters_company_visible, filters_current_project_id=filters_current_project_id, filters_year=filters_year, filters_status=filters_status, filters_last_service_date=filters_last_service_date, filters_next_service_date=filters_next_service_date, search_keyword=search_keyword)
        print("The response of FieldProductivityManagedEquipmentManagedEquipmentCompanyLevelApi->rest_v10_companies_company_id_managed_equipment_query_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityManagedEquipmentManagedEquipmentCompanyLevelApi->rest_v10_companies_company_id_managed_equipment_query_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
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

# **rest_v10_companies_company_id_managed_equipment_setup_managed_equipment_dependents_post**
> rest_v10_companies_company_id_managed_equipment_setup_managed_equipment_dependents_post(procore_company_id, company_id, managed_equipment_dependent_body)

Setup Managed Equipment Taxonomy

Setup Managed Equipment Taxonomy with the specified company.

### Example


```python
import procore_sdk
from procore_sdk.models.managed_equipment_dependent_body import ManagedEquipmentDependentBody
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
    api_instance = procore_sdk.FieldProductivityManagedEquipmentManagedEquipmentCompanyLevelApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    managed_equipment_dependent_body = procore_sdk.ManagedEquipmentDependentBody() # ManagedEquipmentDependentBody | 

    try:
        # Setup Managed Equipment Taxonomy
        api_instance.rest_v10_companies_company_id_managed_equipment_setup_managed_equipment_dependents_post(procore_company_id, company_id, managed_equipment_dependent_body)
    except Exception as e:
        print("Exception when calling FieldProductivityManagedEquipmentManagedEquipmentCompanyLevelApi->rest_v10_companies_company_id_managed_equipment_setup_managed_equipment_dependents_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **managed_equipment_dependent_body** | [**ManagedEquipmentDependentBody**](ManagedEquipmentDependentBody.md)|  | 

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
**200** | OK |  -  |
**422** | Error creating Managed Equipment taxonomy |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_managed_equipment_user_permissions_get**
> List[CompanyManagedEquipmentUserPermission] rest_v10_companies_company_id_managed_equipment_user_permissions_get(procore_company_id, company_id, page=page, per_page=per_page)

List all Company Managed Equipment User Permissions

Return a list of allCompany Managed Equipment User Permissions for a specified company.

### Example


```python
import procore_sdk
from procore_sdk.models.company_managed_equipment_user_permission import CompanyManagedEquipmentUserPermission
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
    api_instance = procore_sdk.FieldProductivityManagedEquipmentManagedEquipmentCompanyLevelApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List all Company Managed Equipment User Permissions
        api_response = api_instance.rest_v10_companies_company_id_managed_equipment_user_permissions_get(procore_company_id, company_id, page=page, per_page=per_page)
        print("The response of FieldProductivityManagedEquipmentManagedEquipmentCompanyLevelApi->rest_v10_companies_company_id_managed_equipment_user_permissions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityManagedEquipmentManagedEquipmentCompanyLevelApi->rest_v10_companies_company_id_managed_equipment_user_permissions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[CompanyManagedEquipmentUserPermission]**](CompanyManagedEquipmentUserPermission.md)

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

# **rest_v10_companies_company_id_managed_equipment_user_permissions_patch**
> CompanyManagedEquipmentUserPermission rest_v10_companies_company_id_managed_equipment_user_permissions_patch(procore_company_id, company_id, managed_equipment_permission_update_body)

Update User Permission

Updating a Company Managed Equipment User Permission

### Example


```python
import procore_sdk
from procore_sdk.models.company_managed_equipment_user_permission import CompanyManagedEquipmentUserPermission
from procore_sdk.models.managed_equipment_permission_update_body import ManagedEquipmentPermissionUpdateBody
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
    api_instance = procore_sdk.FieldProductivityManagedEquipmentManagedEquipmentCompanyLevelApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    managed_equipment_permission_update_body = procore_sdk.ManagedEquipmentPermissionUpdateBody() # ManagedEquipmentPermissionUpdateBody | 

    try:
        # Update User Permission
        api_response = api_instance.rest_v10_companies_company_id_managed_equipment_user_permissions_patch(procore_company_id, company_id, managed_equipment_permission_update_body)
        print("The response of FieldProductivityManagedEquipmentManagedEquipmentCompanyLevelApi->rest_v10_companies_company_id_managed_equipment_user_permissions_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityManagedEquipmentManagedEquipmentCompanyLevelApi->rest_v10_companies_company_id_managed_equipment_user_permissions_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **managed_equipment_permission_update_body** | [**ManagedEquipmentPermissionUpdateBody**](ManagedEquipmentPermissionUpdateBody.md)|  | 

### Return type

[**CompanyManagedEquipmentUserPermission**](CompanyManagedEquipmentUserPermission.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Company Managed Equipment User Permission updated |  -  |
**422** | Error updating a Company Managed Equipment User Permission |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

