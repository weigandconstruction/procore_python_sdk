# procore_sdk.QualitySafetyInspectionsChecklistSignatureRequestsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_checklist_lists_list_id_signature_requests_get**](QualitySafetyInspectionsChecklistSignatureRequestsApi.md#rest_v10_checklist_lists_list_id_signature_requests_get) | **GET** /rest/v1.0/checklist/lists/{list_id}/signature_requests | List Checklist Signature Requests
[**rest_v10_checklist_lists_list_id_signature_requests_id_delete**](QualitySafetyInspectionsChecklistSignatureRequestsApi.md#rest_v10_checklist_lists_list_id_signature_requests_id_delete) | **DELETE** /rest/v1.0/checklist/lists/{list_id}/signature_requests/{id} | Delete Checklist Signature Request
[**rest_v10_checklist_lists_list_id_signature_requests_id_get**](QualitySafetyInspectionsChecklistSignatureRequestsApi.md#rest_v10_checklist_lists_list_id_signature_requests_id_get) | **GET** /rest/v1.0/checklist/lists/{list_id}/signature_requests/{id} | Show Checklist Signature Request
[**rest_v10_checklist_lists_list_id_signature_requests_post**](QualitySafetyInspectionsChecklistSignatureRequestsApi.md#rest_v10_checklist_lists_list_id_signature_requests_post) | **POST** /rest/v1.0/checklist/lists/{list_id}/signature_requests | Create Checklist Signature Request
[**rest_v10_checklist_lists_list_id_signature_requests_signature_request_id_signature_delete**](QualitySafetyInspectionsChecklistSignatureRequestsApi.md#rest_v10_checklist_lists_list_id_signature_requests_signature_request_id_signature_delete) | **DELETE** /rest/v1.0/checklist/lists/{list_id}/signature_requests/{signature_request_id}/signature | Delete Checklist Signature
[**rest_v10_checklist_lists_list_id_signature_requests_signature_request_id_signature_post**](QualitySafetyInspectionsChecklistSignatureRequestsApi.md#rest_v10_checklist_lists_list_id_signature_requests_signature_request_id_signature_post) | **POST** /rest/v1.0/checklist/lists/{list_id}/signature_requests/{signature_request_id}/signature | Create Checklist Signature


# **rest_v10_checklist_lists_list_id_signature_requests_get**
> List[ChecklistSignatureRequest] rest_v10_checklist_lists_list_id_signature_requests_get(procore_company_id, list_id, project_id)

List Checklist Signature Requests

Lists Signature Requests for a specified Checklist

### Example


```python
import procore_sdk
from procore_sdk.models.checklist_signature_request import ChecklistSignatureRequest
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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistSignatureRequestsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    list_id = 56 # int | Checklist ID
    project_id = 56 # int | Unique identifier for the project.

    try:
        # List Checklist Signature Requests
        api_response = api_instance.rest_v10_checklist_lists_list_id_signature_requests_get(procore_company_id, list_id, project_id)
        print("The response of QualitySafetyInspectionsChecklistSignatureRequestsApi->rest_v10_checklist_lists_list_id_signature_requests_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistSignatureRequestsApi->rest_v10_checklist_lists_list_id_signature_requests_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **list_id** | **int**| Checklist ID | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**List[ChecklistSignatureRequest]**](ChecklistSignatureRequest.md)

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
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_checklist_lists_list_id_signature_requests_id_delete**
> rest_v10_checklist_lists_list_id_signature_requests_id_delete(procore_company_id, project_id, list_id, id)

Delete Checklist Signature Request

Deletes a Signature Request for a specified Checklist.

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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistSignatureRequestsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    list_id = 56 # int | Checklist ID
    id = 56 # int | Signature Request ID

    try:
        # Delete Checklist Signature Request
        api_instance.rest_v10_checklist_lists_list_id_signature_requests_id_delete(procore_company_id, project_id, list_id, id)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistSignatureRequestsApi->rest_v10_checklist_lists_list_id_signature_requests_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **list_id** | **int**| Checklist ID | 
 **id** | **int**| Signature Request ID | 

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Unprocessable Entity |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_checklist_lists_list_id_signature_requests_id_get**
> ChecklistSignatureRequest rest_v10_checklist_lists_list_id_signature_requests_id_get(procore_company_id, project_id, list_id, id)

Show Checklist Signature Request

Retrieves Signature Request for a specified Checklist.

### Example


```python
import procore_sdk
from procore_sdk.models.checklist_signature_request import ChecklistSignatureRequest
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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistSignatureRequestsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    list_id = 56 # int | Checklist ID
    id = 56 # int | Signature Request ID

    try:
        # Show Checklist Signature Request
        api_response = api_instance.rest_v10_checklist_lists_list_id_signature_requests_id_get(procore_company_id, project_id, list_id, id)
        print("The response of QualitySafetyInspectionsChecklistSignatureRequestsApi->rest_v10_checklist_lists_list_id_signature_requests_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistSignatureRequestsApi->rest_v10_checklist_lists_list_id_signature_requests_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **list_id** | **int**| Checklist ID | 
 **id** | **int**| Signature Request ID | 

### Return type

[**ChecklistSignatureRequest**](ChecklistSignatureRequest.md)

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
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_checklist_lists_list_id_signature_requests_post**
> ChecklistSignatureRequest rest_v10_checklist_lists_list_id_signature_requests_post(procore_company_id, list_id, project_id, checklist_signature_request_create_body)

Create Checklist Signature Request

Creates a Signature Request for a specified Checklist.

### Example


```python
import procore_sdk
from procore_sdk.models.checklist_signature_request import ChecklistSignatureRequest
from procore_sdk.models.checklist_signature_request_create_body import ChecklistSignatureRequestCreateBody
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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistSignatureRequestsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    list_id = 56 # int | Checklist ID
    project_id = 56 # int | Unique identifier for the project.
    checklist_signature_request_create_body = procore_sdk.ChecklistSignatureRequestCreateBody() # ChecklistSignatureRequestCreateBody | 

    try:
        # Create Checklist Signature Request
        api_response = api_instance.rest_v10_checklist_lists_list_id_signature_requests_post(procore_company_id, list_id, project_id, checklist_signature_request_create_body)
        print("The response of QualitySafetyInspectionsChecklistSignatureRequestsApi->rest_v10_checklist_lists_list_id_signature_requests_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistSignatureRequestsApi->rest_v10_checklist_lists_list_id_signature_requests_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **list_id** | **int**| Checklist ID | 
 **project_id** | **int**| Unique identifier for the project. | 
 **checklist_signature_request_create_body** | [**ChecklistSignatureRequestCreateBody**](ChecklistSignatureRequestCreateBody.md)|  | 

### Return type

[**ChecklistSignatureRequest**](ChecklistSignatureRequest.md)

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
**422** | Unprocessable Entity |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_checklist_lists_list_id_signature_requests_signature_request_id_signature_delete**
> rest_v10_checklist_lists_list_id_signature_requests_signature_request_id_signature_delete(procore_company_id, list_id, signature_request_id, project_id)

Delete Checklist Signature

Deletes a Signature for a specified Checklist Signature Request.

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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistSignatureRequestsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    list_id = 56 # int | Checklist ID
    signature_request_id = 56 # int | Checklist Signature Request ID
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Delete Checklist Signature
        api_instance.rest_v10_checklist_lists_list_id_signature_requests_signature_request_id_signature_delete(procore_company_id, list_id, signature_request_id, project_id)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistSignatureRequestsApi->rest_v10_checklist_lists_list_id_signature_requests_signature_request_id_signature_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **list_id** | **int**| Checklist ID | 
 **signature_request_id** | **int**| Checklist Signature Request ID | 
 **project_id** | **int**| Unique identifier for the project. | 

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_checklist_lists_list_id_signature_requests_signature_request_id_signature_post**
> ChecklistSignatureRequest rest_v10_checklist_lists_list_id_signature_requests_signature_request_id_signature_post(procore_company_id, list_id, signature_request_id, project_id, attachment, attachment_string=attachment_string)

Create Checklist Signature

Creates a Signature for a specified Checklist Signature Request.

### Example


```python
import procore_sdk
from procore_sdk.models.checklist_signature_request import ChecklistSignatureRequest
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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistSignatureRequestsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    list_id = 56 # int | Checklist ID
    signature_request_id = 56 # int | Checklist Signature Request ID
    project_id = 56 # int | Unique identifier for the project.
    attachment = None # bytearray | Attachment representing the Signature. To upload an attachment you must upload the entire payload as `multipart/form-data` content-type and specify each parameter as form-data together with the `signature` file.
    attachment_string = 'attachment_string_example' # str | Base64 encoded string representing PNG image of signature (optional)

    try:
        # Create Checklist Signature
        api_response = api_instance.rest_v10_checklist_lists_list_id_signature_requests_signature_request_id_signature_post(procore_company_id, list_id, signature_request_id, project_id, attachment, attachment_string=attachment_string)
        print("The response of QualitySafetyInspectionsChecklistSignatureRequestsApi->rest_v10_checklist_lists_list_id_signature_requests_signature_request_id_signature_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistSignatureRequestsApi->rest_v10_checklist_lists_list_id_signature_requests_signature_request_id_signature_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **list_id** | **int**| Checklist ID | 
 **signature_request_id** | **int**| Checklist Signature Request ID | 
 **project_id** | **int**| Unique identifier for the project. | 
 **attachment** | **bytearray**| Attachment representing the Signature. To upload an attachment you must upload the entire payload as &#x60;multipart/form-data&#x60; content-type and specify each parameter as form-data together with the &#x60;signature&#x60; file. | 
 **attachment_string** | **str**| Base64 encoded string representing PNG image of signature | [optional] 

### Return type

[**ChecklistSignatureRequest**](ChecklistSignatureRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Unprocessable Entity |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

