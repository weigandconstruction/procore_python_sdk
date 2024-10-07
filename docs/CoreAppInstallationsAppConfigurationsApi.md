# procore_sdk.CoreAppInstallationsAppConfigurationsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_app_configurations_get**](CoreAppInstallationsAppConfigurationsApi.md#rest_v10_companies_company_id_app_configurations_get) | **GET** /rest/v1.0/companies/{company_id}/app_configurations | List app configurations
[**rest_v10_companies_company_id_app_configurations_id_delete**](CoreAppInstallationsAppConfigurationsApi.md#rest_v10_companies_company_id_app_configurations_id_delete) | **DELETE** /rest/v1.0/companies/{company_id}/app_configurations/{id} | Delete app configuration
[**rest_v10_companies_company_id_app_configurations_id_get**](CoreAppInstallationsAppConfigurationsApi.md#rest_v10_companies_company_id_app_configurations_id_get) | **GET** /rest/v1.0/companies/{company_id}/app_configurations/{id} | Show app configuration
[**rest_v10_companies_company_id_app_configurations_id_patch**](CoreAppInstallationsAppConfigurationsApi.md#rest_v10_companies_company_id_app_configurations_id_patch) | **PATCH** /rest/v1.0/companies/{company_id}/app_configurations/{id} | Update app configuration
[**rest_v10_companies_company_id_app_configurations_post**](CoreAppInstallationsAppConfigurationsApi.md#rest_v10_companies_company_id_app_configurations_post) | **POST** /rest/v1.0/companies/{company_id}/app_configurations | Create app configuration


# **rest_v10_companies_company_id_app_configurations_get**
> List[RestV10CompaniesCompanyIdAppConfigurationsGet200ResponseInner] rest_v10_companies_company_id_app_configurations_get(procore_company_id, company_id, sort=sort, page=page, per_page=per_page, filters_app_installation_id=filters_app_installation_id, filters_project_id=filters_project_id)

List app configurations

Returns a list of app configurations on a given company or project

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_app_configurations_get200_response_inner import RestV10CompaniesCompanyIdAppConfigurationsGet200ResponseInner
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
    api_instance = procore_sdk.CoreAppInstallationsAppConfigurationsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    sort = 'sort_example' # str | Direction (asc/desc) can be controlled by the presence or absence of '-' before the sort parameter. (optional)
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_app_installation_id = 56 # int | App installation ID (optional)
    filters_project_id = 56 # int | Project ID (optional)

    try:
        # List app configurations
        api_response = api_instance.rest_v10_companies_company_id_app_configurations_get(procore_company_id, company_id, sort=sort, page=page, per_page=per_page, filters_app_installation_id=filters_app_installation_id, filters_project_id=filters_project_id)
        print("The response of CoreAppInstallationsAppConfigurationsApi->rest_v10_companies_company_id_app_configurations_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreAppInstallationsAppConfigurationsApi->rest_v10_companies_company_id_app_configurations_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **sort** | **str**| Direction (asc/desc) can be controlled by the presence or absence of &#39;-&#39; before the sort parameter. | [optional] 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_app_installation_id** | **int**| App installation ID | [optional] 
 **filters_project_id** | **int**| Project ID | [optional] 

### Return type

[**List[RestV10CompaniesCompanyIdAppConfigurationsGet200ResponseInner]**](RestV10CompaniesCompanyIdAppConfigurationsGet200ResponseInner.md)

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

# **rest_v10_companies_company_id_app_configurations_id_delete**
> rest_v10_companies_company_id_app_configurations_id_delete(procore_company_id, id, company_id)

Delete app configuration

Deletes an app configuration

### Example


```python
import procore_sdk
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
    api_instance = procore_sdk.CoreAppInstallationsAppConfigurationsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | App Configuration ID
    company_id = 56 # int | Unique identifier for the company.

    try:
        # Delete app configuration
        api_instance.rest_v10_companies_company_id_app_configurations_id_delete(procore_company_id, id, company_id)
    except Exception as e:
        print("Exception when calling CoreAppInstallationsAppConfigurationsApi->rest_v10_companies_company_id_app_configurations_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| App Configuration ID | 
 **company_id** | **int**| Unique identifier for the company. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_app_configurations_id_get**
> RestV10CompaniesCompanyIdAppConfigurationsGet200ResponseInner rest_v10_companies_company_id_app_configurations_id_get(procore_company_id, id, company_id)

Show app configuration

Get the details of a single app configuration

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_app_configurations_get200_response_inner import RestV10CompaniesCompanyIdAppConfigurationsGet200ResponseInner
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
    api_instance = procore_sdk.CoreAppInstallationsAppConfigurationsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | App Configuration ID
    company_id = 56 # int | Unique identifier for the company.

    try:
        # Show app configuration
        api_response = api_instance.rest_v10_companies_company_id_app_configurations_id_get(procore_company_id, id, company_id)
        print("The response of CoreAppInstallationsAppConfigurationsApi->rest_v10_companies_company_id_app_configurations_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreAppInstallationsAppConfigurationsApi->rest_v10_companies_company_id_app_configurations_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| App Configuration ID | 
 **company_id** | **int**| Unique identifier for the company. | 

### Return type

[**RestV10CompaniesCompanyIdAppConfigurationsGet200ResponseInner**](RestV10CompaniesCompanyIdAppConfigurationsGet200ResponseInner.md)

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

# **rest_v10_companies_company_id_app_configurations_id_patch**
> RestV10CompaniesCompanyIdAppConfigurationsGet200ResponseInner rest_v10_companies_company_id_app_configurations_id_patch(procore_company_id, id, company_id, rest_v10_companies_company_id_app_configurations_id_patch_request)

Update app configuration

Change the configuration of an existing app configuration

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_app_configurations_get200_response_inner import RestV10CompaniesCompanyIdAppConfigurationsGet200ResponseInner
from procore_sdk.models.rest_v10_companies_company_id_app_configurations_id_patch_request import RestV10CompaniesCompanyIdAppConfigurationsIdPatchRequest
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
    api_instance = procore_sdk.CoreAppInstallationsAppConfigurationsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | App Configuration ID
    company_id = 56 # int | Unique identifier for the company.
    rest_v10_companies_company_id_app_configurations_id_patch_request = procore_sdk.RestV10CompaniesCompanyIdAppConfigurationsIdPatchRequest() # RestV10CompaniesCompanyIdAppConfigurationsIdPatchRequest | 

    try:
        # Update app configuration
        api_response = api_instance.rest_v10_companies_company_id_app_configurations_id_patch(procore_company_id, id, company_id, rest_v10_companies_company_id_app_configurations_id_patch_request)
        print("The response of CoreAppInstallationsAppConfigurationsApi->rest_v10_companies_company_id_app_configurations_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreAppInstallationsAppConfigurationsApi->rest_v10_companies_company_id_app_configurations_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| App Configuration ID | 
 **company_id** | **int**| Unique identifier for the company. | 
 **rest_v10_companies_company_id_app_configurations_id_patch_request** | [**RestV10CompaniesCompanyIdAppConfigurationsIdPatchRequest**](RestV10CompaniesCompanyIdAppConfigurationsIdPatchRequest.md)|  | 

### Return type

[**RestV10CompaniesCompanyIdAppConfigurationsGet200ResponseInner**](RestV10CompaniesCompanyIdAppConfigurationsGet200ResponseInner.md)

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

# **rest_v10_companies_company_id_app_configurations_post**
> RestV10CompaniesCompanyIdAppConfigurationsGet200ResponseInner rest_v10_companies_company_id_app_configurations_post(procore_company_id, company_id, rest_v10_companies_company_id_app_configurations_post_request, sort=sort)

Create app configuration

Create new app configuration for a specified project

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_app_configurations_get200_response_inner import RestV10CompaniesCompanyIdAppConfigurationsGet200ResponseInner
from procore_sdk.models.rest_v10_companies_company_id_app_configurations_post_request import RestV10CompaniesCompanyIdAppConfigurationsPostRequest
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
    api_instance = procore_sdk.CoreAppInstallationsAppConfigurationsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    rest_v10_companies_company_id_app_configurations_post_request = procore_sdk.RestV10CompaniesCompanyIdAppConfigurationsPostRequest() # RestV10CompaniesCompanyIdAppConfigurationsPostRequest | 
    sort = 'sort_example' # str | Direction (asc/desc) can be controlled by the presence or absence of '-' before the sort parameter. (optional)

    try:
        # Create app configuration
        api_response = api_instance.rest_v10_companies_company_id_app_configurations_post(procore_company_id, company_id, rest_v10_companies_company_id_app_configurations_post_request, sort=sort)
        print("The response of CoreAppInstallationsAppConfigurationsApi->rest_v10_companies_company_id_app_configurations_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreAppInstallationsAppConfigurationsApi->rest_v10_companies_company_id_app_configurations_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **rest_v10_companies_company_id_app_configurations_post_request** | [**RestV10CompaniesCompanyIdAppConfigurationsPostRequest**](RestV10CompaniesCompanyIdAppConfigurationsPostRequest.md)|  | 
 **sort** | **str**| Direction (asc/desc) can be controlled by the presence or absence of &#39;-&#39; before the sort parameter. | [optional] 

### Return type

[**RestV10CompaniesCompanyIdAppConfigurationsGet200ResponseInner**](RestV10CompaniesCompanyIdAppConfigurationsGet200ResponseInner.md)

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
**422** | Unprocessible Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

