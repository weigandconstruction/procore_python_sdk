# procore_sdk.UtilitiesWebhooksWebhookResourcesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_webhooks_resources_api_versions_get**](UtilitiesWebhooksWebhookResourcesApi.md#rest_v10_webhooks_resources_api_versions_get) | **GET** /rest/v1.0/webhooks/resources/api_versions | List Webhooks Resources API Versions
[**rest_v10_webhooks_resources_get**](UtilitiesWebhooksWebhookResourcesApi.md#rest_v10_webhooks_resources_get) | **GET** /rest/v1.0/webhooks/resources | List Webhooks Resources


# **rest_v10_webhooks_resources_api_versions_get**
> List[str] rest_v10_webhooks_resources_api_versions_get(procore_company_id, project_id)

List Webhooks Resources API Versions

Returns the list of Webhook Resources API Versions for the given scope.

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
    api_instance = procore_sdk.UtilitiesWebhooksWebhookResourcesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project. You must supply either a company_id or project_id.

    try:
        # List Webhooks Resources API Versions
        api_response = api_instance.rest_v10_webhooks_resources_api_versions_get(procore_company_id, project_id)
        print("The response of UtilitiesWebhooksWebhookResourcesApi->rest_v10_webhooks_resources_api_versions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UtilitiesWebhooksWebhookResourcesApi->rest_v10_webhooks_resources_api_versions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. You must supply either a company_id or project_id. | 

### Return type

**List[str]**

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

# **rest_v10_webhooks_resources_get**
> List[WebhooksResource] rest_v10_webhooks_resources_get(procore_company_id, project_id)

List Webhooks Resources

Returns the list of Webhook Resources for the given scope.

### Example


```python
import procore_sdk
from procore_sdk.models.webhooks_resource import WebhooksResource
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
    api_instance = procore_sdk.UtilitiesWebhooksWebhookResourcesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project. You must supply either a company_id or project_id.

    try:
        # List Webhooks Resources
        api_response = api_instance.rest_v10_webhooks_resources_get(procore_company_id, project_id)
        print("The response of UtilitiesWebhooksWebhookResourcesApi->rest_v10_webhooks_resources_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UtilitiesWebhooksWebhookResourcesApi->rest_v10_webhooks_resources_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. You must supply either a company_id or project_id. | 

### Return type

[**List[WebhooksResource]**](WebhooksResource.md)

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

