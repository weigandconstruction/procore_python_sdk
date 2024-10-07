# procore_sdk.CoreCompanyProjectTypesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_project_types_get**](CoreCompanyProjectTypesApi.md#rest_v10_companies_company_id_project_types_get) | **GET** /rest/v1.0/companies/{company_id}/project_types | List project types
[**rest_v10_companies_company_id_project_types_id_delete**](CoreCompanyProjectTypesApi.md#rest_v10_companies_company_id_project_types_id_delete) | **DELETE** /rest/v1.0/companies/{company_id}/project_types/{id} | Delete project type
[**rest_v10_companies_company_id_project_types_id_get**](CoreCompanyProjectTypesApi.md#rest_v10_companies_company_id_project_types_id_get) | **GET** /rest/v1.0/companies/{company_id}/project_types/{id} | Show project type
[**rest_v10_companies_company_id_project_types_id_patch**](CoreCompanyProjectTypesApi.md#rest_v10_companies_company_id_project_types_id_patch) | **PATCH** /rest/v1.0/companies/{company_id}/project_types/{id} | Update project type
[**rest_v10_companies_company_id_project_types_post**](CoreCompanyProjectTypesApi.md#rest_v10_companies_company_id_project_types_post) | **POST** /rest/v1.0/companies/{company_id}/project_types | Create project type


# **rest_v10_companies_company_id_project_types_get**
> List[ProjectType2] rest_v10_companies_company_id_project_types_get(procore_company_id, company_id, page=page, per_page=per_page)

List project types

Returns a list of Project Types associated with a specified Company.

### Example


```python
import procore_sdk
from procore_sdk.models.project_type2 import ProjectType2
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
    api_instance = procore_sdk.CoreCompanyProjectTypesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List project types
        api_response = api_instance.rest_v10_companies_company_id_project_types_get(procore_company_id, company_id, page=page, per_page=per_page)
        print("The response of CoreCompanyProjectTypesApi->rest_v10_companies_company_id_project_types_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCompanyProjectTypesApi->rest_v10_companies_company_id_project_types_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[ProjectType2]**](ProjectType2.md)

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

# **rest_v10_companies_company_id_project_types_id_delete**
> rest_v10_companies_company_id_project_types_id_delete(procore_company_id, company_id, id)

Delete project type

Delete the specified Project Type.

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
    api_instance = procore_sdk.CoreCompanyProjectTypesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | ID of the project type

    try:
        # Delete project type
        api_instance.rest_v10_companies_company_id_project_types_id_delete(procore_company_id, company_id, id)
    except Exception as e:
        print("Exception when calling CoreCompanyProjectTypesApi->rest_v10_companies_company_id_project_types_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| ID of the project type | 

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
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_project_types_id_get**
> ProjectType2 rest_v10_companies_company_id_project_types_id_get(procore_company_id, company_id, id)

Show project type

Show detail on the specified Project Type.

### Example


```python
import procore_sdk
from procore_sdk.models.project_type2 import ProjectType2
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
    api_instance = procore_sdk.CoreCompanyProjectTypesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | ID of the project type

    try:
        # Show project type
        api_response = api_instance.rest_v10_companies_company_id_project_types_id_get(procore_company_id, company_id, id)
        print("The response of CoreCompanyProjectTypesApi->rest_v10_companies_company_id_project_types_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCompanyProjectTypesApi->rest_v10_companies_company_id_project_types_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| ID of the project type | 

### Return type

[**ProjectType2**](ProjectType2.md)

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

# **rest_v10_companies_company_id_project_types_id_patch**
> ProjectType2 rest_v10_companies_company_id_project_types_id_patch(procore_company_id, company_id, id, body34)

Update project type

Update a Project Type.

### Example


```python
import procore_sdk
from procore_sdk.models.body34 import Body34
from procore_sdk.models.project_type2 import ProjectType2
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
    api_instance = procore_sdk.CoreCompanyProjectTypesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | ID of the project type
    body34 = procore_sdk.Body34() # Body34 | 

    try:
        # Update project type
        api_response = api_instance.rest_v10_companies_company_id_project_types_id_patch(procore_company_id, company_id, id, body34)
        print("The response of CoreCompanyProjectTypesApi->rest_v10_companies_company_id_project_types_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCompanyProjectTypesApi->rest_v10_companies_company_id_project_types_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| ID of the project type | 
 **body34** | [**Body34**](Body34.md)|  | 

### Return type

[**ProjectType2**](ProjectType2.md)

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
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_project_types_post**
> ProjectType2 rest_v10_companies_company_id_project_types_post(procore_company_id, company_id, body34)

Create project type

Create a new Project Type associated with a specific Company.

### Example


```python
import procore_sdk
from procore_sdk.models.body34 import Body34
from procore_sdk.models.project_type2 import ProjectType2
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
    api_instance = procore_sdk.CoreCompanyProjectTypesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    body34 = procore_sdk.Body34() # Body34 | 

    try:
        # Create project type
        api_response = api_instance.rest_v10_companies_company_id_project_types_post(procore_company_id, company_id, body34)
        print("The response of CoreCompanyProjectTypesApi->rest_v10_companies_company_id_project_types_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCompanyProjectTypesApi->rest_v10_companies_company_id_project_types_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **body34** | [**Body34**](Body34.md)|  | 

### Return type

[**ProjectType2**](ProjectType2.md)

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
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

