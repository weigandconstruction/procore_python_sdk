# procore_sdk.AuthenticationUtilitiesMeApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_me_get**](AuthenticationUtilitiesMeApi.md#rest_v10_me_get) | **GET** /rest/v1.0/me | Show User Info


# **rest_v10_me_get**
> RestV10MeGet200Response rest_v10_me_get(company_id=company_id, project_id=project_id)

Show User Info

Returns information on the authenticated user. If a company_id or project_id parameter is included, directory-specific information  on the user will also be returned. Returns a globally unique user id  (across companies). NOTE: This endpoint does not require the ['Procore-Company-Id' header] (https://developers.procore.com/documentation/tutorial-mpz) to be included on a request unless a company_id or project_id parameter  is also included.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_me_get200_response import RestV10MeGet200Response
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
    api_instance = procore_sdk.AuthenticationUtilitiesMeApi(api_client)
    company_id = 56 # int | Unique identifier for the company. You must supply either a company_id or project_id in order for a name to be returned. (optional)
    project_id = 56 # int | Unique identifier for the project. You must supply either a company_id or project_id in order for a name to be returned. (optional)

    try:
        # Show User Info
        api_response = api_instance.rest_v10_me_get(company_id=company_id, project_id=project_id)
        print("The response of AuthenticationUtilitiesMeApi->rest_v10_me_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationUtilitiesMeApi->rest_v10_me_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| Unique identifier for the company. You must supply either a company_id or project_id in order for a name to be returned. | [optional] 
 **project_id** | **int**| Unique identifier for the project. You must supply either a company_id or project_id in order for a name to be returned. | [optional] 

### Return type

[**RestV10MeGet200Response**](RestV10MeGet200Response.md)

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

