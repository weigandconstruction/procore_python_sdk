# procore_sdk.CorePermissionsPermissionsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_settings_permissions_get**](CorePermissionsPermissionsApi.md#rest_v10_settings_permissions_get) | **GET** /rest/v1.0/settings/permissions | Show permission manifest


# **rest_v10_settings_permissions_get**
> RestV10SettingsPermissionsGet200Response rest_v10_settings_permissions_get(procore_company_id, project_id=project_id, company_id=company_id, filter_correspondence_types=filter_correspondence_types)

Show permission manifest

Company or project permission manifest for the current user

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_settings_permissions_get200_response import RestV10SettingsPermissionsGet200Response
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
    api_instance = procore_sdk.CorePermissionsPermissionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | This parameter is required for project level permissions and should be omitted for company level permissions. (optional)
    company_id = 56 # int | This parameter is required for company level permissions and should be omitted for project level permissions. (optional)
    filter_correspondence_types = True # bool | Filter out Correspondence Types from permissions. (optional) (default to True)

    try:
        # Show permission manifest
        api_response = api_instance.rest_v10_settings_permissions_get(procore_company_id, project_id=project_id, company_id=company_id, filter_correspondence_types=filter_correspondence_types)
        print("The response of CorePermissionsPermissionsApi->rest_v10_settings_permissions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CorePermissionsPermissionsApi->rest_v10_settings_permissions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| This parameter is required for project level permissions and should be omitted for company level permissions. | [optional] 
 **company_id** | **int**| This parameter is required for company level permissions and should be omitted for project level permissions. | [optional] 
 **filter_correspondence_types** | **bool**| Filter out Correspondence Types from permissions. | [optional] [default to True]

### Return type

[**RestV10SettingsPermissionsGet200Response**](RestV10SettingsPermissionsGet200Response.md)

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
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

