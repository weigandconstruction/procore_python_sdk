# procore_sdk.CoreCompanyProjectBidTypesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_project_bid_types_get**](CoreCompanyProjectBidTypesApi.md#rest_v10_companies_company_id_project_bid_types_get) | **GET** /rest/v1.0/companies/{company_id}/project_bid_types | List Project Bid Types
[**rest_v10_companies_company_id_project_bid_types_id_delete**](CoreCompanyProjectBidTypesApi.md#rest_v10_companies_company_id_project_bid_types_id_delete) | **DELETE** /rest/v1.0/companies/{company_id}/project_bid_types/{id} | Delete Project Bid Type
[**rest_v10_companies_company_id_project_bid_types_id_get**](CoreCompanyProjectBidTypesApi.md#rest_v10_companies_company_id_project_bid_types_id_get) | **GET** /rest/v1.0/companies/{company_id}/project_bid_types/{id} | Show Project Bid Type
[**rest_v10_companies_company_id_project_bid_types_id_patch**](CoreCompanyProjectBidTypesApi.md#rest_v10_companies_company_id_project_bid_types_id_patch) | **PATCH** /rest/v1.0/companies/{company_id}/project_bid_types/{id} | Update Project Bid Type
[**rest_v10_companies_company_id_project_bid_types_post**](CoreCompanyProjectBidTypesApi.md#rest_v10_companies_company_id_project_bid_types_post) | **POST** /rest/v1.0/companies/{company_id}/project_bid_types | Create Project Bid Type


# **rest_v10_companies_company_id_project_bid_types_get**
> List[ProjectBidType2] rest_v10_companies_company_id_project_bid_types_get(procore_company_id, company_id, page=page, per_page=per_page)

List Project Bid Types

Return a list of Project Bid Types

### Example


```python
import procore_sdk
from procore_sdk.models.project_bid_type2 import ProjectBidType2
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
    api_instance = procore_sdk.CoreCompanyProjectBidTypesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Project Bid Types
        api_response = api_instance.rest_v10_companies_company_id_project_bid_types_get(procore_company_id, company_id, page=page, per_page=per_page)
        print("The response of CoreCompanyProjectBidTypesApi->rest_v10_companies_company_id_project_bid_types_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCompanyProjectBidTypesApi->rest_v10_companies_company_id_project_bid_types_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[ProjectBidType2]**](ProjectBidType2.md)

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

# **rest_v10_companies_company_id_project_bid_types_id_delete**
> rest_v10_companies_company_id_project_bid_types_id_delete(procore_company_id, company_id, id)

Delete Project Bid Type

Delete the specified Project Bid Type.

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
    api_instance = procore_sdk.CoreCompanyProjectBidTypesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | ID of the Project Bid Type

    try:
        # Delete Project Bid Type
        api_instance.rest_v10_companies_company_id_project_bid_types_id_delete(procore_company_id, company_id, id)
    except Exception as e:
        print("Exception when calling CoreCompanyProjectBidTypesApi->rest_v10_companies_company_id_project_bid_types_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| ID of the Project Bid Type | 

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
**422** | Error Deleting Project Bid Type |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_project_bid_types_id_get**
> ProjectBidType2 rest_v10_companies_company_id_project_bid_types_id_get(procore_company_id, company_id, id)

Show Project Bid Type

Show detail on a specified Project Bid Type.

### Example


```python
import procore_sdk
from procore_sdk.models.project_bid_type2 import ProjectBidType2
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
    api_instance = procore_sdk.CoreCompanyProjectBidTypesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | ID of the Project Bid Type

    try:
        # Show Project Bid Type
        api_response = api_instance.rest_v10_companies_company_id_project_bid_types_id_get(procore_company_id, company_id, id)
        print("The response of CoreCompanyProjectBidTypesApi->rest_v10_companies_company_id_project_bid_types_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCompanyProjectBidTypesApi->rest_v10_companies_company_id_project_bid_types_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| ID of the Project Bid Type | 

### Return type

[**ProjectBidType2**](ProjectBidType2.md)

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

# **rest_v10_companies_company_id_project_bid_types_id_patch**
> ProjectBidType2 rest_v10_companies_company_id_project_bid_types_id_patch(procore_company_id, company_id, id, body41)

Update Project Bid Type

Update the specified Project Bid Type.

### Example


```python
import procore_sdk
from procore_sdk.models.body41 import Body41
from procore_sdk.models.project_bid_type2 import ProjectBidType2
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
    api_instance = procore_sdk.CoreCompanyProjectBidTypesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | ID of the Project Bid Type
    body41 = procore_sdk.Body41() # Body41 | 

    try:
        # Update Project Bid Type
        api_response = api_instance.rest_v10_companies_company_id_project_bid_types_id_patch(procore_company_id, company_id, id, body41)
        print("The response of CoreCompanyProjectBidTypesApi->rest_v10_companies_company_id_project_bid_types_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCompanyProjectBidTypesApi->rest_v10_companies_company_id_project_bid_types_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| ID of the Project Bid Type | 
 **body41** | [**Body41**](Body41.md)|  | 

### Return type

[**ProjectBidType2**](ProjectBidType2.md)

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
**422** | Error Updating Project Bid Type |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_project_bid_types_post**
> ProjectBidType2 rest_v10_companies_company_id_project_bid_types_post(procore_company_id, company_id, body41)

Create Project Bid Type

Create a new Project Bid Type in the specified Company.

### Example


```python
import procore_sdk
from procore_sdk.models.body41 import Body41
from procore_sdk.models.project_bid_type2 import ProjectBidType2
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
    api_instance = procore_sdk.CoreCompanyProjectBidTypesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    body41 = procore_sdk.Body41() # Body41 | 

    try:
        # Create Project Bid Type
        api_response = api_instance.rest_v10_companies_company_id_project_bid_types_post(procore_company_id, company_id, body41)
        print("The response of CoreCompanyProjectBidTypesApi->rest_v10_companies_company_id_project_bid_types_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCompanyProjectBidTypesApi->rest_v10_companies_company_id_project_bid_types_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **body41** | [**Body41**](Body41.md)|  | 

### Return type

[**ProjectBidType2**](ProjectBidType2.md)

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
**422** | Error Creating Project Bid Type |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

