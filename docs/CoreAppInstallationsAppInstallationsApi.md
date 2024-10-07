# procore_sdk.CoreAppInstallationsAppInstallationsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_app_installations_get**](CoreAppInstallationsAppInstallationsApi.md#rest_v10_app_installations_get) | **GET** /rest/v1.0/app_installations | List app installations
[**rest_v10_app_installations_id_get**](CoreAppInstallationsAppInstallationsApi.md#rest_v10_app_installations_id_get) | **GET** /rest/v1.0/app_installations/{id} | Show app installation
[**rest_v10_app_installations_id_patch**](CoreAppInstallationsAppInstallationsApi.md#rest_v10_app_installations_id_patch) | **PATCH** /rest/v1.0/app_installations/{id} | Update app installation
[**rest_v10_app_installations_post**](CoreAppInstallationsAppInstallationsApi.md#rest_v10_app_installations_post) | **POST** /rest/v1.0/app_installations | Create app installation


# **rest_v10_app_installations_get**
> List[RestV10AppInstallationsGet200ResponseInner] rest_v10_app_installations_get(procore_company_id, company_id, project_id, page=page, per_page=per_page)

List app installations

Returns a list of app installations on a given company or project

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_app_installations_get200_response_inner import RestV10AppInstallationsGet200ResponseInner
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
    api_instance = procore_sdk.CoreAppInstallationsAppInstallationsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company. You must supply either a company_id or project_id.
    project_id = 56 # int | Unique identifier for the project. You must supply either a company_id or project_id.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List app installations
        api_response = api_instance.rest_v10_app_installations_get(procore_company_id, company_id, project_id, page=page, per_page=per_page)
        print("The response of CoreAppInstallationsAppInstallationsApi->rest_v10_app_installations_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreAppInstallationsAppInstallationsApi->rest_v10_app_installations_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. You must supply either a company_id or project_id. | 
 **project_id** | **int**| Unique identifier for the project. You must supply either a company_id or project_id. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[RestV10AppInstallationsGet200ResponseInner]**](RestV10AppInstallationsGet200ResponseInner.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_app_installations_id_get**
> RestV10AppInstallationsPost201Response rest_v10_app_installations_id_get(procore_company_id, id, company_id, project_id)

Show app installation

Get the details of a single app installation

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_app_installations_post201_response import RestV10AppInstallationsPost201Response
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
    api_instance = procore_sdk.CoreAppInstallationsAppInstallationsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | App installation ID
    company_id = 56 # int | Unique identifier for the company. You must supply either a company_id or project_id.
    project_id = 56 # int | Unique identifier for the project. You must supply either a company_id or project_id.

    try:
        # Show app installation
        api_response = api_instance.rest_v10_app_installations_id_get(procore_company_id, id, company_id, project_id)
        print("The response of CoreAppInstallationsAppInstallationsApi->rest_v10_app_installations_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreAppInstallationsAppInstallationsApi->rest_v10_app_installations_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| App installation ID | 
 **company_id** | **int**| Unique identifier for the company. You must supply either a company_id or project_id. | 
 **project_id** | **int**| Unique identifier for the project. You must supply either a company_id or project_id. | 

### Return type

[**RestV10AppInstallationsPost201Response**](RestV10AppInstallationsPost201Response.md)

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_app_installations_id_patch**
> RestV10AppInstallationsGet200ResponseInner rest_v10_app_installations_id_patch(procore_company_id, id, rest_v10_app_installations_id_patch_request)

Update app installation

Update the status of an application between installed or uninstalled

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_app_installations_get200_response_inner import RestV10AppInstallationsGet200ResponseInner
from procore_sdk.models.rest_v10_app_installations_id_patch_request import RestV10AppInstallationsIdPatchRequest
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
    api_instance = procore_sdk.CoreAppInstallationsAppInstallationsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | App installation ID
    rest_v10_app_installations_id_patch_request = procore_sdk.RestV10AppInstallationsIdPatchRequest() # RestV10AppInstallationsIdPatchRequest | 

    try:
        # Update app installation
        api_response = api_instance.rest_v10_app_installations_id_patch(procore_company_id, id, rest_v10_app_installations_id_patch_request)
        print("The response of CoreAppInstallationsAppInstallationsApi->rest_v10_app_installations_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreAppInstallationsAppInstallationsApi->rest_v10_app_installations_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| App installation ID | 
 **rest_v10_app_installations_id_patch_request** | [**RestV10AppInstallationsIdPatchRequest**](RestV10AppInstallationsIdPatchRequest.md)|  | 

### Return type

[**RestV10AppInstallationsGet200ResponseInner**](RestV10AppInstallationsGet200ResponseInner.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_app_installations_post**
> RestV10AppInstallationsPost201Response rest_v10_app_installations_post(procore_company_id, body146)

Create app installation

Install a new application

### Example


```python
import procore_sdk
from procore_sdk.models.body146 import Body146
from procore_sdk.models.rest_v10_app_installations_post201_response import RestV10AppInstallationsPost201Response
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
    api_instance = procore_sdk.CoreAppInstallationsAppInstallationsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    body146 = procore_sdk.Body146() # Body146 | 

    try:
        # Create app installation
        api_response = api_instance.rest_v10_app_installations_post(procore_company_id, body146)
        print("The response of CoreAppInstallationsAppInstallationsApi->rest_v10_app_installations_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreAppInstallationsAppInstallationsApi->rest_v10_app_installations_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **body146** | [**Body146**](Body146.md)|  | 

### Return type

[**RestV10AppInstallationsPost201Response**](RestV10AppInstallationsPost201Response.md)

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

