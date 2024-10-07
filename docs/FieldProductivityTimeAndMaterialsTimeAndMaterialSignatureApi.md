# procore_sdk.FieldProductivityTimeAndMaterialsTimeAndMaterialSignatureApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_time_and_material_entries_signatures_bulk_destroy_delete**](FieldProductivityTimeAndMaterialsTimeAndMaterialSignatureApi.md#rest_v10_projects_project_id_time_and_material_entries_signatures_bulk_destroy_delete) | **DELETE** /rest/v1.0/projects/{project_id}/time_and_material_entries/signatures/bulk_destroy | Delete Multiple Signatures
[**rest_v10_projects_project_id_time_and_material_entries_signatures_get**](FieldProductivityTimeAndMaterialsTimeAndMaterialSignatureApi.md#rest_v10_projects_project_id_time_and_material_entries_signatures_get) | **GET** /rest/v1.0/projects/{project_id}/time_and_material_entries/signatures | List Signatures
[**rest_v10_projects_project_id_time_and_material_entries_signatures_id_delete**](FieldProductivityTimeAndMaterialsTimeAndMaterialSignatureApi.md#rest_v10_projects_project_id_time_and_material_entries_signatures_id_delete) | **DELETE** /rest/v1.0/projects/{project_id}/time_and_material_entries/signatures/{id} | Delete Signature
[**rest_v10_projects_project_id_time_and_material_entries_signatures_id_get**](FieldProductivityTimeAndMaterialsTimeAndMaterialSignatureApi.md#rest_v10_projects_project_id_time_and_material_entries_signatures_id_get) | **GET** /rest/v1.0/projects/{project_id}/time_and_material_entries/signatures/{id} | Show A Signature
[**rest_v10_projects_project_id_time_and_material_entries_signatures_post**](FieldProductivityTimeAndMaterialsTimeAndMaterialSignatureApi.md#rest_v10_projects_project_id_time_and_material_entries_signatures_post) | **POST** /rest/v1.0/projects/{project_id}/time_and_material_entries/signatures | Create Signature for Time and Material Entry


# **rest_v10_projects_project_id_time_and_material_entries_signatures_bulk_destroy_delete**
> List[RestV10ProjectsProjectIdTimeAndMaterialEntriesSignaturesGet200ResponseInner] rest_v10_projects_project_id_time_and_material_entries_signatures_bulk_destroy_delete(procore_company_id, project_id, time_and_material_signature_bulk_destroy)

Delete Multiple Signatures

Deletes the Signature for the corresponding IDs passed

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_time_and_material_entries_signatures_get200_response_inner import RestV10ProjectsProjectIdTimeAndMaterialEntriesSignaturesGet200ResponseInner
from procore_sdk.models.time_and_material_signature_bulk_destroy import TimeAndMaterialSignatureBulkDestroy
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
    api_instance = procore_sdk.FieldProductivityTimeAndMaterialsTimeAndMaterialSignatureApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    time_and_material_signature_bulk_destroy = procore_sdk.TimeAndMaterialSignatureBulkDestroy() # TimeAndMaterialSignatureBulkDestroy | 

    try:
        # Delete Multiple Signatures
        api_response = api_instance.rest_v10_projects_project_id_time_and_material_entries_signatures_bulk_destroy_delete(procore_company_id, project_id, time_and_material_signature_bulk_destroy)
        print("The response of FieldProductivityTimeAndMaterialsTimeAndMaterialSignatureApi->rest_v10_projects_project_id_time_and_material_entries_signatures_bulk_destroy_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimeAndMaterialsTimeAndMaterialSignatureApi->rest_v10_projects_project_id_time_and_material_entries_signatures_bulk_destroy_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **time_and_material_signature_bulk_destroy** | [**TimeAndMaterialSignatureBulkDestroy**](TimeAndMaterialSignatureBulkDestroy.md)|  | 

### Return type

[**List[RestV10ProjectsProjectIdTimeAndMaterialEntriesSignaturesGet200ResponseInner]**](RestV10ProjectsProjectIdTimeAndMaterialEntriesSignaturesGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | User does not have permission to edit Signatures |  -  |
**404** | Not found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_time_and_material_entries_signatures_get**
> List[RestV10ProjectsProjectIdTimeAndMaterialEntriesSignaturesGet200ResponseInner] rest_v10_projects_project_id_time_and_material_entries_signatures_get(procore_company_id, project_id, page=page, per_page=per_page)

List Signatures

Return all Signatures detailed information.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_time_and_material_entries_signatures_get200_response_inner import RestV10ProjectsProjectIdTimeAndMaterialEntriesSignaturesGet200ResponseInner
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
    api_instance = procore_sdk.FieldProductivityTimeAndMaterialsTimeAndMaterialSignatureApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Signatures
        api_response = api_instance.rest_v10_projects_project_id_time_and_material_entries_signatures_get(procore_company_id, project_id, page=page, per_page=per_page)
        print("The response of FieldProductivityTimeAndMaterialsTimeAndMaterialSignatureApi->rest_v10_projects_project_id_time_and_material_entries_signatures_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimeAndMaterialsTimeAndMaterialSignatureApi->rest_v10_projects_project_id_time_and_material_entries_signatures_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[RestV10ProjectsProjectIdTimeAndMaterialEntriesSignaturesGet200ResponseInner]**](RestV10ProjectsProjectIdTimeAndMaterialEntriesSignaturesGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Per-Page - Number of items retrieved per page <br>  * Total - Total number of items to be retrieved <br>  * Link - Link headers for the first, prev, next, and last link <br>  |
**403** | User does not have permission to view Signatures |  -  |
**404** | Not found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_time_and_material_entries_signatures_id_delete**
> RestV10ProjectsProjectIdTimeAndMaterialEntriesSignaturesGet200ResponseInner rest_v10_projects_project_id_time_and_material_entries_signatures_id_delete(procore_company_id, project_id, id)

Delete Signature

Deletes the Signature for the corresponding ID passed

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_time_and_material_entries_signatures_get200_response_inner import RestV10ProjectsProjectIdTimeAndMaterialEntriesSignaturesGet200ResponseInner
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
    api_instance = procore_sdk.FieldProductivityTimeAndMaterialsTimeAndMaterialSignatureApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Signature ID

    try:
        # Delete Signature
        api_response = api_instance.rest_v10_projects_project_id_time_and_material_entries_signatures_id_delete(procore_company_id, project_id, id)
        print("The response of FieldProductivityTimeAndMaterialsTimeAndMaterialSignatureApi->rest_v10_projects_project_id_time_and_material_entries_signatures_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimeAndMaterialsTimeAndMaterialSignatureApi->rest_v10_projects_project_id_time_and_material_entries_signatures_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Signature ID | 

### Return type

[**RestV10ProjectsProjectIdTimeAndMaterialEntriesSignaturesGet200ResponseInner**](RestV10ProjectsProjectIdTimeAndMaterialEntriesSignaturesGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | User does not have permission to edit Signatures |  -  |
**404** | Not found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_time_and_material_entries_signatures_id_get**
> RestV10ProjectsProjectIdTimeAndMaterialEntriesSignaturesGet200ResponseInner rest_v10_projects_project_id_time_and_material_entries_signatures_id_get(procore_company_id, project_id, id)

Show A Signature

Return Signature detailed information.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_time_and_material_entries_signatures_get200_response_inner import RestV10ProjectsProjectIdTimeAndMaterialEntriesSignaturesGet200ResponseInner
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
    api_instance = procore_sdk.FieldProductivityTimeAndMaterialsTimeAndMaterialSignatureApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Signature ID

    try:
        # Show A Signature
        api_response = api_instance.rest_v10_projects_project_id_time_and_material_entries_signatures_id_get(procore_company_id, project_id, id)
        print("The response of FieldProductivityTimeAndMaterialsTimeAndMaterialSignatureApi->rest_v10_projects_project_id_time_and_material_entries_signatures_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimeAndMaterialsTimeAndMaterialSignatureApi->rest_v10_projects_project_id_time_and_material_entries_signatures_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Signature ID | 

### Return type

[**RestV10ProjectsProjectIdTimeAndMaterialEntriesSignaturesGet200ResponseInner**](RestV10ProjectsProjectIdTimeAndMaterialEntriesSignaturesGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | User does not have permission to view Signatures |  -  |
**404** | Not found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_time_and_material_entries_signatures_post**
> RestV10ProjectsProjectIdTimeAndMaterialEntriesSignaturesGet200ResponseInner rest_v10_projects_project_id_time_and_material_entries_signatures_post(procore_company_id, project_id, time_and_material_signature_create_body)

Create Signature for Time and Material Entry

Create new Signature associated with the specified Project.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_time_and_material_entries_signatures_get200_response_inner import RestV10ProjectsProjectIdTimeAndMaterialEntriesSignaturesGet200ResponseInner
from procore_sdk.models.time_and_material_signature_create_body import TimeAndMaterialSignatureCreateBody
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
    api_instance = procore_sdk.FieldProductivityTimeAndMaterialsTimeAndMaterialSignatureApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    time_and_material_signature_create_body = procore_sdk.TimeAndMaterialSignatureCreateBody() # TimeAndMaterialSignatureCreateBody | 

    try:
        # Create Signature for Time and Material Entry
        api_response = api_instance.rest_v10_projects_project_id_time_and_material_entries_signatures_post(procore_company_id, project_id, time_and_material_signature_create_body)
        print("The response of FieldProductivityTimeAndMaterialsTimeAndMaterialSignatureApi->rest_v10_projects_project_id_time_and_material_entries_signatures_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimeAndMaterialsTimeAndMaterialSignatureApi->rest_v10_projects_project_id_time_and_material_entries_signatures_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **time_and_material_signature_create_body** | [**TimeAndMaterialSignatureCreateBody**](TimeAndMaterialSignatureCreateBody.md)|  | 

### Return type

[**RestV10ProjectsProjectIdTimeAndMaterialEntriesSignaturesGet200ResponseInner**](RestV10ProjectsProjectIdTimeAndMaterialEntriesSignaturesGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Signature Created Succesfully |  -  |
**403** | User does not have permission to create Signatures |  -  |
**422** | Error creating Signatures |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

