# procore_sdk.ConstructionFinancialsCommitmentsContractPaymentsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_contract_payments_get**](ConstructionFinancialsCommitmentsContractPaymentsApi.md#rest_v10_contract_payments_get) | **GET** /rest/v1.0/contract_payments | List Contract Payments
[**rest_v10_contract_payments_id_delete**](ConstructionFinancialsCommitmentsContractPaymentsApi.md#rest_v10_contract_payments_id_delete) | **DELETE** /rest/v1.0/contract_payments/{id} | Delete Contract Payment
[**rest_v10_contract_payments_id_get**](ConstructionFinancialsCommitmentsContractPaymentsApi.md#rest_v10_contract_payments_id_get) | **GET** /rest/v1.0/contract_payments/{id} | Show Contract Payment
[**rest_v10_contract_payments_id_patch**](ConstructionFinancialsCommitmentsContractPaymentsApi.md#rest_v10_contract_payments_id_patch) | **PATCH** /rest/v1.0/contract_payments/{id} | Update Contract Payment
[**rest_v10_contract_payments_post**](ConstructionFinancialsCommitmentsContractPaymentsApi.md#rest_v10_contract_payments_post) | **POST** /rest/v1.0/contract_payments | Create Contract Payment


# **rest_v10_contract_payments_get**
> List[RestV10ContractPaymentsGet200ResponseInner] rest_v10_contract_payments_get(procore_company_id, project_id, contract_id, page=page, per_page=per_page)

List Contract Payments

Return a list of Contract Payments.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_contract_payments_get200_response_inner import RestV10ContractPaymentsGet200ResponseInner
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
    api_instance = procore_sdk.ConstructionFinancialsCommitmentsContractPaymentsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    contract_id = 56 # int | ID of the Contract
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Contract Payments
        api_response = api_instance.rest_v10_contract_payments_get(procore_company_id, project_id, contract_id, page=page, per_page=per_page)
        print("The response of ConstructionFinancialsCommitmentsContractPaymentsApi->rest_v10_contract_payments_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsCommitmentsContractPaymentsApi->rest_v10_contract_payments_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **contract_id** | **int**| ID of the Contract | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[RestV10ContractPaymentsGet200ResponseInner]**](RestV10ContractPaymentsGet200ResponseInner.md)

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

# **rest_v10_contract_payments_id_delete**
> rest_v10_contract_payments_id_delete(procore_company_id, id, project_id, contract_id)

Delete Contract Payment

Deletes a specified Contract Payment.

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
    api_instance = procore_sdk.ConstructionFinancialsCommitmentsContractPaymentsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID
    project_id = 56 # int | Unique identifier for the project.
    contract_id = 56 # int | ID of the Contract

    try:
        # Delete Contract Payment
        api_instance.rest_v10_contract_payments_id_delete(procore_company_id, id, project_id, contract_id)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsCommitmentsContractPaymentsApi->rest_v10_contract_payments_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID | 
 **project_id** | **int**| Unique identifier for the project. | 
 **contract_id** | **int**| ID of the Contract | 

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

# **rest_v10_contract_payments_id_get**
> RestV10ContractPaymentsGet200ResponseInner rest_v10_contract_payments_id_get(procore_company_id, id, project_id, contract_id)

Show Contract Payment

Return detailed information on the specified Contract Payment.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_contract_payments_get200_response_inner import RestV10ContractPaymentsGet200ResponseInner
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
    api_instance = procore_sdk.ConstructionFinancialsCommitmentsContractPaymentsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID
    project_id = 56 # int | Unique identifier for the project.
    contract_id = 56 # int | ID of the Contract

    try:
        # Show Contract Payment
        api_response = api_instance.rest_v10_contract_payments_id_get(procore_company_id, id, project_id, contract_id)
        print("The response of ConstructionFinancialsCommitmentsContractPaymentsApi->rest_v10_contract_payments_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsCommitmentsContractPaymentsApi->rest_v10_contract_payments_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID | 
 **project_id** | **int**| Unique identifier for the project. | 
 **contract_id** | **int**| ID of the Contract | 

### Return type

[**RestV10ContractPaymentsGet200ResponseInner**](RestV10ContractPaymentsGet200ResponseInner.md)

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

# **rest_v10_contract_payments_id_patch**
> RestV10ContractPaymentsGet200ResponseInner rest_v10_contract_payments_id_patch(procore_company_id, id, body109)

Update Contract Payment

Update a Contract Payment. All attributes other than 'attachments', 'origin_id', and 'origin_data' will be locked if the contract payment is synced with an ERP system.

### Example


```python
import procore_sdk
from procore_sdk.models.body109 import Body109
from procore_sdk.models.rest_v10_contract_payments_get200_response_inner import RestV10ContractPaymentsGet200ResponseInner
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
    api_instance = procore_sdk.ConstructionFinancialsCommitmentsContractPaymentsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID
    body109 = procore_sdk.Body109() # Body109 | 

    try:
        # Update Contract Payment
        api_response = api_instance.rest_v10_contract_payments_id_patch(procore_company_id, id, body109)
        print("The response of ConstructionFinancialsCommitmentsContractPaymentsApi->rest_v10_contract_payments_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsCommitmentsContractPaymentsApi->rest_v10_contract_payments_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID | 
 **body109** | [**Body109**](Body109.md)|  | 

### Return type

[**RestV10ContractPaymentsGet200ResponseInner**](RestV10ContractPaymentsGet200ResponseInner.md)

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
**422** | Unprocessable Entity |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_contract_payments_post**
> RestV10ContractPaymentsGet200ResponseInner rest_v10_contract_payments_post(procore_company_id, body109)

Create Contract Payment

Create a new Contract Payment.

### Example


```python
import procore_sdk
from procore_sdk.models.body109 import Body109
from procore_sdk.models.rest_v10_contract_payments_get200_response_inner import RestV10ContractPaymentsGet200ResponseInner
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
    api_instance = procore_sdk.ConstructionFinancialsCommitmentsContractPaymentsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    body109 = procore_sdk.Body109() # Body109 | 

    try:
        # Create Contract Payment
        api_response = api_instance.rest_v10_contract_payments_post(procore_company_id, body109)
        print("The response of ConstructionFinancialsCommitmentsContractPaymentsApi->rest_v10_contract_payments_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsCommitmentsContractPaymentsApi->rest_v10_contract_payments_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **body109** | [**Body109**](Body109.md)|  | 

### Return type

[**RestV10ContractPaymentsGet200ResponseInner**](RestV10ContractPaymentsGet200ResponseInner.md)

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
**422** | Unprocessable Entity |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

