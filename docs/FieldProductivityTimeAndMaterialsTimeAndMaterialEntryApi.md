# procore_sdk.FieldProductivityTimeAndMaterialsTimeAndMaterialEntryApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_time_and_material_entries_bulk_update_patch**](FieldProductivityTimeAndMaterialsTimeAndMaterialEntryApi.md#rest_v10_projects_project_id_time_and_material_entries_bulk_update_patch) | **PATCH** /rest/v1.0/projects/{project_id}/time_and_material_entries/bulk_update | Update Multiple Time And Material Entries
[**rest_v10_projects_project_id_time_and_material_entries_configurable_field_sets_get**](FieldProductivityTimeAndMaterialsTimeAndMaterialEntryApi.md#rest_v10_projects_project_id_time_and_material_entries_configurable_field_sets_get) | **GET** /rest/v1.0/projects/{project_id}/time_and_material_entries/configurable_field_sets | List all Time And Material Entry Configurable Field Sets
[**rest_v10_projects_project_id_time_and_material_entries_create_equipment_post**](FieldProductivityTimeAndMaterialsTimeAndMaterialEntryApi.md#rest_v10_projects_project_id_time_and_material_entries_create_equipment_post) | **POST** /rest/v1.0/projects/{project_id}/time_and_material_entries/create_equipment | Create a piece of Equipment
[**rest_v10_projects_project_id_time_and_material_entries_get**](FieldProductivityTimeAndMaterialsTimeAndMaterialEntryApi.md#rest_v10_projects_project_id_time_and_material_entries_get) | **GET** /rest/v1.0/projects/{project_id}/time_and_material_entries | List all Time And Material Entry
[**rest_v10_projects_project_id_time_and_material_entries_id_change_history_get**](FieldProductivityTimeAndMaterialsTimeAndMaterialEntryApi.md#rest_v10_projects_project_id_time_and_material_entries_id_change_history_get) | **GET** /rest/v1.0/projects/{project_id}/time_and_material_entries/{id}/change_history | Show Change History
[**rest_v10_projects_project_id_time_and_material_entries_id_delete**](FieldProductivityTimeAndMaterialsTimeAndMaterialEntryApi.md#rest_v10_projects_project_id_time_and_material_entries_id_delete) | **DELETE** /rest/v1.0/projects/{project_id}/time_and_material_entries/{id} | Delete a Time And Material Entry
[**rest_v10_projects_project_id_time_and_material_entries_id_email_entry_post**](FieldProductivityTimeAndMaterialsTimeAndMaterialEntryApi.md#rest_v10_projects_project_id_time_and_material_entries_id_email_entry_post) | **POST** /rest/v1.0/projects/{project_id}/time_and_material_entries/{id}/email_entry | Email a Time And Material Entry
[**rest_v10_projects_project_id_time_and_material_entries_id_get**](FieldProductivityTimeAndMaterialsTimeAndMaterialEntryApi.md#rest_v10_projects_project_id_time_and_material_entries_id_get) | **GET** /rest/v1.0/projects/{project_id}/time_and_material_entries/{id} | Show Time And Material Entry
[**rest_v10_projects_project_id_time_and_material_entries_id_patch**](FieldProductivityTimeAndMaterialsTimeAndMaterialEntryApi.md#rest_v10_projects_project_id_time_and_material_entries_id_patch) | **PATCH** /rest/v1.0/projects/{project_id}/time_and_material_entries/{id} | Update a Time And Material Entry
[**rest_v10_projects_project_id_time_and_material_entries_id_restore_patch**](FieldProductivityTimeAndMaterialsTimeAndMaterialEntryApi.md#rest_v10_projects_project_id_time_and_material_entries_id_restore_patch) | **PATCH** /rest/v1.0/projects/{project_id}/time_and_material_entries/{id}/restore | Restore a Time And Material Entry
[**rest_v10_projects_project_id_time_and_material_entries_post**](FieldProductivityTimeAndMaterialsTimeAndMaterialEntryApi.md#rest_v10_projects_project_id_time_and_material_entries_post) | **POST** /rest/v1.0/projects/{project_id}/time_and_material_entries | Create a new Time And Material Entry
[**rest_v10_projects_project_id_time_and_material_entries_search_post**](FieldProductivityTimeAndMaterialsTimeAndMaterialEntryApi.md#rest_v10_projects_project_id_time_and_material_entries_search_post) | **POST** /rest/v1.0/projects/{project_id}/time_and_material_entries/search | List all Time And Material Entry matching the search keyword


# **rest_v10_projects_project_id_time_and_material_entries_bulk_update_patch**
> List[RestV10ProjectsProjectIdTimeAndMaterialEntriesGet200ResponseInner] rest_v10_projects_project_id_time_and_material_entries_bulk_update_patch(procore_company_id, project_id, time_and_material_entry_bulk_update_body, run_configurable_validations=run_configurable_validations)

Update Multiple Time And Material Entries

Multiple Time And Material Entries Updated

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_time_and_material_entries_get200_response_inner import RestV10ProjectsProjectIdTimeAndMaterialEntriesGet200ResponseInner
from procore_sdk.models.time_and_material_entry_bulk_update_body import TimeAndMaterialEntryBulkUpdateBody
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
    api_instance = procore_sdk.FieldProductivityTimeAndMaterialsTimeAndMaterialEntryApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    time_and_material_entry_bulk_update_body = procore_sdk.TimeAndMaterialEntryBulkUpdateBody() # TimeAndMaterialEntryBulkUpdateBody | 
    run_configurable_validations = False # bool | If true, validations are run for the corresponding Configurable Field Set. (optional) (default to False)

    try:
        # Update Multiple Time And Material Entries
        api_response = api_instance.rest_v10_projects_project_id_time_and_material_entries_bulk_update_patch(procore_company_id, project_id, time_and_material_entry_bulk_update_body, run_configurable_validations=run_configurable_validations)
        print("The response of FieldProductivityTimeAndMaterialsTimeAndMaterialEntryApi->rest_v10_projects_project_id_time_and_material_entries_bulk_update_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimeAndMaterialsTimeAndMaterialEntryApi->rest_v10_projects_project_id_time_and_material_entries_bulk_update_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **time_and_material_entry_bulk_update_body** | [**TimeAndMaterialEntryBulkUpdateBody**](TimeAndMaterialEntryBulkUpdateBody.md)|  | 
 **run_configurable_validations** | **bool**| If true, validations are run for the corresponding Configurable Field Set. | [optional] [default to False]

### Return type

[**List[RestV10ProjectsProjectIdTimeAndMaterialEntriesGet200ResponseInner]**](RestV10ProjectsProjectIdTimeAndMaterialEntriesGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the updated Time And Materil Entries |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**422** | Error updating Time And Material Entries |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_time_and_material_entries_configurable_field_sets_get**
> List[ConfigurableFieldSet] rest_v10_projects_project_id_time_and_material_entries_configurable_field_sets_get(procore_company_id, project_id, page=page, per_page=per_page)

List all Time And Material Entry Configurable Field Sets

Return a list of all Time And Material Entry Configurable Field Sets associated with the specified project

### Example


```python
import procore_sdk
from procore_sdk.models.configurable_field_set import ConfigurableFieldSet
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
    api_instance = procore_sdk.FieldProductivityTimeAndMaterialsTimeAndMaterialEntryApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List all Time And Material Entry Configurable Field Sets
        api_response = api_instance.rest_v10_projects_project_id_time_and_material_entries_configurable_field_sets_get(procore_company_id, project_id, page=page, per_page=per_page)
        print("The response of FieldProductivityTimeAndMaterialsTimeAndMaterialEntryApi->rest_v10_projects_project_id_time_and_material_entries_configurable_field_sets_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimeAndMaterialsTimeAndMaterialEntryApi->rest_v10_projects_project_id_time_and_material_entries_configurable_field_sets_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[ConfigurableFieldSet]**](ConfigurableFieldSet.md)

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

# **rest_v10_projects_project_id_time_and_material_entries_create_equipment_post**
> Equipment rest_v10_projects_project_id_time_and_material_entries_create_equipment_post(procore_company_id, project_id, time_and_material_entry_bulk_update_body1)

Create a piece of Equipment

Create a piece of Equipment

### Example


```python
import procore_sdk
from procore_sdk.models.equipment import Equipment
from procore_sdk.models.time_and_material_entry_bulk_update_body1 import TimeAndMaterialEntryBulkUpdateBody1
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
    api_instance = procore_sdk.FieldProductivityTimeAndMaterialsTimeAndMaterialEntryApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    time_and_material_entry_bulk_update_body1 = procore_sdk.TimeAndMaterialEntryBulkUpdateBody1() # TimeAndMaterialEntryBulkUpdateBody1 | 

    try:
        # Create a piece of Equipment
        api_response = api_instance.rest_v10_projects_project_id_time_and_material_entries_create_equipment_post(procore_company_id, project_id, time_and_material_entry_bulk_update_body1)
        print("The response of FieldProductivityTimeAndMaterialsTimeAndMaterialEntryApi->rest_v10_projects_project_id_time_and_material_entries_create_equipment_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimeAndMaterialsTimeAndMaterialEntryApi->rest_v10_projects_project_id_time_and_material_entries_create_equipment_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **time_and_material_entry_bulk_update_body1** | [**TimeAndMaterialEntryBulkUpdateBody1**](TimeAndMaterialEntryBulkUpdateBody1.md)|  | 

### Return type

[**Equipment**](Equipment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Equipment Created |  -  |
**403** | Forbidden |  -  |
**422** | Error creating a piece of Equipment |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_time_and_material_entries_get**
> List[RestV10ProjectsProjectIdTimeAndMaterialEntriesGet200ResponseInner] rest_v10_projects_project_id_time_and_material_entries_get(procore_company_id, project_id, page=page, per_page=per_page)

List all Time And Material Entry

Return a list of all Time And Material Entry associated with the specified project

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_time_and_material_entries_get200_response_inner import RestV10ProjectsProjectIdTimeAndMaterialEntriesGet200ResponseInner
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
    api_instance = procore_sdk.FieldProductivityTimeAndMaterialsTimeAndMaterialEntryApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List all Time And Material Entry
        api_response = api_instance.rest_v10_projects_project_id_time_and_material_entries_get(procore_company_id, project_id, page=page, per_page=per_page)
        print("The response of FieldProductivityTimeAndMaterialsTimeAndMaterialEntryApi->rest_v10_projects_project_id_time_and_material_entries_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimeAndMaterialsTimeAndMaterialEntryApi->rest_v10_projects_project_id_time_and_material_entries_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[RestV10ProjectsProjectIdTimeAndMaterialEntriesGet200ResponseInner]**](RestV10ProjectsProjectIdTimeAndMaterialEntriesGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_time_and_material_entries_id_change_history_get**
> RestV10CompaniesCompanyIdWorkflowPermanentLogsGet401Response rest_v10_projects_project_id_time_and_material_entries_id_change_history_get(procore_company_id, project_id, id)

Show Change History

Show Change History For a Time And Material Entry

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_workflow_permanent_logs_get401_response import RestV10CompaniesCompanyIdWorkflowPermanentLogsGet401Response
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
    api_instance = procore_sdk.FieldProductivityTimeAndMaterialsTimeAndMaterialEntryApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | ID

    try:
        # Show Change History
        api_response = api_instance.rest_v10_projects_project_id_time_and_material_entries_id_change_history_get(procore_company_id, project_id, id)
        print("The response of FieldProductivityTimeAndMaterialsTimeAndMaterialEntryApi->rest_v10_projects_project_id_time_and_material_entries_id_change_history_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimeAndMaterialsTimeAndMaterialEntryApi->rest_v10_projects_project_id_time_and_material_entries_id_change_history_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| ID | 

### Return type

[**RestV10CompaniesCompanyIdWorkflowPermanentLogsGet401Response**](RestV10CompaniesCompanyIdWorkflowPermanentLogsGet401Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**304** | Not Modified |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_time_and_material_entries_id_delete**
> RestV10ProjectsProjectIdTimeAndMaterialEntriesGet200ResponseInner rest_v10_projects_project_id_time_and_material_entries_id_delete(procore_company_id, project_id, id)

Delete a Time And Material Entry

Deleting a Time And Material Entry associated with the specified project

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_time_and_material_entries_get200_response_inner import RestV10ProjectsProjectIdTimeAndMaterialEntriesGet200ResponseInner
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
    api_instance = procore_sdk.FieldProductivityTimeAndMaterialsTimeAndMaterialEntryApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Id of Time And Material Entry

    try:
        # Delete a Time And Material Entry
        api_response = api_instance.rest_v10_projects_project_id_time_and_material_entries_id_delete(procore_company_id, project_id, id)
        print("The response of FieldProductivityTimeAndMaterialsTimeAndMaterialEntryApi->rest_v10_projects_project_id_time_and_material_entries_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimeAndMaterialsTimeAndMaterialEntryApi->rest_v10_projects_project_id_time_and_material_entries_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Id of Time And Material Entry | 

### Return type

[**RestV10ProjectsProjectIdTimeAndMaterialEntriesGet200ResponseInner**](RestV10ProjectsProjectIdTimeAndMaterialEntriesGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Time And Material Entry deleted |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_time_and_material_entries_id_email_entry_post**
> rest_v10_projects_project_id_time_and_material_entries_id_email_entry_post(procore_company_id, project_id, id)

Email a Time And Material Entry

Email a Time And Material Entry associated with the specified project

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
    api_instance = procore_sdk.FieldProductivityTimeAndMaterialsTimeAndMaterialEntryApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Id of the Time And Material Entry

    try:
        # Email a Time And Material Entry
        api_instance.rest_v10_projects_project_id_time_and_material_entries_id_email_entry_post(procore_company_id, project_id, id)
    except Exception as e:
        print("Exception when calling FieldProductivityTimeAndMaterialsTimeAndMaterialEntryApi->rest_v10_projects_project_id_time_and_material_entries_id_email_entry_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Id of the Time And Material Entry | 

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
**204** | Time And Material Entry email sent |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**422** | Error emailing a Time And Material Entry |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_time_and_material_entries_id_get**
> RestV10ProjectsProjectIdTimeAndMaterialEntriesGet200ResponseInner rest_v10_projects_project_id_time_and_material_entries_id_get(procore_company_id, project_id, id)

Show Time And Material Entry

Return Time And Material Entry detailed information.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_time_and_material_entries_get200_response_inner import RestV10ProjectsProjectIdTimeAndMaterialEntriesGet200ResponseInner
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
    api_instance = procore_sdk.FieldProductivityTimeAndMaterialsTimeAndMaterialEntryApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | ID

    try:
        # Show Time And Material Entry
        api_response = api_instance.rest_v10_projects_project_id_time_and_material_entries_id_get(procore_company_id, project_id, id)
        print("The response of FieldProductivityTimeAndMaterialsTimeAndMaterialEntryApi->rest_v10_projects_project_id_time_and_material_entries_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimeAndMaterialsTimeAndMaterialEntryApi->rest_v10_projects_project_id_time_and_material_entries_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| ID | 

### Return type

[**RestV10ProjectsProjectIdTimeAndMaterialEntriesGet200ResponseInner**](RestV10ProjectsProjectIdTimeAndMaterialEntriesGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_time_and_material_entries_id_patch**
> RestV10ProjectsProjectIdTimeAndMaterialEntriesGet200ResponseInner rest_v10_projects_project_id_time_and_material_entries_id_patch(procore_company_id, project_id, id, time_and_material_entry_body, run_configurable_validations=run_configurable_validations)

Update a Time And Material Entry

Updating a Time And Material Entry associated with the specified project

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_time_and_material_entries_get200_response_inner import RestV10ProjectsProjectIdTimeAndMaterialEntriesGet200ResponseInner
from procore_sdk.models.time_and_material_entry_body import TimeAndMaterialEntryBody
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
    api_instance = procore_sdk.FieldProductivityTimeAndMaterialsTimeAndMaterialEntryApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Id of the Time And Material Entry
    time_and_material_entry_body = procore_sdk.TimeAndMaterialEntryBody() # TimeAndMaterialEntryBody | 
    run_configurable_validations = False # bool | If true, validations are run for the corresponding Configurable Field Set. (optional) (default to False)

    try:
        # Update a Time And Material Entry
        api_response = api_instance.rest_v10_projects_project_id_time_and_material_entries_id_patch(procore_company_id, project_id, id, time_and_material_entry_body, run_configurable_validations=run_configurable_validations)
        print("The response of FieldProductivityTimeAndMaterialsTimeAndMaterialEntryApi->rest_v10_projects_project_id_time_and_material_entries_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimeAndMaterialsTimeAndMaterialEntryApi->rest_v10_projects_project_id_time_and_material_entries_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Id of the Time And Material Entry | 
 **time_and_material_entry_body** | [**TimeAndMaterialEntryBody**](TimeAndMaterialEntryBody.md)|  | 
 **run_configurable_validations** | **bool**| If true, validations are run for the corresponding Configurable Field Set. | [optional] [default to False]

### Return type

[**RestV10ProjectsProjectIdTimeAndMaterialEntriesGet200ResponseInner**](RestV10ProjectsProjectIdTimeAndMaterialEntriesGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Time And Material Entry updated |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**422** | Error updating a Time And Material Entry |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_time_and_material_entries_id_restore_patch**
> RestV10ProjectsProjectIdTimeAndMaterialEntriesGet200ResponseInner rest_v10_projects_project_id_time_and_material_entries_id_restore_patch(procore_company_id, project_id, id)

Restore a Time And Material Entry

Restored a deleted Time And Material Entry

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_time_and_material_entries_get200_response_inner import RestV10ProjectsProjectIdTimeAndMaterialEntriesGet200ResponseInner
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
    api_instance = procore_sdk.FieldProductivityTimeAndMaterialsTimeAndMaterialEntryApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Id of the Time And Material Entry

    try:
        # Restore a Time And Material Entry
        api_response = api_instance.rest_v10_projects_project_id_time_and_material_entries_id_restore_patch(procore_company_id, project_id, id)
        print("The response of FieldProductivityTimeAndMaterialsTimeAndMaterialEntryApi->rest_v10_projects_project_id_time_and_material_entries_id_restore_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimeAndMaterialsTimeAndMaterialEntryApi->rest_v10_projects_project_id_time_and_material_entries_id_restore_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Id of the Time And Material Entry | 

### Return type

[**RestV10ProjectsProjectIdTimeAndMaterialEntriesGet200ResponseInner**](RestV10ProjectsProjectIdTimeAndMaterialEntriesGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Time And Material Entry Restored |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**422** | Error updating a Time And Material Entry |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_time_and_material_entries_post**
> RestV10ProjectsProjectIdTimeAndMaterialEntriesGet200ResponseInner rest_v10_projects_project_id_time_and_material_entries_post(procore_company_id, project_id, time_and_material_entry_body, run_configurable_validations=run_configurable_validations)

Create a new Time And Material Entry

Create a new Time And Material Entry associated with the specified project

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_time_and_material_entries_get200_response_inner import RestV10ProjectsProjectIdTimeAndMaterialEntriesGet200ResponseInner
from procore_sdk.models.time_and_material_entry_body import TimeAndMaterialEntryBody
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
    api_instance = procore_sdk.FieldProductivityTimeAndMaterialsTimeAndMaterialEntryApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    time_and_material_entry_body = procore_sdk.TimeAndMaterialEntryBody() # TimeAndMaterialEntryBody | 
    run_configurable_validations = False # bool | If true, validations are run for the corresponding Configurable Field Set. (optional) (default to False)

    try:
        # Create a new Time And Material Entry
        api_response = api_instance.rest_v10_projects_project_id_time_and_material_entries_post(procore_company_id, project_id, time_and_material_entry_body, run_configurable_validations=run_configurable_validations)
        print("The response of FieldProductivityTimeAndMaterialsTimeAndMaterialEntryApi->rest_v10_projects_project_id_time_and_material_entries_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimeAndMaterialsTimeAndMaterialEntryApi->rest_v10_projects_project_id_time_and_material_entries_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **time_and_material_entry_body** | [**TimeAndMaterialEntryBody**](TimeAndMaterialEntryBody.md)|  | 
 **run_configurable_validations** | **bool**| If true, validations are run for the corresponding Configurable Field Set. | [optional] [default to False]

### Return type

[**RestV10ProjectsProjectIdTimeAndMaterialEntriesGet200ResponseInner**](RestV10ProjectsProjectIdTimeAndMaterialEntriesGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Time And Material Entry Created Successfully |  -  |
**403** | Forbidden |  -  |
**422** | Error Creating a Time And Material Entry |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_time_and_material_entries_search_post**
> List[RestV10ProjectsProjectIdTimeAndMaterialEntriesGet200ResponseInner] rest_v10_projects_project_id_time_and_material_entries_search_post(procore_company_id, project_id, search_keyword=search_keyword)

List all Time And Material Entry matching the search keyword

Return a list of all Time And Material Entry matching the search keyword

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_time_and_material_entries_get200_response_inner import RestV10ProjectsProjectIdTimeAndMaterialEntriesGet200ResponseInner
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
    api_instance = procore_sdk.FieldProductivityTimeAndMaterialsTimeAndMaterialEntryApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    search_keyword = 'search_keyword_example' # str | Keyword for looking up Time And Material Entries (optional)

    try:
        # List all Time And Material Entry matching the search keyword
        api_response = api_instance.rest_v10_projects_project_id_time_and_material_entries_search_post(procore_company_id, project_id, search_keyword=search_keyword)
        print("The response of FieldProductivityTimeAndMaterialsTimeAndMaterialEntryApi->rest_v10_projects_project_id_time_and_material_entries_search_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimeAndMaterialsTimeAndMaterialEntryApi->rest_v10_projects_project_id_time_and_material_entries_search_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **search_keyword** | **str**| Keyword for looking up Time And Material Entries | [optional] 

### Return type

[**List[RestV10ProjectsProjectIdTimeAndMaterialEntriesGet200ResponseInner]**](RestV10ProjectsProjectIdTimeAndMaterialEntriesGet200ResponseInner.md)

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

