# procore_sdk.FieldProductivityTimesheetRoundingConfigurationApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_rounding_configuration_delete**](FieldProductivityTimesheetRoundingConfigurationApi.md#rest_v10_companies_company_id_rounding_configuration_delete) | **DELETE** /rest/v1.0/companies/{company_id}/rounding_configuration | Delete rounding configuration
[**rest_v10_companies_company_id_rounding_configuration_get**](FieldProductivityTimesheetRoundingConfigurationApi.md#rest_v10_companies_company_id_rounding_configuration_get) | **GET** /rest/v1.0/companies/{company_id}/rounding_configuration | Show rounding configuration
[**rest_v10_companies_company_id_rounding_configuration_patch**](FieldProductivityTimesheetRoundingConfigurationApi.md#rest_v10_companies_company_id_rounding_configuration_patch) | **PATCH** /rest/v1.0/companies/{company_id}/rounding_configuration | Update rounding configuration
[**rest_v10_companies_company_id_rounding_configuration_post**](FieldProductivityTimesheetRoundingConfigurationApi.md#rest_v10_companies_company_id_rounding_configuration_post) | **POST** /rest/v1.0/companies/{company_id}/rounding_configuration | Create rounding configuration


# **rest_v10_companies_company_id_rounding_configuration_delete**
> rest_v10_companies_company_id_rounding_configuration_delete(procore_company_id, company_id)

Delete rounding configuration

Delete rounding configuration

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
    api_instance = procore_sdk.FieldProductivityTimesheetRoundingConfigurationApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.

    try:
        # Delete rounding configuration
        api_instance.rest_v10_companies_company_id_rounding_configuration_delete(procore_company_id, company_id)
    except Exception as e:
        print("Exception when calling FieldProductivityTimesheetRoundingConfigurationApi->rest_v10_companies_company_id_rounding_configuration_delete: %s\n" % e)
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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_rounding_configuration_get**
> RoundingConfiguration rest_v10_companies_company_id_rounding_configuration_get(procore_company_id, company_id)

Show rounding configuration

Show time increments and rounding rules for company timesheets

### Example


```python
import procore_sdk
from procore_sdk.models.rounding_configuration import RoundingConfiguration
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
    api_instance = procore_sdk.FieldProductivityTimesheetRoundingConfigurationApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.

    try:
        # Show rounding configuration
        api_response = api_instance.rest_v10_companies_company_id_rounding_configuration_get(procore_company_id, company_id)
        print("The response of FieldProductivityTimesheetRoundingConfigurationApi->rest_v10_companies_company_id_rounding_configuration_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimesheetRoundingConfigurationApi->rest_v10_companies_company_id_rounding_configuration_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 

### Return type

[**RoundingConfiguration**](RoundingConfiguration.md)

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

# **rest_v10_companies_company_id_rounding_configuration_patch**
> RoundingConfiguration rest_v10_companies_company_id_rounding_configuration_patch(procore_company_id, company_id, rounding_configuration_body)

Update rounding configuration

Update rounding configuration

### Example


```python
import procore_sdk
from procore_sdk.models.rounding_configuration import RoundingConfiguration
from procore_sdk.models.rounding_configuration_body import RoundingConfigurationBody
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
    api_instance = procore_sdk.FieldProductivityTimesheetRoundingConfigurationApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    rounding_configuration_body = procore_sdk.RoundingConfigurationBody() # RoundingConfigurationBody | 

    try:
        # Update rounding configuration
        api_response = api_instance.rest_v10_companies_company_id_rounding_configuration_patch(procore_company_id, company_id, rounding_configuration_body)
        print("The response of FieldProductivityTimesheetRoundingConfigurationApi->rest_v10_companies_company_id_rounding_configuration_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimesheetRoundingConfigurationApi->rest_v10_companies_company_id_rounding_configuration_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **rounding_configuration_body** | [**RoundingConfigurationBody**](RoundingConfigurationBody.md)|  | 

### Return type

[**RoundingConfiguration**](RoundingConfiguration.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_rounding_configuration_post**
> RoundingConfiguration rest_v10_companies_company_id_rounding_configuration_post(procore_company_id, company_id, rounding_configuration_body)

Create rounding configuration

Create rounding configuration

### Example


```python
import procore_sdk
from procore_sdk.models.rounding_configuration import RoundingConfiguration
from procore_sdk.models.rounding_configuration_body import RoundingConfigurationBody
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
    api_instance = procore_sdk.FieldProductivityTimesheetRoundingConfigurationApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    rounding_configuration_body = procore_sdk.RoundingConfigurationBody() # RoundingConfigurationBody | 

    try:
        # Create rounding configuration
        api_response = api_instance.rest_v10_companies_company_id_rounding_configuration_post(procore_company_id, company_id, rounding_configuration_body)
        print("The response of FieldProductivityTimesheetRoundingConfigurationApi->rest_v10_companies_company_id_rounding_configuration_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimesheetRoundingConfigurationApi->rest_v10_companies_company_id_rounding_configuration_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **rounding_configuration_body** | [**RoundingConfigurationBody**](RoundingConfigurationBody.md)|  | 

### Return type

[**RoundingConfiguration**](RoundingConfiguration.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

