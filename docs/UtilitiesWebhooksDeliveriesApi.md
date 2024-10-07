# procore_sdk.UtilitiesWebhooksDeliveriesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_webhooks_hooks_hook_id_deliveries_get**](UtilitiesWebhooksDeliveriesApi.md#rest_v10_webhooks_hooks_hook_id_deliveries_get) | **GET** /rest/v1.0/webhooks/hooks/{hook_id}/deliveries | List Webhooks Deliveries


# **rest_v10_webhooks_hooks_hook_id_deliveries_get**
> List[WebhooksDelivery] rest_v10_webhooks_hooks_hook_id_deliveries_get(procore_company_id, hook_id, company_id, project_id, page_size=page_size, page_start=page_start, filters_status=filters_status)

List Webhooks Deliveries

Deliveries must be listed within a company and/or project scope.

### Example


```python
import procore_sdk
from procore_sdk.models.webhooks_delivery import WebhooksDelivery
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
    api_instance = procore_sdk.UtilitiesWebhooksDeliveriesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    hook_id = 56 # int | Webhooks Hook ID
    company_id = 56 # int | Unique identifier for the company. You must supply either a company_id or project_id.
    project_id = 56 # int | Unique identifier for the project. You must supply either a company_id or project_id.
    page_size = 56 # int | Number of items to return for a page (default: 100) (optional)
    page_start = 56 # int | The last id of the previous page. (optional)
    filters_status = 'filters_status_example' # str | Filter on status for \"any\", \"successful\", \"failing\" or \"discarded\" (optional)

    try:
        # List Webhooks Deliveries
        api_response = api_instance.rest_v10_webhooks_hooks_hook_id_deliveries_get(procore_company_id, hook_id, company_id, project_id, page_size=page_size, page_start=page_start, filters_status=filters_status)
        print("The response of UtilitiesWebhooksDeliveriesApi->rest_v10_webhooks_hooks_hook_id_deliveries_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UtilitiesWebhooksDeliveriesApi->rest_v10_webhooks_hooks_hook_id_deliveries_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **hook_id** | **int**| Webhooks Hook ID | 
 **company_id** | **int**| Unique identifier for the company. You must supply either a company_id or project_id. | 
 **project_id** | **int**| Unique identifier for the project. You must supply either a company_id or project_id. | 
 **page_size** | **int**| Number of items to return for a page (default: 100) | [optional] 
 **page_start** | **int**| The last id of the previous page. | [optional] 
 **filters_status** | **str**| Filter on status for \&quot;any\&quot;, \&quot;successful\&quot;, \&quot;failing\&quot; or \&quot;discarded\&quot; | [optional] 

### Return type

[**List[WebhooksDelivery]**](WebhooksDelivery.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

