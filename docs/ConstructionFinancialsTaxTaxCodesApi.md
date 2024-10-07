# procore_sdk.ConstructionFinancialsTaxTaxCodesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_tax_codes_get**](ConstructionFinancialsTaxTaxCodesApi.md#rest_v10_tax_codes_get) | **GET** /rest/v1.0/tax_codes | List Tax Codes
[**rest_v10_tax_codes_id_get**](ConstructionFinancialsTaxTaxCodesApi.md#rest_v10_tax_codes_id_get) | **GET** /rest/v1.0/tax_codes/{id} | Show Tax Code
[**rest_v10_tax_codes_id_patch**](ConstructionFinancialsTaxTaxCodesApi.md#rest_v10_tax_codes_id_patch) | **PATCH** /rest/v1.0/tax_codes/{id} | Update Tax Code
[**rest_v10_tax_codes_post**](ConstructionFinancialsTaxTaxCodesApi.md#rest_v10_tax_codes_post) | **POST** /rest/v1.0/tax_codes | Create Tax Code
[**rest_v10_tax_codes_sync_patch**](ConstructionFinancialsTaxTaxCodesApi.md#rest_v10_tax_codes_sync_patch) | **PATCH** /rest/v1.0/tax_codes/sync | Sync Tax Codes


# **rest_v10_tax_codes_get**
> List[RestV10TaxCodesGet200ResponseInner] rest_v10_tax_codes_get(procore_company_id, company_id, page=page, per_page=per_page)

List Tax Codes

Return a list of all Tax Codes for a given Company  When tax suport is enabled in Procore you can associate line items with a specific Tax Code. The Tax Code (sometimes known as a Tax Group) determines the tax rate to be applied to the line item for each Tax Type defined in Procore (Note that presently Procore only supports a single Tax Type per company).  You may define as many Tax Codes as required. Through the web interface, a Procore admin user may identify one of these tax codes as the default value to be shown when creating new line items.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_tax_codes_get200_response_inner import RestV10TaxCodesGet200ResponseInner
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
    api_instance = procore_sdk.ConstructionFinancialsTaxTaxCodesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Tax Codes
        api_response = api_instance.rest_v10_tax_codes_get(procore_company_id, company_id, page=page, per_page=per_page)
        print("The response of ConstructionFinancialsTaxTaxCodesApi->rest_v10_tax_codes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsTaxTaxCodesApi->rest_v10_tax_codes_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[RestV10TaxCodesGet200ResponseInner]**](RestV10TaxCodesGet200ResponseInner.md)

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

# **rest_v10_tax_codes_id_get**
> RestV10TaxCodesGet200ResponseInner rest_v10_tax_codes_id_get(procore_company_id, id, company_id)

Show Tax Code

Show detailed information for a specific Tax Code

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_tax_codes_get200_response_inner import RestV10TaxCodesGet200ResponseInner
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
    api_instance = procore_sdk.ConstructionFinancialsTaxTaxCodesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 'id_example' # str | The Tax Code ID
    company_id = 56 # int | Unique identifier for the company.

    try:
        # Show Tax Code
        api_response = api_instance.rest_v10_tax_codes_id_get(procore_company_id, id, company_id)
        print("The response of ConstructionFinancialsTaxTaxCodesApi->rest_v10_tax_codes_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsTaxTaxCodesApi->rest_v10_tax_codes_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **str**| The Tax Code ID | 
 **company_id** | **int**| Unique identifier for the company. | 

### Return type

[**RestV10TaxCodesGet200ResponseInner**](RestV10TaxCodesGet200ResponseInner.md)

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

# **rest_v10_tax_codes_id_patch**
> RestV10TaxCodesGet200ResponseInner rest_v10_tax_codes_id_patch(procore_company_id, id, company_id, rest_v10_tax_codes_id_patch_request)

Update Tax Code

Update a Tax Code's attributes

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_tax_codes_get200_response_inner import RestV10TaxCodesGet200ResponseInner
from procore_sdk.models.rest_v10_tax_codes_id_patch_request import RestV10TaxCodesIdPatchRequest
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
    api_instance = procore_sdk.ConstructionFinancialsTaxTaxCodesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 'id_example' # str | The Tax Code ID
    company_id = 56 # int | Unique identifier for the company.
    rest_v10_tax_codes_id_patch_request = procore_sdk.RestV10TaxCodesIdPatchRequest() # RestV10TaxCodesIdPatchRequest | 

    try:
        # Update Tax Code
        api_response = api_instance.rest_v10_tax_codes_id_patch(procore_company_id, id, company_id, rest_v10_tax_codes_id_patch_request)
        print("The response of ConstructionFinancialsTaxTaxCodesApi->rest_v10_tax_codes_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsTaxTaxCodesApi->rest_v10_tax_codes_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **str**| The Tax Code ID | 
 **company_id** | **int**| Unique identifier for the company. | 
 **rest_v10_tax_codes_id_patch_request** | [**RestV10TaxCodesIdPatchRequest**](RestV10TaxCodesIdPatchRequest.md)|  | 

### Return type

[**RestV10TaxCodesGet200ResponseInner**](RestV10TaxCodesGet200ResponseInner.md)

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

# **rest_v10_tax_codes_post**
> RestV10TaxCodesGet200ResponseInner rest_v10_tax_codes_post(procore_company_id, company_id, rest_v10_tax_codes_post_request)

Create Tax Code

Creates a Tax Code for a given Company

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_tax_codes_get200_response_inner import RestV10TaxCodesGet200ResponseInner
from procore_sdk.models.rest_v10_tax_codes_post_request import RestV10TaxCodesPostRequest
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
    api_instance = procore_sdk.ConstructionFinancialsTaxTaxCodesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    rest_v10_tax_codes_post_request = procore_sdk.RestV10TaxCodesPostRequest() # RestV10TaxCodesPostRequest | 

    try:
        # Create Tax Code
        api_response = api_instance.rest_v10_tax_codes_post(procore_company_id, company_id, rest_v10_tax_codes_post_request)
        print("The response of ConstructionFinancialsTaxTaxCodesApi->rest_v10_tax_codes_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsTaxTaxCodesApi->rest_v10_tax_codes_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **rest_v10_tax_codes_post_request** | [**RestV10TaxCodesPostRequest**](RestV10TaxCodesPostRequest.md)|  | 

### Return type

[**RestV10TaxCodesGet200ResponseInner**](RestV10TaxCodesGet200ResponseInner.md)

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

# **rest_v10_tax_codes_sync_patch**
> RestV10TaxCodesSyncPatch200Response rest_v10_tax_codes_sync_patch(procore_company_id, body13)

Sync Tax Codes

This endpoint creates or updates a batch of Tax Codes

### Example


```python
import procore_sdk
from procore_sdk.models.body13 import Body13
from procore_sdk.models.rest_v10_tax_codes_sync_patch200_response import RestV10TaxCodesSyncPatch200Response
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
    api_instance = procore_sdk.ConstructionFinancialsTaxTaxCodesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    body13 = procore_sdk.Body13() # Body13 | 

    try:
        # Sync Tax Codes
        api_response = api_instance.rest_v10_tax_codes_sync_patch(procore_company_id, body13)
        print("The response of ConstructionFinancialsTaxTaxCodesApi->rest_v10_tax_codes_sync_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsTaxTaxCodesApi->rest_v10_tax_codes_sync_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **body13** | [**Body13**](Body13.md)|  | 

### Return type

[**RestV10TaxCodesSyncPatch200Response**](RestV10TaxCodesSyncPatch200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

