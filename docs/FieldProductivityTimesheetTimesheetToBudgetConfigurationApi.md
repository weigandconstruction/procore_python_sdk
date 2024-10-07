# procore_sdk.FieldProductivityTimesheetTimesheetToBudgetConfigurationApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_timesheets_timesheet_to_budget_configuration_delete**](FieldProductivityTimesheetTimesheetToBudgetConfigurationApi.md#rest_v10_companies_company_id_timesheets_timesheet_to_budget_configuration_delete) | **DELETE** /rest/v1.0/companies/{company_id}/timesheets/timesheet_to_budget_configuration | Delete timesheet to budget configuration
[**rest_v10_companies_company_id_timesheets_timesheet_to_budget_configuration_get**](FieldProductivityTimesheetTimesheetToBudgetConfigurationApi.md#rest_v10_companies_company_id_timesheets_timesheet_to_budget_configuration_get) | **GET** /rest/v1.0/companies/{company_id}/timesheets/timesheet_to_budget_configuration | Show timesheet to budget configuration
[**rest_v10_companies_company_id_timesheets_timesheet_to_budget_configuration_patch**](FieldProductivityTimesheetTimesheetToBudgetConfigurationApi.md#rest_v10_companies_company_id_timesheets_timesheet_to_budget_configuration_patch) | **PATCH** /rest/v1.0/companies/{company_id}/timesheets/timesheet_to_budget_configuration | Update timesheet to budget configuration
[**rest_v10_companies_company_id_timesheets_timesheet_to_budget_configuration_post**](FieldProductivityTimesheetTimesheetToBudgetConfigurationApi.md#rest_v10_companies_company_id_timesheets_timesheet_to_budget_configuration_post) | **POST** /rest/v1.0/companies/{company_id}/timesheets/timesheet_to_budget_configuration | Create timesheet to budget configuration


# **rest_v10_companies_company_id_timesheets_timesheet_to_budget_configuration_delete**
> rest_v10_companies_company_id_timesheets_timesheet_to_budget_configuration_delete(procore_company_id, company_id)

Delete timesheet to budget configuration

Delete timesheet to budget configuration

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
    api_instance = procore_sdk.FieldProductivityTimesheetTimesheetToBudgetConfigurationApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.

    try:
        # Delete timesheet to budget configuration
        api_instance.rest_v10_companies_company_id_timesheets_timesheet_to_budget_configuration_delete(procore_company_id, company_id)
    except Exception as e:
        print("Exception when calling FieldProductivityTimesheetTimesheetToBudgetConfigurationApi->rest_v10_companies_company_id_timesheets_timesheet_to_budget_configuration_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
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
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_timesheets_timesheet_to_budget_configuration_get**
> TimesheetToBudgetConfiguration rest_v10_companies_company_id_timesheets_timesheet_to_budget_configuration_get(procore_company_id, company_id)

Show timesheet to budget configuration

Show timesheet to budget configuration

### Example


```python
import procore_sdk
from procore_sdk.models.timesheet_to_budget_configuration import TimesheetToBudgetConfiguration
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
    api_instance = procore_sdk.FieldProductivityTimesheetTimesheetToBudgetConfigurationApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.

    try:
        # Show timesheet to budget configuration
        api_response = api_instance.rest_v10_companies_company_id_timesheets_timesheet_to_budget_configuration_get(procore_company_id, company_id)
        print("The response of FieldProductivityTimesheetTimesheetToBudgetConfigurationApi->rest_v10_companies_company_id_timesheets_timesheet_to_budget_configuration_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimesheetTimesheetToBudgetConfigurationApi->rest_v10_companies_company_id_timesheets_timesheet_to_budget_configuration_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 

### Return type

[**TimesheetToBudgetConfiguration**](TimesheetToBudgetConfiguration.md)

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

# **rest_v10_companies_company_id_timesheets_timesheet_to_budget_configuration_patch**
> TimesheetToBudgetConfiguration rest_v10_companies_company_id_timesheets_timesheet_to_budget_configuration_patch(procore_company_id, company_id, rest_v10_companies_company_id_timesheets_timesheet_to_budget_configuration_patch_request)

Update timesheet to budget configuration

Update timesheet to budget configuration

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_timesheets_timesheet_to_budget_configuration_patch_request import RestV10CompaniesCompanyIdTimesheetsTimesheetToBudgetConfigurationPatchRequest
from procore_sdk.models.timesheet_to_budget_configuration import TimesheetToBudgetConfiguration
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
    api_instance = procore_sdk.FieldProductivityTimesheetTimesheetToBudgetConfigurationApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    rest_v10_companies_company_id_timesheets_timesheet_to_budget_configuration_patch_request = procore_sdk.RestV10CompaniesCompanyIdTimesheetsTimesheetToBudgetConfigurationPatchRequest() # RestV10CompaniesCompanyIdTimesheetsTimesheetToBudgetConfigurationPatchRequest | 

    try:
        # Update timesheet to budget configuration
        api_response = api_instance.rest_v10_companies_company_id_timesheets_timesheet_to_budget_configuration_patch(procore_company_id, company_id, rest_v10_companies_company_id_timesheets_timesheet_to_budget_configuration_patch_request)
        print("The response of FieldProductivityTimesheetTimesheetToBudgetConfigurationApi->rest_v10_companies_company_id_timesheets_timesheet_to_budget_configuration_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimesheetTimesheetToBudgetConfigurationApi->rest_v10_companies_company_id_timesheets_timesheet_to_budget_configuration_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **rest_v10_companies_company_id_timesheets_timesheet_to_budget_configuration_patch_request** | [**RestV10CompaniesCompanyIdTimesheetsTimesheetToBudgetConfigurationPatchRequest**](RestV10CompaniesCompanyIdTimesheetsTimesheetToBudgetConfigurationPatchRequest.md)|  | 

### Return type

[**TimesheetToBudgetConfiguration**](TimesheetToBudgetConfiguration.md)

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_timesheets_timesheet_to_budget_configuration_post**
> TimesheetToBudgetConfiguration rest_v10_companies_company_id_timesheets_timesheet_to_budget_configuration_post(procore_company_id, company_id, rest_v10_companies_company_id_timesheets_timesheet_to_budget_configuration_post_request)

Create timesheet to budget configuration

Create timesheet to budget configuration

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_timesheets_timesheet_to_budget_configuration_post_request import RestV10CompaniesCompanyIdTimesheetsTimesheetToBudgetConfigurationPostRequest
from procore_sdk.models.timesheet_to_budget_configuration import TimesheetToBudgetConfiguration
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
    api_instance = procore_sdk.FieldProductivityTimesheetTimesheetToBudgetConfigurationApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    rest_v10_companies_company_id_timesheets_timesheet_to_budget_configuration_post_request = procore_sdk.RestV10CompaniesCompanyIdTimesheetsTimesheetToBudgetConfigurationPostRequest() # RestV10CompaniesCompanyIdTimesheetsTimesheetToBudgetConfigurationPostRequest | 

    try:
        # Create timesheet to budget configuration
        api_response = api_instance.rest_v10_companies_company_id_timesheets_timesheet_to_budget_configuration_post(procore_company_id, company_id, rest_v10_companies_company_id_timesheets_timesheet_to_budget_configuration_post_request)
        print("The response of FieldProductivityTimesheetTimesheetToBudgetConfigurationApi->rest_v10_companies_company_id_timesheets_timesheet_to_budget_configuration_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimesheetTimesheetToBudgetConfigurationApi->rest_v10_companies_company_id_timesheets_timesheet_to_budget_configuration_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **rest_v10_companies_company_id_timesheets_timesheet_to_budget_configuration_post_request** | [**RestV10CompaniesCompanyIdTimesheetsTimesheetToBudgetConfigurationPostRequest**](RestV10CompaniesCompanyIdTimesheetsTimesheetToBudgetConfigurationPostRequest.md)|  | 

### Return type

[**TimesheetToBudgetConfiguration**](TimesheetToBudgetConfiguration.md)

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
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

