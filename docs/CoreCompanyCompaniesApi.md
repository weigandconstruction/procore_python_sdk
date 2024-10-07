# procore_sdk.CoreCompanyCompaniesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_get**](CoreCompanyCompaniesApi.md#rest_v10_companies_get) | **GET** /rest/v1.0/companies | List Companies


# **rest_v10_companies_get**
> List[Company] rest_v10_companies_get(page=page, per_page=per_page, include_free_companies=include_free_companies)

List Companies

Return a list of Companies visible to the User.  NOTE: This endpoint does not require the ['Procore-Company-Id' header] (https://developers.procore.com/documentation/tutorial-mpz) to be included on a request.

### Example


```python
import procore_sdk
from procore_sdk.models.company import Company
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
    api_instance = procore_sdk.CoreCompanyCompaniesApi(api_client)
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    include_free_companies = True # bool | By default the endpoint excludes free companies. Provide include_free_companies=true to include them (optional)

    try:
        # List Companies
        api_response = api_instance.rest_v10_companies_get(page=page, per_page=per_page, include_free_companies=include_free_companies)
        print("The response of CoreCompanyCompaniesApi->rest_v10_companies_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCompanyCompaniesApi->rest_v10_companies_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **include_free_companies** | **bool**| By default the endpoint excludes free companies. Provide include_free_companies&#x3D;true to include them | [optional] 

### Return type

[**List[Company]**](Company.md)

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

