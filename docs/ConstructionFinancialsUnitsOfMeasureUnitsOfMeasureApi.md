# procore_sdk.ConstructionFinancialsUnitsOfMeasureUnitsOfMeasureApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_uoms_get**](ConstructionFinancialsUnitsOfMeasureUnitsOfMeasureApi.md#rest_v10_companies_company_id_uoms_get) | **GET** /rest/v1.0/companies/{company_id}/uoms | List Units of Measure
[**rest_v10_companies_company_id_uoms_id_delete**](ConstructionFinancialsUnitsOfMeasureUnitsOfMeasureApi.md#rest_v10_companies_company_id_uoms_id_delete) | **DELETE** /rest/v1.0/companies/{company_id}/uoms/{id} | Delete Unit of Measure
[**rest_v10_companies_company_id_uoms_id_get**](ConstructionFinancialsUnitsOfMeasureUnitsOfMeasureApi.md#rest_v10_companies_company_id_uoms_id_get) | **GET** /rest/v1.0/companies/{company_id}/uoms/{id} | Show Unit of Measure
[**rest_v10_companies_company_id_uoms_id_patch**](ConstructionFinancialsUnitsOfMeasureUnitsOfMeasureApi.md#rest_v10_companies_company_id_uoms_id_patch) | **PATCH** /rest/v1.0/companies/{company_id}/uoms/{id} | Update Unit of Measure
[**rest_v10_companies_company_id_uoms_post**](ConstructionFinancialsUnitsOfMeasureUnitsOfMeasureApi.md#rest_v10_companies_company_id_uoms_post) | **POST** /rest/v1.0/companies/{company_id}/uoms | Create Unit of Measure
[**rest_v10_companies_company_id_uoms_sync_patch**](ConstructionFinancialsUnitsOfMeasureUnitsOfMeasureApi.md#rest_v10_companies_company_id_uoms_sync_patch) | **PATCH** /rest/v1.0/companies/{company_id}/uoms/sync | Sync Units of Measure


# **rest_v10_companies_company_id_uoms_get**
> List[RestV10CompaniesCompanyIdUomsGet200ResponseInner] rest_v10_companies_company_id_uoms_get(procore_company_id, company_id, page=page, per_page=per_page)

List Units of Measure

Return a list of all Units of Measure (UOM)

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_uoms_get200_response_inner import RestV10CompaniesCompanyIdUomsGet200ResponseInner
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
    api_instance = procore_sdk.ConstructionFinancialsUnitsOfMeasureUnitsOfMeasureApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Units of Measure
        api_response = api_instance.rest_v10_companies_company_id_uoms_get(procore_company_id, company_id, page=page, per_page=per_page)
        print("The response of ConstructionFinancialsUnitsOfMeasureUnitsOfMeasureApi->rest_v10_companies_company_id_uoms_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsUnitsOfMeasureUnitsOfMeasureApi->rest_v10_companies_company_id_uoms_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[RestV10CompaniesCompanyIdUomsGet200ResponseInner]**](RestV10CompaniesCompanyIdUomsGet200ResponseInner.md)

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

# **rest_v10_companies_company_id_uoms_id_delete**
> rest_v10_companies_company_id_uoms_id_delete(procore_company_id, company_id, id)

Delete Unit of Measure

Delete a Unit of Measure (UOM)

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
    api_instance = procore_sdk.ConstructionFinancialsUnitsOfMeasureUnitsOfMeasureApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | Unit of Measure ID

    try:
        # Delete Unit of Measure
        api_instance.rest_v10_companies_company_id_uoms_id_delete(procore_company_id, company_id, id)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsUnitsOfMeasureUnitsOfMeasureApi->rest_v10_companies_company_id_uoms_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| Unit of Measure ID | 

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

# **rest_v10_companies_company_id_uoms_id_get**
> RestV10CompaniesCompanyIdUomsGet200ResponseInner rest_v10_companies_company_id_uoms_id_get(procore_company_id, company_id, id)

Show Unit of Measure

Show a given Unit of Measure (UOM)

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_uoms_get200_response_inner import RestV10CompaniesCompanyIdUomsGet200ResponseInner
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
    api_instance = procore_sdk.ConstructionFinancialsUnitsOfMeasureUnitsOfMeasureApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | Unit of Measure ID

    try:
        # Show Unit of Measure
        api_response = api_instance.rest_v10_companies_company_id_uoms_id_get(procore_company_id, company_id, id)
        print("The response of ConstructionFinancialsUnitsOfMeasureUnitsOfMeasureApi->rest_v10_companies_company_id_uoms_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsUnitsOfMeasureUnitsOfMeasureApi->rest_v10_companies_company_id_uoms_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| Unit of Measure ID | 

### Return type

[**RestV10CompaniesCompanyIdUomsGet200ResponseInner**](RestV10CompaniesCompanyIdUomsGet200ResponseInner.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_uoms_id_patch**
> RestV10CompaniesCompanyIdUomsGet200ResponseInner rest_v10_companies_company_id_uoms_id_patch(procore_company_id, company_id, id, body7)

Update Unit of Measure

Update Unit of Measure (UOM) attributes

### Example


```python
import procore_sdk
from procore_sdk.models.body7 import Body7
from procore_sdk.models.rest_v10_companies_company_id_uoms_get200_response_inner import RestV10CompaniesCompanyIdUomsGet200ResponseInner
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
    api_instance = procore_sdk.ConstructionFinancialsUnitsOfMeasureUnitsOfMeasureApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | Unit of Measure ID
    body7 = procore_sdk.Body7() # Body7 | 

    try:
        # Update Unit of Measure
        api_response = api_instance.rest_v10_companies_company_id_uoms_id_patch(procore_company_id, company_id, id, body7)
        print("The response of ConstructionFinancialsUnitsOfMeasureUnitsOfMeasureApi->rest_v10_companies_company_id_uoms_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsUnitsOfMeasureUnitsOfMeasureApi->rest_v10_companies_company_id_uoms_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| Unit of Measure ID | 
 **body7** | [**Body7**](Body7.md)|  | 

### Return type

[**RestV10CompaniesCompanyIdUomsGet200ResponseInner**](RestV10CompaniesCompanyIdUomsGet200ResponseInner.md)

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
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_uoms_post**
> RestV10CompaniesCompanyIdUomsGet200ResponseInner rest_v10_companies_company_id_uoms_post(procore_company_id, company_id, body7)

Create Unit of Measure

Create a new Unit of Measure (UOM)

### Example


```python
import procore_sdk
from procore_sdk.models.body7 import Body7
from procore_sdk.models.rest_v10_companies_company_id_uoms_get200_response_inner import RestV10CompaniesCompanyIdUomsGet200ResponseInner
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
    api_instance = procore_sdk.ConstructionFinancialsUnitsOfMeasureUnitsOfMeasureApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    body7 = procore_sdk.Body7() # Body7 | 

    try:
        # Create Unit of Measure
        api_response = api_instance.rest_v10_companies_company_id_uoms_post(procore_company_id, company_id, body7)
        print("The response of ConstructionFinancialsUnitsOfMeasureUnitsOfMeasureApi->rest_v10_companies_company_id_uoms_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsUnitsOfMeasureUnitsOfMeasureApi->rest_v10_companies_company_id_uoms_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **body7** | [**Body7**](Body7.md)|  | 

### Return type

[**RestV10CompaniesCompanyIdUomsGet200ResponseInner**](RestV10CompaniesCompanyIdUomsGet200ResponseInner.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_uoms_sync_patch**
> ArrayOfUnitsOfMeasure rest_v10_companies_company_id_uoms_sync_patch(procore_company_id, company_id, body8)

Sync Units of Measure

This endpoint creates or updates a batch of Units of Measure. See [Using Sync Actions](/documentation/using-sync-actions) for additional information.

### Example


```python
import procore_sdk
from procore_sdk.models.array_of_units_of_measure import ArrayOfUnitsOfMeasure
from procore_sdk.models.body8 import Body8
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
    api_instance = procore_sdk.ConstructionFinancialsUnitsOfMeasureUnitsOfMeasureApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    body8 = procore_sdk.Body8() # Body8 | 

    try:
        # Sync Units of Measure
        api_response = api_instance.rest_v10_companies_company_id_uoms_sync_patch(procore_company_id, company_id, body8)
        print("The response of ConstructionFinancialsUnitsOfMeasureUnitsOfMeasureApi->rest_v10_companies_company_id_uoms_sync_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsUnitsOfMeasureUnitsOfMeasureApi->rest_v10_companies_company_id_uoms_sync_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **body8** | [**Body8**](Body8.md)|  | 

### Return type

[**ArrayOfUnitsOfMeasure**](ArrayOfUnitsOfMeasure.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Array of Units of Measure |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

