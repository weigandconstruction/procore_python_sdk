# procore_sdk.ProjectManagementBiddingCompanyBidFormsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_bid_bid_id_bid_forms_bid_form_id_get**](ProjectManagementBiddingCompanyBidFormsApi.md#rest_v10_companies_company_id_bid_bid_id_bid_forms_bid_form_id_get) | **GET** /rest/v1.0/companies/{company_id}/bid/{bid_id}/bid_forms/{bid_form_id} | View Bid Form


# **rest_v10_companies_company_id_bid_bid_id_bid_forms_bid_form_id_get**
> RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGet200Response rest_v10_companies_company_id_bid_bid_id_bid_forms_bid_form_id_get(procore_company_id, company_id, bid_id, bid_form_id)

View Bid Form

View single Bid Form.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_bid_bid_id_bid_forms_bid_form_id_get200_response import RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGet200Response
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
    api_instance = procore_sdk.ProjectManagementBiddingCompanyBidFormsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    bid_id = 56 # int | Bid ID
    bid_form_id = 56 # int | Bid Form ID

    try:
        # View Bid Form
        api_response = api_instance.rest_v10_companies_company_id_bid_bid_id_bid_forms_bid_form_id_get(procore_company_id, company_id, bid_id, bid_form_id)
        print("The response of ProjectManagementBiddingCompanyBidFormsApi->rest_v10_companies_company_id_bid_bid_id_bid_forms_bid_form_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementBiddingCompanyBidFormsApi->rest_v10_companies_company_id_bid_bid_id_bid_forms_bid_form_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **bid_id** | **int**| Bid ID | 
 **bid_form_id** | **int**| Bid Form ID | 

### Return type

[**RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGet200Response**](RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | User does not have right permissions |  -  |
**404** | Cannot find bid form |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

