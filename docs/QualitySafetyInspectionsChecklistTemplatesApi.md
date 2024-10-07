# procore_sdk.QualitySafetyInspectionsChecklistTemplatesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_checklist_list_templates_get**](QualitySafetyInspectionsChecklistTemplatesApi.md#rest_v10_checklist_list_templates_get) | **GET** /rest/v1.0/checklist/list_templates | List Checklist Templates
[**rest_v10_checklist_list_templates_id_get**](QualitySafetyInspectionsChecklistTemplatesApi.md#rest_v10_checklist_list_templates_id_get) | **GET** /rest/v1.0/checklist/list_templates/{id} | Show Checklist Template
[**rest_v10_checklist_list_templates_id_remove_alternative_response_set_patch**](QualitySafetyInspectionsChecklistTemplatesApi.md#rest_v10_checklist_list_templates_id_remove_alternative_response_set_patch) | **PATCH** /rest/v1.0/checklist/list_templates/{id}/remove_alternative_response_set | Remove Checklist Template Alternative Response Set
[**rest_v10_checklist_list_templates_id_use_alternative_response_set_patch**](QualitySafetyInspectionsChecklistTemplatesApi.md#rest_v10_checklist_list_templates_id_use_alternative_response_set_patch) | **PATCH** /rest/v1.0/checklist/list_templates/{id}/use_alternative_response_set | Add Checklist Template Alternative Response Set


# **rest_v10_checklist_list_templates_get**
> List[ChecklistTemplate4] rest_v10_checklist_list_templates_get(procore_company_id, project_id, page=page, per_page=per_page)

List Checklist Templates

Returns a list of all Inspection Checklist Templates for a specified Project.

### Example


```python
import procore_sdk
from procore_sdk.models.checklist_template4 import ChecklistTemplate4
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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistTemplatesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Checklist Templates
        api_response = api_instance.rest_v10_checklist_list_templates_get(procore_company_id, project_id, page=page, per_page=per_page)
        print("The response of QualitySafetyInspectionsChecklistTemplatesApi->rest_v10_checklist_list_templates_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistTemplatesApi->rest_v10_checklist_list_templates_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[ChecklistTemplate4]**](ChecklistTemplate4.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Per-Page - Number of items retrieved per page <br>  * Total - Total number of items to be retrieved <br>  * Link - Link headers for the first, prev, next, and last link <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_checklist_list_templates_id_get**
> ChecklistTemplate4 rest_v10_checklist_list_templates_id_get(procore_company_id, id, project_id)

Show Checklist Template

Shows an Inspection Checklist Template.

### Example


```python
import procore_sdk
from procore_sdk.models.checklist_template4 import ChecklistTemplate4
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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistTemplatesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | Checklist Template ID
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Show Checklist Template
        api_response = api_instance.rest_v10_checklist_list_templates_id_get(procore_company_id, id, project_id)
        print("The response of QualitySafetyInspectionsChecklistTemplatesApi->rest_v10_checklist_list_templates_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistTemplatesApi->rest_v10_checklist_list_templates_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| Checklist Template ID | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**ChecklistTemplate4**](ChecklistTemplate4.md)

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

# **rest_v10_checklist_list_templates_id_remove_alternative_response_set_patch**
> ChecklistTemplate5 rest_v10_checklist_list_templates_id_remove_alternative_response_set_patch(procore_company_id, id, rest_v10_checklist_list_templates_id_remove_alternative_response_set_patch_request)

Remove Checklist Template Alternative Response Set

Removes a Checklist Template's Alternative Response Set, returning the template to the default Response Set

### Example


```python
import procore_sdk
from procore_sdk.models.checklist_template5 import ChecklistTemplate5
from procore_sdk.models.rest_v10_checklist_list_templates_id_remove_alternative_response_set_patch_request import RestV10ChecklistListTemplatesIdRemoveAlternativeResponseSetPatchRequest
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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistTemplatesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | Checklist Template ID
    rest_v10_checklist_list_templates_id_remove_alternative_response_set_patch_request = procore_sdk.RestV10ChecklistListTemplatesIdRemoveAlternativeResponseSetPatchRequest() # RestV10ChecklistListTemplatesIdRemoveAlternativeResponseSetPatchRequest | 

    try:
        # Remove Checklist Template Alternative Response Set
        api_response = api_instance.rest_v10_checklist_list_templates_id_remove_alternative_response_set_patch(procore_company_id, id, rest_v10_checklist_list_templates_id_remove_alternative_response_set_patch_request)
        print("The response of QualitySafetyInspectionsChecklistTemplatesApi->rest_v10_checklist_list_templates_id_remove_alternative_response_set_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistTemplatesApi->rest_v10_checklist_list_templates_id_remove_alternative_response_set_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| Checklist Template ID | 
 **rest_v10_checklist_list_templates_id_remove_alternative_response_set_patch_request** | [**RestV10ChecklistListTemplatesIdRemoveAlternativeResponseSetPatchRequest**](RestV10ChecklistListTemplatesIdRemoveAlternativeResponseSetPatchRequest.md)|  | 

### Return type

[**ChecklistTemplate5**](ChecklistTemplate5.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_checklist_list_templates_id_use_alternative_response_set_patch**
> ChecklistTemplate5 rest_v10_checklist_list_templates_id_use_alternative_response_set_patch(procore_company_id, id, rest_v10_checklist_list_templates_id_use_alternative_response_set_patch_request)

Add Checklist Template Alternative Response Set

Sets a Checklist Template's Response Set to the specified Alternative Response Set.

### Example


```python
import procore_sdk
from procore_sdk.models.checklist_template5 import ChecklistTemplate5
from procore_sdk.models.rest_v10_checklist_list_templates_id_use_alternative_response_set_patch_request import RestV10ChecklistListTemplatesIdUseAlternativeResponseSetPatchRequest
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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistTemplatesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | Checklist Template ID
    rest_v10_checklist_list_templates_id_use_alternative_response_set_patch_request = procore_sdk.RestV10ChecklistListTemplatesIdUseAlternativeResponseSetPatchRequest() # RestV10ChecklistListTemplatesIdUseAlternativeResponseSetPatchRequest | 

    try:
        # Add Checklist Template Alternative Response Set
        api_response = api_instance.rest_v10_checklist_list_templates_id_use_alternative_response_set_patch(procore_company_id, id, rest_v10_checklist_list_templates_id_use_alternative_response_set_patch_request)
        print("The response of QualitySafetyInspectionsChecklistTemplatesApi->rest_v10_checklist_list_templates_id_use_alternative_response_set_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistTemplatesApi->rest_v10_checklist_list_templates_id_use_alternative_response_set_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| Checklist Template ID | 
 **rest_v10_checklist_list_templates_id_use_alternative_response_set_patch_request** | [**RestV10ChecklistListTemplatesIdUseAlternativeResponseSetPatchRequest**](RestV10ChecklistListTemplatesIdUseAlternativeResponseSetPatchRequest.md)|  | 

### Return type

[**ChecklistTemplate5**](ChecklistTemplate5.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

