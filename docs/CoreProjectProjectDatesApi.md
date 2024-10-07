# procore_sdk.CoreProjectProjectDatesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_project_dates_get**](CoreProjectProjectDatesApi.md#rest_v10_project_dates_get) | **GET** /rest/v1.0/project_dates | List Project Dates
[**rest_v10_project_dates_id_get**](CoreProjectProjectDatesApi.md#rest_v10_project_dates_id_get) | **GET** /rest/v1.0/project_dates/{id} | Show Project Date
[**rest_v10_projects_project_id_project_dates_get**](CoreProjectProjectDatesApi.md#rest_v10_projects_project_id_project_dates_get) | **GET** /rest/v1.0/projects/{project_id}/project_dates | List Project Dates
[**rest_v10_projects_project_id_project_dates_id_get**](CoreProjectProjectDatesApi.md#rest_v10_projects_project_id_project_dates_id_get) | **GET** /rest/v1.0/projects/{project_id}/project_dates/{id} | Show Project Date
[**rest_v10_projects_project_id_project_dates_post**](CoreProjectProjectDatesApi.md#rest_v10_projects_project_id_project_dates_post) | **POST** /rest/v1.0/projects/{project_id}/project_dates | Creates or updates project date
[**rest_v20_companies_company_id_projects_project_id_project_dates_get**](CoreProjectProjectDatesApi.md#rest_v20_companies_company_id_projects_project_id_project_dates_get) | **GET** /rest/v2.0/companies/{company_id}/projects/{project_id}/project_dates | List project dates


# **rest_v10_project_dates_get**
> RestV10ProjectsProjectIdProjectDatesGet200Response rest_v10_project_dates_get(procore_company_id, project_id, page=page, per_page=per_page)

List Project Dates

Returns a list of Project Dates.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_project_dates_get200_response import RestV10ProjectsProjectIdProjectDatesGet200Response
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
    api_instance = procore_sdk.CoreProjectProjectDatesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Project Dates
        api_response = api_instance.rest_v10_project_dates_get(procore_company_id, project_id, page=page, per_page=per_page)
        print("The response of CoreProjectProjectDatesApi->rest_v10_project_dates_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectProjectDatesApi->rest_v10_project_dates_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**RestV10ProjectsProjectIdProjectDatesGet200Response**](RestV10ProjectsProjectIdProjectDatesGet200Response.md)

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

# **rest_v10_project_dates_id_get**
> RestV10ProjectsProjectIdProjectDatesIdGet200Response rest_v10_project_dates_id_get(procore_company_id, id, project_id)

Show Project Date

Show details of the specified Project Date

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_project_dates_id_get200_response import RestV10ProjectsProjectIdProjectDatesIdGet200Response
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
    api_instance = procore_sdk.CoreProjectProjectDatesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the Project Date
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Show Project Date
        api_response = api_instance.rest_v10_project_dates_id_get(procore_company_id, id, project_id)
        print("The response of CoreProjectProjectDatesApi->rest_v10_project_dates_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectProjectDatesApi->rest_v10_project_dates_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the Project Date | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**RestV10ProjectsProjectIdProjectDatesIdGet200Response**](RestV10ProjectsProjectIdProjectDatesIdGet200Response.md)

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

# **rest_v10_projects_project_id_project_dates_get**
> RestV10ProjectsProjectIdProjectDatesGet200Response rest_v10_projects_project_id_project_dates_get(procore_company_id, project_id, page=page, per_page=per_page)

List Project Dates

Returns a list of Project Dates.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_project_dates_get200_response import RestV10ProjectsProjectIdProjectDatesGet200Response
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
    api_instance = procore_sdk.CoreProjectProjectDatesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Project Dates
        api_response = api_instance.rest_v10_projects_project_id_project_dates_get(procore_company_id, project_id, page=page, per_page=per_page)
        print("The response of CoreProjectProjectDatesApi->rest_v10_projects_project_id_project_dates_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectProjectDatesApi->rest_v10_projects_project_id_project_dates_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**RestV10ProjectsProjectIdProjectDatesGet200Response**](RestV10ProjectsProjectIdProjectDatesGet200Response.md)

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

# **rest_v10_projects_project_id_project_dates_id_get**
> RestV10ProjectsProjectIdProjectDatesIdGet200Response rest_v10_projects_project_id_project_dates_id_get(procore_company_id, id, project_id)

Show Project Date

Show details of the specified Project Date

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_project_dates_id_get200_response import RestV10ProjectsProjectIdProjectDatesIdGet200Response
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
    api_instance = procore_sdk.CoreProjectProjectDatesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the Project Date
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Show Project Date
        api_response = api_instance.rest_v10_projects_project_id_project_dates_id_get(procore_company_id, id, project_id)
        print("The response of CoreProjectProjectDatesApi->rest_v10_projects_project_id_project_dates_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectProjectDatesApi->rest_v10_projects_project_id_project_dates_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the Project Date | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**RestV10ProjectsProjectIdProjectDatesIdGet200Response**](RestV10ProjectsProjectIdProjectDatesIdGet200Response.md)

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

# **rest_v10_projects_project_id_project_dates_post**
> rest_v10_projects_project_id_project_dates_post(procore_company_id, project_id, rest_v10_projects_project_id_project_dates_post_request=rest_v10_projects_project_id_project_dates_post_request)

Creates or updates project date

Associates a project with a given project date or updates the date

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_project_dates_post_request import RestV10ProjectsProjectIdProjectDatesPostRequest
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
    api_instance = procore_sdk.CoreProjectProjectDatesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_projects_project_id_project_dates_post_request = procore_sdk.RestV10ProjectsProjectIdProjectDatesPostRequest() # RestV10ProjectsProjectIdProjectDatesPostRequest |  (optional)

    try:
        # Creates or updates project date
        api_instance.rest_v10_projects_project_id_project_dates_post(procore_company_id, project_id, rest_v10_projects_project_id_project_dates_post_request=rest_v10_projects_project_id_project_dates_post_request)
    except Exception as e:
        print("Exception when calling CoreProjectProjectDatesApi->rest_v10_projects_project_id_project_dates_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_projects_project_id_project_dates_post_request** | [**RestV10ProjectsProjectIdProjectDatesPostRequest**](RestV10ProjectsProjectIdProjectDatesPostRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v20_companies_company_id_projects_project_id_project_dates_get**
> RestV20CompaniesCompanyIdProjectsProjectIdProjectDatesGet200Response rest_v20_companies_company_id_projects_project_id_project_dates_get(procore_company_id, company_id, project_id, per_page=per_page)

List project dates

List project dates associated with a project

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v20_companies_company_id_projects_project_id_project_dates_get200_response import RestV20CompaniesCompanyIdProjectsProjectIdProjectDatesGet200Response
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
    api_instance = procore_sdk.CoreProjectProjectDatesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 'company_id_example' # str | Unique identifier for the company.
    project_id = 'project_id_example' # str | Unique identifier for the project.
    per_page = 10 # int | Elements per page (optional) (default to 10)

    try:
        # List project dates
        api_response = api_instance.rest_v20_companies_company_id_projects_project_id_project_dates_get(procore_company_id, company_id, project_id, per_page=per_page)
        print("The response of CoreProjectProjectDatesApi->rest_v20_companies_company_id_projects_project_id_project_dates_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectProjectDatesApi->rest_v20_companies_company_id_projects_project_id_project_dates_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **str**| Unique identifier for the company. | 
 **project_id** | **str**| Unique identifier for the project. | 
 **per_page** | **int**| Elements per page | [optional] [default to 10]

### Return type

[**RestV20CompaniesCompanyIdProjectsProjectIdProjectDatesGet200Response**](RestV20CompaniesCompanyIdProjectsProjectIdProjectDatesGet200Response.md)

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

