# procore_sdk.ProjectManagementBiddingBidContactsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_bid_contacts_get**](ProjectManagementBiddingBidContactsApi.md#rest_v10_projects_project_id_bid_contacts_get) | **GET** /rest/v1.0/projects/{project_id}/bid_contacts | List Bid Contacts


# **rest_v10_projects_project_id_bid_contacts_get**
> List[CompanyUser7] rest_v10_projects_project_id_bid_contacts_get(procore_company_id, project_id, page=page, per_page=per_page, filters_created_at=filters_created_at, filters_updated_at=filters_updated_at, filters_vendor_id=filters_vendor_id, filters_origin_id=filters_origin_id, filters_trade_id=filters_trade_id, filters_search=filters_search, sort=sort)

List Bid Contacts

Get a list of all the contacts of a company or contacts of a perticular vendor of the company (with vendor_id as a parameter).   See [Filtering on List Actions](https://developers.procore.com/documentation/filtering-on-list-actions) for information on using the filtering capabilities provided by this endpoint.

### Example


```python
import procore_sdk
from procore_sdk.models.company_user7 import CompanyUser7
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
    api_instance = procore_sdk.ProjectManagementBiddingBidContactsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_created_at = '2013-10-20' # date | Return item(s) created within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_vendor_id = [56] # List[int] | Return item(s) with the specified Vendor IDs. (optional)
    filters_origin_id = 'filters_origin_id_example' # str | Origin ID. Returns item(s) with the specified Origin ID. (optional)
    filters_trade_id = [56] # List[int] | Returns users whose vendor record is associated with the specified trade id(s). (optional)
    filters_search = 'filters_search_example' # str | Return users where the search string matches the user's first name, last name, email address, keywords, job title, or company name (optional)
    sort = 'sort_example' # str | Return items with the specified sort. (optional)

    try:
        # List Bid Contacts
        api_response = api_instance.rest_v10_projects_project_id_bid_contacts_get(procore_company_id, project_id, page=page, per_page=per_page, filters_created_at=filters_created_at, filters_updated_at=filters_updated_at, filters_vendor_id=filters_vendor_id, filters_origin_id=filters_origin_id, filters_trade_id=filters_trade_id, filters_search=filters_search, sort=sort)
        print("The response of ProjectManagementBiddingBidContactsApi->rest_v10_projects_project_id_bid_contacts_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementBiddingBidContactsApi->rest_v10_projects_project_id_bid_contacts_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_created_at** | **date**| Return item(s) created within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_vendor_id** | [**List[int]**](int.md)| Return item(s) with the specified Vendor IDs. | [optional] 
 **filters_origin_id** | **str**| Origin ID. Returns item(s) with the specified Origin ID. | [optional] 
 **filters_trade_id** | [**List[int]**](int.md)| Returns users whose vendor record is associated with the specified trade id(s). | [optional] 
 **filters_search** | **str**| Return users where the search string matches the user&#39;s first name, last name, email address, keywords, job title, or company name | [optional] 
 **sort** | **str**| Return items with the specified sort. | [optional] 

### Return type

[**List[CompanyUser7]**](CompanyUser7.md)

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

