# procore_sdk.CoreCompanyProjectOwnerTypesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_project_owner_types_get**](CoreCompanyProjectOwnerTypesApi.md#rest_v10_companies_company_id_project_owner_types_get) | **GET** /rest/v1.0/companies/{company_id}/project_owner_types | List Project Owner Types
[**rest_v10_companies_company_id_project_owner_types_id_delete**](CoreCompanyProjectOwnerTypesApi.md#rest_v10_companies_company_id_project_owner_types_id_delete) | **DELETE** /rest/v1.0/companies/{company_id}/project_owner_types/{id} | Delete Project Owner Type
[**rest_v10_companies_company_id_project_owner_types_id_get**](CoreCompanyProjectOwnerTypesApi.md#rest_v10_companies_company_id_project_owner_types_id_get) | **GET** /rest/v1.0/companies/{company_id}/project_owner_types/{id} | Show Project Owner Type
[**rest_v10_companies_company_id_project_owner_types_id_patch**](CoreCompanyProjectOwnerTypesApi.md#rest_v10_companies_company_id_project_owner_types_id_patch) | **PATCH** /rest/v1.0/companies/{company_id}/project_owner_types/{id} | Update Project Owner Type
[**rest_v10_companies_company_id_project_owner_types_post**](CoreCompanyProjectOwnerTypesApi.md#rest_v10_companies_company_id_project_owner_types_post) | **POST** /rest/v1.0/companies/{company_id}/project_owner_types | Create Project Owner Type


# **rest_v10_companies_company_id_project_owner_types_get**
> List[ProjectOwnerType2] rest_v10_companies_company_id_project_owner_types_get(procore_company_id, company_id, page=page, per_page=per_page)

List Project Owner Types

Return a list of Project Owner Types

### Example


```python
import procore_sdk
from procore_sdk.models.project_owner_type2 import ProjectOwnerType2
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
    api_instance = procore_sdk.CoreCompanyProjectOwnerTypesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Project Owner Types
        api_response = api_instance.rest_v10_companies_company_id_project_owner_types_get(procore_company_id, company_id, page=page, per_page=per_page)
        print("The response of CoreCompanyProjectOwnerTypesApi->rest_v10_companies_company_id_project_owner_types_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCompanyProjectOwnerTypesApi->rest_v10_companies_company_id_project_owner_types_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[ProjectOwnerType2]**](ProjectOwnerType2.md)

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

# **rest_v10_companies_company_id_project_owner_types_id_delete**
> rest_v10_companies_company_id_project_owner_types_id_delete(procore_company_id, company_id, id)

Delete Project Owner Type

Delete the specified Project Owner Type.

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
    api_instance = procore_sdk.CoreCompanyProjectOwnerTypesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | ID of the Project Owner Type

    try:
        # Delete Project Owner Type
        api_instance.rest_v10_companies_company_id_project_owner_types_id_delete(procore_company_id, company_id, id)
    except Exception as e:
        print("Exception when calling CoreCompanyProjectOwnerTypesApi->rest_v10_companies_company_id_project_owner_types_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| ID of the Project Owner Type | 

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
**404** | Not Found |  -  |
**422** | Error Deleting Project Owner Type |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_project_owner_types_id_get**
> ProjectOwnerType2 rest_v10_companies_company_id_project_owner_types_id_get(procore_company_id, company_id, id)

Show Project Owner Type

Show detail on a specified Project Owner Type.

### Example


```python
import procore_sdk
from procore_sdk.models.project_owner_type2 import ProjectOwnerType2
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
    api_instance = procore_sdk.CoreCompanyProjectOwnerTypesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | ID of the Project Owner Type

    try:
        # Show Project Owner Type
        api_response = api_instance.rest_v10_companies_company_id_project_owner_types_id_get(procore_company_id, company_id, id)
        print("The response of CoreCompanyProjectOwnerTypesApi->rest_v10_companies_company_id_project_owner_types_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCompanyProjectOwnerTypesApi->rest_v10_companies_company_id_project_owner_types_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| ID of the Project Owner Type | 

### Return type

[**ProjectOwnerType2**](ProjectOwnerType2.md)

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
**404** | Not Found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_project_owner_types_id_patch**
> ProjectOwnerType2 rest_v10_companies_company_id_project_owner_types_id_patch(procore_company_id, company_id, id, body38)

Update Project Owner Type

Update the specified Project Owner Type.

### Example


```python
import procore_sdk
from procore_sdk.models.body38 import Body38
from procore_sdk.models.project_owner_type2 import ProjectOwnerType2
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
    api_instance = procore_sdk.CoreCompanyProjectOwnerTypesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | ID of the Project Owner Type
    body38 = procore_sdk.Body38() # Body38 | 

    try:
        # Update Project Owner Type
        api_response = api_instance.rest_v10_companies_company_id_project_owner_types_id_patch(procore_company_id, company_id, id, body38)
        print("The response of CoreCompanyProjectOwnerTypesApi->rest_v10_companies_company_id_project_owner_types_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCompanyProjectOwnerTypesApi->rest_v10_companies_company_id_project_owner_types_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| ID of the Project Owner Type | 
 **body38** | [**Body38**](Body38.md)|  | 

### Return type

[**ProjectOwnerType2**](ProjectOwnerType2.md)

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
**404** | Not Found |  -  |
**422** | Error Updating Project Owner Type |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_project_owner_types_post**
> ProjectOwnerType2 rest_v10_companies_company_id_project_owner_types_post(procore_company_id, company_id, body38)

Create Project Owner Type

Create a new Project Owner Type in the specified Company.

### Example


```python
import procore_sdk
from procore_sdk.models.body38 import Body38
from procore_sdk.models.project_owner_type2 import ProjectOwnerType2
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
    api_instance = procore_sdk.CoreCompanyProjectOwnerTypesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    body38 = procore_sdk.Body38() # Body38 | 

    try:
        # Create Project Owner Type
        api_response = api_instance.rest_v10_companies_company_id_project_owner_types_post(procore_company_id, company_id, body38)
        print("The response of CoreCompanyProjectOwnerTypesApi->rest_v10_companies_company_id_project_owner_types_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCompanyProjectOwnerTypesApi->rest_v10_companies_company_id_project_owner_types_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **body38** | [**Body38**](Body38.md)|  | 

### Return type

[**ProjectOwnerType2**](ProjectOwnerType2.md)

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
**404** | Not Found |  -  |
**422** | Error Creating Project Owner Type |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

