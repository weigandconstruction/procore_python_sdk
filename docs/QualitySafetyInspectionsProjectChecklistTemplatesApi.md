# procore_sdk.QualitySafetyInspectionsProjectChecklistTemplatesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_checklist_list_templates_create_from_company_template_post**](QualitySafetyInspectionsProjectChecklistTemplatesApi.md#rest_v10_projects_project_id_checklist_list_templates_create_from_company_template_post) | **POST** /rest/v1.0/projects/{project_id}/checklist/list_templates/create_from_company_template | Create a Project Checklist Template from a Company Checklist Template
[**rest_v10_projects_project_id_checklist_list_templates_get**](QualitySafetyInspectionsProjectChecklistTemplatesApi.md#rest_v10_projects_project_id_checklist_list_templates_get) | **GET** /rest/v1.0/projects/{project_id}/checklist/list_templates | List Project Checklist Templates
[**rest_v10_projects_project_id_checklist_list_templates_id_delete**](QualitySafetyInspectionsProjectChecklistTemplatesApi.md#rest_v10_projects_project_id_checklist_list_templates_id_delete) | **DELETE** /rest/v1.0/projects/{project_id}/checklist/list_templates/{id} | Delete Project Checklist Template
[**rest_v10_projects_project_id_checklist_list_templates_id_get**](QualitySafetyInspectionsProjectChecklistTemplatesApi.md#rest_v10_projects_project_id_checklist_list_templates_id_get) | **GET** /rest/v1.0/projects/{project_id}/checklist/list_templates/{id} | Show Project Checklist Template
[**rest_v10_projects_project_id_checklist_list_templates_id_patch**](QualitySafetyInspectionsProjectChecklistTemplatesApi.md#rest_v10_projects_project_id_checklist_list_templates_id_patch) | **PATCH** /rest/v1.0/projects/{project_id}/checklist/list_templates/{id} | Update Project Checklist Template
[**rest_v10_projects_project_id_checklist_list_templates_id_remove_alternative_response_set_patch**](QualitySafetyInspectionsProjectChecklistTemplatesApi.md#rest_v10_projects_project_id_checklist_list_templates_id_remove_alternative_response_set_patch) | **PATCH** /rest/v1.0/projects/{project_id}/checklist/list_templates/{id}/remove_alternative_response_set | Remove Alternative Response Set from Project Checklist Template
[**rest_v10_projects_project_id_checklist_list_templates_id_use_alternative_response_set_patch**](QualitySafetyInspectionsProjectChecklistTemplatesApi.md#rest_v10_projects_project_id_checklist_list_templates_id_use_alternative_response_set_patch) | **PATCH** /rest/v1.0/projects/{project_id}/checklist/list_templates/{id}/use_alternative_response_set | Add Alternative Response Set to Project Checklist Template
[**rest_v10_projects_project_id_checklist_list_templates_post**](QualitySafetyInspectionsProjectChecklistTemplatesApi.md#rest_v10_projects_project_id_checklist_list_templates_post) | **POST** /rest/v1.0/projects/{project_id}/checklist/list_templates | Create Project Checklist Template
[**rest_v10_projects_project_id_recycle_bin_checklist_list_templates_get**](QualitySafetyInspectionsProjectChecklistTemplatesApi.md#rest_v10_projects_project_id_recycle_bin_checklist_list_templates_get) | **GET** /rest/v1.0/projects/{project_id}/recycle_bin/checklist/list_templates | List Recycled Checklist Templates
[**rest_v10_projects_project_id_recycle_bin_checklist_list_templates_id_get**](QualitySafetyInspectionsProjectChecklistTemplatesApi.md#rest_v10_projects_project_id_recycle_bin_checklist_list_templates_id_get) | **GET** /rest/v1.0/projects/{project_id}/recycle_bin/checklist/list_templates/{id} | Show Recycled Checklist Template
[**rest_v10_projects_project_id_recycle_bin_checklist_list_templates_id_restore_patch**](QualitySafetyInspectionsProjectChecklistTemplatesApi.md#rest_v10_projects_project_id_recycle_bin_checklist_list_templates_id_restore_patch) | **PATCH** /rest/v1.0/projects/{project_id}/recycle_bin/checklist/list_templates/{id}/restore | Restore Recycled Checklist Template
[**rest_v11_projects_project_id_checklist_list_templates_get**](QualitySafetyInspectionsProjectChecklistTemplatesApi.md#rest_v11_projects_project_id_checklist_list_templates_get) | **GET** /rest/v1.1/projects/{project_id}/checklist/list_templates | List Project Checklist Templates
[**rest_v11_projects_project_id_checklist_list_templates_id_get**](QualitySafetyInspectionsProjectChecklistTemplatesApi.md#rest_v11_projects_project_id_checklist_list_templates_id_get) | **GET** /rest/v1.1/projects/{project_id}/checklist/list_templates/{id} | Show Project Checklist Template
[**rest_v11_projects_project_id_recycle_bin_checklist_list_templates_id_restore_patch**](QualitySafetyInspectionsProjectChecklistTemplatesApi.md#rest_v11_projects_project_id_recycle_bin_checklist_list_templates_id_restore_patch) | **PATCH** /rest/v1.1/projects/{project_id}/recycle_bin/checklist/list_templates/{id}/restore | Restore Recycled Checklist Template


# **rest_v10_projects_project_id_checklist_list_templates_create_from_company_template_post**
> RestV10ProjectsProjectIdChecklistListTemplatesCreateFromCompanyTemplatePost201Response rest_v10_projects_project_id_checklist_list_templates_create_from_company_template_post(procore_company_id, project_id, rest_v10_projects_project_id_checklist_list_templates_create_from_company_template_post_request)

Create a Project Checklist Template from a Company Checklist Template

Creates a Project Checklist Template from a Company Checklist Template. Sections and Items on the Company Template are copied to the Project Template and changes to these company level records, including the template itself, are synced down to the project level. You may not create more than 1 project template per company template.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_checklist_list_templates_create_from_company_template_post201_response import RestV10ProjectsProjectIdChecklistListTemplatesCreateFromCompanyTemplatePost201Response
from procore_sdk.models.rest_v10_projects_project_id_checklist_list_templates_create_from_company_template_post_request import RestV10ProjectsProjectIdChecklistListTemplatesCreateFromCompanyTemplatePostRequest
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
    api_instance = procore_sdk.QualitySafetyInspectionsProjectChecklistTemplatesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_projects_project_id_checklist_list_templates_create_from_company_template_post_request = procore_sdk.RestV10ProjectsProjectIdChecklistListTemplatesCreateFromCompanyTemplatePostRequest() # RestV10ProjectsProjectIdChecklistListTemplatesCreateFromCompanyTemplatePostRequest | 

    try:
        # Create a Project Checklist Template from a Company Checklist Template
        api_response = api_instance.rest_v10_projects_project_id_checklist_list_templates_create_from_company_template_post(procore_company_id, project_id, rest_v10_projects_project_id_checklist_list_templates_create_from_company_template_post_request)
        print("The response of QualitySafetyInspectionsProjectChecklistTemplatesApi->rest_v10_projects_project_id_checklist_list_templates_create_from_company_template_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsProjectChecklistTemplatesApi->rest_v10_projects_project_id_checklist_list_templates_create_from_company_template_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_projects_project_id_checklist_list_templates_create_from_company_template_post_request** | [**RestV10ProjectsProjectIdChecklistListTemplatesCreateFromCompanyTemplatePostRequest**](RestV10ProjectsProjectIdChecklistListTemplatesCreateFromCompanyTemplatePostRequest.md)|  | 

### Return type

[**RestV10ProjectsProjectIdChecklistListTemplatesCreateFromCompanyTemplatePost201Response**](RestV10ProjectsProjectIdChecklistListTemplatesCreateFromCompanyTemplatePost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_checklist_list_templates_get**
> List[ProjectChecklistTemplate1] rest_v10_projects_project_id_checklist_list_templates_get(procore_company_id, project_id, page=page, per_page=per_page, filters_inspection_type_id=filters_inspection_type_id, filters_trade_ids=filters_trade_ids, filters_query=filters_query, sort=sort)

List Project Checklist Templates

Returns a list of all Inspection Checklist Templates for a specified Project. See [Filtering on List Actions](https://developers.procore.com/documentation/filtering-on-list-actions) for information on using the filtering capabilities provided by this endpoint.

### Example


```python
import procore_sdk
from procore_sdk.models.project_checklist_template1 import ProjectChecklistTemplate1
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
    api_instance = procore_sdk.QualitySafetyInspectionsProjectChecklistTemplatesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_inspection_type_id = [56] # List[int] | Array of Inspection Type IDs. Return item(s) associated with the specified Inspection Type IDs. (optional)
    filters_trade_ids = [56] # List[int] | Array of Trade IDs. Returns item(s) with the specified Trade IDs. (optional)
    filters_query = 'filters_query_example' # str | Return item(s) containing search query (optional)
    sort = 'sort_example' # str | Sorts the list of Checklist Templates on the attribute given. By default the list is in ascending order. Use '-attribute' to sort in descending order. Ex. 'sort=-trade'. (optional)

    try:
        # List Project Checklist Templates
        api_response = api_instance.rest_v10_projects_project_id_checklist_list_templates_get(procore_company_id, project_id, page=page, per_page=per_page, filters_inspection_type_id=filters_inspection_type_id, filters_trade_ids=filters_trade_ids, filters_query=filters_query, sort=sort)
        print("The response of QualitySafetyInspectionsProjectChecklistTemplatesApi->rest_v10_projects_project_id_checklist_list_templates_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsProjectChecklistTemplatesApi->rest_v10_projects_project_id_checklist_list_templates_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_inspection_type_id** | [**List[int]**](int.md)| Array of Inspection Type IDs. Return item(s) associated with the specified Inspection Type IDs. | [optional] 
 **filters_trade_ids** | [**List[int]**](int.md)| Array of Trade IDs. Returns item(s) with the specified Trade IDs. | [optional] 
 **filters_query** | **str**| Return item(s) containing search query | [optional] 
 **sort** | **str**| Sorts the list of Checklist Templates on the attribute given. By default the list is in ascending order. Use &#39;-attribute&#39; to sort in descending order. Ex. &#39;sort&#x3D;-trade&#39;. | [optional] 

### Return type

[**List[ProjectChecklistTemplate1]**](ProjectChecklistTemplate1.md)

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

# **rest_v10_projects_project_id_checklist_list_templates_id_delete**
> rest_v10_projects_project_id_checklist_list_templates_id_delete(procore_company_id, id, project_id)

Delete Project Checklist Template

Deletes an Inspection Checklist Template.

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
    api_instance = procore_sdk.QualitySafetyInspectionsProjectChecklistTemplatesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | Checklist Template ID
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Delete Project Checklist Template
        api_instance.rest_v10_projects_project_id_checklist_list_templates_id_delete(procore_company_id, id, project_id)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsProjectChecklistTemplatesApi->rest_v10_projects_project_id_checklist_list_templates_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| Checklist Template ID | 
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
**204** | No Content |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_checklist_list_templates_id_get**
> RestV10ProjectsProjectIdChecklistListTemplatesPost201Response rest_v10_projects_project_id_checklist_list_templates_id_get(procore_company_id, id, project_id)

Show Project Checklist Template

Shows an Inspection Checklist Template.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_checklist_list_templates_post201_response import RestV10ProjectsProjectIdChecklistListTemplatesPost201Response
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
    api_instance = procore_sdk.QualitySafetyInspectionsProjectChecklistTemplatesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | Checklist Template ID
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Show Project Checklist Template
        api_response = api_instance.rest_v10_projects_project_id_checklist_list_templates_id_get(procore_company_id, id, project_id)
        print("The response of QualitySafetyInspectionsProjectChecklistTemplatesApi->rest_v10_projects_project_id_checklist_list_templates_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsProjectChecklistTemplatesApi->rest_v10_projects_project_id_checklist_list_templates_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| Checklist Template ID | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**RestV10ProjectsProjectIdChecklistListTemplatesPost201Response**](RestV10ProjectsProjectIdChecklistListTemplatesPost201Response.md)

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

# **rest_v10_projects_project_id_checklist_list_templates_id_patch**
> RestV10ProjectsProjectIdChecklistListTemplatesPost201Response rest_v10_projects_project_id_checklist_list_templates_id_patch(procore_company_id, id, project_id, checklist_template_body)

Update Project Checklist Template

Updates an Inspection Checklist Template.

### Example


```python
import procore_sdk
from procore_sdk.models.checklist_template_body import ChecklistTemplateBody
from procore_sdk.models.rest_v10_projects_project_id_checklist_list_templates_post201_response import RestV10ProjectsProjectIdChecklistListTemplatesPost201Response
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
    api_instance = procore_sdk.QualitySafetyInspectionsProjectChecklistTemplatesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | Checklist Template ID
    project_id = 56 # int | Unique identifier for the project.
    checklist_template_body = procore_sdk.ChecklistTemplateBody() # ChecklistTemplateBody | 

    try:
        # Update Project Checklist Template
        api_response = api_instance.rest_v10_projects_project_id_checklist_list_templates_id_patch(procore_company_id, id, project_id, checklist_template_body)
        print("The response of QualitySafetyInspectionsProjectChecklistTemplatesApi->rest_v10_projects_project_id_checklist_list_templates_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsProjectChecklistTemplatesApi->rest_v10_projects_project_id_checklist_list_templates_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| Checklist Template ID | 
 **project_id** | **int**| Unique identifier for the project. | 
 **checklist_template_body** | [**ChecklistTemplateBody**](ChecklistTemplateBody.md)|  | 

### Return type

[**RestV10ProjectsProjectIdChecklistListTemplatesPost201Response**](RestV10ProjectsProjectIdChecklistListTemplatesPost201Response.md)

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

# **rest_v10_projects_project_id_checklist_list_templates_id_remove_alternative_response_set_patch**
> RestV10ProjectsProjectIdChecklistListTemplatesPost201Response rest_v10_projects_project_id_checklist_list_templates_id_remove_alternative_response_set_patch(procore_company_id, id, project_id)

Remove Alternative Response Set from Project Checklist Template

Removes a Project Checklist Template's Alternative Response Set, returning the template to the default Response Set.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_checklist_list_templates_post201_response import RestV10ProjectsProjectIdChecklistListTemplatesPost201Response
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
    api_instance = procore_sdk.QualitySafetyInspectionsProjectChecklistTemplatesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | Checklist Template ID
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Remove Alternative Response Set from Project Checklist Template
        api_response = api_instance.rest_v10_projects_project_id_checklist_list_templates_id_remove_alternative_response_set_patch(procore_company_id, id, project_id)
        print("The response of QualitySafetyInspectionsProjectChecklistTemplatesApi->rest_v10_projects_project_id_checklist_list_templates_id_remove_alternative_response_set_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsProjectChecklistTemplatesApi->rest_v10_projects_project_id_checklist_list_templates_id_remove_alternative_response_set_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| Checklist Template ID | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**RestV10ProjectsProjectIdChecklistListTemplatesPost201Response**](RestV10ProjectsProjectIdChecklistListTemplatesPost201Response.md)

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

# **rest_v10_projects_project_id_checklist_list_templates_id_use_alternative_response_set_patch**
> RestV10ProjectsProjectIdChecklistListTemplatesIdUseAlternativeResponseSetPatch200Response rest_v10_projects_project_id_checklist_list_templates_id_use_alternative_response_set_patch(procore_company_id, project_id, id, rest_v10_projects_project_id_checklist_list_templates_id_use_alternative_response_set_patch_request)

Add Alternative Response Set to Project Checklist Template

Sets a Project Checklist Template's Response Set to the specified Alternative Response Set.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_checklist_list_templates_id_use_alternative_response_set_patch200_response import RestV10ProjectsProjectIdChecklistListTemplatesIdUseAlternativeResponseSetPatch200Response
from procore_sdk.models.rest_v10_projects_project_id_checklist_list_templates_id_use_alternative_response_set_patch_request import RestV10ProjectsProjectIdChecklistListTemplatesIdUseAlternativeResponseSetPatchRequest
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
    api_instance = procore_sdk.QualitySafetyInspectionsProjectChecklistTemplatesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Checklist Template ID
    rest_v10_projects_project_id_checklist_list_templates_id_use_alternative_response_set_patch_request = procore_sdk.RestV10ProjectsProjectIdChecklistListTemplatesIdUseAlternativeResponseSetPatchRequest() # RestV10ProjectsProjectIdChecklistListTemplatesIdUseAlternativeResponseSetPatchRequest | 

    try:
        # Add Alternative Response Set to Project Checklist Template
        api_response = api_instance.rest_v10_projects_project_id_checklist_list_templates_id_use_alternative_response_set_patch(procore_company_id, project_id, id, rest_v10_projects_project_id_checklist_list_templates_id_use_alternative_response_set_patch_request)
        print("The response of QualitySafetyInspectionsProjectChecklistTemplatesApi->rest_v10_projects_project_id_checklist_list_templates_id_use_alternative_response_set_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsProjectChecklistTemplatesApi->rest_v10_projects_project_id_checklist_list_templates_id_use_alternative_response_set_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Checklist Template ID | 
 **rest_v10_projects_project_id_checklist_list_templates_id_use_alternative_response_set_patch_request** | [**RestV10ProjectsProjectIdChecklistListTemplatesIdUseAlternativeResponseSetPatchRequest**](RestV10ProjectsProjectIdChecklistListTemplatesIdUseAlternativeResponseSetPatchRequest.md)|  | 

### Return type

[**RestV10ProjectsProjectIdChecklistListTemplatesIdUseAlternativeResponseSetPatch200Response**](RestV10ProjectsProjectIdChecklistListTemplatesIdUseAlternativeResponseSetPatch200Response.md)

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

# **rest_v10_projects_project_id_checklist_list_templates_post**
> RestV10ProjectsProjectIdChecklistListTemplatesPost201Response rest_v10_projects_project_id_checklist_list_templates_post(procore_company_id, project_id, checklist_template_body)

Create Project Checklist Template

Creates a Project Inspection Template for a specified Project.

### Example


```python
import procore_sdk
from procore_sdk.models.checklist_template_body import ChecklistTemplateBody
from procore_sdk.models.rest_v10_projects_project_id_checklist_list_templates_post201_response import RestV10ProjectsProjectIdChecklistListTemplatesPost201Response
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
    api_instance = procore_sdk.QualitySafetyInspectionsProjectChecklistTemplatesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    checklist_template_body = procore_sdk.ChecklistTemplateBody() # ChecklistTemplateBody | 

    try:
        # Create Project Checklist Template
        api_response = api_instance.rest_v10_projects_project_id_checklist_list_templates_post(procore_company_id, project_id, checklist_template_body)
        print("The response of QualitySafetyInspectionsProjectChecklistTemplatesApi->rest_v10_projects_project_id_checklist_list_templates_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsProjectChecklistTemplatesApi->rest_v10_projects_project_id_checklist_list_templates_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **checklist_template_body** | [**ChecklistTemplateBody**](ChecklistTemplateBody.md)|  | 

### Return type

[**RestV10ProjectsProjectIdChecklistListTemplatesPost201Response**](RestV10ProjectsProjectIdChecklistListTemplatesPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_recycle_bin_checklist_list_templates_get**
> List[ChecklistTemplate1] rest_v10_projects_project_id_recycle_bin_checklist_list_templates_get(procore_company_id, project_id, page=page, per_page=per_page)

List Recycled Checklist Templates

Returns a list of all Recycled Checklist Templates for a given Project.

### Example


```python
import procore_sdk
from procore_sdk.models.checklist_template1 import ChecklistTemplate1
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
    api_instance = procore_sdk.QualitySafetyInspectionsProjectChecklistTemplatesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Recycled Checklist Templates
        api_response = api_instance.rest_v10_projects_project_id_recycle_bin_checklist_list_templates_get(procore_company_id, project_id, page=page, per_page=per_page)
        print("The response of QualitySafetyInspectionsProjectChecklistTemplatesApi->rest_v10_projects_project_id_recycle_bin_checklist_list_templates_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsProjectChecklistTemplatesApi->rest_v10_projects_project_id_recycle_bin_checklist_list_templates_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[ChecklistTemplate1]**](ChecklistTemplate1.md)

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

# **rest_v10_projects_project_id_recycle_bin_checklist_list_templates_id_get**
> ChecklistTemplate2 rest_v10_projects_project_id_recycle_bin_checklist_list_templates_id_get(procore_company_id, project_id, id, page=page, per_page=per_page)

Show Recycled Checklist Template

Shows a Recycled Checklist Template

### Example


```python
import procore_sdk
from procore_sdk.models.checklist_template2 import ChecklistTemplate2
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
    api_instance = procore_sdk.QualitySafetyInspectionsProjectChecklistTemplatesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Checklist Template ID
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # Show Recycled Checklist Template
        api_response = api_instance.rest_v10_projects_project_id_recycle_bin_checklist_list_templates_id_get(procore_company_id, project_id, id, page=page, per_page=per_page)
        print("The response of QualitySafetyInspectionsProjectChecklistTemplatesApi->rest_v10_projects_project_id_recycle_bin_checklist_list_templates_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsProjectChecklistTemplatesApi->rest_v10_projects_project_id_recycle_bin_checklist_list_templates_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Checklist Template ID | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**ChecklistTemplate2**](ChecklistTemplate2.md)

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

# **rest_v10_projects_project_id_recycle_bin_checklist_list_templates_id_restore_patch**
> rest_v10_projects_project_id_recycle_bin_checklist_list_templates_id_restore_patch(procore_company_id, project_id, id)

Restore Recycled Checklist Template

Restores the specified Checklist Template from the Recycle Bin.

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
    api_instance = procore_sdk.QualitySafetyInspectionsProjectChecklistTemplatesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Checklist Template ID

    try:
        # Restore Recycled Checklist Template
        api_instance.rest_v10_projects_project_id_recycle_bin_checklist_list_templates_id_restore_patch(procore_company_id, project_id, id)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsProjectChecklistTemplatesApi->rest_v10_projects_project_id_recycle_bin_checklist_list_templates_id_restore_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Checklist Template ID | 

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
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v11_projects_project_id_checklist_list_templates_get**
> List[ProjectChecklistTemplate] rest_v11_projects_project_id_checklist_list_templates_get(procore_company_id, project_id, page=page, per_page=per_page, filters_inspection_type_id=filters_inspection_type_id, filters_trade_ids=filters_trade_ids, filters_query=filters_query, sort=sort)

List Project Checklist Templates

Returns a list of all Inspection Checklist Templates for a specified Project. See [Filtering on List Actions](https://developers.procore.com/documentation/filtering-on-list-actions) for information on using the filtering capabilities provided by this endpoint. Note: A User with read-only and above permissions to Inspections has access to this endpoint and the URL to individual templates on the web

### Example


```python
import procore_sdk
from procore_sdk.models.project_checklist_template import ProjectChecklistTemplate
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
    api_instance = procore_sdk.QualitySafetyInspectionsProjectChecklistTemplatesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_inspection_type_id = [56] # List[int] | Array of Inspection Type IDs. Return item(s) associated with the specified Inspection Type IDs. (optional)
    filters_trade_ids = [56] # List[int] | Array of Trade IDs. Returns item(s) with the specified Trade IDs. (optional)
    filters_query = 'filters_query_example' # str | Return item(s) containing search query (optional)
    sort = 'sort_example' # str | Sorts the list of Checklist Templates on the attribute given. By default the list is in ascending order. Use '-attribute' to sort in descending order. Ex. 'sort=-trade'. (optional)

    try:
        # List Project Checklist Templates
        api_response = api_instance.rest_v11_projects_project_id_checklist_list_templates_get(procore_company_id, project_id, page=page, per_page=per_page, filters_inspection_type_id=filters_inspection_type_id, filters_trade_ids=filters_trade_ids, filters_query=filters_query, sort=sort)
        print("The response of QualitySafetyInspectionsProjectChecklistTemplatesApi->rest_v11_projects_project_id_checklist_list_templates_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsProjectChecklistTemplatesApi->rest_v11_projects_project_id_checklist_list_templates_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_inspection_type_id** | [**List[int]**](int.md)| Array of Inspection Type IDs. Return item(s) associated with the specified Inspection Type IDs. | [optional] 
 **filters_trade_ids** | [**List[int]**](int.md)| Array of Trade IDs. Returns item(s) with the specified Trade IDs. | [optional] 
 **filters_query** | **str**| Return item(s) containing search query | [optional] 
 **sort** | **str**| Sorts the list of Checklist Templates on the attribute given. By default the list is in ascending order. Use &#39;-attribute&#39; to sort in descending order. Ex. &#39;sort&#x3D;-trade&#39;. | [optional] 

### Return type

[**List[ProjectChecklistTemplate]**](ProjectChecklistTemplate.md)

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

# **rest_v11_projects_project_id_checklist_list_templates_id_get**
> RestV11ProjectsProjectIdChecklistListTemplatesIdGet200Response rest_v11_projects_project_id_checklist_list_templates_id_get(procore_company_id, id, project_id)

Show Project Checklist Template

Shows an Inspection Checklist Template. Note: A User with read-only and above permissions to Inspections has access to this endpoint and the URL to the template on the web

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v11_projects_project_id_checklist_list_templates_id_get200_response import RestV11ProjectsProjectIdChecklistListTemplatesIdGet200Response
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
    api_instance = procore_sdk.QualitySafetyInspectionsProjectChecklistTemplatesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | Checklist Template ID
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Show Project Checklist Template
        api_response = api_instance.rest_v11_projects_project_id_checklist_list_templates_id_get(procore_company_id, id, project_id)
        print("The response of QualitySafetyInspectionsProjectChecklistTemplatesApi->rest_v11_projects_project_id_checklist_list_templates_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsProjectChecklistTemplatesApi->rest_v11_projects_project_id_checklist_list_templates_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| Checklist Template ID | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**RestV11ProjectsProjectIdChecklistListTemplatesIdGet200Response**](RestV11ProjectsProjectIdChecklistListTemplatesIdGet200Response.md)

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

# **rest_v11_projects_project_id_recycle_bin_checklist_list_templates_id_restore_patch**
> rest_v11_projects_project_id_recycle_bin_checklist_list_templates_id_restore_patch(procore_company_id, project_id, id)

Restore Recycled Checklist Template

Restores the specified Checklist Template from the Recycle Bin.

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
    api_instance = procore_sdk.QualitySafetyInspectionsProjectChecklistTemplatesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Checklist Template ID

    try:
        # Restore Recycled Checklist Template
        api_instance.rest_v11_projects_project_id_recycle_bin_checklist_list_templates_id_restore_patch(procore_company_id, project_id, id)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsProjectChecklistTemplatesApi->rest_v11_projects_project_id_recycle_bin_checklist_list_templates_id_restore_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Checklist Template ID | 

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
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

