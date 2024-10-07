# procore_sdk.ConstructionFinancialsCommitmentsRFQsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_rfqs_get**](ConstructionFinancialsCommitmentsRFQsApi.md#rest_v10_rfqs_get) | **GET** /rest/v1.0/rfqs | List RFQs
[**rest_v10_rfqs_id_delete**](ConstructionFinancialsCommitmentsRFQsApi.md#rest_v10_rfqs_id_delete) | **DELETE** /rest/v1.0/rfqs/{id} | Delete RFQ
[**rest_v10_rfqs_id_get**](ConstructionFinancialsCommitmentsRFQsApi.md#rest_v10_rfqs_id_get) | **GET** /rest/v1.0/rfqs/{id} | Show RFQ
[**rest_v10_rfqs_id_patch**](ConstructionFinancialsCommitmentsRFQsApi.md#rest_v10_rfqs_id_patch) | **PATCH** /rest/v1.0/rfqs/{id} | Update RFQ
[**rest_v10_rfqs_post**](ConstructionFinancialsCommitmentsRFQsApi.md#rest_v10_rfqs_post) | **POST** /rest/v1.0/rfqs | Create RFQ
[**rest_v10_rfqs_rfq_id_quotes_get**](ConstructionFinancialsCommitmentsRFQsApi.md#rest_v10_rfqs_rfq_id_quotes_get) | **GET** /rest/v1.0/rfqs/{rfq_id}/quotes | List RFQ Quotes
[**rest_v10_rfqs_rfq_id_quotes_id_get**](ConstructionFinancialsCommitmentsRFQsApi.md#rest_v10_rfqs_rfq_id_quotes_id_get) | **GET** /rest/v1.0/rfqs/{rfq_id}/quotes/{id} | Show RFQ Quote
[**rest_v10_rfqs_rfq_id_quotes_id_patch**](ConstructionFinancialsCommitmentsRFQsApi.md#rest_v10_rfqs_rfq_id_quotes_id_patch) | **PATCH** /rest/v1.0/rfqs/{rfq_id}/quotes/{id} | Update RFQ Quote
[**rest_v10_rfqs_rfq_id_quotes_post**](ConstructionFinancialsCommitmentsRFQsApi.md#rest_v10_rfqs_rfq_id_quotes_post) | **POST** /rest/v1.0/rfqs/{rfq_id}/quotes | Create RFQ Quote
[**rest_v10_rfqs_rfq_id_responses_get**](ConstructionFinancialsCommitmentsRFQsApi.md#rest_v10_rfqs_rfq_id_responses_get) | **GET** /rest/v1.0/rfqs/{rfq_id}/responses | List RFQ Responses
[**rest_v10_rfqs_rfq_id_responses_id_get**](ConstructionFinancialsCommitmentsRFQsApi.md#rest_v10_rfqs_rfq_id_responses_id_get) | **GET** /rest/v1.0/rfqs/{rfq_id}/responses/{id} | Show RFQ Response
[**rest_v10_rfqs_rfq_id_responses_id_patch**](ConstructionFinancialsCommitmentsRFQsApi.md#rest_v10_rfqs_rfq_id_responses_id_patch) | **PATCH** /rest/v1.0/rfqs/{rfq_id}/responses/{id} | Update RFQ Response
[**rest_v10_rfqs_rfq_id_responses_post**](ConstructionFinancialsCommitmentsRFQsApi.md#rest_v10_rfqs_rfq_id_responses_post) | **POST** /rest/v1.0/rfqs/{rfq_id}/responses | Create RFQ Response


# **rest_v10_rfqs_get**
> List[RFQ] rest_v10_rfqs_get(procore_company_id, project_id, contract_id, page=page, per_page=per_page, filters_status=filters_status, filters_created_at=filters_created_at, filters_updated_at=filters_updated_at, filters_commitment_contract_id=filters_commitment_contract_id)

List RFQs

Return a list of all RFQs in a specified Project and Contract.  See [Filtering on List Actions](https://developers.procore.com/documentation/filtering-on-list-actions) for information on using the filtering capabilities provided by this endpoint.

### Example


```python
import procore_sdk
from procore_sdk.models.rfq import RFQ
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
    api_instance = procore_sdk.ConstructionFinancialsCommitmentsRFQsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    contract_id = 56 # int | Contract ID
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_status = 'filters_status_example' # str | Returns item(s) with the specified value for RFQ status. (optional)
    filters_created_at = '2013-10-20' # date | Return item(s) created within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_commitment_contract_id = 56 # int | Return item(s) with the specified Commitment Contract ID. (optional)

    try:
        # List RFQs
        api_response = api_instance.rest_v10_rfqs_get(procore_company_id, project_id, contract_id, page=page, per_page=per_page, filters_status=filters_status, filters_created_at=filters_created_at, filters_updated_at=filters_updated_at, filters_commitment_contract_id=filters_commitment_contract_id)
        print("The response of ConstructionFinancialsCommitmentsRFQsApi->rest_v10_rfqs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsCommitmentsRFQsApi->rest_v10_rfqs_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **contract_id** | **int**| Contract ID | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_status** | **str**| Returns item(s) with the specified value for RFQ status. | [optional] 
 **filters_created_at** | **date**| Return item(s) created within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_commitment_contract_id** | **int**| Return item(s) with the specified Commitment Contract ID. | [optional] 

### Return type

[**List[RFQ]**](RFQ.md)

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

# **rest_v10_rfqs_id_delete**
> rest_v10_rfqs_id_delete(procore_company_id, id, project_id, contract_id)

Delete RFQ

Delete a specified RFQ in a specified Project and Contract.

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
    api_instance = procore_sdk.ConstructionFinancialsCommitmentsRFQsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID
    project_id = 56 # int | Unique identifier for the project.
    contract_id = 56 # int | Contract ID

    try:
        # Delete RFQ
        api_instance.rest_v10_rfqs_id_delete(procore_company_id, id, project_id, contract_id)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsCommitmentsRFQsApi->rest_v10_rfqs_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID | 
 **project_id** | **int**| Unique identifier for the project. | 
 **contract_id** | **int**| Contract ID | 

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
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_rfqs_id_get**
> RFQ rest_v10_rfqs_id_get(procore_company_id, id, project_id, contract_id)

Show RFQ

Return detailed information about a specified RFQ in a specified Project and Contract.

### Example


```python
import procore_sdk
from procore_sdk.models.rfq import RFQ
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
    api_instance = procore_sdk.ConstructionFinancialsCommitmentsRFQsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID
    project_id = 56 # int | Unique identifier for the project.
    contract_id = 56 # int | Contract ID

    try:
        # Show RFQ
        api_response = api_instance.rest_v10_rfqs_id_get(procore_company_id, id, project_id, contract_id)
        print("The response of ConstructionFinancialsCommitmentsRFQsApi->rest_v10_rfqs_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsCommitmentsRFQsApi->rest_v10_rfqs_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID | 
 **project_id** | **int**| Unique identifier for the project. | 
 **contract_id** | **int**| Contract ID | 

### Return type

[**RFQ**](RFQ.md)

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

# **rest_v10_rfqs_id_patch**
> RFQ rest_v10_rfqs_id_patch(procore_company_id, id, rest_v10_rfqs_id_patch_request)

Update RFQ

Update an RFQ in a specified Project and Contract.

### Example


```python
import procore_sdk
from procore_sdk.models.rfq import RFQ
from procore_sdk.models.rest_v10_rfqs_id_patch_request import RestV10RfqsIdPatchRequest
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
    api_instance = procore_sdk.ConstructionFinancialsCommitmentsRFQsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID
    rest_v10_rfqs_id_patch_request = procore_sdk.RestV10RfqsIdPatchRequest() # RestV10RfqsIdPatchRequest | 

    try:
        # Update RFQ
        api_response = api_instance.rest_v10_rfqs_id_patch(procore_company_id, id, rest_v10_rfqs_id_patch_request)
        print("The response of ConstructionFinancialsCommitmentsRFQsApi->rest_v10_rfqs_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsCommitmentsRFQsApi->rest_v10_rfqs_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID | 
 **rest_v10_rfqs_id_patch_request** | [**RestV10RfqsIdPatchRequest**](RestV10RfqsIdPatchRequest.md)|  | 

### Return type

[**RFQ**](RFQ.md)

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

# **rest_v10_rfqs_post**
> RFQ2 rest_v10_rfqs_post(procore_company_id, rest_v10_rfqs_post_request)

Create RFQ

Create a new RFQ in a specified Project and Contract.

### Example


```python
import procore_sdk
from procore_sdk.models.rfq2 import RFQ2
from procore_sdk.models.rest_v10_rfqs_post_request import RestV10RfqsPostRequest
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
    api_instance = procore_sdk.ConstructionFinancialsCommitmentsRFQsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    rest_v10_rfqs_post_request = procore_sdk.RestV10RfqsPostRequest() # RestV10RfqsPostRequest | 

    try:
        # Create RFQ
        api_response = api_instance.rest_v10_rfqs_post(procore_company_id, rest_v10_rfqs_post_request)
        print("The response of ConstructionFinancialsCommitmentsRFQsApi->rest_v10_rfqs_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsCommitmentsRFQsApi->rest_v10_rfqs_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **rest_v10_rfqs_post_request** | [**RestV10RfqsPostRequest**](RestV10RfqsPostRequest.md)|  | 

### Return type

[**RFQ2**](RFQ2.md)

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

# **rest_v10_rfqs_rfq_id_quotes_get**
> List[RFQQuote] rest_v10_rfqs_rfq_id_quotes_get(procore_company_id, rfq_id, project_id, contract_id, page=page, per_page=per_page)

List RFQ Quotes

Return a list of all Quotes in a specified RFQ.

### Example


```python
import procore_sdk
from procore_sdk.models.rfq_quote import RFQQuote
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
    api_instance = procore_sdk.ConstructionFinancialsCommitmentsRFQsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    rfq_id = 56 # int | RFQ ID
    project_id = 56 # int | Unique identifier for the project.
    contract_id = 56 # int | Contract ID
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List RFQ Quotes
        api_response = api_instance.rest_v10_rfqs_rfq_id_quotes_get(procore_company_id, rfq_id, project_id, contract_id, page=page, per_page=per_page)
        print("The response of ConstructionFinancialsCommitmentsRFQsApi->rest_v10_rfqs_rfq_id_quotes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsCommitmentsRFQsApi->rest_v10_rfqs_rfq_id_quotes_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **rfq_id** | **int**| RFQ ID | 
 **project_id** | **int**| Unique identifier for the project. | 
 **contract_id** | **int**| Contract ID | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[RFQQuote]**](RFQQuote.md)

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

# **rest_v10_rfqs_rfq_id_quotes_id_get**
> RFQQuote rest_v10_rfqs_rfq_id_quotes_id_get(procore_company_id, rfq_id, id, project_id, contract_id)

Show RFQ Quote

Return detailed information about a specified Quote in a specified RFQ.

### Example


```python
import procore_sdk
from procore_sdk.models.rfq_quote import RFQQuote
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
    api_instance = procore_sdk.ConstructionFinancialsCommitmentsRFQsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    rfq_id = 56 # int | RFQ ID
    id = 56 # int | RFQ Quote ID
    project_id = 56 # int | Unique identifier for the project.
    contract_id = 56 # int | Contract ID

    try:
        # Show RFQ Quote
        api_response = api_instance.rest_v10_rfqs_rfq_id_quotes_id_get(procore_company_id, rfq_id, id, project_id, contract_id)
        print("The response of ConstructionFinancialsCommitmentsRFQsApi->rest_v10_rfqs_rfq_id_quotes_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsCommitmentsRFQsApi->rest_v10_rfqs_rfq_id_quotes_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **rfq_id** | **int**| RFQ ID | 
 **id** | **int**| RFQ Quote ID | 
 **project_id** | **int**| Unique identifier for the project. | 
 **contract_id** | **int**| Contract ID | 

### Return type

[**RFQQuote**](RFQQuote.md)

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

# **rest_v10_rfqs_rfq_id_quotes_id_patch**
> RFQQuote rest_v10_rfqs_rfq_id_quotes_id_patch(procore_company_id, rfq_id, id, rest_v10_rfqs_rfq_id_quotes_post_request)

Update RFQ Quote

Update a specified Quote in a specified RFQ.

### Example


```python
import procore_sdk
from procore_sdk.models.rfq_quote import RFQQuote
from procore_sdk.models.rest_v10_rfqs_rfq_id_quotes_post_request import RestV10RfqsRfqIdQuotesPostRequest
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
    api_instance = procore_sdk.ConstructionFinancialsCommitmentsRFQsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    rfq_id = 56 # int | RFQ ID
    id = 56 # int | RFQ Quote ID
    rest_v10_rfqs_rfq_id_quotes_post_request = procore_sdk.RestV10RfqsRfqIdQuotesPostRequest() # RestV10RfqsRfqIdQuotesPostRequest | 

    try:
        # Update RFQ Quote
        api_response = api_instance.rest_v10_rfqs_rfq_id_quotes_id_patch(procore_company_id, rfq_id, id, rest_v10_rfqs_rfq_id_quotes_post_request)
        print("The response of ConstructionFinancialsCommitmentsRFQsApi->rest_v10_rfqs_rfq_id_quotes_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsCommitmentsRFQsApi->rest_v10_rfqs_rfq_id_quotes_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **rfq_id** | **int**| RFQ ID | 
 **id** | **int**| RFQ Quote ID | 
 **rest_v10_rfqs_rfq_id_quotes_post_request** | [**RestV10RfqsRfqIdQuotesPostRequest**](RestV10RfqsRfqIdQuotesPostRequest.md)|  | 

### Return type

[**RFQQuote**](RFQQuote.md)

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

# **rest_v10_rfqs_rfq_id_quotes_post**
> RFQQuote rest_v10_rfqs_rfq_id_quotes_post(procore_company_id, rfq_id, rest_v10_rfqs_rfq_id_quotes_post_request)

Create RFQ Quote

Create a new Quote in a specified RFQ.

### Example


```python
import procore_sdk
from procore_sdk.models.rfq_quote import RFQQuote
from procore_sdk.models.rest_v10_rfqs_rfq_id_quotes_post_request import RestV10RfqsRfqIdQuotesPostRequest
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
    api_instance = procore_sdk.ConstructionFinancialsCommitmentsRFQsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    rfq_id = 56 # int | RFQ ID
    rest_v10_rfqs_rfq_id_quotes_post_request = procore_sdk.RestV10RfqsRfqIdQuotesPostRequest() # RestV10RfqsRfqIdQuotesPostRequest | 

    try:
        # Create RFQ Quote
        api_response = api_instance.rest_v10_rfqs_rfq_id_quotes_post(procore_company_id, rfq_id, rest_v10_rfqs_rfq_id_quotes_post_request)
        print("The response of ConstructionFinancialsCommitmentsRFQsApi->rest_v10_rfqs_rfq_id_quotes_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsCommitmentsRFQsApi->rest_v10_rfqs_rfq_id_quotes_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **rfq_id** | **int**| RFQ ID | 
 **rest_v10_rfqs_rfq_id_quotes_post_request** | [**RestV10RfqsRfqIdQuotesPostRequest**](RestV10RfqsRfqIdQuotesPostRequest.md)|  | 

### Return type

[**RFQQuote**](RFQQuote.md)

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

# **rest_v10_rfqs_rfq_id_responses_get**
> List[RFQResponse] rest_v10_rfqs_rfq_id_responses_get(procore_company_id, rfq_id, project_id, contract_id, page=page, per_page=per_page)

List RFQ Responses

Return a list of all Responses in a specified RFQ.

### Example


```python
import procore_sdk
from procore_sdk.models.rfq_response import RFQResponse
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
    api_instance = procore_sdk.ConstructionFinancialsCommitmentsRFQsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    rfq_id = 56 # int | RFQ ID
    project_id = 56 # int | Unique identifier for the project.
    contract_id = 56 # int | Contract ID
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List RFQ Responses
        api_response = api_instance.rest_v10_rfqs_rfq_id_responses_get(procore_company_id, rfq_id, project_id, contract_id, page=page, per_page=per_page)
        print("The response of ConstructionFinancialsCommitmentsRFQsApi->rest_v10_rfqs_rfq_id_responses_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsCommitmentsRFQsApi->rest_v10_rfqs_rfq_id_responses_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **rfq_id** | **int**| RFQ ID | 
 **project_id** | **int**| Unique identifier for the project. | 
 **contract_id** | **int**| Contract ID | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[RFQResponse]**](RFQResponse.md)

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

# **rest_v10_rfqs_rfq_id_responses_id_get**
> RFQResponse rest_v10_rfqs_rfq_id_responses_id_get(procore_company_id, rfq_id, id, project_id, contract_id)

Show RFQ Response

Return detailed information about a specified Response in a specified RFQ.

### Example


```python
import procore_sdk
from procore_sdk.models.rfq_response import RFQResponse
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
    api_instance = procore_sdk.ConstructionFinancialsCommitmentsRFQsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    rfq_id = 56 # int | RFQ ID
    id = 56 # int | ID
    project_id = 56 # int | Unique identifier for the project.
    contract_id = 56 # int | Contract ID

    try:
        # Show RFQ Response
        api_response = api_instance.rest_v10_rfqs_rfq_id_responses_id_get(procore_company_id, rfq_id, id, project_id, contract_id)
        print("The response of ConstructionFinancialsCommitmentsRFQsApi->rest_v10_rfqs_rfq_id_responses_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsCommitmentsRFQsApi->rest_v10_rfqs_rfq_id_responses_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **rfq_id** | **int**| RFQ ID | 
 **id** | **int**| ID | 
 **project_id** | **int**| Unique identifier for the project. | 
 **contract_id** | **int**| Contract ID | 

### Return type

[**RFQResponse**](RFQResponse.md)

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

# **rest_v10_rfqs_rfq_id_responses_id_patch**
> RFQResponse rest_v10_rfqs_rfq_id_responses_id_patch(procore_company_id, rfq_id, id, rest_v10_rfqs_rfq_id_responses_post_request)

Update RFQ Response

Update a specified Response in a specified RFQ.

### Example


```python
import procore_sdk
from procore_sdk.models.rfq_response import RFQResponse
from procore_sdk.models.rest_v10_rfqs_rfq_id_responses_post_request import RestV10RfqsRfqIdResponsesPostRequest
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
    api_instance = procore_sdk.ConstructionFinancialsCommitmentsRFQsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    rfq_id = 56 # int | RFQ ID
    id = 56 # int | ID
    rest_v10_rfqs_rfq_id_responses_post_request = procore_sdk.RestV10RfqsRfqIdResponsesPostRequest() # RestV10RfqsRfqIdResponsesPostRequest | 

    try:
        # Update RFQ Response
        api_response = api_instance.rest_v10_rfqs_rfq_id_responses_id_patch(procore_company_id, rfq_id, id, rest_v10_rfqs_rfq_id_responses_post_request)
        print("The response of ConstructionFinancialsCommitmentsRFQsApi->rest_v10_rfqs_rfq_id_responses_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsCommitmentsRFQsApi->rest_v10_rfqs_rfq_id_responses_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **rfq_id** | **int**| RFQ ID | 
 **id** | **int**| ID | 
 **rest_v10_rfqs_rfq_id_responses_post_request** | [**RestV10RfqsRfqIdResponsesPostRequest**](RestV10RfqsRfqIdResponsesPostRequest.md)|  | 

### Return type

[**RFQResponse**](RFQResponse.md)

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

# **rest_v10_rfqs_rfq_id_responses_post**
> RFQResponse rest_v10_rfqs_rfq_id_responses_post(procore_company_id, rfq_id, rest_v10_rfqs_rfq_id_responses_post_request)

Create RFQ Response

Create a new Response in a specified RFQ.

### Example


```python
import procore_sdk
from procore_sdk.models.rfq_response import RFQResponse
from procore_sdk.models.rest_v10_rfqs_rfq_id_responses_post_request import RestV10RfqsRfqIdResponsesPostRequest
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
    api_instance = procore_sdk.ConstructionFinancialsCommitmentsRFQsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    rfq_id = 56 # int | RFQ ID
    rest_v10_rfqs_rfq_id_responses_post_request = procore_sdk.RestV10RfqsRfqIdResponsesPostRequest() # RestV10RfqsRfqIdResponsesPostRequest | 

    try:
        # Create RFQ Response
        api_response = api_instance.rest_v10_rfqs_rfq_id_responses_post(procore_company_id, rfq_id, rest_v10_rfqs_rfq_id_responses_post_request)
        print("The response of ConstructionFinancialsCommitmentsRFQsApi->rest_v10_rfqs_rfq_id_responses_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsCommitmentsRFQsApi->rest_v10_rfqs_rfq_id_responses_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **rfq_id** | **int**| RFQ ID | 
 **rest_v10_rfqs_rfq_id_responses_post_request** | [**RestV10RfqsRfqIdResponsesPostRequest**](RestV10RfqsRfqIdResponsesPostRequest.md)|  | 

### Return type

[**RFQResponse**](RFQResponse.md)

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

