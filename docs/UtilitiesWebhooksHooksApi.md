# procore_sdk.UtilitiesWebhooksHooksApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_webhooks_hooks_get**](UtilitiesWebhooksHooksApi.md#rest_v10_webhooks_hooks_get) | **GET** /rest/v1.0/webhooks/hooks | List Webhooks Hooks
[**rest_v10_webhooks_hooks_id_delete**](UtilitiesWebhooksHooksApi.md#rest_v10_webhooks_hooks_id_delete) | **DELETE** /rest/v1.0/webhooks/hooks/{id} | Delete Webhooks Hook
[**rest_v10_webhooks_hooks_id_patch**](UtilitiesWebhooksHooksApi.md#rest_v10_webhooks_hooks_id_patch) | **PATCH** /rest/v1.0/webhooks/hooks/{id} | Update Webhooks Hook
[**rest_v10_webhooks_hooks_post**](UtilitiesWebhooksHooksApi.md#rest_v10_webhooks_hooks_post) | **POST** /rest/v1.0/webhooks/hooks | Create Webhooks Hook


# **rest_v10_webhooks_hooks_get**
> List[WebhooksHook] rest_v10_webhooks_hooks_get(procore_company_id, company_id, project_id, namespace=namespace, api_version=api_version)

List Webhooks Hooks

Hooks must be listed within a company and/or project scope.

### Example


```python
import procore_sdk
from procore_sdk.models.webhooks_hook import WebhooksHook
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
    api_instance = procore_sdk.UtilitiesWebhooksHooksApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company. You must supply either a company_id or project_id.
    project_id = 56 # int | Unique identifier for the project. You must supply either a company_id or project_id.
    namespace = 'namespace_example' # str | Hook namespace to query. Use * to return hooks from all namespaces. (optional)
    api_version = 'api_version_example' # str | API Version (optional)

    try:
        # List Webhooks Hooks
        api_response = api_instance.rest_v10_webhooks_hooks_get(procore_company_id, company_id, project_id, namespace=namespace, api_version=api_version)
        print("The response of UtilitiesWebhooksHooksApi->rest_v10_webhooks_hooks_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UtilitiesWebhooksHooksApi->rest_v10_webhooks_hooks_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. You must supply either a company_id or project_id. | 
 **project_id** | **int**| Unique identifier for the project. You must supply either a company_id or project_id. | 
 **namespace** | **str**| Hook namespace to query. Use * to return hooks from all namespaces. | [optional] 
 **api_version** | **str**| API Version | [optional] 

### Return type

[**List[WebhooksHook]**](WebhooksHook.md)

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

# **rest_v10_webhooks_hooks_id_delete**
> rest_v10_webhooks_hooks_id_delete(procore_company_id, id, company_id, project_id)

Delete Webhooks Hook

Triggers must be deleted within a company and/or project scope.

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
    api_instance = procore_sdk.UtilitiesWebhooksHooksApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | Webhooks Hook ID
    company_id = 56 # int | Unique identifier for the company. You must supply either a company_id or project_id.
    project_id = 56 # int | Unique identifier for the project. You must supply either a company_id or project_id.

    try:
        # Delete Webhooks Hook
        api_instance.rest_v10_webhooks_hooks_id_delete(procore_company_id, id, company_id, project_id)
    except Exception as e:
        print("Exception when calling UtilitiesWebhooksHooksApi->rest_v10_webhooks_hooks_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| Webhooks Hook ID | 
 **company_id** | **int**| Unique identifier for the company. You must supply either a company_id or project_id. | 
 **project_id** | **int**| Unique identifier for the project. You must supply either a company_id or project_id. | 

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
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_webhooks_hooks_id_patch**
> WebhooksHook rest_v10_webhooks_hooks_id_patch(procore_company_id, id, rest_v10_webhooks_hooks_id_patch_request)

Update Webhooks Hook

Hooks must be updated within a company and/or project scope.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_webhooks_hooks_id_patch_request import RestV10WebhooksHooksIdPatchRequest
from procore_sdk.models.webhooks_hook import WebhooksHook
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
    api_instance = procore_sdk.UtilitiesWebhooksHooksApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | Webhooks Hook ID
    rest_v10_webhooks_hooks_id_patch_request = procore_sdk.RestV10WebhooksHooksIdPatchRequest() # RestV10WebhooksHooksIdPatchRequest | 

    try:
        # Update Webhooks Hook
        api_response = api_instance.rest_v10_webhooks_hooks_id_patch(procore_company_id, id, rest_v10_webhooks_hooks_id_patch_request)
        print("The response of UtilitiesWebhooksHooksApi->rest_v10_webhooks_hooks_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UtilitiesWebhooksHooksApi->rest_v10_webhooks_hooks_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| Webhooks Hook ID | 
 **rest_v10_webhooks_hooks_id_patch_request** | [**RestV10WebhooksHooksIdPatchRequest**](RestV10WebhooksHooksIdPatchRequest.md)|  | 

### Return type

[**WebhooksHook**](WebhooksHook.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Server Error |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_webhooks_hooks_post**
> WebhooksHook rest_v10_webhooks_hooks_post(procore_company_id, rest_v10_webhooks_hooks_post_request)

Create Webhooks Hook

Hooks must be created within a company and/or project scope.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_webhooks_hooks_post_request import RestV10WebhooksHooksPostRequest
from procore_sdk.models.webhooks_hook import WebhooksHook
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
    api_instance = procore_sdk.UtilitiesWebhooksHooksApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    rest_v10_webhooks_hooks_post_request = procore_sdk.RestV10WebhooksHooksPostRequest() # RestV10WebhooksHooksPostRequest | 

    try:
        # Create Webhooks Hook
        api_response = api_instance.rest_v10_webhooks_hooks_post(procore_company_id, rest_v10_webhooks_hooks_post_request)
        print("The response of UtilitiesWebhooksHooksApi->rest_v10_webhooks_hooks_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UtilitiesWebhooksHooksApi->rest_v10_webhooks_hooks_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **rest_v10_webhooks_hooks_post_request** | [**RestV10WebhooksHooksPostRequest**](RestV10WebhooksHooksPostRequest.md)|  | 

### Return type

[**WebhooksHook**](WebhooksHook.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**500** | Internal Server Error |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

