# procore_sdk.FieldProductivityTimeAndMaterialsTimeAndMaterialEquipmentLogApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_time_and_material_equipment_logs_bulk_create_post**](FieldProductivityTimeAndMaterialsTimeAndMaterialEquipmentLogApi.md#rest_v10_projects_project_id_time_and_material_equipment_logs_bulk_create_post) | **POST** /rest/v1.0/projects/{project_id}/time_and_material_equipment_logs/bulk_create | Bulk Create Time and material equipment logs
[**rest_v10_projects_project_id_time_and_material_equipment_logs_bulk_destroy_delete**](FieldProductivityTimeAndMaterialsTimeAndMaterialEquipmentLogApi.md#rest_v10_projects_project_id_time_and_material_equipment_logs_bulk_destroy_delete) | **DELETE** /rest/v1.0/projects/{project_id}/time_and_material_equipment_logs/bulk_destroy | Bulk Delete Time and material equipment logs
[**rest_v10_projects_project_id_time_and_material_equipment_logs_bulk_update_patch**](FieldProductivityTimeAndMaterialsTimeAndMaterialEquipmentLogApi.md#rest_v10_projects_project_id_time_and_material_equipment_logs_bulk_update_patch) | **PATCH** /rest/v1.0/projects/{project_id}/time_and_material_equipment_logs/bulk_update | Bulk Update Time and Material Equipment logs
[**rest_v10_projects_project_id_time_and_material_equipment_logs_get**](FieldProductivityTimeAndMaterialsTimeAndMaterialEquipmentLogApi.md#rest_v10_projects_project_id_time_and_material_equipment_logs_get) | **GET** /rest/v1.0/projects/{project_id}/time_and_material_equipment_logs | List of all Time and Material Equipment Logs
[**rest_v10_projects_project_id_time_and_material_equipment_logs_id_delete**](FieldProductivityTimeAndMaterialsTimeAndMaterialEquipmentLogApi.md#rest_v10_projects_project_id_time_and_material_equipment_logs_id_delete) | **DELETE** /rest/v1.0/projects/{project_id}/time_and_material_equipment_logs/{id} | Delete a Time And Material Equipment Log
[**rest_v10_projects_project_id_time_and_material_equipment_logs_id_get**](FieldProductivityTimeAndMaterialsTimeAndMaterialEquipmentLogApi.md#rest_v10_projects_project_id_time_and_material_equipment_logs_id_get) | **GET** /rest/v1.0/projects/{project_id}/time_and_material_equipment_logs/{id} | Show Time And Material Equipment Log
[**rest_v10_projects_project_id_time_and_material_equipment_logs_id_patch**](FieldProductivityTimeAndMaterialsTimeAndMaterialEquipmentLogApi.md#rest_v10_projects_project_id_time_and_material_equipment_logs_id_patch) | **PATCH** /rest/v1.0/projects/{project_id}/time_and_material_equipment_logs/{id} | Update a Time And Material Equipment Log
[**rest_v10_projects_project_id_time_and_material_equipment_logs_post**](FieldProductivityTimeAndMaterialsTimeAndMaterialEquipmentLogApi.md#rest_v10_projects_project_id_time_and_material_equipment_logs_post) | **POST** /rest/v1.0/projects/{project_id}/time_and_material_equipment_logs | Create a new Time And Material Equipment Log


# **rest_v10_projects_project_id_time_and_material_equipment_logs_bulk_create_post**
> List[RestV10ProjectsProjectIdTimeAndMaterialEquipmentLogsGet200ResponseInner] rest_v10_projects_project_id_time_and_material_equipment_logs_bulk_create_post(procore_company_id, project_id, time_and_material_equipment_log_bulk_create_body)

Bulk Create Time and material equipment logs

Bulk create Time and material equipment logs with one request.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_time_and_material_equipment_logs_get200_response_inner import RestV10ProjectsProjectIdTimeAndMaterialEquipmentLogsGet200ResponseInner
from procore_sdk.models.time_and_material_equipment_log_bulk_create_body import TimeAndMaterialEquipmentLogBulkCreateBody
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
    api_instance = procore_sdk.FieldProductivityTimeAndMaterialsTimeAndMaterialEquipmentLogApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    time_and_material_equipment_log_bulk_create_body = procore_sdk.TimeAndMaterialEquipmentLogBulkCreateBody() # TimeAndMaterialEquipmentLogBulkCreateBody | 

    try:
        # Bulk Create Time and material equipment logs
        api_response = api_instance.rest_v10_projects_project_id_time_and_material_equipment_logs_bulk_create_post(procore_company_id, project_id, time_and_material_equipment_log_bulk_create_body)
        print("The response of FieldProductivityTimeAndMaterialsTimeAndMaterialEquipmentLogApi->rest_v10_projects_project_id_time_and_material_equipment_logs_bulk_create_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimeAndMaterialsTimeAndMaterialEquipmentLogApi->rest_v10_projects_project_id_time_and_material_equipment_logs_bulk_create_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **time_and_material_equipment_log_bulk_create_body** | [**TimeAndMaterialEquipmentLogBulkCreateBody**](TimeAndMaterialEquipmentLogBulkCreateBody.md)|  | 

### Return type

[**List[RestV10ProjectsProjectIdTimeAndMaterialEquipmentLogsGet200ResponseInner]**](RestV10ProjectsProjectIdTimeAndMaterialEquipmentLogsGet200ResponseInner.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_time_and_material_equipment_logs_bulk_destroy_delete**
> List[RestV10ProjectsProjectIdTimeAndMaterialEquipmentLogsGet200ResponseInner] rest_v10_projects_project_id_time_and_material_equipment_logs_bulk_destroy_delete(procore_company_id, project_id, time_and_material_equipment_log_bulk_destroy_body)

Bulk Delete Time and material equipment logs

Bulk delete Time and material equipment logs with one request.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_time_and_material_equipment_logs_get200_response_inner import RestV10ProjectsProjectIdTimeAndMaterialEquipmentLogsGet200ResponseInner
from procore_sdk.models.time_and_material_equipment_log_bulk_destroy_body import TimeAndMaterialEquipmentLogBulkDestroyBody
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
    api_instance = procore_sdk.FieldProductivityTimeAndMaterialsTimeAndMaterialEquipmentLogApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    time_and_material_equipment_log_bulk_destroy_body = procore_sdk.TimeAndMaterialEquipmentLogBulkDestroyBody() # TimeAndMaterialEquipmentLogBulkDestroyBody | 

    try:
        # Bulk Delete Time and material equipment logs
        api_response = api_instance.rest_v10_projects_project_id_time_and_material_equipment_logs_bulk_destroy_delete(procore_company_id, project_id, time_and_material_equipment_log_bulk_destroy_body)
        print("The response of FieldProductivityTimeAndMaterialsTimeAndMaterialEquipmentLogApi->rest_v10_projects_project_id_time_and_material_equipment_logs_bulk_destroy_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimeAndMaterialsTimeAndMaterialEquipmentLogApi->rest_v10_projects_project_id_time_and_material_equipment_logs_bulk_destroy_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **time_and_material_equipment_log_bulk_destroy_body** | [**TimeAndMaterialEquipmentLogBulkDestroyBody**](TimeAndMaterialEquipmentLogBulkDestroyBody.md)|  | 

### Return type

[**List[RestV10ProjectsProjectIdTimeAndMaterialEquipmentLogsGet200ResponseInner]**](RestV10ProjectsProjectIdTimeAndMaterialEquipmentLogsGet200ResponseInner.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_time_and_material_equipment_logs_bulk_update_patch**
> List[RestV10ProjectsProjectIdTimeAndMaterialEquipmentLogsGet200ResponseInner] rest_v10_projects_project_id_time_and_material_equipment_logs_bulk_update_patch(procore_company_id, project_id, time_and_material_equipment_log_bulk_update_body)

Bulk Update Time and Material Equipment logs

Bulk update Time and Material Equipment logs with one request.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_time_and_material_equipment_logs_get200_response_inner import RestV10ProjectsProjectIdTimeAndMaterialEquipmentLogsGet200ResponseInner
from procore_sdk.models.time_and_material_equipment_log_bulk_update_body import TimeAndMaterialEquipmentLogBulkUpdateBody
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
    api_instance = procore_sdk.FieldProductivityTimeAndMaterialsTimeAndMaterialEquipmentLogApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    time_and_material_equipment_log_bulk_update_body = procore_sdk.TimeAndMaterialEquipmentLogBulkUpdateBody() # TimeAndMaterialEquipmentLogBulkUpdateBody | 

    try:
        # Bulk Update Time and Material Equipment logs
        api_response = api_instance.rest_v10_projects_project_id_time_and_material_equipment_logs_bulk_update_patch(procore_company_id, project_id, time_and_material_equipment_log_bulk_update_body)
        print("The response of FieldProductivityTimeAndMaterialsTimeAndMaterialEquipmentLogApi->rest_v10_projects_project_id_time_and_material_equipment_logs_bulk_update_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimeAndMaterialsTimeAndMaterialEquipmentLogApi->rest_v10_projects_project_id_time_and_material_equipment_logs_bulk_update_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **time_and_material_equipment_log_bulk_update_body** | [**TimeAndMaterialEquipmentLogBulkUpdateBody**](TimeAndMaterialEquipmentLogBulkUpdateBody.md)|  | 

### Return type

[**List[RestV10ProjectsProjectIdTimeAndMaterialEquipmentLogsGet200ResponseInner]**](RestV10ProjectsProjectIdTimeAndMaterialEquipmentLogsGet200ResponseInner.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_time_and_material_equipment_logs_get**
> List[RestV10ProjectsProjectIdTimeAndMaterialEquipmentLogsGet200ResponseInner] rest_v10_projects_project_id_time_and_material_equipment_logs_get(procore_company_id, project_id, page=page, per_page=per_page)

List of all Time and Material Equipment Logs

List of all Time and Material Equipment Logs

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_time_and_material_equipment_logs_get200_response_inner import RestV10ProjectsProjectIdTimeAndMaterialEquipmentLogsGet200ResponseInner
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
    api_instance = procore_sdk.FieldProductivityTimeAndMaterialsTimeAndMaterialEquipmentLogApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List of all Time and Material Equipment Logs
        api_response = api_instance.rest_v10_projects_project_id_time_and_material_equipment_logs_get(procore_company_id, project_id, page=page, per_page=per_page)
        print("The response of FieldProductivityTimeAndMaterialsTimeAndMaterialEquipmentLogApi->rest_v10_projects_project_id_time_and_material_equipment_logs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimeAndMaterialsTimeAndMaterialEquipmentLogApi->rest_v10_projects_project_id_time_and_material_equipment_logs_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[RestV10ProjectsProjectIdTimeAndMaterialEquipmentLogsGet200ResponseInner]**](RestV10ProjectsProjectIdTimeAndMaterialEquipmentLogsGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_time_and_material_equipment_logs_id_delete**
> RestV10ProjectsProjectIdTimeAndMaterialEquipmentLogsGet200ResponseInner rest_v10_projects_project_id_time_and_material_equipment_logs_id_delete(procore_company_id, project_id, id)

Delete a Time And Material Equipment Log

Deleting a Time And Material Equipment Log

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_time_and_material_equipment_logs_get200_response_inner import RestV10ProjectsProjectIdTimeAndMaterialEquipmentLogsGet200ResponseInner
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
    api_instance = procore_sdk.FieldProductivityTimeAndMaterialsTimeAndMaterialEquipmentLogApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Id of the Time And Material Equipment Log

    try:
        # Delete a Time And Material Equipment Log
        api_response = api_instance.rest_v10_projects_project_id_time_and_material_equipment_logs_id_delete(procore_company_id, project_id, id)
        print("The response of FieldProductivityTimeAndMaterialsTimeAndMaterialEquipmentLogApi->rest_v10_projects_project_id_time_and_material_equipment_logs_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimeAndMaterialsTimeAndMaterialEquipmentLogApi->rest_v10_projects_project_id_time_and_material_equipment_logs_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Id of the Time And Material Equipment Log | 

### Return type

[**RestV10ProjectsProjectIdTimeAndMaterialEquipmentLogsGet200ResponseInner**](RestV10ProjectsProjectIdTimeAndMaterialEquipmentLogsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Time And Material Equipment Log deleted |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_time_and_material_equipment_logs_id_get**
> RestV10ProjectsProjectIdTimeAndMaterialEquipmentLogsGet200ResponseInner rest_v10_projects_project_id_time_and_material_equipment_logs_id_get(procore_company_id, project_id, id)

Show Time And Material Equipment Log

Return Time And Material Equipment Log detailed information.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_time_and_material_equipment_logs_get200_response_inner import RestV10ProjectsProjectIdTimeAndMaterialEquipmentLogsGet200ResponseInner
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
    api_instance = procore_sdk.FieldProductivityTimeAndMaterialsTimeAndMaterialEquipmentLogApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | ID

    try:
        # Show Time And Material Equipment Log
        api_response = api_instance.rest_v10_projects_project_id_time_and_material_equipment_logs_id_get(procore_company_id, project_id, id)
        print("The response of FieldProductivityTimeAndMaterialsTimeAndMaterialEquipmentLogApi->rest_v10_projects_project_id_time_and_material_equipment_logs_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimeAndMaterialsTimeAndMaterialEquipmentLogApi->rest_v10_projects_project_id_time_and_material_equipment_logs_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| ID | 

### Return type

[**RestV10ProjectsProjectIdTimeAndMaterialEquipmentLogsGet200ResponseInner**](RestV10ProjectsProjectIdTimeAndMaterialEquipmentLogsGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_time_and_material_equipment_logs_id_patch**
> RestV10ProjectsProjectIdTimeAndMaterialEquipmentLogsGet200ResponseInner rest_v10_projects_project_id_time_and_material_equipment_logs_id_patch(procore_company_id, project_id, id, time_and_material_equipment_log, run_configurable_validations=run_configurable_validations)

Update a Time And Material Equipment Log

Updating a Time And Material Equipment Log

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_time_and_material_equipment_logs_get200_response_inner import RestV10ProjectsProjectIdTimeAndMaterialEquipmentLogsGet200ResponseInner
from procore_sdk.models.time_and_material_equipment_log import TimeAndMaterialEquipmentLog
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
    api_instance = procore_sdk.FieldProductivityTimeAndMaterialsTimeAndMaterialEquipmentLogApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Id of the Time And Material Equipment Log
    time_and_material_equipment_log = procore_sdk.TimeAndMaterialEquipmentLog() # TimeAndMaterialEquipmentLog | 
    run_configurable_validations = False # bool | If true, validations are run for the corresponding Configurable Field Set. (optional) (default to False)

    try:
        # Update a Time And Material Equipment Log
        api_response = api_instance.rest_v10_projects_project_id_time_and_material_equipment_logs_id_patch(procore_company_id, project_id, id, time_and_material_equipment_log, run_configurable_validations=run_configurable_validations)
        print("The response of FieldProductivityTimeAndMaterialsTimeAndMaterialEquipmentLogApi->rest_v10_projects_project_id_time_and_material_equipment_logs_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimeAndMaterialsTimeAndMaterialEquipmentLogApi->rest_v10_projects_project_id_time_and_material_equipment_logs_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Id of the Time And Material Equipment Log | 
 **time_and_material_equipment_log** | [**TimeAndMaterialEquipmentLog**](TimeAndMaterialEquipmentLog.md)|  | 
 **run_configurable_validations** | **bool**| If true, validations are run for the corresponding Configurable Field Set. | [optional] [default to False]

### Return type

[**RestV10ProjectsProjectIdTimeAndMaterialEquipmentLogsGet200ResponseInner**](RestV10ProjectsProjectIdTimeAndMaterialEquipmentLogsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | T&amp;M equipment log  updated |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**422** | Error updating a Time And Material Equipment Log |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_time_and_material_equipment_logs_post**
> RestV10ProjectsProjectIdTimeAndMaterialEquipmentLogsGet200ResponseInner rest_v10_projects_project_id_time_and_material_equipment_logs_post(procore_company_id, project_id, time_and_material_equipment_log, run_configurable_validations=run_configurable_validations)

Create a new Time And Material Equipment Log

Create a new Time And Material Equipment log

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_time_and_material_equipment_logs_get200_response_inner import RestV10ProjectsProjectIdTimeAndMaterialEquipmentLogsGet200ResponseInner
from procore_sdk.models.time_and_material_equipment_log import TimeAndMaterialEquipmentLog
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
    api_instance = procore_sdk.FieldProductivityTimeAndMaterialsTimeAndMaterialEquipmentLogApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    time_and_material_equipment_log = procore_sdk.TimeAndMaterialEquipmentLog() # TimeAndMaterialEquipmentLog | 
    run_configurable_validations = False # bool | If true, validations are run for the corresponding Configurable Field Set. (optional) (default to False)

    try:
        # Create a new Time And Material Equipment Log
        api_response = api_instance.rest_v10_projects_project_id_time_and_material_equipment_logs_post(procore_company_id, project_id, time_and_material_equipment_log, run_configurable_validations=run_configurable_validations)
        print("The response of FieldProductivityTimeAndMaterialsTimeAndMaterialEquipmentLogApi->rest_v10_projects_project_id_time_and_material_equipment_logs_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimeAndMaterialsTimeAndMaterialEquipmentLogApi->rest_v10_projects_project_id_time_and_material_equipment_logs_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **time_and_material_equipment_log** | [**TimeAndMaterialEquipmentLog**](TimeAndMaterialEquipmentLog.md)|  | 
 **run_configurable_validations** | **bool**| If true, validations are run for the corresponding Configurable Field Set. | [optional] [default to False]

### Return type

[**RestV10ProjectsProjectIdTimeAndMaterialEquipmentLogsGet200ResponseInner**](RestV10ProjectsProjectIdTimeAndMaterialEquipmentLogsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | T&amp;M equipment log Created Succesfully |  -  |
**403** | Forbidden |  -  |
**422** | Error creating a Time And Material Equipment Log |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

