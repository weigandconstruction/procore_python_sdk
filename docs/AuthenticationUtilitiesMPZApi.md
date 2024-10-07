# procore_sdk.AuthenticationUtilitiesMPZApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_company_base_url_get**](AuthenticationUtilitiesMPZApi.md#rest_v10_company_base_url_get) | **GET** /rest/v1.0/company_base_url | Check Company Zone


# **rest_v10_company_base_url_get**
> RestV10CompanyBaseUrlGet200Response rest_v10_company_base_url_get(procore_company_id)

Check Company Zone

Get a response indicating zone routing and web url for zone

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_company_base_url_get200_response import RestV10CompanyBaseUrlGet200Response
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
    api_instance = procore_sdk.AuthenticationUtilitiesMPZApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.

    try:
        # Check Company Zone
        api_response = api_instance.rest_v10_company_base_url_get(procore_company_id)
        print("The response of AuthenticationUtilitiesMPZApi->rest_v10_company_base_url_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationUtilitiesMPZApi->rest_v10_company_base_url_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 

### Return type

[**RestV10CompanyBaseUrlGet200Response**](RestV10CompanyBaseUrlGet200Response.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

