# procore_sdk.CoreCompanyCompanySettingsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_settings_logo_delete**](CoreCompanyCompanySettingsApi.md#rest_v10_companies_company_id_settings_logo_delete) | **DELETE** /rest/v1.0/companies/{company_id}/settings/logo | Delete company logo
[**rest_v10_companies_company_id_settings_logo_put**](CoreCompanyCompanySettingsApi.md#rest_v10_companies_company_id_settings_logo_put) | **PUT** /rest/v1.0/companies/{company_id}/settings/logo | Update company&#39;s logo


# **rest_v10_companies_company_id_settings_logo_delete**
> List[RestV10CompaniesCompanyIdSettingsLogoPut200ResponseInner] rest_v10_companies_company_id_settings_logo_delete(procore_company_id, company_id)

Delete company logo

Delete company logo

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_settings_logo_put200_response_inner import RestV10CompaniesCompanyIdSettingsLogoPut200ResponseInner
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
    api_instance = procore_sdk.CoreCompanyCompanySettingsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.

    try:
        # Delete company logo
        api_response = api_instance.rest_v10_companies_company_id_settings_logo_delete(procore_company_id, company_id)
        print("The response of CoreCompanyCompanySettingsApi->rest_v10_companies_company_id_settings_logo_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCompanyCompanySettingsApi->rest_v10_companies_company_id_settings_logo_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 

### Return type

[**List[RestV10CompaniesCompanyIdSettingsLogoPut200ResponseInner]**](RestV10CompaniesCompanyIdSettingsLogoPut200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Deleted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Server Error |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_settings_logo_put**
> List[RestV10CompaniesCompanyIdSettingsLogoPut200ResponseInner] rest_v10_companies_company_id_settings_logo_put(procore_company_id, company_id, type=type, rest_v10_companies_company_id_settings_my_avatar_put_request=rest_v10_companies_company_id_settings_my_avatar_put_request)

Update company's logo

Upload and set company logo

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_settings_logo_put200_response_inner import RestV10CompaniesCompanyIdSettingsLogoPut200ResponseInner
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
    api_instance = procore_sdk.CoreCompanyCompanySettingsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    type = 'type_example' # str | Type of requesting entity (optional)
    rest_v10_companies_company_id_settings_my_avatar_put_request = procore_sdk.RestV10CompaniesCompanyIdSettingsMyAvatarPutRequest() # RestV10CompaniesCompanyIdSettingsMyAvatarPutRequest |  (optional)

    try:
        # Update company's logo
        api_response = api_instance.rest_v10_companies_company_id_settings_logo_put(procore_company_id, company_id, type=type, rest_v10_companies_company_id_settings_my_avatar_put_request=rest_v10_companies_company_id_settings_my_avatar_put_request)
        print("The response of CoreCompanyCompanySettingsApi->rest_v10_companies_company_id_settings_logo_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCompanyCompanySettingsApi->rest_v10_companies_company_id_settings_logo_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **type** | **str**| Type of requesting entity | [optional] 
 **rest_v10_companies_company_id_settings_my_avatar_put_request** | [**RestV10CompaniesCompanyIdSettingsMyAvatarPutRequest**](RestV10CompaniesCompanyIdSettingsMyAvatarPutRequest.md)|  | [optional] 

### Return type

[**List[RestV10CompaniesCompanyIdSettingsLogoPut200ResponseInner]**](RestV10CompaniesCompanyIdSettingsLogoPut200ResponseInner.md)

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

