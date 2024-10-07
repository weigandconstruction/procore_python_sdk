# procore_sdk.CoreCompanyProjectRegionsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_project_regions_get**](CoreCompanyProjectRegionsApi.md#rest_v10_companies_company_id_project_regions_get) | **GET** /rest/v1.0/companies/{company_id}/project_regions | List Project Regions
[**rest_v10_companies_company_id_project_regions_id_delete**](CoreCompanyProjectRegionsApi.md#rest_v10_companies_company_id_project_regions_id_delete) | **DELETE** /rest/v1.0/companies/{company_id}/project_regions/{id} | Delete Project Region
[**rest_v10_companies_company_id_project_regions_id_get**](CoreCompanyProjectRegionsApi.md#rest_v10_companies_company_id_project_regions_id_get) | **GET** /rest/v1.0/companies/{company_id}/project_regions/{id} | Show Project Region
[**rest_v10_companies_company_id_project_regions_id_patch**](CoreCompanyProjectRegionsApi.md#rest_v10_companies_company_id_project_regions_id_patch) | **PATCH** /rest/v1.0/companies/{company_id}/project_regions/{id} | Update Project Region
[**rest_v10_companies_company_id_project_regions_post**](CoreCompanyProjectRegionsApi.md#rest_v10_companies_company_id_project_regions_post) | **POST** /rest/v1.0/companies/{company_id}/project_regions | Create Project Region


# **rest_v10_companies_company_id_project_regions_get**
> List[ProjectRegion2] rest_v10_companies_company_id_project_regions_get(procore_company_id, company_id, page=page, per_page=per_page)

List Project Regions

Return a list of Project Regions.

### Example


```python
import procore_sdk
from procore_sdk.models.project_region2 import ProjectRegion2
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
    api_instance = procore_sdk.CoreCompanyProjectRegionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Project Regions
        api_response = api_instance.rest_v10_companies_company_id_project_regions_get(procore_company_id, company_id, page=page, per_page=per_page)
        print("The response of CoreCompanyProjectRegionsApi->rest_v10_companies_company_id_project_regions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCompanyProjectRegionsApi->rest_v10_companies_company_id_project_regions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[ProjectRegion2]**](ProjectRegion2.md)

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

# **rest_v10_companies_company_id_project_regions_id_delete**
> object rest_v10_companies_company_id_project_regions_id_delete(procore_company_id, company_id, id)

Delete Project Region

Delete the specified Project Region.

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
    api_instance = procore_sdk.CoreCompanyProjectRegionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | ID of the Project Region

    try:
        # Delete Project Region
        api_response = api_instance.rest_v10_companies_company_id_project_regions_id_delete(procore_company_id, company_id, id)
        print("The response of CoreCompanyProjectRegionsApi->rest_v10_companies_company_id_project_regions_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCompanyProjectRegionsApi->rest_v10_companies_company_id_project_regions_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| ID of the Project Region | 

### Return type

**object**

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
**422** | Error Deleting Project Region |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_project_regions_id_get**
> ProjectRegion2 rest_v10_companies_company_id_project_regions_id_get(procore_company_id, company_id, id)

Show Project Region

Show detail on a specified Project Region.

### Example


```python
import procore_sdk
from procore_sdk.models.project_region2 import ProjectRegion2
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
    api_instance = procore_sdk.CoreCompanyProjectRegionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | ID of the Project Region

    try:
        # Show Project Region
        api_response = api_instance.rest_v10_companies_company_id_project_regions_id_get(procore_company_id, company_id, id)
        print("The response of CoreCompanyProjectRegionsApi->rest_v10_companies_company_id_project_regions_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCompanyProjectRegionsApi->rest_v10_companies_company_id_project_regions_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| ID of the Project Region | 

### Return type

[**ProjectRegion2**](ProjectRegion2.md)

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

# **rest_v10_companies_company_id_project_regions_id_patch**
> ProjectRegion2 rest_v10_companies_company_id_project_regions_id_patch(procore_company_id, company_id, id, body37)

Update Project Region

Update the specified Project Region.

### Example


```python
import procore_sdk
from procore_sdk.models.body37 import Body37
from procore_sdk.models.project_region2 import ProjectRegion2
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
    api_instance = procore_sdk.CoreCompanyProjectRegionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | ID of the Project Region
    body37 = procore_sdk.Body37() # Body37 | 

    try:
        # Update Project Region
        api_response = api_instance.rest_v10_companies_company_id_project_regions_id_patch(procore_company_id, company_id, id, body37)
        print("The response of CoreCompanyProjectRegionsApi->rest_v10_companies_company_id_project_regions_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCompanyProjectRegionsApi->rest_v10_companies_company_id_project_regions_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| ID of the Project Region | 
 **body37** | [**Body37**](Body37.md)|  | 

### Return type

[**ProjectRegion2**](ProjectRegion2.md)

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
**422** | Error Updating Project Region |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_project_regions_post**
> ProjectRegion2 rest_v10_companies_company_id_project_regions_post(procore_company_id, company_id, body37)

Create Project Region

Create a new Project Region in the specified Company.

### Example


```python
import procore_sdk
from procore_sdk.models.body37 import Body37
from procore_sdk.models.project_region2 import ProjectRegion2
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
    api_instance = procore_sdk.CoreCompanyProjectRegionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    body37 = procore_sdk.Body37() # Body37 | 

    try:
        # Create Project Region
        api_response = api_instance.rest_v10_companies_company_id_project_regions_post(procore_company_id, company_id, body37)
        print("The response of CoreCompanyProjectRegionsApi->rest_v10_companies_company_id_project_regions_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCompanyProjectRegionsApi->rest_v10_companies_company_id_project_regions_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **body37** | [**Body37**](Body37.md)|  | 

### Return type

[**ProjectRegion2**](ProjectRegion2.md)

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
**422** | Error Creating Project Region |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

