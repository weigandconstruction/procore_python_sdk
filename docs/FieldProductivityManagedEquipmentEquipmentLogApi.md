# procore_sdk.FieldProductivityManagedEquipmentEquipmentLogApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_managed_equipment_logs_get**](FieldProductivityManagedEquipmentEquipmentLogApi.md#rest_v10_companies_company_id_managed_equipment_logs_get) | **GET** /rest/v1.0/companies/{company_id}/managed_equipment_logs | List all equipment logs
[**rest_v10_companies_company_id_managed_equipment_logs_id_get**](FieldProductivityManagedEquipmentEquipmentLogApi.md#rest_v10_companies_company_id_managed_equipment_logs_id_get) | **GET** /rest/v1.0/companies/{company_id}/managed_equipment_logs/{id} | Show an equipment log
[**rest_v10_companies_company_id_managed_equipment_logs_post**](FieldProductivityManagedEquipmentEquipmentLogApi.md#rest_v10_companies_company_id_managed_equipment_logs_post) | **POST** /rest/v1.0/companies/{company_id}/managed_equipment_logs | Create equipment log.
[**rest_v10_projects_project_id_managed_equipment_logs_get**](FieldProductivityManagedEquipmentEquipmentLogApi.md#rest_v10_projects_project_id_managed_equipment_logs_get) | **GET** /rest/v1.0/projects/{project_id}/managed_equipment_logs | List Project Equipment Logs
[**rest_v10_projects_project_id_managed_equipment_logs_id_delete**](FieldProductivityManagedEquipmentEquipmentLogApi.md#rest_v10_projects_project_id_managed_equipment_logs_id_delete) | **DELETE** /rest/v1.0/projects/{project_id}/managed_equipment_logs/{id} | Delete an Project Equipment Log
[**rest_v10_projects_project_id_managed_equipment_logs_id_get**](FieldProductivityManagedEquipmentEquipmentLogApi.md#rest_v10_projects_project_id_managed_equipment_logs_id_get) | **GET** /rest/v1.0/projects/{project_id}/managed_equipment_logs/{id} | Show an Project Equipment Log
[**rest_v10_projects_project_id_managed_equipment_logs_id_patch**](FieldProductivityManagedEquipmentEquipmentLogApi.md#rest_v10_projects_project_id_managed_equipment_logs_id_patch) | **PATCH** /rest/v1.0/projects/{project_id}/managed_equipment_logs/{id} | Update an Project Equipment Log
[**rest_v10_projects_project_id_managed_equipment_logs_post**](FieldProductivityManagedEquipmentEquipmentLogApi.md#rest_v10_projects_project_id_managed_equipment_logs_post) | **POST** /rest/v1.0/projects/{project_id}/managed_equipment_logs | Create an Project Equipment Log


# **rest_v10_companies_company_id_managed_equipment_logs_get**
> List[RestV10CompaniesCompanyIdManagedEquipmentLogsGet200ResponseInner] rest_v10_companies_company_id_managed_equipment_logs_get(procore_company_id, company_id, page=page, per_page=per_page)

List all equipment logs

Return a list of all equipment Logs for the projects the current user has access to.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_managed_equipment_logs_get200_response_inner import RestV10CompaniesCompanyIdManagedEquipmentLogsGet200ResponseInner
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
    api_instance = procore_sdk.FieldProductivityManagedEquipmentEquipmentLogApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List all equipment logs
        api_response = api_instance.rest_v10_companies_company_id_managed_equipment_logs_get(procore_company_id, company_id, page=page, per_page=per_page)
        print("The response of FieldProductivityManagedEquipmentEquipmentLogApi->rest_v10_companies_company_id_managed_equipment_logs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityManagedEquipmentEquipmentLogApi->rest_v10_companies_company_id_managed_equipment_logs_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[RestV10CompaniesCompanyIdManagedEquipmentLogsGet200ResponseInner]**](RestV10CompaniesCompanyIdManagedEquipmentLogsGet200ResponseInner.md)

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

# **rest_v10_companies_company_id_managed_equipment_logs_id_get**
> RestV10CompaniesCompanyIdManagedEquipmentLogsGet200ResponseInner rest_v10_companies_company_id_managed_equipment_logs_id_get(procore_company_id, id, company_id)

Show an equipment log

Return detailed information about a specific equipment log

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_managed_equipment_logs_get200_response_inner import RestV10CompaniesCompanyIdManagedEquipmentLogsGet200ResponseInner
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
    api_instance = procore_sdk.FieldProductivityManagedEquipmentEquipmentLogApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the log to get
    company_id = 56 # int | Unique identifier for the company.

    try:
        # Show an equipment log
        api_response = api_instance.rest_v10_companies_company_id_managed_equipment_logs_id_get(procore_company_id, id, company_id)
        print("The response of FieldProductivityManagedEquipmentEquipmentLogApi->rest_v10_companies_company_id_managed_equipment_logs_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityManagedEquipmentEquipmentLogApi->rest_v10_companies_company_id_managed_equipment_logs_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the log to get | 
 **company_id** | **int**| Unique identifier for the company. | 

### Return type

[**RestV10CompaniesCompanyIdManagedEquipmentLogsGet200ResponseInner**](RestV10CompaniesCompanyIdManagedEquipmentLogsGet200ResponseInner.md)

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

# **rest_v10_companies_company_id_managed_equipment_logs_post**
> RestV10CompaniesCompanyIdManagedEquipmentLogsGet200ResponseInner rest_v10_companies_company_id_managed_equipment_logs_post(procore_company_id, company_id, rest_v10_companies_company_id_managed_equipment_logs_post_request=rest_v10_companies_company_id_managed_equipment_logs_post_request)

Create equipment log.

Create a new equipment log.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_managed_equipment_logs_get200_response_inner import RestV10CompaniesCompanyIdManagedEquipmentLogsGet200ResponseInner
from procore_sdk.models.rest_v10_companies_company_id_managed_equipment_logs_post_request import RestV10CompaniesCompanyIdManagedEquipmentLogsPostRequest
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
    api_instance = procore_sdk.FieldProductivityManagedEquipmentEquipmentLogApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    rest_v10_companies_company_id_managed_equipment_logs_post_request = procore_sdk.RestV10CompaniesCompanyIdManagedEquipmentLogsPostRequest() # RestV10CompaniesCompanyIdManagedEquipmentLogsPostRequest |  (optional)

    try:
        # Create equipment log.
        api_response = api_instance.rest_v10_companies_company_id_managed_equipment_logs_post(procore_company_id, company_id, rest_v10_companies_company_id_managed_equipment_logs_post_request=rest_v10_companies_company_id_managed_equipment_logs_post_request)
        print("The response of FieldProductivityManagedEquipmentEquipmentLogApi->rest_v10_companies_company_id_managed_equipment_logs_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityManagedEquipmentEquipmentLogApi->rest_v10_companies_company_id_managed_equipment_logs_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **rest_v10_companies_company_id_managed_equipment_logs_post_request** | [**RestV10CompaniesCompanyIdManagedEquipmentLogsPostRequest**](RestV10CompaniesCompanyIdManagedEquipmentLogsPostRequest.md)|  | [optional] 

### Return type

[**RestV10CompaniesCompanyIdManagedEquipmentLogsGet200ResponseInner**](RestV10CompaniesCompanyIdManagedEquipmentLogsGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_managed_equipment_logs_get**
> List[RestV10CompaniesCompanyIdManagedEquipmentLogsGet200ResponseInner] rest_v10_projects_project_id_managed_equipment_logs_get(procore_company_id, project_id, page=page, per_page=per_page)

List Project Equipment Logs

Return a list of all equipment logs for a specified project

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_managed_equipment_logs_get200_response_inner import RestV10CompaniesCompanyIdManagedEquipmentLogsGet200ResponseInner
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
    api_instance = procore_sdk.FieldProductivityManagedEquipmentEquipmentLogApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Project Equipment Logs
        api_response = api_instance.rest_v10_projects_project_id_managed_equipment_logs_get(procore_company_id, project_id, page=page, per_page=per_page)
        print("The response of FieldProductivityManagedEquipmentEquipmentLogApi->rest_v10_projects_project_id_managed_equipment_logs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityManagedEquipmentEquipmentLogApi->rest_v10_projects_project_id_managed_equipment_logs_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[RestV10CompaniesCompanyIdManagedEquipmentLogsGet200ResponseInner]**](RestV10CompaniesCompanyIdManagedEquipmentLogsGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_managed_equipment_logs_id_delete**
> RestV10CompaniesCompanyIdManagedEquipmentLogsGet200ResponseInner rest_v10_projects_project_id_managed_equipment_logs_id_delete(procore_company_id, project_id, id)

Delete an Project Equipment Log

Detete a specific equipment log

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_managed_equipment_logs_get200_response_inner import RestV10CompaniesCompanyIdManagedEquipmentLogsGet200ResponseInner
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
    api_instance = procore_sdk.FieldProductivityManagedEquipmentEquipmentLogApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | ID of the company to get the logs for

    try:
        # Delete an Project Equipment Log
        api_response = api_instance.rest_v10_projects_project_id_managed_equipment_logs_id_delete(procore_company_id, project_id, id)
        print("The response of FieldProductivityManagedEquipmentEquipmentLogApi->rest_v10_projects_project_id_managed_equipment_logs_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityManagedEquipmentEquipmentLogApi->rest_v10_projects_project_id_managed_equipment_logs_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| ID of the company to get the logs for | 

### Return type

[**RestV10CompaniesCompanyIdManagedEquipmentLogsGet200ResponseInner**](RestV10CompaniesCompanyIdManagedEquipmentLogsGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_managed_equipment_logs_id_get**
> RestV10CompaniesCompanyIdManagedEquipmentLogsGet200ResponseInner rest_v10_projects_project_id_managed_equipment_logs_id_get(procore_company_id, project_id, id)

Show an Project Equipment Log

Return detailed information about a specific equipment log

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_managed_equipment_logs_get200_response_inner import RestV10CompaniesCompanyIdManagedEquipmentLogsGet200ResponseInner
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
    api_instance = procore_sdk.FieldProductivityManagedEquipmentEquipmentLogApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | ID of the company to get the logs for

    try:
        # Show an Project Equipment Log
        api_response = api_instance.rest_v10_projects_project_id_managed_equipment_logs_id_get(procore_company_id, project_id, id)
        print("The response of FieldProductivityManagedEquipmentEquipmentLogApi->rest_v10_projects_project_id_managed_equipment_logs_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityManagedEquipmentEquipmentLogApi->rest_v10_projects_project_id_managed_equipment_logs_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| ID of the company to get the logs for | 

### Return type

[**RestV10CompaniesCompanyIdManagedEquipmentLogsGet200ResponseInner**](RestV10CompaniesCompanyIdManagedEquipmentLogsGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_managed_equipment_logs_id_patch**
> RestV10CompaniesCompanyIdManagedEquipmentLogsGet200ResponseInner rest_v10_projects_project_id_managed_equipment_logs_id_patch(procore_company_id, project_id, id, rest_v10_companies_company_id_managed_equipment_logs_post_request=rest_v10_companies_company_id_managed_equipment_logs_post_request)

Update an Project Equipment Log

Update a specified equipment log

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_managed_equipment_logs_get200_response_inner import RestV10CompaniesCompanyIdManagedEquipmentLogsGet200ResponseInner
from procore_sdk.models.rest_v10_companies_company_id_managed_equipment_logs_post_request import RestV10CompaniesCompanyIdManagedEquipmentLogsPostRequest
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
    api_instance = procore_sdk.FieldProductivityManagedEquipmentEquipmentLogApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | ID of the company to get the logs for
    rest_v10_companies_company_id_managed_equipment_logs_post_request = procore_sdk.RestV10CompaniesCompanyIdManagedEquipmentLogsPostRequest() # RestV10CompaniesCompanyIdManagedEquipmentLogsPostRequest |  (optional)

    try:
        # Update an Project Equipment Log
        api_response = api_instance.rest_v10_projects_project_id_managed_equipment_logs_id_patch(procore_company_id, project_id, id, rest_v10_companies_company_id_managed_equipment_logs_post_request=rest_v10_companies_company_id_managed_equipment_logs_post_request)
        print("The response of FieldProductivityManagedEquipmentEquipmentLogApi->rest_v10_projects_project_id_managed_equipment_logs_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityManagedEquipmentEquipmentLogApi->rest_v10_projects_project_id_managed_equipment_logs_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| ID of the company to get the logs for | 
 **rest_v10_companies_company_id_managed_equipment_logs_post_request** | [**RestV10CompaniesCompanyIdManagedEquipmentLogsPostRequest**](RestV10CompaniesCompanyIdManagedEquipmentLogsPostRequest.md)|  | [optional] 

### Return type

[**RestV10CompaniesCompanyIdManagedEquipmentLogsGet200ResponseInner**](RestV10CompaniesCompanyIdManagedEquipmentLogsGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_managed_equipment_logs_post**
> RestV10CompaniesCompanyIdManagedEquipmentLogsGet200ResponseInner rest_v10_projects_project_id_managed_equipment_logs_post(procore_company_id, project_id, rest_v10_companies_company_id_managed_equipment_logs_post_request=rest_v10_companies_company_id_managed_equipment_logs_post_request)

Create an Project Equipment Log

Create a new equipment log entry

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_managed_equipment_logs_get200_response_inner import RestV10CompaniesCompanyIdManagedEquipmentLogsGet200ResponseInner
from procore_sdk.models.rest_v10_companies_company_id_managed_equipment_logs_post_request import RestV10CompaniesCompanyIdManagedEquipmentLogsPostRequest
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
    api_instance = procore_sdk.FieldProductivityManagedEquipmentEquipmentLogApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_companies_company_id_managed_equipment_logs_post_request = procore_sdk.RestV10CompaniesCompanyIdManagedEquipmentLogsPostRequest() # RestV10CompaniesCompanyIdManagedEquipmentLogsPostRequest |  (optional)

    try:
        # Create an Project Equipment Log
        api_response = api_instance.rest_v10_projects_project_id_managed_equipment_logs_post(procore_company_id, project_id, rest_v10_companies_company_id_managed_equipment_logs_post_request=rest_v10_companies_company_id_managed_equipment_logs_post_request)
        print("The response of FieldProductivityManagedEquipmentEquipmentLogApi->rest_v10_projects_project_id_managed_equipment_logs_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityManagedEquipmentEquipmentLogApi->rest_v10_projects_project_id_managed_equipment_logs_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_companies_company_id_managed_equipment_logs_post_request** | [**RestV10CompaniesCompanyIdManagedEquipmentLogsPostRequest**](RestV10CompaniesCompanyIdManagedEquipmentLogsPostRequest.md)|  | [optional] 

### Return type

[**RestV10CompaniesCompanyIdManagedEquipmentLogsGet200ResponseInner**](RestV10CompaniesCompanyIdManagedEquipmentLogsGet200ResponseInner.md)

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

