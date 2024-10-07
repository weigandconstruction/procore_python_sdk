# procore_sdk.ProjectManagementBiddingBidUploadsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_bids_bid_id_uploads_get**](ProjectManagementBiddingBidUploadsApi.md#rest_v10_companies_company_id_bids_bid_id_uploads_get) | **GET** /rest/v1.0/companies/{company_id}/bids/{bid_id}/uploads | List Bid Uploads


# **rest_v10_companies_company_id_bids_bid_id_uploads_get**
> List[RestV10CompaniesCompanyIdBidsBidIdUploadsGet200ResponseInner] rest_v10_companies_company_id_bids_bid_id_uploads_get(procore_company_id, company_id, bid_id)

List Bid Uploads

Fetches a list of Bid Uploads for a Bid

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_bids_bid_id_uploads_get200_response_inner import RestV10CompaniesCompanyIdBidsBidIdUploadsGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementBiddingBidUploadsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    bid_id = 56 # int | Bid ID

    try:
        # List Bid Uploads
        api_response = api_instance.rest_v10_companies_company_id_bids_bid_id_uploads_get(procore_company_id, company_id, bid_id)
        print("The response of ProjectManagementBiddingBidUploadsApi->rest_v10_companies_company_id_bids_bid_id_uploads_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementBiddingBidUploadsApi->rest_v10_companies_company_id_bids_bid_id_uploads_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **bid_id** | **int**| Bid ID | 

### Return type

[**List[RestV10CompaniesCompanyIdBidsBidIdUploadsGet200ResponseInner]**](RestV10CompaniesCompanyIdBidsBidIdUploadsGet200ResponseInner.md)

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
**403** | User does not have right permissions |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

