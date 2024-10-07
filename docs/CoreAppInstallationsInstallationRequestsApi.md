# procore_sdk.CoreAppInstallationsInstallationRequestsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_installation_requests_get**](CoreAppInstallationsInstallationRequestsApi.md#rest_v10_installation_requests_get) | **GET** /rest/v1.0/installation_requests | List app installations
[**rest_v10_installation_requests_post**](CoreAppInstallationsInstallationRequestsApi.md#rest_v10_installation_requests_post) | **POST** /rest/v1.0/installation_requests | Create installation request


# **rest_v10_installation_requests_get**
> List[RestV10InstallationRequestsGet200ResponseInner] rest_v10_installation_requests_get(procore_company_id, company_id, developer_app_id, implicit)

List app installations

Returns a list of app installation requests on a given company

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_installation_requests_get200_response_inner import RestV10InstallationRequestsGet200ResponseInner
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
    api_instance = procore_sdk.CoreAppInstallationsInstallationRequestsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    developer_app_id = 'developer_app_id_example' # str | Developer App ID
    implicit = True # bool | False if the request was made via API, true if it was made on attempting to authenticate an app 

    try:
        # List app installations
        api_response = api_instance.rest_v10_installation_requests_get(procore_company_id, company_id, developer_app_id, implicit)
        print("The response of CoreAppInstallationsInstallationRequestsApi->rest_v10_installation_requests_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreAppInstallationsInstallationRequestsApi->rest_v10_installation_requests_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **developer_app_id** | **str**| Developer App ID | 
 **implicit** | **bool**| False if the request was made via API, true if it was made on attempting to authenticate an app  | 

### Return type

[**List[RestV10InstallationRequestsGet200ResponseInner]**](RestV10InstallationRequestsGet200ResponseInner.md)

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

# **rest_v10_installation_requests_post**
> RestV10InstallationRequestsGet200ResponseInner rest_v10_installation_requests_post(procore_company_id, body77)

Create installation request

Request to install a new application

### Example


```python
import procore_sdk
from procore_sdk.models.body77 import Body77
from procore_sdk.models.rest_v10_installation_requests_get200_response_inner import RestV10InstallationRequestsGet200ResponseInner
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
    api_instance = procore_sdk.CoreAppInstallationsInstallationRequestsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    body77 = procore_sdk.Body77() # Body77 | 

    try:
        # Create installation request
        api_response = api_instance.rest_v10_installation_requests_post(procore_company_id, body77)
        print("The response of CoreAppInstallationsInstallationRequestsApi->rest_v10_installation_requests_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreAppInstallationsInstallationRequestsApi->rest_v10_installation_requests_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **body77** | [**Body77**](Body77.md)|  | 

### Return type

[**RestV10InstallationRequestsGet200ResponseInner**](RestV10InstallationRequestsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

