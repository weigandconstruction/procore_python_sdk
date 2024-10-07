# procore_sdk.ConstructionFinancialsPrimeContractPrimeContractsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_prime_contract_get**](ConstructionFinancialsPrimeContractPrimeContractsApi.md#rest_v10_prime_contract_get) | **GET** /rest/v1.0/prime_contract | Show First Prime Contract
[**rest_v10_prime_contract_id_delete**](ConstructionFinancialsPrimeContractPrimeContractsApi.md#rest_v10_prime_contract_id_delete) | **DELETE** /rest/v1.0/prime_contract/{id} | Delete Prime Contract
[**rest_v10_prime_contract_id_get**](ConstructionFinancialsPrimeContractPrimeContractsApi.md#rest_v10_prime_contract_id_get) | **GET** /rest/v1.0/prime_contract/{id} | Show Prime Contract
[**rest_v10_prime_contract_id_patch**](ConstructionFinancialsPrimeContractPrimeContractsApi.md#rest_v10_prime_contract_id_patch) | **PATCH** /rest/v1.0/prime_contract/{id} | Update Prime Contract
[**rest_v10_prime_contract_post**](ConstructionFinancialsPrimeContractPrimeContractsApi.md#rest_v10_prime_contract_post) | **POST** /rest/v1.0/prime_contract | Create Prime Contract
[**rest_v10_prime_contracts_get**](ConstructionFinancialsPrimeContractPrimeContractsApi.md#rest_v10_prime_contracts_get) | **GET** /rest/v1.0/prime_contracts | List all Prime Contracts


# **rest_v10_prime_contract_get**
> RestV10PrimeContractGet200Response rest_v10_prime_contract_get(procore_company_id, project_id)

Show First Prime Contract

Returns the first Prime Contract created for the specified Project. Use the `/prime_contracts` endpoint if you need to return more than one Prime Contract.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_prime_contract_get200_response import RestV10PrimeContractGet200Response
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
    api_instance = procore_sdk.ConstructionFinancialsPrimeContractPrimeContractsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Show First Prime Contract
        api_response = api_instance.rest_v10_prime_contract_get(procore_company_id, project_id)
        print("The response of ConstructionFinancialsPrimeContractPrimeContractsApi->rest_v10_prime_contract_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsPrimeContractPrimeContractsApi->rest_v10_prime_contract_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**RestV10PrimeContractGet200Response**](RestV10PrimeContractGet200Response.md)

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

# **rest_v10_prime_contract_id_delete**
> rest_v10_prime_contract_id_delete(procore_company_id, id, project_id)

Delete Prime Contract

Delete the specified Prime Contract.

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
    api_instance = procore_sdk.ConstructionFinancialsPrimeContractPrimeContractsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the Prime Contract
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Delete Prime Contract
        api_instance.rest_v10_prime_contract_id_delete(procore_company_id, id, project_id)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsPrimeContractPrimeContractsApi->rest_v10_prime_contract_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the Prime Contract | 
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
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_prime_contract_id_get**
> RestV10PrimeContractGet200Response rest_v10_prime_contract_id_get(procore_company_id, id, project_id)

Show Prime Contract

Show the details of a Project's Prime Contract.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_prime_contract_get200_response import RestV10PrimeContractGet200Response
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
    api_instance = procore_sdk.ConstructionFinancialsPrimeContractPrimeContractsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the Prime Contract
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Show Prime Contract
        api_response = api_instance.rest_v10_prime_contract_id_get(procore_company_id, id, project_id)
        print("The response of ConstructionFinancialsPrimeContractPrimeContractsApi->rest_v10_prime_contract_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsPrimeContractPrimeContractsApi->rest_v10_prime_contract_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the Prime Contract | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**RestV10PrimeContractGet200Response**](RestV10PrimeContractGet200Response.md)

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

# **rest_v10_prime_contract_id_patch**
> RestV10PrimeContractGet200Response rest_v10_prime_contract_id_patch(procore_company_id, id, body44, run_configurable_validations=run_configurable_validations)

Update Prime Contract

Update the specified Prime Contract.

### Example


```python
import procore_sdk
from procore_sdk.models.body44 import Body44
from procore_sdk.models.rest_v10_prime_contract_get200_response import RestV10PrimeContractGet200Response
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
    api_instance = procore_sdk.ConstructionFinancialsPrimeContractPrimeContractsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the Prime Contract
    body44 = procore_sdk.Body44() # Body44 | 
    run_configurable_validations = False # bool | If true, validations are run for the corresponding Configurable Field Set. (optional) (default to False)

    try:
        # Update Prime Contract
        api_response = api_instance.rest_v10_prime_contract_id_patch(procore_company_id, id, body44, run_configurable_validations=run_configurable_validations)
        print("The response of ConstructionFinancialsPrimeContractPrimeContractsApi->rest_v10_prime_contract_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsPrimeContractPrimeContractsApi->rest_v10_prime_contract_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the Prime Contract | 
 **body44** | [**Body44**](Body44.md)|  | 
 **run_configurable_validations** | **bool**| If true, validations are run for the corresponding Configurable Field Set. | [optional] [default to False]

### Return type

[**RestV10PrimeContractGet200Response**](RestV10PrimeContractGet200Response.md)

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

# **rest_v10_prime_contract_post**
> RestV10PrimeContractGet200Response rest_v10_prime_contract_post(procore_company_id, body44, run_configurable_validations=run_configurable_validations)

Create Prime Contract

Create a new Prime Contract.

### Example


```python
import procore_sdk
from procore_sdk.models.body44 import Body44
from procore_sdk.models.rest_v10_prime_contract_get200_response import RestV10PrimeContractGet200Response
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
    api_instance = procore_sdk.ConstructionFinancialsPrimeContractPrimeContractsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    body44 = procore_sdk.Body44() # Body44 | 
    run_configurable_validations = False # bool | If true, validations are run for the corresponding Configurable Field Set. (optional) (default to False)

    try:
        # Create Prime Contract
        api_response = api_instance.rest_v10_prime_contract_post(procore_company_id, body44, run_configurable_validations=run_configurable_validations)
        print("The response of ConstructionFinancialsPrimeContractPrimeContractsApi->rest_v10_prime_contract_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsPrimeContractPrimeContractsApi->rest_v10_prime_contract_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **body44** | [**Body44**](Body44.md)|  | 
 **run_configurable_validations** | **bool**| If true, validations are run for the corresponding Configurable Field Set. | [optional] [default to False]

### Return type

[**RestV10PrimeContractGet200Response**](RestV10PrimeContractGet200Response.md)

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

# **rest_v10_prime_contracts_get**
> List[RestV10PrimeContractsGet200ResponseInner] rest_v10_prime_contracts_get(procore_company_id, project_id, page=page, per_page=per_page, filters_id=filters_id, filters_updated_at=filters_updated_at)

List all Prime Contracts

Returns all Prime Contracts for the specified Project.  See [Filtering on List Actions](https://developers.procore.com/documentation/filtering-on-list-actions) for information on using the filtering capabilities provided by this endpoint.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_prime_contracts_get200_response_inner import RestV10PrimeContractsGet200ResponseInner
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
    api_instance = procore_sdk.ConstructionFinancialsPrimeContractPrimeContractsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)

    try:
        # List all Prime Contracts
        api_response = api_instance.rest_v10_prime_contracts_get(procore_company_id, project_id, page=page, per_page=per_page, filters_id=filters_id, filters_updated_at=filters_updated_at)
        print("The response of ConstructionFinancialsPrimeContractPrimeContractsApi->rest_v10_prime_contracts_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsPrimeContractPrimeContractsApi->rest_v10_prime_contracts_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_id** | [**List[int]**](int.md)| Return item(s) with the specified IDs. | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 

### Return type

[**List[RestV10PrimeContractsGet200ResponseInner]**](RestV10PrimeContractsGet200ResponseInner.md)

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

