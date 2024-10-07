# procore_sdk.CoreProjectDepartmentsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_departments_get**](CoreProjectDepartmentsApi.md#rest_v10_departments_get) | **GET** /rest/v1.0/departments | List Departments
[**rest_v10_departments_id_delete**](CoreProjectDepartmentsApi.md#rest_v10_departments_id_delete) | **DELETE** /rest/v1.0/departments/{id} | Delete Department
[**rest_v10_departments_id_get**](CoreProjectDepartmentsApi.md#rest_v10_departments_id_get) | **GET** /rest/v1.0/departments/{id} | Show Department
[**rest_v10_departments_id_patch**](CoreProjectDepartmentsApi.md#rest_v10_departments_id_patch) | **PATCH** /rest/v1.0/departments/{id} | Update Department
[**rest_v10_departments_post**](CoreProjectDepartmentsApi.md#rest_v10_departments_post) | **POST** /rest/v1.0/departments | Create Department


# **rest_v10_departments_get**
> List[Department] rest_v10_departments_get(procore_company_id, company_id, page=page, per_page=per_page)

List Departments

Return a list of Departments.

### Example


```python
import procore_sdk
from procore_sdk.models.department import Department
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
    api_instance = procore_sdk.CoreProjectDepartmentsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Departments
        api_response = api_instance.rest_v10_departments_get(procore_company_id, company_id, page=page, per_page=per_page)
        print("The response of CoreProjectDepartmentsApi->rest_v10_departments_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectDepartmentsApi->rest_v10_departments_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[Department]**](Department.md)

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

# **rest_v10_departments_id_delete**
> rest_v10_departments_id_delete(procore_company_id, id, company_id)

Delete Department

Delete a Department.

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
    api_instance = procore_sdk.CoreProjectDepartmentsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | Department ID
    company_id = 56 # int | Unique identifier for the company.

    try:
        # Delete Department
        api_instance.rest_v10_departments_id_delete(procore_company_id, id, company_id)
    except Exception as e:
        print("Exception when calling CoreProjectDepartmentsApi->rest_v10_departments_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| Department ID | 
 **company_id** | **int**| Unique identifier for the company. | 

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
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Department not found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_departments_id_get**
> Department rest_v10_departments_id_get(procore_company_id, id, company_id)

Show Department

Return details for a Department.

### Example


```python
import procore_sdk
from procore_sdk.models.department import Department
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
    api_instance = procore_sdk.CoreProjectDepartmentsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | Department ID
    company_id = 56 # int | Unique identifier for the company.

    try:
        # Show Department
        api_response = api_instance.rest_v10_departments_id_get(procore_company_id, id, company_id)
        print("The response of CoreProjectDepartmentsApi->rest_v10_departments_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectDepartmentsApi->rest_v10_departments_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| Department ID | 
 **company_id** | **int**| Unique identifier for the company. | 

### Return type

[**Department**](Department.md)

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
**404** | Department not found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_departments_id_patch**
> Department rest_v10_departments_id_patch(procore_company_id, id, department_body)

Update Department

Update a Department.

### Example


```python
import procore_sdk
from procore_sdk.models.department import Department
from procore_sdk.models.department_body import DepartmentBody
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
    api_instance = procore_sdk.CoreProjectDepartmentsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | Department ID
    department_body = procore_sdk.DepartmentBody() # DepartmentBody | 

    try:
        # Update Department
        api_response = api_instance.rest_v10_departments_id_patch(procore_company_id, id, department_body)
        print("The response of CoreProjectDepartmentsApi->rest_v10_departments_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectDepartmentsApi->rest_v10_departments_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| Department ID | 
 **department_body** | [**DepartmentBody**](DepartmentBody.md)|  | 

### Return type

[**Department**](Department.md)

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
**404** | Department not found |  -  |
**422** | Error updating Department |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_departments_post**
> Department rest_v10_departments_post(procore_company_id, department_body)

Create Department

Create a new Department.

### Example


```python
import procore_sdk
from procore_sdk.models.department import Department
from procore_sdk.models.department_body import DepartmentBody
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
    api_instance = procore_sdk.CoreProjectDepartmentsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    department_body = procore_sdk.DepartmentBody() # DepartmentBody | 

    try:
        # Create Department
        api_response = api_instance.rest_v10_departments_post(procore_company_id, department_body)
        print("The response of CoreProjectDepartmentsApi->rest_v10_departments_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectDepartmentsApi->rest_v10_departments_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **department_body** | [**DepartmentBody**](DepartmentBody.md)|  | 

### Return type

[**Department**](Department.md)

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
**422** | Error creating Department |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

