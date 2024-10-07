# procore_sdk.QualitySafetyIncidentsBodyPartsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_incidents_body_parts_get**](QualitySafetyIncidentsBodyPartsApi.md#rest_v10_companies_company_id_incidents_body_parts_get) | **GET** /rest/v1.0/companies/{company_id}/incidents/body_parts | List Body Parts


# **rest_v10_companies_company_id_incidents_body_parts_get**
> List[BodyPart] rest_v10_companies_company_id_incidents_body_parts_get(procore_company_id, company_id, page=page, per_page=per_page, filters_selectable=filters_selectable, filters_id=filters_id, filters_updated_at=filters_updated_at, sort=sort)

List Body Parts

Return a list of all supported Body Parts.

### Example


```python
import procore_sdk
from procore_sdk.models.body_part import BodyPart
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
    api_instance = procore_sdk.QualitySafetyIncidentsBodyPartsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_selectable = True # bool | If true, return item(s) with 'selectable' status. (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    sort = 'sort_example' # str | Body Parts (optional)

    try:
        # List Body Parts
        api_response = api_instance.rest_v10_companies_company_id_incidents_body_parts_get(procore_company_id, company_id, page=page, per_page=per_page, filters_selectable=filters_selectable, filters_id=filters_id, filters_updated_at=filters_updated_at, sort=sort)
        print("The response of QualitySafetyIncidentsBodyPartsApi->rest_v10_companies_company_id_incidents_body_parts_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsBodyPartsApi->rest_v10_companies_company_id_incidents_body_parts_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_selectable** | **bool**| If true, return item(s) with &#39;selectable&#39; status. | [optional] 
 **filters_id** | [**List[int]**](int.md)| Return item(s) with the specified IDs. | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **sort** | **str**| Body Parts | [optional] 

### Return type

[**List[BodyPart]**](BodyPart.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

