# procore_sdk.FieldProductivityTimesheetTimesheetsFiltersApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_timesheets_filters_approval_status_get**](FieldProductivityTimesheetTimesheetsFiltersApi.md#rest_v10_companies_company_id_timesheets_filters_approval_status_get) | **GET** /rest/v1.0/companies/{company_id}/timesheets/filters/approval_status | Show timesheet approval status filters
[**rest_v10_companies_company_id_timesheets_filters_billable_get**](FieldProductivityTimesheetTimesheetsFiltersApi.md#rest_v10_companies_company_id_timesheets_filters_billable_get) | **GET** /rest/v1.0/companies/{company_id}/timesheets/filters/billable | Show timesheet billable filters
[**rest_v10_companies_company_id_timesheets_filters_cost_codes_get**](FieldProductivityTimesheetTimesheetsFiltersApi.md#rest_v10_companies_company_id_timesheets_filters_cost_codes_get) | **GET** /rest/v1.0/companies/{company_id}/timesheets/filters/cost_codes | Show timesheet cost code filters
[**rest_v10_companies_company_id_timesheets_filters_created_by_get**](FieldProductivityTimesheetTimesheetsFiltersApi.md#rest_v10_companies_company_id_timesheets_filters_created_by_get) | **GET** /rest/v1.0/companies/{company_id}/timesheets/filters/created_by | Show timesheet created by filters
[**rest_v10_companies_company_id_timesheets_filters_crews_get**](FieldProductivityTimesheetTimesheetsFiltersApi.md#rest_v10_companies_company_id_timesheets_filters_crews_get) | **GET** /rest/v1.0/companies/{company_id}/timesheets/filters/crews | Show timesheet crews filters
[**rest_v10_companies_company_id_timesheets_filters_departments_get**](FieldProductivityTimesheetTimesheetsFiltersApi.md#rest_v10_companies_company_id_timesheets_filters_departments_get) | **GET** /rest/v1.0/companies/{company_id}/timesheets/filters/departments | Show timesheet department filters
[**rest_v10_companies_company_id_timesheets_filters_employee_ids_get**](FieldProductivityTimesheetTimesheetsFiltersApi.md#rest_v10_companies_company_id_timesheets_filters_employee_ids_get) | **GET** /rest/v1.0/companies/{company_id}/timesheets/filters/employee_ids | Show timesheet employee id filters
[**rest_v10_companies_company_id_timesheets_filters_employees_get**](FieldProductivityTimesheetTimesheetsFiltersApi.md#rest_v10_companies_company_id_timesheets_filters_employees_get) | **GET** /rest/v1.0/companies/{company_id}/timesheets/filters/employees | Show timesheet employee filters
[**rest_v10_companies_company_id_timesheets_filters_locations_get**](FieldProductivityTimesheetTimesheetsFiltersApi.md#rest_v10_companies_company_id_timesheets_filters_locations_get) | **GET** /rest/v1.0/companies/{company_id}/timesheets/filters/locations | Show timesheet location filters
[**rest_v10_companies_company_id_timesheets_filters_projects_get**](FieldProductivityTimesheetTimesheetsFiltersApi.md#rest_v10_companies_company_id_timesheets_filters_projects_get) | **GET** /rest/v1.0/companies/{company_id}/timesheets/filters/projects | Show timesheet project filters
[**rest_v10_companies_company_id_timesheets_filters_regions_get**](FieldProductivityTimesheetTimesheetsFiltersApi.md#rest_v10_companies_company_id_timesheets_filters_regions_get) | **GET** /rest/v1.0/companies/{company_id}/timesheets/filters/regions | Show timesheet region filters
[**rest_v10_companies_company_id_timesheets_filters_sub_job_get**](FieldProductivityTimesheetTimesheetsFiltersApi.md#rest_v10_companies_company_id_timesheets_filters_sub_job_get) | **GET** /rest/v1.0/companies/{company_id}/timesheets/filters/sub_job | Show timesheet sub job filters
[**rest_v10_companies_company_id_timesheets_filters_time_type_get**](FieldProductivityTimesheetTimesheetsFiltersApi.md#rest_v10_companies_company_id_timesheets_filters_time_type_get) | **GET** /rest/v1.0/companies/{company_id}/timesheets/filters/time_type | Show timesheet time type filters
[**rest_v10_companies_company_id_timesheets_filters_wbs_codes_get**](FieldProductivityTimesheetTimesheetsFiltersApi.md#rest_v10_companies_company_id_timesheets_filters_wbs_codes_get) | **GET** /rest/v1.0/companies/{company_id}/timesheets/filters/wbs_codes | Show timesheet wbs code filters
[**rest_v10_companies_company_id_timesheets_filters_work_classifications_get**](FieldProductivityTimesheetTimesheetsFiltersApi.md#rest_v10_companies_company_id_timesheets_filters_work_classifications_get) | **GET** /rest/v1.0/companies/{company_id}/timesheets/filters/work_classifications | Show timesheet work classification filters


# **rest_v10_companies_company_id_timesheets_filters_approval_status_get**
> List[RestV10CompaniesCompanyIdTimesheetsFiltersApprovalStatusGet200ResponseInner] rest_v10_companies_company_id_timesheets_filters_approval_status_get(procore_company_id, company_id)

Show timesheet approval status filters

Show timesheet approval status filters

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_timesheets_filters_approval_status_get200_response_inner import RestV10CompaniesCompanyIdTimesheetsFiltersApprovalStatusGet200ResponseInner
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
    api_instance = procore_sdk.FieldProductivityTimesheetTimesheetsFiltersApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.

    try:
        # Show timesheet approval status filters
        api_response = api_instance.rest_v10_companies_company_id_timesheets_filters_approval_status_get(procore_company_id, company_id)
        print("The response of FieldProductivityTimesheetTimesheetsFiltersApi->rest_v10_companies_company_id_timesheets_filters_approval_status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimesheetTimesheetsFiltersApi->rest_v10_companies_company_id_timesheets_filters_approval_status_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 

### Return type

[**List[RestV10CompaniesCompanyIdTimesheetsFiltersApprovalStatusGet200ResponseInner]**](RestV10CompaniesCompanyIdTimesheetsFiltersApprovalStatusGet200ResponseInner.md)

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_timesheets_filters_billable_get**
> List[RestV10CompaniesCompanyIdTimesheetsFiltersBillableGet200ResponseInner] rest_v10_companies_company_id_timesheets_filters_billable_get(procore_company_id, company_id)

Show timesheet billable filters

Show timesheet billable filters

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_timesheets_filters_billable_get200_response_inner import RestV10CompaniesCompanyIdTimesheetsFiltersBillableGet200ResponseInner
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
    api_instance = procore_sdk.FieldProductivityTimesheetTimesheetsFiltersApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.

    try:
        # Show timesheet billable filters
        api_response = api_instance.rest_v10_companies_company_id_timesheets_filters_billable_get(procore_company_id, company_id)
        print("The response of FieldProductivityTimesheetTimesheetsFiltersApi->rest_v10_companies_company_id_timesheets_filters_billable_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimesheetTimesheetsFiltersApi->rest_v10_companies_company_id_timesheets_filters_billable_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 

### Return type

[**List[RestV10CompaniesCompanyIdTimesheetsFiltersBillableGet200ResponseInner]**](RestV10CompaniesCompanyIdTimesheetsFiltersBillableGet200ResponseInner.md)

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_timesheets_filters_cost_codes_get**
> List[RestV10CompaniesCompanyIdTimesheetsFiltersCostCodesGet200ResponseInner] rest_v10_companies_company_id_timesheets_filters_cost_codes_get(procore_company_id, company_id)

Show timesheet cost code filters

Show timesheet cost code filters

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_timesheets_filters_cost_codes_get200_response_inner import RestV10CompaniesCompanyIdTimesheetsFiltersCostCodesGet200ResponseInner
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
    api_instance = procore_sdk.FieldProductivityTimesheetTimesheetsFiltersApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.

    try:
        # Show timesheet cost code filters
        api_response = api_instance.rest_v10_companies_company_id_timesheets_filters_cost_codes_get(procore_company_id, company_id)
        print("The response of FieldProductivityTimesheetTimesheetsFiltersApi->rest_v10_companies_company_id_timesheets_filters_cost_codes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimesheetTimesheetsFiltersApi->rest_v10_companies_company_id_timesheets_filters_cost_codes_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 

### Return type

[**List[RestV10CompaniesCompanyIdTimesheetsFiltersCostCodesGet200ResponseInner]**](RestV10CompaniesCompanyIdTimesheetsFiltersCostCodesGet200ResponseInner.md)

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_timesheets_filters_created_by_get**
> List[RestV10CompaniesCompanyIdTimesheetsFiltersCreatedByGet200ResponseInner] rest_v10_companies_company_id_timesheets_filters_created_by_get(procore_company_id, company_id)

Show timesheet created by filters

Show timesheet created by filters

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_timesheets_filters_created_by_get200_response_inner import RestV10CompaniesCompanyIdTimesheetsFiltersCreatedByGet200ResponseInner
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
    api_instance = procore_sdk.FieldProductivityTimesheetTimesheetsFiltersApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.

    try:
        # Show timesheet created by filters
        api_response = api_instance.rest_v10_companies_company_id_timesheets_filters_created_by_get(procore_company_id, company_id)
        print("The response of FieldProductivityTimesheetTimesheetsFiltersApi->rest_v10_companies_company_id_timesheets_filters_created_by_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimesheetTimesheetsFiltersApi->rest_v10_companies_company_id_timesheets_filters_created_by_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 

### Return type

[**List[RestV10CompaniesCompanyIdTimesheetsFiltersCreatedByGet200ResponseInner]**](RestV10CompaniesCompanyIdTimesheetsFiltersCreatedByGet200ResponseInner.md)

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_timesheets_filters_crews_get**
> List[RestV10CompaniesCompanyIdTimesheetsFiltersCrewsGet200ResponseInner] rest_v10_companies_company_id_timesheets_filters_crews_get(procore_company_id, company_id)

Show timesheet crews filters

Show timesheet crews filters

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_timesheets_filters_crews_get200_response_inner import RestV10CompaniesCompanyIdTimesheetsFiltersCrewsGet200ResponseInner
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
    api_instance = procore_sdk.FieldProductivityTimesheetTimesheetsFiltersApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.

    try:
        # Show timesheet crews filters
        api_response = api_instance.rest_v10_companies_company_id_timesheets_filters_crews_get(procore_company_id, company_id)
        print("The response of FieldProductivityTimesheetTimesheetsFiltersApi->rest_v10_companies_company_id_timesheets_filters_crews_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimesheetTimesheetsFiltersApi->rest_v10_companies_company_id_timesheets_filters_crews_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 

### Return type

[**List[RestV10CompaniesCompanyIdTimesheetsFiltersCrewsGet200ResponseInner]**](RestV10CompaniesCompanyIdTimesheetsFiltersCrewsGet200ResponseInner.md)

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_timesheets_filters_departments_get**
> List[RestV10CompaniesCompanyIdTimesheetsFiltersDepartmentsGet200ResponseInner] rest_v10_companies_company_id_timesheets_filters_departments_get(procore_company_id, company_id)

Show timesheet department filters

Show timesheet department filters

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_timesheets_filters_departments_get200_response_inner import RestV10CompaniesCompanyIdTimesheetsFiltersDepartmentsGet200ResponseInner
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
    api_instance = procore_sdk.FieldProductivityTimesheetTimesheetsFiltersApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.

    try:
        # Show timesheet department filters
        api_response = api_instance.rest_v10_companies_company_id_timesheets_filters_departments_get(procore_company_id, company_id)
        print("The response of FieldProductivityTimesheetTimesheetsFiltersApi->rest_v10_companies_company_id_timesheets_filters_departments_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimesheetTimesheetsFiltersApi->rest_v10_companies_company_id_timesheets_filters_departments_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 

### Return type

[**List[RestV10CompaniesCompanyIdTimesheetsFiltersDepartmentsGet200ResponseInner]**](RestV10CompaniesCompanyIdTimesheetsFiltersDepartmentsGet200ResponseInner.md)

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_timesheets_filters_employee_ids_get**
> List[RestV10CompaniesCompanyIdTimesheetsFiltersEmployeeIdsGet200ResponseInner] rest_v10_companies_company_id_timesheets_filters_employee_ids_get(procore_company_id, company_id)

Show timesheet employee id filters

Show timesheet employee id filters

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_timesheets_filters_employee_ids_get200_response_inner import RestV10CompaniesCompanyIdTimesheetsFiltersEmployeeIdsGet200ResponseInner
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
    api_instance = procore_sdk.FieldProductivityTimesheetTimesheetsFiltersApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.

    try:
        # Show timesheet employee id filters
        api_response = api_instance.rest_v10_companies_company_id_timesheets_filters_employee_ids_get(procore_company_id, company_id)
        print("The response of FieldProductivityTimesheetTimesheetsFiltersApi->rest_v10_companies_company_id_timesheets_filters_employee_ids_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimesheetTimesheetsFiltersApi->rest_v10_companies_company_id_timesheets_filters_employee_ids_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 

### Return type

[**List[RestV10CompaniesCompanyIdTimesheetsFiltersEmployeeIdsGet200ResponseInner]**](RestV10CompaniesCompanyIdTimesheetsFiltersEmployeeIdsGet200ResponseInner.md)

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_timesheets_filters_employees_get**
> List[RestV10CompaniesCompanyIdTimesheetsFiltersEmployeesGet200ResponseInner] rest_v10_companies_company_id_timesheets_filters_employees_get(procore_company_id, company_id)

Show timesheet employee filters

Show timesheet employee filters

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_timesheets_filters_employees_get200_response_inner import RestV10CompaniesCompanyIdTimesheetsFiltersEmployeesGet200ResponseInner
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
    api_instance = procore_sdk.FieldProductivityTimesheetTimesheetsFiltersApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.

    try:
        # Show timesheet employee filters
        api_response = api_instance.rest_v10_companies_company_id_timesheets_filters_employees_get(procore_company_id, company_id)
        print("The response of FieldProductivityTimesheetTimesheetsFiltersApi->rest_v10_companies_company_id_timesheets_filters_employees_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimesheetTimesheetsFiltersApi->rest_v10_companies_company_id_timesheets_filters_employees_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 

### Return type

[**List[RestV10CompaniesCompanyIdTimesheetsFiltersEmployeesGet200ResponseInner]**](RestV10CompaniesCompanyIdTimesheetsFiltersEmployeesGet200ResponseInner.md)

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_timesheets_filters_locations_get**
> List[RestV10CompaniesCompanyIdTimesheetsFiltersLocationsGet200ResponseInner] rest_v10_companies_company_id_timesheets_filters_locations_get(procore_company_id, company_id)

Show timesheet location filters

Show timesheet location filters

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_timesheets_filters_locations_get200_response_inner import RestV10CompaniesCompanyIdTimesheetsFiltersLocationsGet200ResponseInner
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
    api_instance = procore_sdk.FieldProductivityTimesheetTimesheetsFiltersApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.

    try:
        # Show timesheet location filters
        api_response = api_instance.rest_v10_companies_company_id_timesheets_filters_locations_get(procore_company_id, company_id)
        print("The response of FieldProductivityTimesheetTimesheetsFiltersApi->rest_v10_companies_company_id_timesheets_filters_locations_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimesheetTimesheetsFiltersApi->rest_v10_companies_company_id_timesheets_filters_locations_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 

### Return type

[**List[RestV10CompaniesCompanyIdTimesheetsFiltersLocationsGet200ResponseInner]**](RestV10CompaniesCompanyIdTimesheetsFiltersLocationsGet200ResponseInner.md)

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_timesheets_filters_projects_get**
> List[RestV10CompaniesCompanyIdTimesheetsFiltersProjectsGet200ResponseInner] rest_v10_companies_company_id_timesheets_filters_projects_get(procore_company_id, company_id)

Show timesheet project filters

Show timesheet approval status filters

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_timesheets_filters_projects_get200_response_inner import RestV10CompaniesCompanyIdTimesheetsFiltersProjectsGet200ResponseInner
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
    api_instance = procore_sdk.FieldProductivityTimesheetTimesheetsFiltersApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.

    try:
        # Show timesheet project filters
        api_response = api_instance.rest_v10_companies_company_id_timesheets_filters_projects_get(procore_company_id, company_id)
        print("The response of FieldProductivityTimesheetTimesheetsFiltersApi->rest_v10_companies_company_id_timesheets_filters_projects_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimesheetTimesheetsFiltersApi->rest_v10_companies_company_id_timesheets_filters_projects_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 

### Return type

[**List[RestV10CompaniesCompanyIdTimesheetsFiltersProjectsGet200ResponseInner]**](RestV10CompaniesCompanyIdTimesheetsFiltersProjectsGet200ResponseInner.md)

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_timesheets_filters_regions_get**
> List[RestV10CompaniesCompanyIdTimesheetsFiltersRegionsGet200ResponseInner] rest_v10_companies_company_id_timesheets_filters_regions_get(procore_company_id, company_id)

Show timesheet region filters

Show timesheet region filters

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_timesheets_filters_regions_get200_response_inner import RestV10CompaniesCompanyIdTimesheetsFiltersRegionsGet200ResponseInner
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
    api_instance = procore_sdk.FieldProductivityTimesheetTimesheetsFiltersApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.

    try:
        # Show timesheet region filters
        api_response = api_instance.rest_v10_companies_company_id_timesheets_filters_regions_get(procore_company_id, company_id)
        print("The response of FieldProductivityTimesheetTimesheetsFiltersApi->rest_v10_companies_company_id_timesheets_filters_regions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimesheetTimesheetsFiltersApi->rest_v10_companies_company_id_timesheets_filters_regions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 

### Return type

[**List[RestV10CompaniesCompanyIdTimesheetsFiltersRegionsGet200ResponseInner]**](RestV10CompaniesCompanyIdTimesheetsFiltersRegionsGet200ResponseInner.md)

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_timesheets_filters_sub_job_get**
> List[RestV10CompaniesCompanyIdTimesheetsFiltersSubJobGet200ResponseInner] rest_v10_companies_company_id_timesheets_filters_sub_job_get(procore_company_id, company_id)

Show timesheet sub job filters

Show timesheet sub job filters

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_timesheets_filters_sub_job_get200_response_inner import RestV10CompaniesCompanyIdTimesheetsFiltersSubJobGet200ResponseInner
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
    api_instance = procore_sdk.FieldProductivityTimesheetTimesheetsFiltersApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.

    try:
        # Show timesheet sub job filters
        api_response = api_instance.rest_v10_companies_company_id_timesheets_filters_sub_job_get(procore_company_id, company_id)
        print("The response of FieldProductivityTimesheetTimesheetsFiltersApi->rest_v10_companies_company_id_timesheets_filters_sub_job_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimesheetTimesheetsFiltersApi->rest_v10_companies_company_id_timesheets_filters_sub_job_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 

### Return type

[**List[RestV10CompaniesCompanyIdTimesheetsFiltersSubJobGet200ResponseInner]**](RestV10CompaniesCompanyIdTimesheetsFiltersSubJobGet200ResponseInner.md)

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_timesheets_filters_time_type_get**
> List[RestV10CompaniesCompanyIdTimesheetsFiltersTimeTypeGet200ResponseInner] rest_v10_companies_company_id_timesheets_filters_time_type_get(procore_company_id, company_id)

Show timesheet time type filters

Show timesheet time type filters

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_timesheets_filters_time_type_get200_response_inner import RestV10CompaniesCompanyIdTimesheetsFiltersTimeTypeGet200ResponseInner
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
    api_instance = procore_sdk.FieldProductivityTimesheetTimesheetsFiltersApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.

    try:
        # Show timesheet time type filters
        api_response = api_instance.rest_v10_companies_company_id_timesheets_filters_time_type_get(procore_company_id, company_id)
        print("The response of FieldProductivityTimesheetTimesheetsFiltersApi->rest_v10_companies_company_id_timesheets_filters_time_type_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimesheetTimesheetsFiltersApi->rest_v10_companies_company_id_timesheets_filters_time_type_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 

### Return type

[**List[RestV10CompaniesCompanyIdTimesheetsFiltersTimeTypeGet200ResponseInner]**](RestV10CompaniesCompanyIdTimesheetsFiltersTimeTypeGet200ResponseInner.md)

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_timesheets_filters_wbs_codes_get**
> List[RestV10CompaniesCompanyIdTimesheetsFiltersWbsCodesGet200ResponseInner] rest_v10_companies_company_id_timesheets_filters_wbs_codes_get(procore_company_id, company_id)

Show timesheet wbs code filters

Show timesheet wbs code filters

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_timesheets_filters_wbs_codes_get200_response_inner import RestV10CompaniesCompanyIdTimesheetsFiltersWbsCodesGet200ResponseInner
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
    api_instance = procore_sdk.FieldProductivityTimesheetTimesheetsFiltersApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.

    try:
        # Show timesheet wbs code filters
        api_response = api_instance.rest_v10_companies_company_id_timesheets_filters_wbs_codes_get(procore_company_id, company_id)
        print("The response of FieldProductivityTimesheetTimesheetsFiltersApi->rest_v10_companies_company_id_timesheets_filters_wbs_codes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimesheetTimesheetsFiltersApi->rest_v10_companies_company_id_timesheets_filters_wbs_codes_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 

### Return type

[**List[RestV10CompaniesCompanyIdTimesheetsFiltersWbsCodesGet200ResponseInner]**](RestV10CompaniesCompanyIdTimesheetsFiltersWbsCodesGet200ResponseInner.md)

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_timesheets_filters_work_classifications_get**
> List[RestV10CompaniesCompanyIdTimesheetsFiltersWorkClassificationsGet200ResponseInner] rest_v10_companies_company_id_timesheets_filters_work_classifications_get(procore_company_id, company_id)

Show timesheet work classification filters

Show timesheet work classification filters

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_timesheets_filters_work_classifications_get200_response_inner import RestV10CompaniesCompanyIdTimesheetsFiltersWorkClassificationsGet200ResponseInner
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
    api_instance = procore_sdk.FieldProductivityTimesheetTimesheetsFiltersApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.

    try:
        # Show timesheet work classification filters
        api_response = api_instance.rest_v10_companies_company_id_timesheets_filters_work_classifications_get(procore_company_id, company_id)
        print("The response of FieldProductivityTimesheetTimesheetsFiltersApi->rest_v10_companies_company_id_timesheets_filters_work_classifications_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimesheetTimesheetsFiltersApi->rest_v10_companies_company_id_timesheets_filters_work_classifications_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 

### Return type

[**List[RestV10CompaniesCompanyIdTimesheetsFiltersWorkClassificationsGet200ResponseInner]**](RestV10CompaniesCompanyIdTimesheetsFiltersWorkClassificationsGet200ResponseInner.md)

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

