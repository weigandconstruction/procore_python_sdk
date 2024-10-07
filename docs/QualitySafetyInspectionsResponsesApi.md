# procore_sdk.QualitySafetyInspectionsResponsesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_checklist_responses_get**](QualitySafetyInspectionsResponsesApi.md#rest_v10_companies_company_id_checklist_responses_get) | **GET** /rest/v1.0/companies/{company_id}/checklist/responses | List Responses
[**rest_v10_companies_company_id_checklist_responses_id_delete**](QualitySafetyInspectionsResponsesApi.md#rest_v10_companies_company_id_checklist_responses_id_delete) | **DELETE** /rest/v1.0/companies/{company_id}/checklist/responses/{id} | Delete a Response
[**rest_v10_companies_company_id_checklist_responses_id_get**](QualitySafetyInspectionsResponsesApi.md#rest_v10_companies_company_id_checklist_responses_id_get) | **GET** /rest/v1.0/companies/{company_id}/checklist/responses/{id} | Show Response
[**rest_v10_companies_company_id_checklist_responses_id_patch**](QualitySafetyInspectionsResponsesApi.md#rest_v10_companies_company_id_checklist_responses_id_patch) | **PATCH** /rest/v1.0/companies/{company_id}/checklist/responses/{id} | Update a Response
[**rest_v10_companies_company_id_checklist_responses_post**](QualitySafetyInspectionsResponsesApi.md#rest_v10_companies_company_id_checklist_responses_post) | **POST** /rest/v1.0/companies/{company_id}/checklist/responses | Create a Response


# **rest_v10_companies_company_id_checklist_responses_get**
> List[ChecklistResponse] rest_v10_companies_company_id_checklist_responses_get(procore_company_id, company_id, filters_corresponding_status=filters_corresponding_status, sort=sort)

List Responses

List Responses for a Company

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
    api_instance = procore_sdk.QualitySafetyInspectionsResponsesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    filters_corresponding_status = ['filters_corresponding_status_example'] # List[str] | Array of Corresponding Statuses. Return item(s) with the specified Corresponding Statuses - 'yes', 'no', or 'n/a'. (optional)
    sort = 'sort_example' # str |  (optional)

    try:
        # List Responses
        api_response = api_instance.rest_v10_companies_company_id_checklist_responses_get(procore_company_id, company_id, filters_corresponding_status=filters_corresponding_status, sort=sort)
        print("The response of QualitySafetyInspectionsResponsesApi->rest_v10_companies_company_id_checklist_responses_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsResponsesApi->rest_v10_companies_company_id_checklist_responses_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_checklist_responses_id_delete**
> rest_v10_companies_company_id_checklist_responses_id_delete(procore_company_id, company_id, id)

Delete a Response

Deletes a Response

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
    api_instance = procore_sdk.QualitySafetyInspectionsResponsesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | The ID of the Response

    try:
        # Delete a Response
        api_instance.rest_v10_companies_company_id_checklist_responses_id_delete(procore_company_id, company_id, id)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsResponsesApi->rest_v10_companies_company_id_checklist_responses_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
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
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_checklist_responses_id_get**
> ChecklistResponse rest_v10_companies_company_id_checklist_responses_id_get(procore_company_id, company_id, id)

Show Response

Returns a specified Response

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
    api_instance = procore_sdk.QualitySafetyInspectionsResponsesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | The ID of the Response

    try:
        # Show Response
        api_response = api_instance.rest_v10_companies_company_id_checklist_responses_id_get(procore_company_id, company_id, id)
        print("The response of QualitySafetyInspectionsResponsesApi->rest_v10_companies_company_id_checklist_responses_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsResponsesApi->rest_v10_companies_company_id_checklist_responses_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_checklist_responses_id_patch**
> ChecklistResponse rest_v10_companies_company_id_checklist_responses_id_patch(procore_company_id, company_id, id, checklist_response_body1)

Update a Response

Update a Response

### Example


```python
import procore_sdk
from procore_sdk.models.checklist_response import ChecklistResponse
from procore_sdk.models.checklist_response_body1 import ChecklistResponseBody1
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
    api_instance = procore_sdk.QualitySafetyInspectionsResponsesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | The ID of the Response
    checklist_response_body1 = procore_sdk.ChecklistResponseBody1() # ChecklistResponseBody1 | 

    try:
        # Update a Response
        api_response = api_instance.rest_v10_companies_company_id_checklist_responses_id_patch(procore_company_id, company_id, id, checklist_response_body1)
        print("The response of QualitySafetyInspectionsResponsesApi->rest_v10_companies_company_id_checklist_responses_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsResponsesApi->rest_v10_companies_company_id_checklist_responses_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| The ID of the Response | 
 **checklist_response_body1** | [**ChecklistResponseBody1**](ChecklistResponseBody1.md)|  | 

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
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_checklist_responses_post**
> ChecklistResponse rest_v10_companies_company_id_checklist_responses_post(procore_company_id, company_id, checklist_response_body)

Create a Response

Creates a Response for a specified Company.

### Example


```python
import procore_sdk
from procore_sdk.models.checklist_response import ChecklistResponse
from procore_sdk.models.checklist_response_body import ChecklistResponseBody
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
    api_instance = procore_sdk.QualitySafetyInspectionsResponsesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    checklist_response_body = procore_sdk.ChecklistResponseBody() # ChecklistResponseBody | 

    try:
        # Create a Response
        api_response = api_instance.rest_v10_companies_company_id_checklist_responses_post(procore_company_id, company_id, checklist_response_body)
        print("The response of QualitySafetyInspectionsResponsesApi->rest_v10_companies_company_id_checklist_responses_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsResponsesApi->rest_v10_companies_company_id_checklist_responses_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **checklist_response_body** | [**ChecklistResponseBody**](ChecklistResponseBody.md)|  | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

