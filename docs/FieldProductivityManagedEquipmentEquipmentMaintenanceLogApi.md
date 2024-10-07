# procore_sdk.FieldProductivityManagedEquipmentEquipmentMaintenanceLogApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_managed_equipment_maintenance_logs_get**](FieldProductivityManagedEquipmentEquipmentMaintenanceLogApi.md#rest_v10_companies_company_id_managed_equipment_maintenance_logs_get) | **GET** /rest/v1.0/companies/{company_id}/managed_equipment_maintenance_logs | List Equipment Maintenance Logs
[**rest_v10_companies_company_id_managed_equipment_maintenance_logs_id_delete**](FieldProductivityManagedEquipmentEquipmentMaintenanceLogApi.md#rest_v10_companies_company_id_managed_equipment_maintenance_logs_id_delete) | **DELETE** /rest/v1.0/companies/{company_id}/managed_equipment_maintenance_logs/{id} | Delete Equipment Maintenance Log
[**rest_v10_companies_company_id_managed_equipment_maintenance_logs_id_get**](FieldProductivityManagedEquipmentEquipmentMaintenanceLogApi.md#rest_v10_companies_company_id_managed_equipment_maintenance_logs_id_get) | **GET** /rest/v1.0/companies/{company_id}/managed_equipment_maintenance_logs/{id} | Show Equipment Maintenance Log
[**rest_v10_companies_company_id_managed_equipment_maintenance_logs_id_patch**](FieldProductivityManagedEquipmentEquipmentMaintenanceLogApi.md#rest_v10_companies_company_id_managed_equipment_maintenance_logs_id_patch) | **PATCH** /rest/v1.0/companies/{company_id}/managed_equipment_maintenance_logs/{id} | Update Equipment Maintenance Log
[**rest_v10_companies_company_id_managed_equipment_maintenance_logs_post**](FieldProductivityManagedEquipmentEquipmentMaintenanceLogApi.md#rest_v10_companies_company_id_managed_equipment_maintenance_logs_post) | **POST** /rest/v1.0/companies/{company_id}/managed_equipment_maintenance_logs | Create Equipment Maintenance Log
[**rest_v10_projects_project_id_managed_equipment_maintenance_logs_get**](FieldProductivityManagedEquipmentEquipmentMaintenanceLogApi.md#rest_v10_projects_project_id_managed_equipment_maintenance_logs_get) | **GET** /rest/v1.0/projects/{project_id}/managed_equipment_maintenance_logs | List Project Equipment Maintenance Logs
[**rest_v10_projects_project_id_managed_equipment_maintenance_logs_id_delete**](FieldProductivityManagedEquipmentEquipmentMaintenanceLogApi.md#rest_v10_projects_project_id_managed_equipment_maintenance_logs_id_delete) | **DELETE** /rest/v1.0/projects/{project_id}/managed_equipment_maintenance_logs/{id} | Delete Project Equipment Maintenance Log
[**rest_v10_projects_project_id_managed_equipment_maintenance_logs_id_get**](FieldProductivityManagedEquipmentEquipmentMaintenanceLogApi.md#rest_v10_projects_project_id_managed_equipment_maintenance_logs_id_get) | **GET** /rest/v1.0/projects/{project_id}/managed_equipment_maintenance_logs/{id} | Show Project Equipment Maintenance Log
[**rest_v10_projects_project_id_managed_equipment_maintenance_logs_id_patch**](FieldProductivityManagedEquipmentEquipmentMaintenanceLogApi.md#rest_v10_projects_project_id_managed_equipment_maintenance_logs_id_patch) | **PATCH** /rest/v1.0/projects/{project_id}/managed_equipment_maintenance_logs/{id} | Update Project Equipment Maintenance Log
[**rest_v10_projects_project_id_managed_equipment_maintenance_logs_post**](FieldProductivityManagedEquipmentEquipmentMaintenanceLogApi.md#rest_v10_projects_project_id_managed_equipment_maintenance_logs_post) | **POST** /rest/v1.0/projects/{project_id}/managed_equipment_maintenance_logs | Create Project Equipment Maintenance Log


# **rest_v10_companies_company_id_managed_equipment_maintenance_logs_get**
> List[RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsGet200ResponseInner] rest_v10_companies_company_id_managed_equipment_maintenance_logs_get(procore_company_id, company_id, page=page, per_page=per_page)

List Equipment Maintenance Logs

Return a list of all Equipment Maintenance Logs.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_managed_equipment_maintenance_logs_get200_response_inner import RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsGet200ResponseInner
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
    api_instance = procore_sdk.FieldProductivityManagedEquipmentEquipmentMaintenanceLogApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Equipment Maintenance Logs
        api_response = api_instance.rest_v10_companies_company_id_managed_equipment_maintenance_logs_get(procore_company_id, company_id, page=page, per_page=per_page)
        print("The response of FieldProductivityManagedEquipmentEquipmentMaintenanceLogApi->rest_v10_companies_company_id_managed_equipment_maintenance_logs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityManagedEquipmentEquipmentMaintenanceLogApi->rest_v10_companies_company_id_managed_equipment_maintenance_logs_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsGet200ResponseInner]**](RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsGet200ResponseInner.md)

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

# **rest_v10_companies_company_id_managed_equipment_maintenance_logs_id_delete**
> RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsGet200ResponseInner rest_v10_companies_company_id_managed_equipment_maintenance_logs_id_delete(procore_company_id, id, company_id)

Delete Equipment Maintenance Log

Detete a specific equipment maintenance log

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_managed_equipment_maintenance_logs_get200_response_inner import RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsGet200ResponseInner
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
    api_instance = procore_sdk.FieldProductivityManagedEquipmentEquipmentMaintenanceLogApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the company to get the makes for
    company_id = 56 # int | Unique identifier for the company.

    try:
        # Delete Equipment Maintenance Log
        api_response = api_instance.rest_v10_companies_company_id_managed_equipment_maintenance_logs_id_delete(procore_company_id, id, company_id)
        print("The response of FieldProductivityManagedEquipmentEquipmentMaintenanceLogApi->rest_v10_companies_company_id_managed_equipment_maintenance_logs_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityManagedEquipmentEquipmentMaintenanceLogApi->rest_v10_companies_company_id_managed_equipment_maintenance_logs_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the company to get the makes for | 
 **company_id** | **int**| Unique identifier for the company. | 

### Return type

[**RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsGet200ResponseInner**](RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_managed_equipment_maintenance_logs_id_get**
> RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsGet200ResponseInner rest_v10_companies_company_id_managed_equipment_maintenance_logs_id_get(procore_company_id, id, company_id)

Show Equipment Maintenance Log

Return detailed information about a specific equipment Maintenance Log.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_managed_equipment_maintenance_logs_get200_response_inner import RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsGet200ResponseInner
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
    api_instance = procore_sdk.FieldProductivityManagedEquipmentEquipmentMaintenanceLogApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the company to get the makes for
    company_id = 56 # int | Unique identifier for the company.

    try:
        # Show Equipment Maintenance Log
        api_response = api_instance.rest_v10_companies_company_id_managed_equipment_maintenance_logs_id_get(procore_company_id, id, company_id)
        print("The response of FieldProductivityManagedEquipmentEquipmentMaintenanceLogApi->rest_v10_companies_company_id_managed_equipment_maintenance_logs_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityManagedEquipmentEquipmentMaintenanceLogApi->rest_v10_companies_company_id_managed_equipment_maintenance_logs_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the company to get the makes for | 
 **company_id** | **int**| Unique identifier for the company. | 

### Return type

[**RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsGet200ResponseInner**](RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsGet200ResponseInner.md)

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

# **rest_v10_companies_company_id_managed_equipment_maintenance_logs_id_patch**
> RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsGet200ResponseInner rest_v10_companies_company_id_managed_equipment_maintenance_logs_id_patch(procore_company_id, id, company_id, rest_v10_companies_company_id_managed_equipment_maintenance_logs_post_request=rest_v10_companies_company_id_managed_equipment_maintenance_logs_post_request)

Update Equipment Maintenance Log

Update a specified equipment maintenance log

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_managed_equipment_maintenance_logs_get200_response_inner import RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsGet200ResponseInner
from procore_sdk.models.rest_v10_companies_company_id_managed_equipment_maintenance_logs_post_request import RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsPostRequest
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
    api_instance = procore_sdk.FieldProductivityManagedEquipmentEquipmentMaintenanceLogApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the company to get the makes for
    company_id = 56 # int | Unique identifier for the company.
    rest_v10_companies_company_id_managed_equipment_maintenance_logs_post_request = procore_sdk.RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsPostRequest() # RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsPostRequest |  (optional)

    try:
        # Update Equipment Maintenance Log
        api_response = api_instance.rest_v10_companies_company_id_managed_equipment_maintenance_logs_id_patch(procore_company_id, id, company_id, rest_v10_companies_company_id_managed_equipment_maintenance_logs_post_request=rest_v10_companies_company_id_managed_equipment_maintenance_logs_post_request)
        print("The response of FieldProductivityManagedEquipmentEquipmentMaintenanceLogApi->rest_v10_companies_company_id_managed_equipment_maintenance_logs_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityManagedEquipmentEquipmentMaintenanceLogApi->rest_v10_companies_company_id_managed_equipment_maintenance_logs_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the company to get the makes for | 
 **company_id** | **int**| Unique identifier for the company. | 
 **rest_v10_companies_company_id_managed_equipment_maintenance_logs_post_request** | [**RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsPostRequest**](RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsPostRequest.md)|  | [optional] 

### Return type

[**RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsGet200ResponseInner**](RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsGet200ResponseInner.md)

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

# **rest_v10_companies_company_id_managed_equipment_maintenance_logs_post**
> RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsGet200ResponseInner rest_v10_companies_company_id_managed_equipment_maintenance_logs_post(procore_company_id, company_id, rest_v10_companies_company_id_managed_equipment_maintenance_logs_post_request=rest_v10_companies_company_id_managed_equipment_maintenance_logs_post_request)

Create Equipment Maintenance Log

Create a new equipment maintenance log entry

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_managed_equipment_maintenance_logs_get200_response_inner import RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsGet200ResponseInner
from procore_sdk.models.rest_v10_companies_company_id_managed_equipment_maintenance_logs_post_request import RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsPostRequest
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
    api_instance = procore_sdk.FieldProductivityManagedEquipmentEquipmentMaintenanceLogApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    rest_v10_companies_company_id_managed_equipment_maintenance_logs_post_request = procore_sdk.RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsPostRequest() # RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsPostRequest |  (optional)

    try:
        # Create Equipment Maintenance Log
        api_response = api_instance.rest_v10_companies_company_id_managed_equipment_maintenance_logs_post(procore_company_id, company_id, rest_v10_companies_company_id_managed_equipment_maintenance_logs_post_request=rest_v10_companies_company_id_managed_equipment_maintenance_logs_post_request)
        print("The response of FieldProductivityManagedEquipmentEquipmentMaintenanceLogApi->rest_v10_companies_company_id_managed_equipment_maintenance_logs_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityManagedEquipmentEquipmentMaintenanceLogApi->rest_v10_companies_company_id_managed_equipment_maintenance_logs_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **rest_v10_companies_company_id_managed_equipment_maintenance_logs_post_request** | [**RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsPostRequest**](RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsPostRequest.md)|  | [optional] 

### Return type

[**RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsGet200ResponseInner**](RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_managed_equipment_maintenance_logs_get**
> List[RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsGet200ResponseInner] rest_v10_projects_project_id_managed_equipment_maintenance_logs_get(procore_company_id, project_id, page=page, per_page=per_page)

List Project Equipment Maintenance Logs

Return a list of all Equipment Maintenance Logs

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_managed_equipment_maintenance_logs_get200_response_inner import RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsGet200ResponseInner
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
    api_instance = procore_sdk.FieldProductivityManagedEquipmentEquipmentMaintenanceLogApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Project Equipment Maintenance Logs
        api_response = api_instance.rest_v10_projects_project_id_managed_equipment_maintenance_logs_get(procore_company_id, project_id, page=page, per_page=per_page)
        print("The response of FieldProductivityManagedEquipmentEquipmentMaintenanceLogApi->rest_v10_projects_project_id_managed_equipment_maintenance_logs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityManagedEquipmentEquipmentMaintenanceLogApi->rest_v10_projects_project_id_managed_equipment_maintenance_logs_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsGet200ResponseInner]**](RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_managed_equipment_maintenance_logs_id_delete**
> RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsGet200ResponseInner rest_v10_projects_project_id_managed_equipment_maintenance_logs_id_delete(procore_company_id, id, project_id)

Delete Project Equipment Maintenance Log

Detete a specific Equipment Maintenance Log.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_managed_equipment_maintenance_logs_get200_response_inner import RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsGet200ResponseInner
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
    api_instance = procore_sdk.FieldProductivityManagedEquipmentEquipmentMaintenanceLogApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the company to get the maintenance logs for
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Delete Project Equipment Maintenance Log
        api_response = api_instance.rest_v10_projects_project_id_managed_equipment_maintenance_logs_id_delete(procore_company_id, id, project_id)
        print("The response of FieldProductivityManagedEquipmentEquipmentMaintenanceLogApi->rest_v10_projects_project_id_managed_equipment_maintenance_logs_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityManagedEquipmentEquipmentMaintenanceLogApi->rest_v10_projects_project_id_managed_equipment_maintenance_logs_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the company to get the maintenance logs for | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsGet200ResponseInner**](RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_managed_equipment_maintenance_logs_id_get**
> RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsGet200ResponseInner rest_v10_projects_project_id_managed_equipment_maintenance_logs_id_get(procore_company_id, id, project_id)

Show Project Equipment Maintenance Log

Return detailed information about a specific Equipment Maintenance Log.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_managed_equipment_maintenance_logs_get200_response_inner import RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsGet200ResponseInner
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
    api_instance = procore_sdk.FieldProductivityManagedEquipmentEquipmentMaintenanceLogApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the company to get the maintenance logs for
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Show Project Equipment Maintenance Log
        api_response = api_instance.rest_v10_projects_project_id_managed_equipment_maintenance_logs_id_get(procore_company_id, id, project_id)
        print("The response of FieldProductivityManagedEquipmentEquipmentMaintenanceLogApi->rest_v10_projects_project_id_managed_equipment_maintenance_logs_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityManagedEquipmentEquipmentMaintenanceLogApi->rest_v10_projects_project_id_managed_equipment_maintenance_logs_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the company to get the maintenance logs for | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsGet200ResponseInner**](RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_managed_equipment_maintenance_logs_id_patch**
> RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsGet200ResponseInner rest_v10_projects_project_id_managed_equipment_maintenance_logs_id_patch(procore_company_id, id, project_id, rest_v10_companies_company_id_managed_equipment_maintenance_logs_post_request=rest_v10_companies_company_id_managed_equipment_maintenance_logs_post_request)

Update Project Equipment Maintenance Log

Update a specified Equipment Maintenance Log.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_managed_equipment_maintenance_logs_get200_response_inner import RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsGet200ResponseInner
from procore_sdk.models.rest_v10_companies_company_id_managed_equipment_maintenance_logs_post_request import RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsPostRequest
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
    api_instance = procore_sdk.FieldProductivityManagedEquipmentEquipmentMaintenanceLogApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the company to get the maintenance logs for
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_companies_company_id_managed_equipment_maintenance_logs_post_request = procore_sdk.RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsPostRequest() # RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsPostRequest |  (optional)

    try:
        # Update Project Equipment Maintenance Log
        api_response = api_instance.rest_v10_projects_project_id_managed_equipment_maintenance_logs_id_patch(procore_company_id, id, project_id, rest_v10_companies_company_id_managed_equipment_maintenance_logs_post_request=rest_v10_companies_company_id_managed_equipment_maintenance_logs_post_request)
        print("The response of FieldProductivityManagedEquipmentEquipmentMaintenanceLogApi->rest_v10_projects_project_id_managed_equipment_maintenance_logs_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityManagedEquipmentEquipmentMaintenanceLogApi->rest_v10_projects_project_id_managed_equipment_maintenance_logs_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the company to get the maintenance logs for | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_companies_company_id_managed_equipment_maintenance_logs_post_request** | [**RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsPostRequest**](RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsPostRequest.md)|  | [optional] 

### Return type

[**RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsGet200ResponseInner**](RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_managed_equipment_maintenance_logs_post**
> RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsGet200ResponseInner rest_v10_projects_project_id_managed_equipment_maintenance_logs_post(procore_company_id, project_id, rest_v10_companies_company_id_managed_equipment_maintenance_logs_post_request=rest_v10_companies_company_id_managed_equipment_maintenance_logs_post_request)

Create Project Equipment Maintenance Log

Create a new Equipment Maintenance Log Entry.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_managed_equipment_maintenance_logs_get200_response_inner import RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsGet200ResponseInner
from procore_sdk.models.rest_v10_companies_company_id_managed_equipment_maintenance_logs_post_request import RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsPostRequest
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
    api_instance = procore_sdk.FieldProductivityManagedEquipmentEquipmentMaintenanceLogApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_companies_company_id_managed_equipment_maintenance_logs_post_request = procore_sdk.RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsPostRequest() # RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsPostRequest |  (optional)

    try:
        # Create Project Equipment Maintenance Log
        api_response = api_instance.rest_v10_projects_project_id_managed_equipment_maintenance_logs_post(procore_company_id, project_id, rest_v10_companies_company_id_managed_equipment_maintenance_logs_post_request=rest_v10_companies_company_id_managed_equipment_maintenance_logs_post_request)
        print("The response of FieldProductivityManagedEquipmentEquipmentMaintenanceLogApi->rest_v10_projects_project_id_managed_equipment_maintenance_logs_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityManagedEquipmentEquipmentMaintenanceLogApi->rest_v10_projects_project_id_managed_equipment_maintenance_logs_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_companies_company_id_managed_equipment_maintenance_logs_post_request** | [**RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsPostRequest**](RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsPostRequest.md)|  | [optional] 

### Return type

[**RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsGet200ResponseInner**](RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsGet200ResponseInner.md)

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

