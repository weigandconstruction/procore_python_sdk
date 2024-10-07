# procore_sdk.CoreCompanyTradesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_trades_get**](CoreCompanyTradesApi.md#rest_v10_companies_company_id_trades_get) | **GET** /rest/v1.0/companies/{company_id}/trades | List trades
[**rest_v10_companies_company_id_trades_id_get**](CoreCompanyTradesApi.md#rest_v10_companies_company_id_trades_id_get) | **GET** /rest/v1.0/companies/{company_id}/trades/{id} | Show Trade
[**rest_v10_companies_company_id_trades_post**](CoreCompanyTradesApi.md#rest_v10_companies_company_id_trades_post) | **POST** /rest/v1.0/companies/{company_id}/trades | Create Trade


# **rest_v10_companies_company_id_trades_get**
> List[Trade] rest_v10_companies_company_id_trades_get(procore_company_id, company_id, page=page, per_page=per_page, filters_updated_at=filters_updated_at, filters_active=filters_active, filters_query=filters_query)

List trades

Return a list of all Trades associated with a Company.

### Example


```python
import procore_sdk
from procore_sdk.models.trade import Trade
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
    api_instance = procore_sdk.CoreCompanyTradesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_active = True # bool | Limit results to available trades (optional)
    filters_query = 'filters_query_example' # str | Query trades by name (optional)

    try:
        # List trades
        api_response = api_instance.rest_v10_companies_company_id_trades_get(procore_company_id, company_id, page=page, per_page=per_page, filters_updated_at=filters_updated_at, filters_active=filters_active, filters_query=filters_query)
        print("The response of CoreCompanyTradesApi->rest_v10_companies_company_id_trades_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCompanyTradesApi->rest_v10_companies_company_id_trades_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_active** | **bool**| Limit results to available trades | [optional] 
 **filters_query** | **str**| Query trades by name | [optional] 

### Return type

[**List[Trade]**](Trade.md)

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

# **rest_v10_companies_company_id_trades_id_get**
> Trade rest_v10_companies_company_id_trades_id_get(procore_company_id, company_id, id)

Show Trade

Returns the details for a specified Trade.

### Example


```python
import procore_sdk
from procore_sdk.models.trade import Trade
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
    api_instance = procore_sdk.CoreCompanyTradesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | Trade ID

    try:
        # Show Trade
        api_response = api_instance.rest_v10_companies_company_id_trades_id_get(procore_company_id, company_id, id)
        print("The response of CoreCompanyTradesApi->rest_v10_companies_company_id_trades_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCompanyTradesApi->rest_v10_companies_company_id_trades_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| Trade ID | 

### Return type

[**Trade**](Trade.md)

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_trades_post**
> Trade rest_v10_companies_company_id_trades_post(procore_company_id, company_id, body9=body9)

Create Trade

Creates a Trade associated to a Company.

### Example


```python
import procore_sdk
from procore_sdk.models.body9 import Body9
from procore_sdk.models.trade import Trade
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
    api_instance = procore_sdk.CoreCompanyTradesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    body9 = procore_sdk.Body9() # Body9 |  (optional)

    try:
        # Create Trade
        api_response = api_instance.rest_v10_companies_company_id_trades_post(procore_company_id, company_id, body9=body9)
        print("The response of CoreCompanyTradesApi->rest_v10_companies_company_id_trades_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCompanyTradesApi->rest_v10_companies_company_id_trades_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **body9** | [**Body9**](Body9.md)|  | [optional] 

### Return type

[**Trade**](Trade.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Unprocessed Entity |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

