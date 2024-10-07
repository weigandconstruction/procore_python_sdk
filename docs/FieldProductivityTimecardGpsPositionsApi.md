# procore_sdk.FieldProductivityTimecardGpsPositionsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_gps_positions_get**](FieldProductivityTimecardGpsPositionsApi.md#rest_v10_companies_company_id_gps_positions_get) | **GET** /rest/v1.0/companies/{company_id}/gps_positions | List Gps Positions
[**rest_v10_companies_company_id_gps_positions_id_get**](FieldProductivityTimecardGpsPositionsApi.md#rest_v10_companies_company_id_gps_positions_id_get) | **GET** /rest/v1.0/companies/{company_id}/gps_positions/{id} | Show Gps Position
[**rest_v10_companies_company_id_gps_positions_post**](FieldProductivityTimecardGpsPositionsApi.md#rest_v10_companies_company_id_gps_positions_post) | **POST** /rest/v1.0/companies/{company_id}/gps_positions | Create Gps Position


# **rest_v10_companies_company_id_gps_positions_get**
> List[RestV10CompaniesCompanyIdGpsPositionsGet200ResponseInner] rest_v10_companies_company_id_gps_positions_get(procore_company_id, company_id, filters_id=filters_id, filters_created_by_id=filters_created_by_id, filters_updated_at=filters_updated_at, page=page, per_page=per_page)

List Gps Positions

Return a list of all Gps Positions.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_gps_positions_get200_response_inner import RestV10CompaniesCompanyIdGpsPositionsGet200ResponseInner
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
    api_instance = procore_sdk.FieldProductivityTimecardGpsPositionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_created_by_id = [56] # List[int] | Returns item(s) created by the specified User IDs. (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Gps Positions
        api_response = api_instance.rest_v10_companies_company_id_gps_positions_get(procore_company_id, company_id, filters_id=filters_id, filters_created_by_id=filters_created_by_id, filters_updated_at=filters_updated_at, page=page, per_page=per_page)
        print("The response of FieldProductivityTimecardGpsPositionsApi->rest_v10_companies_company_id_gps_positions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimecardGpsPositionsApi->rest_v10_companies_company_id_gps_positions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **filters_id** | [**List[int]**](int.md)| Return item(s) with the specified IDs. | [optional] 
 **filters_created_by_id** | [**List[int]**](int.md)| Returns item(s) created by the specified User IDs. | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[RestV10CompaniesCompanyIdGpsPositionsGet200ResponseInner]**](RestV10CompaniesCompanyIdGpsPositionsGet200ResponseInner.md)

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

# **rest_v10_companies_company_id_gps_positions_id_get**
> RestV10CompaniesCompanyIdGpsPositionsGet200ResponseInner rest_v10_companies_company_id_gps_positions_id_get(procore_company_id, id, company_id)

Show Gps Position

Return detailed information about a specific Gps Position.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_gps_positions_get200_response_inner import RestV10CompaniesCompanyIdGpsPositionsGet200ResponseInner
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
    api_instance = procore_sdk.FieldProductivityTimecardGpsPositionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the Gps Position
    company_id = 56 # int | Unique identifier for the company.

    try:
        # Show Gps Position
        api_response = api_instance.rest_v10_companies_company_id_gps_positions_id_get(procore_company_id, id, company_id)
        print("The response of FieldProductivityTimecardGpsPositionsApi->rest_v10_companies_company_id_gps_positions_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimecardGpsPositionsApi->rest_v10_companies_company_id_gps_positions_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the Gps Position | 
 **company_id** | **int**| Unique identifier for the company. | 

### Return type

[**RestV10CompaniesCompanyIdGpsPositionsGet200ResponseInner**](RestV10CompaniesCompanyIdGpsPositionsGet200ResponseInner.md)

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

# **rest_v10_companies_company_id_gps_positions_post**
> RestV10CompaniesCompanyIdGpsPositionsGet200ResponseInner rest_v10_companies_company_id_gps_positions_post(procore_company_id, company_id, rest_v10_companies_company_id_gps_positions_post_request)

Create Gps Position

Create a new Gps Position.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_gps_positions_get200_response_inner import RestV10CompaniesCompanyIdGpsPositionsGet200ResponseInner
from procore_sdk.models.rest_v10_companies_company_id_gps_positions_post_request import RestV10CompaniesCompanyIdGpsPositionsPostRequest
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
    api_instance = procore_sdk.FieldProductivityTimecardGpsPositionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    rest_v10_companies_company_id_gps_positions_post_request = procore_sdk.RestV10CompaniesCompanyIdGpsPositionsPostRequest() # RestV10CompaniesCompanyIdGpsPositionsPostRequest | 

    try:
        # Create Gps Position
        api_response = api_instance.rest_v10_companies_company_id_gps_positions_post(procore_company_id, company_id, rest_v10_companies_company_id_gps_positions_post_request)
        print("The response of FieldProductivityTimecardGpsPositionsApi->rest_v10_companies_company_id_gps_positions_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimecardGpsPositionsApi->rest_v10_companies_company_id_gps_positions_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **rest_v10_companies_company_id_gps_positions_post_request** | [**RestV10CompaniesCompanyIdGpsPositionsPostRequest**](RestV10CompaniesCompanyIdGpsPositionsPostRequest.md)|  | 

### Return type

[**RestV10CompaniesCompanyIdGpsPositionsGet200ResponseInner**](RestV10CompaniesCompanyIdGpsPositionsGet200ResponseInner.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

