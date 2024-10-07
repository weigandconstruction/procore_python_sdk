# procore_sdk.QualitySafetyInspectionsItemResponseSetResponsesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_checklist_item_response_sets_response_set_id_responses_get**](QualitySafetyInspectionsItemResponseSetResponsesApi.md#rest_v10_companies_company_id_checklist_item_response_sets_response_set_id_responses_get) | **GET** /rest/v1.0/companies/{company_id}/checklist/item/response_sets/{response_set_id}/responses | List Responses in the Specified Item Response Set
[**rest_v10_companies_company_id_checklist_item_response_sets_response_set_id_responses_id_delete**](QualitySafetyInspectionsItemResponseSetResponsesApi.md#rest_v10_companies_company_id_checklist_item_response_sets_response_set_id_responses_id_delete) | **DELETE** /rest/v1.0/companies/{company_id}/checklist/item/response_sets/{response_set_id}/responses/{id} | Remove a Response from an Item Response Set
[**rest_v10_companies_company_id_checklist_item_response_sets_response_set_id_responses_id_get**](QualitySafetyInspectionsItemResponseSetResponsesApi.md#rest_v10_companies_company_id_checklist_item_response_sets_response_set_id_responses_id_get) | **GET** /rest/v1.0/companies/{company_id}/checklist/item/response_sets/{response_set_id}/responses/{id} | Show Item Response Set Response
[**rest_v10_companies_company_id_checklist_item_response_sets_response_set_id_responses_id_patch**](QualitySafetyInspectionsItemResponseSetResponsesApi.md#rest_v10_companies_company_id_checklist_item_response_sets_response_set_id_responses_id_patch) | **PATCH** /rest/v1.0/companies/{company_id}/checklist/item/response_sets/{response_set_id}/responses/{id} | Add an existing Response to an Item Response Set
[**rest_v10_companies_company_id_checklist_item_response_sets_response_set_id_responses_post**](QualitySafetyInspectionsItemResponseSetResponsesApi.md#rest_v10_companies_company_id_checklist_item_response_sets_response_set_id_responses_post) | **POST** /rest/v1.0/companies/{company_id}/checklist/item/response_sets/{response_set_id}/responses | Create a Response in the Specified Item Response Set


# **rest_v10_companies_company_id_checklist_item_response_sets_response_set_id_responses_get**
> List[ChecklistResponse] rest_v10_companies_company_id_checklist_item_response_sets_response_set_id_responses_get(procore_company_id, company_id, response_set_id, filters_corresponding_status=filters_corresponding_status, sort=sort)

List Responses in the Specified Item Response Set

List Responses for an Item Response Set.

### Example


```python
import procore_sdk
from procore_sdk.models.checklist_response import ChecklistResponse
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
    api_instance = procore_sdk.QualitySafetyInspectionsItemResponseSetResponsesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    response_set_id = 56 # int | The ID of the Response Set
    filters_corresponding_status = ['filters_corresponding_status_example'] # List[str] | Array of Corresponding Statuses. Return item(s) with the specified Corresponding Statuses - 'yes', 'no', or 'n/a'. (optional)
    sort = 'sort_example' # str |  (optional)

    try:
        # List Responses in the Specified Item Response Set
        api_response = api_instance.rest_v10_companies_company_id_checklist_item_response_sets_response_set_id_responses_get(procore_company_id, company_id, response_set_id, filters_corresponding_status=filters_corresponding_status, sort=sort)
        print("The response of QualitySafetyInspectionsItemResponseSetResponsesApi->rest_v10_companies_company_id_checklist_item_response_sets_response_set_id_responses_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsItemResponseSetResponsesApi->rest_v10_companies_company_id_checklist_item_response_sets_response_set_id_responses_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **response_set_id** | **int**| The ID of the Response Set | 
 **filters_corresponding_status** | [**List[str]**](str.md)| Array of Corresponding Statuses. Return item(s) with the specified Corresponding Statuses - &#39;yes&#39;, &#39;no&#39;, or &#39;n/a&#39;. | [optional] 
 **sort** | **str**|  | [optional] 

### Return type

[**List[ChecklistResponse]**](ChecklistResponse.md)

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_checklist_item_response_sets_response_set_id_responses_id_delete**
> rest_v10_companies_company_id_checklist_item_response_sets_response_set_id_responses_id_delete(procore_company_id, company_id, response_set_id, id)

Remove a Response from an Item Response Set

Remove a Response from an Item Response Set.

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
    api_instance = procore_sdk.QualitySafetyInspectionsItemResponseSetResponsesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    response_set_id = 56 # int | Checklist Item Response Set ID
    id = 56 # int | The ID of the Response

    try:
        # Remove a Response from an Item Response Set
        api_instance.rest_v10_companies_company_id_checklist_item_response_sets_response_set_id_responses_id_delete(procore_company_id, company_id, response_set_id, id)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsItemResponseSetResponsesApi->rest_v10_companies_company_id_checklist_item_response_sets_response_set_id_responses_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **response_set_id** | **int**| Checklist Item Response Set ID | 
 **id** | **int**| The ID of the Response | 

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
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_checklist_item_response_sets_response_set_id_responses_id_get**
> ChecklistResponse rest_v10_companies_company_id_checklist_item_response_sets_response_set_id_responses_id_get(procore_company_id, company_id, response_set_id, id)

Show Item Response Set Response

Returns a specified Response from the Item Response Set.

### Example


```python
import procore_sdk
from procore_sdk.models.checklist_response import ChecklistResponse
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
    api_instance = procore_sdk.QualitySafetyInspectionsItemResponseSetResponsesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    response_set_id = 56 # int | Checklist Item Response Set ID
    id = 56 # int | The ID of the Response

    try:
        # Show Item Response Set Response
        api_response = api_instance.rest_v10_companies_company_id_checklist_item_response_sets_response_set_id_responses_id_get(procore_company_id, company_id, response_set_id, id)
        print("The response of QualitySafetyInspectionsItemResponseSetResponsesApi->rest_v10_companies_company_id_checklist_item_response_sets_response_set_id_responses_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsItemResponseSetResponsesApi->rest_v10_companies_company_id_checklist_item_response_sets_response_set_id_responses_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **response_set_id** | **int**| Checklist Item Response Set ID | 
 **id** | **int**| The ID of the Response | 

### Return type

[**ChecklistResponse**](ChecklistResponse.md)

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_checklist_item_response_sets_response_set_id_responses_id_patch**
> ChecklistResponse rest_v10_companies_company_id_checklist_item_response_sets_response_set_id_responses_id_patch(procore_company_id, company_id, response_set_id, id)

Add an existing Response to an Item Response Set

Adds an existing Response to the specified Item Response Set.

### Example


```python
import procore_sdk
from procore_sdk.models.checklist_response import ChecklistResponse
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
    api_instance = procore_sdk.QualitySafetyInspectionsItemResponseSetResponsesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    response_set_id = 56 # int | Checklist Item Response Set ID
    id = 56 # int | The ID of the Response

    try:
        # Add an existing Response to an Item Response Set
        api_response = api_instance.rest_v10_companies_company_id_checklist_item_response_sets_response_set_id_responses_id_patch(procore_company_id, company_id, response_set_id, id)
        print("The response of QualitySafetyInspectionsItemResponseSetResponsesApi->rest_v10_companies_company_id_checklist_item_response_sets_response_set_id_responses_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsItemResponseSetResponsesApi->rest_v10_companies_company_id_checklist_item_response_sets_response_set_id_responses_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **response_set_id** | **int**| Checklist Item Response Set ID | 
 **id** | **int**| The ID of the Response | 

### Return type

[**ChecklistResponse**](ChecklistResponse.md)

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_checklist_item_response_sets_response_set_id_responses_post**
> ChecklistResponse rest_v10_companies_company_id_checklist_item_response_sets_response_set_id_responses_post(procore_company_id, company_id, response_set_id, checklist_response_body2)

Create a Response in the Specified Item Response Set

Creates a Response for a specified Item Response Set.

### Example


```python
import procore_sdk
from procore_sdk.models.checklist_response import ChecklistResponse
from procore_sdk.models.checklist_response_body2 import ChecklistResponseBody2
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
    api_instance = procore_sdk.QualitySafetyInspectionsItemResponseSetResponsesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    response_set_id = 56 # int | The ID of the Response Set
    checklist_response_body2 = procore_sdk.ChecklistResponseBody2() # ChecklistResponseBody2 | 

    try:
        # Create a Response in the Specified Item Response Set
        api_response = api_instance.rest_v10_companies_company_id_checklist_item_response_sets_response_set_id_responses_post(procore_company_id, company_id, response_set_id, checklist_response_body2)
        print("The response of QualitySafetyInspectionsItemResponseSetResponsesApi->rest_v10_companies_company_id_checklist_item_response_sets_response_set_id_responses_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsItemResponseSetResponsesApi->rest_v10_companies_company_id_checklist_item_response_sets_response_set_id_responses_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **response_set_id** | **int**| The ID of the Response Set | 
 **checklist_response_body2** | [**ChecklistResponseBody2**](ChecklistResponseBody2.md)|  | 

### Return type

[**ChecklistResponse**](ChecklistResponse.md)

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
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

