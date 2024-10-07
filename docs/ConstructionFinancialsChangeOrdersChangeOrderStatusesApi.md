# procore_sdk.ConstructionFinancialsChangeOrdersChangeOrderStatusesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_change_order_statuses_get**](ConstructionFinancialsChangeOrdersChangeOrderStatusesApi.md#rest_v10_change_order_statuses_get) | **GET** /rest/v1.0/change_order/statuses | List Change Order Statuses


# **rest_v10_change_order_statuses_get**
> List[RestV10ChangeOrderStatusesGet200ResponseInner] rest_v10_change_order_statuses_get(procore_company_id, company_id, page=page, per_page=per_page)

List Change Order Statuses

Return a list of all Change Order Statuses.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_change_order_statuses_get200_response_inner import RestV10ChangeOrderStatusesGet200ResponseInner
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
    api_instance = procore_sdk.ConstructionFinancialsChangeOrdersChangeOrderStatusesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Change Order Statuses
        api_response = api_instance.rest_v10_change_order_statuses_get(procore_company_id, company_id, page=page, per_page=per_page)
        print("The response of ConstructionFinancialsChangeOrdersChangeOrderStatusesApi->rest_v10_change_order_statuses_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsChangeOrdersChangeOrderStatusesApi->rest_v10_change_order_statuses_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[RestV10ChangeOrderStatusesGet200ResponseInner]**](RestV10ChangeOrderStatusesGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Per-Page - Number of items retrieved per page <br>  * Total - Total number of items to be retrieved <br>  * Link - Link headers for the first, prev, next, and last link <br>  |
**403** | User does not have permission to access Change Order Statuses. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

