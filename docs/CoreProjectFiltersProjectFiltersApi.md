# procore_sdk.CoreProjectFiltersProjectFiltersApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_filters_get**](CoreProjectFiltersProjectFiltersApi.md#rest_v10_companies_company_id_filters_get) | **GET** /rest/v1.0/companies/{company_id}/filters | List filters
[**rest_v10_companies_company_id_filters_name_get**](CoreProjectFiltersProjectFiltersApi.md#rest_v10_companies_company_id_filters_name_get) | **GET** /rest/v1.0/companies/{company_id}/filters/{name} | Return a filter


# **rest_v10_companies_company_id_filters_get**
> RestV10CompaniesCompanyIdFiltersGet200Response rest_v10_companies_company_id_filters_get(procore_company_id, company_id)

List filters

Return a list of available filters.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_filters_get200_response import RestV10CompaniesCompanyIdFiltersGet200Response
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
    api_instance = procore_sdk.CoreProjectFiltersProjectFiltersApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.

    try:
        # List filters
        api_response = api_instance.rest_v10_companies_company_id_filters_get(procore_company_id, company_id)
        print("The response of CoreProjectFiltersProjectFiltersApi->rest_v10_companies_company_id_filters_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectFiltersProjectFiltersApi->rest_v10_companies_company_id_filters_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 

### Return type

[**RestV10CompaniesCompanyIdFiltersGet200Response**](RestV10CompaniesCompanyIdFiltersGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of filters |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_filters_name_get**
> RestV10CompaniesCompanyIdFiltersGet200Response rest_v10_companies_company_id_filters_name_get(procore_company_id, company_id, name)

Return a filter

Return a filter by a specific name.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_filters_get200_response import RestV10CompaniesCompanyIdFiltersGet200Response
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
    api_instance = procore_sdk.CoreProjectFiltersProjectFiltersApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    name = 'name_example' # str | Filter name.

    try:
        # Return a filter
        api_response = api_instance.rest_v10_companies_company_id_filters_name_get(procore_company_id, company_id, name)
        print("The response of CoreProjectFiltersProjectFiltersApi->rest_v10_companies_company_id_filters_name_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectFiltersProjectFiltersApi->rest_v10_companies_company_id_filters_name_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **name** | **str**| Filter name. | 

### Return type

[**RestV10CompaniesCompanyIdFiltersGet200Response**](RestV10CompaniesCompanyIdFiltersGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of filters |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

