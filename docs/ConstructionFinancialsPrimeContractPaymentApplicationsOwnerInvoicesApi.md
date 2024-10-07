# procore_sdk.ConstructionFinancialsPrimeContractPaymentApplicationsOwnerInvoicesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_payment_applications_get**](ConstructionFinancialsPrimeContractPaymentApplicationsOwnerInvoicesApi.md#rest_v10_payment_applications_get) | **GET** /rest/v1.0/payment_applications | List Payment Applications (Owner Invoices) for a Project
[**rest_v10_payment_applications_id_delete**](ConstructionFinancialsPrimeContractPaymentApplicationsOwnerInvoicesApi.md#rest_v10_payment_applications_id_delete) | **DELETE** /rest/v1.0/payment_applications/{id} | Delete a Payment Application (Owner Invoice)
[**rest_v10_payment_applications_id_get**](ConstructionFinancialsPrimeContractPaymentApplicationsOwnerInvoicesApi.md#rest_v10_payment_applications_id_get) | **GET** /rest/v1.0/payment_applications/{id} | Show Payment Application (Owner Invoice)
[**rest_v10_prime_contracts_prime_contract_id_payment_applications_get**](ConstructionFinancialsPrimeContractPaymentApplicationsOwnerInvoicesApi.md#rest_v10_prime_contracts_prime_contract_id_payment_applications_get) | **GET** /rest/v1.0/prime_contracts/{prime_contract_id}/payment_applications | List Payment Applications (Owner Invoices) for Prime Contract
[**rest_v10_prime_contracts_prime_contract_id_payment_applications_id_patch**](ConstructionFinancialsPrimeContractPaymentApplicationsOwnerInvoicesApi.md#rest_v10_prime_contracts_prime_contract_id_payment_applications_id_patch) | **PATCH** /rest/v1.0/prime_contracts/{prime_contract_id}/payment_applications/{id} | Update Payment Application (Owner Invoice) for Prime Contract
[**rest_v10_prime_contracts_prime_contract_id_payment_applications_post**](ConstructionFinancialsPrimeContractPaymentApplicationsOwnerInvoicesApi.md#rest_v10_prime_contracts_prime_contract_id_payment_applications_post) | **POST** /rest/v1.0/prime_contracts/{prime_contract_id}/payment_applications | Create Payment Application (Owner Invoice) for Prime Contract


# **rest_v10_payment_applications_get**
> List[RestV10PaymentApplicationsGet200ResponseInner] rest_v10_payment_applications_get(procore_company_id, project_id, page=page, per_page=per_page)

List Payment Applications (Owner Invoices) for a Project

Return a list of all Payment Applications (Owner Invoices) on a specified Project  See [Filtering on List Actions](https://developers.procore.com/documentation/filtering-on-list-actions) for information on using the filtering capabilities provided by this endpoint.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_payment_applications_get200_response_inner import RestV10PaymentApplicationsGet200ResponseInner
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
    api_instance = procore_sdk.ConstructionFinancialsPrimeContractPaymentApplicationsOwnerInvoicesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Payment Applications (Owner Invoices) for a Project
        api_response = api_instance.rest_v10_payment_applications_get(procore_company_id, project_id, page=page, per_page=per_page)
        print("The response of ConstructionFinancialsPrimeContractPaymentApplicationsOwnerInvoicesApi->rest_v10_payment_applications_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsPrimeContractPaymentApplicationsOwnerInvoicesApi->rest_v10_payment_applications_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[RestV10PaymentApplicationsGet200ResponseInner]**](RestV10PaymentApplicationsGet200ResponseInner.md)

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
**404** | Not Found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_payment_applications_id_delete**
> rest_v10_payment_applications_id_delete(procore_company_id, id, project_id)

Delete a Payment Application (Owner Invoice)

Delete a Payment Application (Owner Invoice) based on its id

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
    api_instance = procore_sdk.ConstructionFinancialsPrimeContractPaymentApplicationsOwnerInvoicesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | Payment Application (Owner Invoice) ID
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Delete a Payment Application (Owner Invoice)
        api_instance.rest_v10_payment_applications_id_delete(procore_company_id, id, project_id)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsPrimeContractPaymentApplicationsOwnerInvoicesApi->rest_v10_payment_applications_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| Payment Application (Owner Invoice) ID | 
 **project_id** | **int**| Unique identifier for the project. | 

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_payment_applications_id_get**
> RestV10PaymentApplicationsIdGet200Response rest_v10_payment_applications_id_get(procore_company_id, id, project_id)

Show Payment Application (Owner Invoice)

Return a Payment Application (Owner Invoice)

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_payment_applications_id_get200_response import RestV10PaymentApplicationsIdGet200Response
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
    api_instance = procore_sdk.ConstructionFinancialsPrimeContractPaymentApplicationsOwnerInvoicesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | Payment Application (Owner Invoice) ID
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Show Payment Application (Owner Invoice)
        api_response = api_instance.rest_v10_payment_applications_id_get(procore_company_id, id, project_id)
        print("The response of ConstructionFinancialsPrimeContractPaymentApplicationsOwnerInvoicesApi->rest_v10_payment_applications_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsPrimeContractPaymentApplicationsOwnerInvoicesApi->rest_v10_payment_applications_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| Payment Application (Owner Invoice) ID | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**RestV10PaymentApplicationsIdGet200Response**](RestV10PaymentApplicationsIdGet200Response.md)

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

# **rest_v10_prime_contracts_prime_contract_id_payment_applications_get**
> List[RestV10PrimeContractsPrimeContractIdPaymentApplicationsGet200ResponseInner] rest_v10_prime_contracts_prime_contract_id_payment_applications_get(procore_company_id, prime_contract_id, project_id, page=page, per_page=per_page)

List Payment Applications (Owner Invoices) for Prime Contract

Return a list of all Payment Applications (Owner Invoices) on a specified Prime Contract  See [Filtering on List Actions](https://developers.procore.com/documentation/filtering-on-list-actions) for information on using the filtering capabilities provided by this endpoint.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_prime_contracts_prime_contract_id_payment_applications_get200_response_inner import RestV10PrimeContractsPrimeContractIdPaymentApplicationsGet200ResponseInner
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
    api_instance = procore_sdk.ConstructionFinancialsPrimeContractPaymentApplicationsOwnerInvoicesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    prime_contract_id = 56 # int | Prime Contract ID
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (default 30) (optional)

    try:
        # List Payment Applications (Owner Invoices) for Prime Contract
        api_response = api_instance.rest_v10_prime_contracts_prime_contract_id_payment_applications_get(procore_company_id, prime_contract_id, project_id, page=page, per_page=per_page)
        print("The response of ConstructionFinancialsPrimeContractPaymentApplicationsOwnerInvoicesApi->rest_v10_prime_contracts_prime_contract_id_payment_applications_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsPrimeContractPaymentApplicationsOwnerInvoicesApi->rest_v10_prime_contracts_prime_contract_id_payment_applications_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **prime_contract_id** | **int**| Prime Contract ID | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page (default 30) | [optional] 

### Return type

[**List[RestV10PrimeContractsPrimeContractIdPaymentApplicationsGet200ResponseInner]**](RestV10PrimeContractsPrimeContractIdPaymentApplicationsGet200ResponseInner.md)

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
**404** | Not Found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_prime_contracts_prime_contract_id_payment_applications_id_patch**
> RestV10PrimeContractsPrimeContractIdPaymentApplicationsPost201Response rest_v10_prime_contracts_prime_contract_id_payment_applications_id_patch(procore_company_id, prime_contract_id, id, body51)

Update Payment Application (Owner Invoice) for Prime Contract

Update a Payment Application (Owner Invoice) on a specified Prime Contract.

### Example


```python
import procore_sdk
from procore_sdk.models.body51 import Body51
from procore_sdk.models.rest_v10_prime_contracts_prime_contract_id_payment_applications_post201_response import RestV10PrimeContractsPrimeContractIdPaymentApplicationsPost201Response
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
    api_instance = procore_sdk.ConstructionFinancialsPrimeContractPaymentApplicationsOwnerInvoicesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    prime_contract_id = 56 # int | Prime Contract ID
    id = 56 # int | Payment Application (Owner Invoice) ID
    body51 = procore_sdk.Body51() # Body51 | 

    try:
        # Update Payment Application (Owner Invoice) for Prime Contract
        api_response = api_instance.rest_v10_prime_contracts_prime_contract_id_payment_applications_id_patch(procore_company_id, prime_contract_id, id, body51)
        print("The response of ConstructionFinancialsPrimeContractPaymentApplicationsOwnerInvoicesApi->rest_v10_prime_contracts_prime_contract_id_payment_applications_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsPrimeContractPaymentApplicationsOwnerInvoicesApi->rest_v10_prime_contracts_prime_contract_id_payment_applications_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **prime_contract_id** | **int**| Prime Contract ID | 
 **id** | **int**| Payment Application (Owner Invoice) ID | 
 **body51** | [**Body51**](Body51.md)|  | 

### Return type

[**RestV10PrimeContractsPrimeContractIdPaymentApplicationsPost201Response**](RestV10PrimeContractsPrimeContractIdPaymentApplicationsPost201Response.md)

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
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_prime_contracts_prime_contract_id_payment_applications_post**
> RestV10PrimeContractsPrimeContractIdPaymentApplicationsPost201Response rest_v10_prime_contracts_prime_contract_id_payment_applications_post(procore_company_id, prime_contract_id, body50)

Create Payment Application (Owner Invoice) for Prime Contract

Create a Payment Application (Owner Invoice) on a specified Prime Contract

### Example


```python
import procore_sdk
from procore_sdk.models.body50 import Body50
from procore_sdk.models.rest_v10_prime_contracts_prime_contract_id_payment_applications_post201_response import RestV10PrimeContractsPrimeContractIdPaymentApplicationsPost201Response
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
    api_instance = procore_sdk.ConstructionFinancialsPrimeContractPaymentApplicationsOwnerInvoicesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    prime_contract_id = 56 # int | Prime Contract ID
    body50 = procore_sdk.Body50() # Body50 | 

    try:
        # Create Payment Application (Owner Invoice) for Prime Contract
        api_response = api_instance.rest_v10_prime_contracts_prime_contract_id_payment_applications_post(procore_company_id, prime_contract_id, body50)
        print("The response of ConstructionFinancialsPrimeContractPaymentApplicationsOwnerInvoicesApi->rest_v10_prime_contracts_prime_contract_id_payment_applications_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsPrimeContractPaymentApplicationsOwnerInvoicesApi->rest_v10_prime_contracts_prime_contract_id_payment_applications_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **prime_contract_id** | **int**| Prime Contract ID | 
 **body50** | [**Body50**](Body50.md)|  | 

### Return type

[**RestV10PrimeContractsPrimeContractIdPaymentApplicationsPost201Response**](RestV10PrimeContractsPrimeContractIdPaymentApplicationsPost201Response.md)

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
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

