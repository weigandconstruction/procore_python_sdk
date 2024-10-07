# procore_sdk.UtilitiesWebhooksTriggersApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_webhooks_hooks_hook_id_triggers_bulk_delete**](UtilitiesWebhooksTriggersApi.md#rest_v10_webhooks_hooks_hook_id_triggers_bulk_delete) | **DELETE** /rest/v1.0/webhooks/hooks/{hook_id}/triggers/bulk | Bulk Delete Triggers
[**rest_v10_webhooks_hooks_hook_id_triggers_bulk_post**](UtilitiesWebhooksTriggersApi.md#rest_v10_webhooks_hooks_hook_id_triggers_bulk_post) | **POST** /rest/v1.0/webhooks/hooks/{hook_id}/triggers/bulk | Bulk Create Triggers
[**rest_v10_webhooks_hooks_hook_id_triggers_get**](UtilitiesWebhooksTriggersApi.md#rest_v10_webhooks_hooks_hook_id_triggers_get) | **GET** /rest/v1.0/webhooks/hooks/{hook_id}/triggers | List Webhooks Triggers
[**rest_v10_webhooks_hooks_hook_id_triggers_id_delete**](UtilitiesWebhooksTriggersApi.md#rest_v10_webhooks_hooks_hook_id_triggers_id_delete) | **DELETE** /rest/v1.0/webhooks/hooks/{hook_id}/triggers/{id} | Delete Webhooks Trigger
[**rest_v10_webhooks_hooks_hook_id_triggers_post**](UtilitiesWebhooksTriggersApi.md#rest_v10_webhooks_hooks_hook_id_triggers_post) | **POST** /rest/v1.0/webhooks/hooks/{hook_id}/triggers | Create Webhooks Trigger


# **rest_v10_webhooks_hooks_hook_id_triggers_bulk_delete**
> RestV10WebhooksHooksHookIdTriggersBulkDelete200Response rest_v10_webhooks_hooks_hook_id_triggers_bulk_delete(procore_company_id, hook_id, rest_v10_webhooks_hooks_hook_id_triggers_bulk_delete_request)

Bulk Delete Triggers

Delete multiple webhook triggers in a single request. All triggers must be within the same hook, and provide company and/or project scope. Max 500 triggers.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_webhooks_hooks_hook_id_triggers_bulk_delete200_response import RestV10WebhooksHooksHookIdTriggersBulkDelete200Response
from procore_sdk.models.rest_v10_webhooks_hooks_hook_id_triggers_bulk_delete_request import RestV10WebhooksHooksHookIdTriggersBulkDeleteRequest
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
    api_instance = procore_sdk.UtilitiesWebhooksTriggersApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    hook_id = 56 # int | Webhooks Hook ID
    rest_v10_webhooks_hooks_hook_id_triggers_bulk_delete_request = procore_sdk.RestV10WebhooksHooksHookIdTriggersBulkDeleteRequest() # RestV10WebhooksHooksHookIdTriggersBulkDeleteRequest | 

    try:
        # Bulk Delete Triggers
        api_response = api_instance.rest_v10_webhooks_hooks_hook_id_triggers_bulk_delete(procore_company_id, hook_id, rest_v10_webhooks_hooks_hook_id_triggers_bulk_delete_request)
        print("The response of UtilitiesWebhooksTriggersApi->rest_v10_webhooks_hooks_hook_id_triggers_bulk_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UtilitiesWebhooksTriggersApi->rest_v10_webhooks_hooks_hook_id_triggers_bulk_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **hook_id** | **int**| Webhooks Hook ID | 
 **rest_v10_webhooks_hooks_hook_id_triggers_bulk_delete_request** | [**RestV10WebhooksHooksHookIdTriggersBulkDeleteRequest**](RestV10WebhooksHooksHookIdTriggersBulkDeleteRequest.md)|  | 

### Return type

[**RestV10WebhooksHooksHookIdTriggersBulkDelete200Response**](RestV10WebhooksHooksHookIdTriggersBulkDelete200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**207** | Multi-Status |  -  |
**403** | Forbidden |  -  |
**413** | Payload Too Large |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_webhooks_hooks_hook_id_triggers_bulk_post**
> RestV10WebhooksHooksHookIdTriggersBulkPost200Response rest_v10_webhooks_hooks_hook_id_triggers_bulk_post(procore_company_id, hook_id, rest_v10_webhooks_hooks_hook_id_triggers_bulk_post_request)

Bulk Create Triggers

Create multiple webhook triggers in a single request. All triggers must be within the same hook, and provide company and/or project scope. Max 500 triggers.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_webhooks_hooks_hook_id_triggers_bulk_post200_response import RestV10WebhooksHooksHookIdTriggersBulkPost200Response
from procore_sdk.models.rest_v10_webhooks_hooks_hook_id_triggers_bulk_post_request import RestV10WebhooksHooksHookIdTriggersBulkPostRequest
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
    api_instance = procore_sdk.UtilitiesWebhooksTriggersApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    hook_id = 56 # int | Webhooks Hook ID
    rest_v10_webhooks_hooks_hook_id_triggers_bulk_post_request = procore_sdk.RestV10WebhooksHooksHookIdTriggersBulkPostRequest() # RestV10WebhooksHooksHookIdTriggersBulkPostRequest | 

    try:
        # Bulk Create Triggers
        api_response = api_instance.rest_v10_webhooks_hooks_hook_id_triggers_bulk_post(procore_company_id, hook_id, rest_v10_webhooks_hooks_hook_id_triggers_bulk_post_request)
        print("The response of UtilitiesWebhooksTriggersApi->rest_v10_webhooks_hooks_hook_id_triggers_bulk_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UtilitiesWebhooksTriggersApi->rest_v10_webhooks_hooks_hook_id_triggers_bulk_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **hook_id** | **int**| Webhooks Hook ID | 
 **rest_v10_webhooks_hooks_hook_id_triggers_bulk_post_request** | [**RestV10WebhooksHooksHookIdTriggersBulkPostRequest**](RestV10WebhooksHooksHookIdTriggersBulkPostRequest.md)|  | 

### Return type

[**RestV10WebhooksHooksHookIdTriggersBulkPost200Response**](RestV10WebhooksHooksHookIdTriggersBulkPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**207** | Multi-Status |  -  |
**403** | Forbidden |  -  |
**413** | Payload Too Large |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_webhooks_hooks_hook_id_triggers_get**
> List[WebhooksTrigger] rest_v10_webhooks_hooks_hook_id_triggers_get(procore_company_id, hook_id, company_id, project_id)

List Webhooks Triggers

Triggers must be listed within a company and/or project scope.

### Example


```python
import procore_sdk
from procore_sdk.models.webhooks_trigger import WebhooksTrigger
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
    api_instance = procore_sdk.UtilitiesWebhooksTriggersApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    hook_id = 56 # int | Webhooks Hook ID
    company_id = 56 # int | Unique identifier for the company. You must supply either a company_id or project_id.
    project_id = 56 # int | Unique identifier for the project. You must supply either a company_id or project_id.

    try:
        # List Webhooks Triggers
        api_response = api_instance.rest_v10_webhooks_hooks_hook_id_triggers_get(procore_company_id, hook_id, company_id, project_id)
        print("The response of UtilitiesWebhooksTriggersApi->rest_v10_webhooks_hooks_hook_id_triggers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UtilitiesWebhooksTriggersApi->rest_v10_webhooks_hooks_hook_id_triggers_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **hook_id** | **int**| Webhooks Hook ID | 
 **company_id** | **int**| Unique identifier for the company. You must supply either a company_id or project_id. | 
 **project_id** | **int**| Unique identifier for the project. You must supply either a company_id or project_id. | 

### Return type

[**List[WebhooksTrigger]**](WebhooksTrigger.md)

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

# **rest_v10_webhooks_hooks_hook_id_triggers_id_delete**
> rest_v10_webhooks_hooks_hook_id_triggers_id_delete(procore_company_id, hook_id, id, company_id, project_id)

Delete Webhooks Trigger

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
    api_instance = procore_sdk.UtilitiesWebhooksTriggersApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    hook_id = 56 # int | Webhooks Hook ID
    id = 56 # int | Webhooks Trigger ID
    company_id = 56 # int | Unique identifier for the company. You must supply either a company_id or project_id.
    project_id = 56 # int | Unique identifier for the project. You must supply either a company_id or project_id.

    try:
        # Delete Webhooks Trigger
        api_instance.rest_v10_webhooks_hooks_hook_id_triggers_id_delete(procore_company_id, hook_id, id, company_id, project_id)
    except Exception as e:
        print("Exception when calling UtilitiesWebhooksTriggersApi->rest_v10_webhooks_hooks_hook_id_triggers_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **hook_id** | **int**| Webhooks Hook ID | 
 **id** | **int**| Webhooks Trigger ID | 
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

# **rest_v10_webhooks_hooks_hook_id_triggers_post**
> WebhooksTrigger rest_v10_webhooks_hooks_hook_id_triggers_post(procore_company_id, hook_id, rest_v10_webhooks_hooks_hook_id_triggers_post_request)

Create Webhooks Trigger

Triggers must be created within a company and/or project scope.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_webhooks_hooks_hook_id_triggers_post_request import RestV10WebhooksHooksHookIdTriggersPostRequest
from procore_sdk.models.webhooks_trigger import WebhooksTrigger
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
    api_instance = procore_sdk.UtilitiesWebhooksTriggersApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    hook_id = 56 # int | Webhooks Hook ID
    rest_v10_webhooks_hooks_hook_id_triggers_post_request = procore_sdk.RestV10WebhooksHooksHookIdTriggersPostRequest() # RestV10WebhooksHooksHookIdTriggersPostRequest | 

    try:
        # Create Webhooks Trigger
        api_response = api_instance.rest_v10_webhooks_hooks_hook_id_triggers_post(procore_company_id, hook_id, rest_v10_webhooks_hooks_hook_id_triggers_post_request)
        print("The response of UtilitiesWebhooksTriggersApi->rest_v10_webhooks_hooks_hook_id_triggers_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UtilitiesWebhooksTriggersApi->rest_v10_webhooks_hooks_hook_id_triggers_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **hook_id** | **int**| Webhooks Hook ID | 
 **rest_v10_webhooks_hooks_hook_id_triggers_post_request** | [**RestV10WebhooksHooksHookIdTriggersPostRequest**](RestV10WebhooksHooksHookIdTriggersPostRequest.md)|  | 

### Return type

[**WebhooksTrigger**](WebhooksTrigger.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

