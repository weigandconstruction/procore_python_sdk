# procore_sdk.CoreCompanyCompanyConfigurationsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_company_configuration_get**](CoreCompanyCompanyConfigurationsApi.md#rest_v10_company_configuration_get) | **GET** /rest/v1.0/company_configuration | Show Company Configuration


# **rest_v10_company_configuration_get**
> RestV10CompanyConfigurationGet200Response rest_v10_company_configuration_get(procore_company_id, company_id)

Show Company Configuration

Returns company configuration.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_company_configuration_get200_response import RestV10CompanyConfigurationGet200Response
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
    api_instance = procore_sdk.CoreCompanyCompanyConfigurationsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.

    try:
        # Show Company Configuration
        api_response = api_instance.rest_v10_company_configuration_get(procore_company_id, company_id)
        print("The response of CoreCompanyCompanyConfigurationsApi->rest_v10_company_configuration_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCompanyCompanyConfigurationsApi->rest_v10_company_configuration_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 

### Return type

[**RestV10CompanyConfigurationGet200Response**](RestV10CompanyConfigurationGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

