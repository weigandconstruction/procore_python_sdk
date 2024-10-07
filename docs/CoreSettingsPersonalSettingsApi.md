# procore_sdk.CoreSettingsPersonalSettingsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_settings_my_avatar_get**](CoreSettingsPersonalSettingsApi.md#rest_v10_companies_company_id_settings_my_avatar_get) | **GET** /rest/v1.0/companies/{company_id}/settings/my/avatar | Returns avatar of the current user
[**rest_v10_companies_company_id_settings_my_avatar_put**](CoreSettingsPersonalSettingsApi.md#rest_v10_companies_company_id_settings_my_avatar_put) | **PUT** /rest/v1.0/companies/{company_id}/settings/my/avatar | Bulk create/update UI flags


# **rest_v10_companies_company_id_settings_my_avatar_get**
> RestV10CompaniesCompanyIdSettingsMyAvatarGet200Response rest_v10_companies_company_id_settings_my_avatar_get(procore_company_id, company_id)

Returns avatar of the current user

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_settings_my_avatar_get200_response import RestV10CompaniesCompanyIdSettingsMyAvatarGet200Response
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
    api_instance = procore_sdk.CoreSettingsPersonalSettingsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.

    try:
        # Returns avatar of the current user
        api_response = api_instance.rest_v10_companies_company_id_settings_my_avatar_get(procore_company_id, company_id)
        print("The response of CoreSettingsPersonalSettingsApi->rest_v10_companies_company_id_settings_my_avatar_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreSettingsPersonalSettingsApi->rest_v10_companies_company_id_settings_my_avatar_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 

### Return type

[**RestV10CompaniesCompanyIdSettingsMyAvatarGet200Response**](RestV10CompaniesCompanyIdSettingsMyAvatarGet200Response.md)

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
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_settings_my_avatar_put**
> RestV10CompaniesCompanyIdSettingsMyAvatarPut200Response rest_v10_companies_company_id_settings_my_avatar_put(procore_company_id, company_id, rest_v10_companies_company_id_settings_my_avatar_put_request=rest_v10_companies_company_id_settings_my_avatar_put_request)

Bulk create/update UI flags

Create or update UI flags associated with company, and user

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_settings_my_avatar_put200_response import RestV10CompaniesCompanyIdSettingsMyAvatarPut200Response
from procore_sdk.models.rest_v10_companies_company_id_settings_my_avatar_put_request import RestV10CompaniesCompanyIdSettingsMyAvatarPutRequest
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
    api_instance = procore_sdk.CoreSettingsPersonalSettingsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    rest_v10_companies_company_id_settings_my_avatar_put_request = procore_sdk.RestV10CompaniesCompanyIdSettingsMyAvatarPutRequest() # RestV10CompaniesCompanyIdSettingsMyAvatarPutRequest |  (optional)

    try:
        # Bulk create/update UI flags
        api_response = api_instance.rest_v10_companies_company_id_settings_my_avatar_put(procore_company_id, company_id, rest_v10_companies_company_id_settings_my_avatar_put_request=rest_v10_companies_company_id_settings_my_avatar_put_request)
        print("The response of CoreSettingsPersonalSettingsApi->rest_v10_companies_company_id_settings_my_avatar_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreSettingsPersonalSettingsApi->rest_v10_companies_company_id_settings_my_avatar_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **rest_v10_companies_company_id_settings_my_avatar_put_request** | [**RestV10CompaniesCompanyIdSettingsMyAvatarPutRequest**](RestV10CompaniesCompanyIdSettingsMyAvatarPutRequest.md)|  | [optional] 

### Return type

[**RestV10CompaniesCompanyIdSettingsMyAvatarPut200Response**](RestV10CompaniesCompanyIdSettingsMyAvatarPut200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

