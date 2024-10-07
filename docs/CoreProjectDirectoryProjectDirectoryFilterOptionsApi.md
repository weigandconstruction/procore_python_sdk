# procore_sdk.CoreProjectDirectoryProjectDirectoryFilterOptionsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_directory_filter_options_country_codes_get**](CoreProjectDirectoryProjectDirectoryFilterOptionsApi.md#rest_v10_projects_project_id_directory_filter_options_country_codes_get) | **GET** /rest/v1.0/projects/{project_id}/directory/filter_options/country_codes | List Project Country Codes
[**rest_v10_projects_project_id_directory_filter_options_job_titles_get**](CoreProjectDirectoryProjectDirectoryFilterOptionsApi.md#rest_v10_projects_project_id_directory_filter_options_job_titles_get) | **GET** /rest/v1.0/projects/{project_id}/directory/filter_options/job_titles | List Project Job Titles
[**rest_v10_projects_project_id_directory_filter_options_permission_templates_get**](CoreProjectDirectoryProjectDirectoryFilterOptionsApi.md#rest_v10_projects_project_id_directory_filter_options_permission_templates_get) | **GET** /rest/v1.0/projects/{project_id}/directory/filter_options/permission_templates | List Project Permission Templates
[**rest_v10_projects_project_id_directory_filter_options_state_codes_get**](CoreProjectDirectoryProjectDirectoryFilterOptionsApi.md#rest_v10_projects_project_id_directory_filter_options_state_codes_get) | **GET** /rest/v1.0/projects/{project_id}/directory/filter_options/state_codes | List Project State Codes
[**rest_v10_projects_project_id_directory_filter_options_trades_get**](CoreProjectDirectoryProjectDirectoryFilterOptionsApi.md#rest_v10_projects_project_id_directory_filter_options_trades_get) | **GET** /rest/v1.0/projects/{project_id}/directory/filter_options/trades | List Project Trades


# **rest_v10_projects_project_id_directory_filter_options_country_codes_get**
> List[RestV10ProjectsProjectIdDirectoryFilterOptionsCountryCodesGet200ResponseInner] rest_v10_projects_project_id_directory_filter_options_country_codes_get(procore_company_id, project_id)

List Project Country Codes

Return a distinct list of country codes for a project

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_directory_filter_options_country_codes_get200_response_inner import RestV10ProjectsProjectIdDirectoryFilterOptionsCountryCodesGet200ResponseInner
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
    api_instance = procore_sdk.CoreProjectDirectoryProjectDirectoryFilterOptionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.

    try:
        # List Project Country Codes
        api_response = api_instance.rest_v10_projects_project_id_directory_filter_options_country_codes_get(procore_company_id, project_id)
        print("The response of CoreProjectDirectoryProjectDirectoryFilterOptionsApi->rest_v10_projects_project_id_directory_filter_options_country_codes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectDirectoryProjectDirectoryFilterOptionsApi->rest_v10_projects_project_id_directory_filter_options_country_codes_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**List[RestV10ProjectsProjectIdDirectoryFilterOptionsCountryCodesGet200ResponseInner]**](RestV10ProjectsProjectIdDirectoryFilterOptionsCountryCodesGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_directory_filter_options_job_titles_get**
> List[RestV10ProjectsProjectIdDirectoryFilterOptionsJobTitlesGet200ResponseInner] rest_v10_projects_project_id_directory_filter_options_job_titles_get(procore_company_id, project_id)

List Project Job Titles

Return a distinct list of job titles for all contacts on a project

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_directory_filter_options_job_titles_get200_response_inner import RestV10ProjectsProjectIdDirectoryFilterOptionsJobTitlesGet200ResponseInner
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
    api_instance = procore_sdk.CoreProjectDirectoryProjectDirectoryFilterOptionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.

    try:
        # List Project Job Titles
        api_response = api_instance.rest_v10_projects_project_id_directory_filter_options_job_titles_get(procore_company_id, project_id)
        print("The response of CoreProjectDirectoryProjectDirectoryFilterOptionsApi->rest_v10_projects_project_id_directory_filter_options_job_titles_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectDirectoryProjectDirectoryFilterOptionsApi->rest_v10_projects_project_id_directory_filter_options_job_titles_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**List[RestV10ProjectsProjectIdDirectoryFilterOptionsJobTitlesGet200ResponseInner]**](RestV10ProjectsProjectIdDirectoryFilterOptionsJobTitlesGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_directory_filter_options_permission_templates_get**
> List[RestV10ProjectsProjectIdDirectoryFilterOptionsPermissionTemplatesGet200ResponseInner] rest_v10_projects_project_id_directory_filter_options_permission_templates_get(procore_company_id, project_id)

List Project Permission Templates

Return a distinct list of permission templates in use on a project

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_directory_filter_options_permission_templates_get200_response_inner import RestV10ProjectsProjectIdDirectoryFilterOptionsPermissionTemplatesGet200ResponseInner
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
    api_instance = procore_sdk.CoreProjectDirectoryProjectDirectoryFilterOptionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.

    try:
        # List Project Permission Templates
        api_response = api_instance.rest_v10_projects_project_id_directory_filter_options_permission_templates_get(procore_company_id, project_id)
        print("The response of CoreProjectDirectoryProjectDirectoryFilterOptionsApi->rest_v10_projects_project_id_directory_filter_options_permission_templates_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectDirectoryProjectDirectoryFilterOptionsApi->rest_v10_projects_project_id_directory_filter_options_permission_templates_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**List[RestV10ProjectsProjectIdDirectoryFilterOptionsPermissionTemplatesGet200ResponseInner]**](RestV10ProjectsProjectIdDirectoryFilterOptionsPermissionTemplatesGet200ResponseInner.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_directory_filter_options_state_codes_get**
> List[RestV10ProjectsProjectIdDirectoryFilterOptionsStateCodesGet200ResponseInner] rest_v10_projects_project_id_directory_filter_options_state_codes_get(procore_company_id, project_id, country_code)

List Project State Codes

Return the list of states for a country

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_directory_filter_options_state_codes_get200_response_inner import RestV10ProjectsProjectIdDirectoryFilterOptionsStateCodesGet200ResponseInner
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
    api_instance = procore_sdk.CoreProjectDirectoryProjectDirectoryFilterOptionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    country_code = 'country_code_example' # str | Code that identifies a country

    try:
        # List Project State Codes
        api_response = api_instance.rest_v10_projects_project_id_directory_filter_options_state_codes_get(procore_company_id, project_id, country_code)
        print("The response of CoreProjectDirectoryProjectDirectoryFilterOptionsApi->rest_v10_projects_project_id_directory_filter_options_state_codes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectDirectoryProjectDirectoryFilterOptionsApi->rest_v10_projects_project_id_directory_filter_options_state_codes_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **country_code** | **str**| Code that identifies a country | 

### Return type

[**List[RestV10ProjectsProjectIdDirectoryFilterOptionsStateCodesGet200ResponseInner]**](RestV10ProjectsProjectIdDirectoryFilterOptionsStateCodesGet200ResponseInner.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_directory_filter_options_trades_get**
> List[RestV10ProjectsProjectIdDirectoryFilterOptionsTradesGet200ResponseInner] rest_v10_projects_project_id_directory_filter_options_trades_get(procore_company_id, project_id)

List Project Trades

Return a distinct list of trades in use on vendors for a given project

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_directory_filter_options_trades_get200_response_inner import RestV10ProjectsProjectIdDirectoryFilterOptionsTradesGet200ResponseInner
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
    api_instance = procore_sdk.CoreProjectDirectoryProjectDirectoryFilterOptionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.

    try:
        # List Project Trades
        api_response = api_instance.rest_v10_projects_project_id_directory_filter_options_trades_get(procore_company_id, project_id)
        print("The response of CoreProjectDirectoryProjectDirectoryFilterOptionsApi->rest_v10_projects_project_id_directory_filter_options_trades_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectDirectoryProjectDirectoryFilterOptionsApi->rest_v10_projects_project_id_directory_filter_options_trades_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**List[RestV10ProjectsProjectIdDirectoryFilterOptionsTradesGet200ResponseInner]**](RestV10ProjectsProjectIdDirectoryFilterOptionsTradesGet200ResponseInner.md)

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

