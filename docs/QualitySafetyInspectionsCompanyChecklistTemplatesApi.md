# procore_sdk.QualitySafetyInspectionsCompanyChecklistTemplatesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_checklist_list_templates_get**](QualitySafetyInspectionsCompanyChecklistTemplatesApi.md#rest_v10_companies_company_id_checklist_list_templates_get) | **GET** /rest/v1.0/companies/{company_id}/checklist/list_templates | List Company Checklist Templates
[**rest_v10_companies_company_id_checklist_list_templates_id_delete**](QualitySafetyInspectionsCompanyChecklistTemplatesApi.md#rest_v10_companies_company_id_checklist_list_templates_id_delete) | **DELETE** /rest/v1.0/companies/{company_id}/checklist/list_templates/{id} | Delete Company Checklist Template
[**rest_v10_companies_company_id_checklist_list_templates_id_get**](QualitySafetyInspectionsCompanyChecklistTemplatesApi.md#rest_v10_companies_company_id_checklist_list_templates_id_get) | **GET** /rest/v1.0/companies/{company_id}/checklist/list_templates/{id} | Show Company Checklist Template
[**rest_v10_companies_company_id_checklist_list_templates_id_patch**](QualitySafetyInspectionsCompanyChecklistTemplatesApi.md#rest_v10_companies_company_id_checklist_list_templates_id_patch) | **PATCH** /rest/v1.0/companies/{company_id}/checklist/list_templates/{id} | Update Company Checklist Template
[**rest_v10_companies_company_id_checklist_list_templates_id_remove_alternative_response_set_patch**](QualitySafetyInspectionsCompanyChecklistTemplatesApi.md#rest_v10_companies_company_id_checklist_list_templates_id_remove_alternative_response_set_patch) | **PATCH** /rest/v1.0/companies/{company_id}/checklist/list_templates/{id}/remove_alternative_response_set | Remove Company Checklist Template Alternative Response Set
[**rest_v10_companies_company_id_checklist_list_templates_id_use_alternative_response_set_patch**](QualitySafetyInspectionsCompanyChecklistTemplatesApi.md#rest_v10_companies_company_id_checklist_list_templates_id_use_alternative_response_set_patch) | **PATCH** /rest/v1.0/companies/{company_id}/checklist/list_templates/{id}/use_alternative_response_set | Add Company Checklist Template Alternative Response Set
[**rest_v10_companies_company_id_checklist_list_templates_post**](QualitySafetyInspectionsCompanyChecklistTemplatesApi.md#rest_v10_companies_company_id_checklist_list_templates_post) | **POST** /rest/v1.0/companies/{company_id}/checklist/list_templates | Create Company Checklist Template
[**rest_v10_companies_company_id_recycle_bin_checklist_list_templates_get**](QualitySafetyInspectionsCompanyChecklistTemplatesApi.md#rest_v10_companies_company_id_recycle_bin_checklist_list_templates_get) | **GET** /rest/v1.0/companies/{company_id}/recycle_bin/checklist/list_templates | List Recycled Company Checklist Templates
[**rest_v10_companies_company_id_recycle_bin_checklist_list_templates_id_get**](QualitySafetyInspectionsCompanyChecklistTemplatesApi.md#rest_v10_companies_company_id_recycle_bin_checklist_list_templates_id_get) | **GET** /rest/v1.0/companies/{company_id}/recycle_bin/checklist/list_templates/{id} | Show Recycled Company Checklist Template
[**rest_v10_companies_company_id_recycle_bin_checklist_list_templates_id_restore_patch**](QualitySafetyInspectionsCompanyChecklistTemplatesApi.md#rest_v10_companies_company_id_recycle_bin_checklist_list_templates_id_restore_patch) | **PATCH** /rest/v1.0/companies/{company_id}/recycle_bin/checklist/list_templates/{id}/restore | Restore a Recycled Company Checklist Template


# **rest_v10_companies_company_id_checklist_list_templates_get**
> List[CompanyChecklistTemplate] rest_v10_companies_company_id_checklist_list_templates_get(procore_company_id, company_id, filters_id=filters_id, filters_inspection_type_id=filters_inspection_type_id, filters_query=filters_query, filters_trade_id=filters_trade_id, filters_updated_at=filters_updated_at, sort=sort, page=page, per_page=per_page)

List Company Checklist Templates

Returns a collection of Company Checklist Templates for a specified Company.

### Example


```python
import procore_sdk
from procore_sdk.models.company_checklist_template import CompanyChecklistTemplate
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
    api_instance = procore_sdk.QualitySafetyInspectionsCompanyChecklistTemplatesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_inspection_type_id = [56] # List[int] | Array of Inspection Type IDs. Return item(s) associated with the specified Inspection Type IDs. (optional)
    filters_query = 'filters_query_example' # str | Return item(s) containing search query (optional)
    filters_trade_id = 56 # int | Trade ID (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    sort = 'sort_example' # str |  (optional)
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Company Checklist Templates
        api_response = api_instance.rest_v10_companies_company_id_checklist_list_templates_get(procore_company_id, company_id, filters_id=filters_id, filters_inspection_type_id=filters_inspection_type_id, filters_query=filters_query, filters_trade_id=filters_trade_id, filters_updated_at=filters_updated_at, sort=sort, page=page, per_page=per_page)
        print("The response of QualitySafetyInspectionsCompanyChecklistTemplatesApi->rest_v10_companies_company_id_checklist_list_templates_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsCompanyChecklistTemplatesApi->rest_v10_companies_company_id_checklist_list_templates_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **filters_id** | [**List[int]**](int.md)| Return item(s) with the specified IDs. | [optional] 
 **filters_inspection_type_id** | [**List[int]**](int.md)| Array of Inspection Type IDs. Return item(s) associated with the specified Inspection Type IDs. | [optional] 
 **filters_query** | **str**| Return item(s) containing search query | [optional] 
 **filters_trade_id** | **int**| Trade ID | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **sort** | **str**|  | [optional] 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[CompanyChecklistTemplate]**](CompanyChecklistTemplate.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_checklist_list_templates_id_delete**
> rest_v10_companies_company_id_checklist_list_templates_id_delete(procore_company_id, company_id, id)

Delete Company Checklist Template

Delete a Company Checklist Template

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
    api_instance = procore_sdk.QualitySafetyInspectionsCompanyChecklistTemplatesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | Company Checklist Template ID

    try:
        # Delete Company Checklist Template
        api_instance.rest_v10_companies_company_id_checklist_list_templates_id_delete(procore_company_id, company_id, id)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsCompanyChecklistTemplatesApi->rest_v10_companies_company_id_checklist_list_templates_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| Company Checklist Template ID | 

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
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_checklist_list_templates_id_get**
> RestV10CompaniesCompanyIdChecklistListTemplatesIdGet200Response rest_v10_companies_company_id_checklist_list_templates_id_get(procore_company_id, company_id, id)

Show Company Checklist Template

Returns the details for a specified Company Checklist Template

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_checklist_list_templates_id_get200_response import RestV10CompaniesCompanyIdChecklistListTemplatesIdGet200Response
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
    api_instance = procore_sdk.QualitySafetyInspectionsCompanyChecklistTemplatesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | Company Checklist Template ID

    try:
        # Show Company Checklist Template
        api_response = api_instance.rest_v10_companies_company_id_checklist_list_templates_id_get(procore_company_id, company_id, id)
        print("The response of QualitySafetyInspectionsCompanyChecklistTemplatesApi->rest_v10_companies_company_id_checklist_list_templates_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsCompanyChecklistTemplatesApi->rest_v10_companies_company_id_checklist_list_templates_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| Company Checklist Template ID | 

### Return type

[**RestV10CompaniesCompanyIdChecklistListTemplatesIdGet200Response**](RestV10CompaniesCompanyIdChecklistListTemplatesIdGet200Response.md)

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

# **rest_v10_companies_company_id_checklist_list_templates_id_patch**
> RestV10CompaniesCompanyIdChecklistListTemplatesPost201Response rest_v10_companies_company_id_checklist_list_templates_id_patch(procore_company_id, company_id, id, checklist_template_body)

Update Company Checklist Template

Updates a Company Checklist Template for a specified Company.

### Example


```python
import procore_sdk
from procore_sdk.models.checklist_template_body import ChecklistTemplateBody
from procore_sdk.models.rest_v10_companies_company_id_checklist_list_templates_post201_response import RestV10CompaniesCompanyIdChecklistListTemplatesPost201Response
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
    api_instance = procore_sdk.QualitySafetyInspectionsCompanyChecklistTemplatesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | Company Checklist Template ID
    checklist_template_body = procore_sdk.ChecklistTemplateBody() # ChecklistTemplateBody | 

    try:
        # Update Company Checklist Template
        api_response = api_instance.rest_v10_companies_company_id_checklist_list_templates_id_patch(procore_company_id, company_id, id, checklist_template_body)
        print("The response of QualitySafetyInspectionsCompanyChecklistTemplatesApi->rest_v10_companies_company_id_checklist_list_templates_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsCompanyChecklistTemplatesApi->rest_v10_companies_company_id_checklist_list_templates_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| Company Checklist Template ID | 
 **checklist_template_body** | [**ChecklistTemplateBody**](ChecklistTemplateBody.md)|  | 

### Return type

[**RestV10CompaniesCompanyIdChecklistListTemplatesPost201Response**](RestV10CompaniesCompanyIdChecklistListTemplatesPost201Response.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_checklist_list_templates_id_remove_alternative_response_set_patch**
> RestV10CompaniesCompanyIdChecklistListTemplatesIdGet200Response rest_v10_companies_company_id_checklist_list_templates_id_remove_alternative_response_set_patch(procore_company_id, id, company_id)

Remove Company Checklist Template Alternative Response Set

Removes a Company Checklist Template's Alternative Response Set, returning the template to the default Response Set

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_checklist_list_templates_id_get200_response import RestV10CompaniesCompanyIdChecklistListTemplatesIdGet200Response
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
    api_instance = procore_sdk.QualitySafetyInspectionsCompanyChecklistTemplatesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | Company Checklist Template ID
    company_id = 56 # int | Unique identifier for the company.

    try:
        # Remove Company Checklist Template Alternative Response Set
        api_response = api_instance.rest_v10_companies_company_id_checklist_list_templates_id_remove_alternative_response_set_patch(procore_company_id, id, company_id)
        print("The response of QualitySafetyInspectionsCompanyChecklistTemplatesApi->rest_v10_companies_company_id_checklist_list_templates_id_remove_alternative_response_set_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsCompanyChecklistTemplatesApi->rest_v10_companies_company_id_checklist_list_templates_id_remove_alternative_response_set_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| Company Checklist Template ID | 
 **company_id** | **int**| Unique identifier for the company. | 

### Return type

[**RestV10CompaniesCompanyIdChecklistListTemplatesIdGet200Response**](RestV10CompaniesCompanyIdChecklistListTemplatesIdGet200Response.md)

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

# **rest_v10_companies_company_id_checklist_list_templates_id_use_alternative_response_set_patch**
> RestV10CompaniesCompanyIdChecklistListTemplatesPost201Response rest_v10_companies_company_id_checklist_list_templates_id_use_alternative_response_set_patch(procore_company_id, id, company_id, rest_v10_projects_project_id_checklist_list_templates_id_use_alternative_response_set_patch_request)

Add Company Checklist Template Alternative Response Set

Sets a Company Checklist Template's Response Set to the specified Alternative Response Set.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_checklist_list_templates_post201_response import RestV10CompaniesCompanyIdChecklistListTemplatesPost201Response
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
    api_instance = procore_sdk.QualitySafetyInspectionsCompanyChecklistTemplatesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | Company Checklist Template ID
    company_id = 56 # int | Unique identifier for the company.
    rest_v10_projects_project_id_checklist_list_templates_id_use_alternative_response_set_patch_request = procore_sdk.RestV10ProjectsProjectIdChecklistListTemplatesIdUseAlternativeResponseSetPatchRequest() # RestV10ProjectsProjectIdChecklistListTemplatesIdUseAlternativeResponseSetPatchRequest | 

    try:
        # Add Company Checklist Template Alternative Response Set
        api_response = api_instance.rest_v10_companies_company_id_checklist_list_templates_id_use_alternative_response_set_patch(procore_company_id, id, company_id, rest_v10_projects_project_id_checklist_list_templates_id_use_alternative_response_set_patch_request)
        print("The response of QualitySafetyInspectionsCompanyChecklistTemplatesApi->rest_v10_companies_company_id_checklist_list_templates_id_use_alternative_response_set_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsCompanyChecklistTemplatesApi->rest_v10_companies_company_id_checklist_list_templates_id_use_alternative_response_set_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| Company Checklist Template ID | 
 **company_id** | **int**| Unique identifier for the company. | 
 **rest_v10_projects_project_id_checklist_list_templates_id_use_alternative_response_set_patch_request** | [**RestV10ProjectsProjectIdChecklistListTemplatesIdUseAlternativeResponseSetPatchRequest**](RestV10ProjectsProjectIdChecklistListTemplatesIdUseAlternativeResponseSetPatchRequest.md)|  | 

### Return type

[**RestV10CompaniesCompanyIdChecklistListTemplatesPost201Response**](RestV10CompaniesCompanyIdChecklistListTemplatesPost201Response.md)

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

# **rest_v10_companies_company_id_checklist_list_templates_post**
> RestV10CompaniesCompanyIdChecklistListTemplatesPost201Response rest_v10_companies_company_id_checklist_list_templates_post(procore_company_id, company_id, checklist_template_body)

Create Company Checklist Template

Creates a Company Checklist Template for a specified Company.

### Example


```python
import procore_sdk
from procore_sdk.models.checklist_template_body import ChecklistTemplateBody
from procore_sdk.models.rest_v10_companies_company_id_checklist_list_templates_post201_response import RestV10CompaniesCompanyIdChecklistListTemplatesPost201Response
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
    api_instance = procore_sdk.QualitySafetyInspectionsCompanyChecklistTemplatesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    checklist_template_body = procore_sdk.ChecklistTemplateBody() # ChecklistTemplateBody | 

    try:
        # Create Company Checklist Template
        api_response = api_instance.rest_v10_companies_company_id_checklist_list_templates_post(procore_company_id, company_id, checklist_template_body)
        print("The response of QualitySafetyInspectionsCompanyChecklistTemplatesApi->rest_v10_companies_company_id_checklist_list_templates_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsCompanyChecklistTemplatesApi->rest_v10_companies_company_id_checklist_list_templates_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **checklist_template_body** | [**ChecklistTemplateBody**](ChecklistTemplateBody.md)|  | 

### Return type

[**RestV10CompaniesCompanyIdChecklistListTemplatesPost201Response**](RestV10CompaniesCompanyIdChecklistListTemplatesPost201Response.md)

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

# **rest_v10_companies_company_id_recycle_bin_checklist_list_templates_get**
> List[ChecklistTemplate3] rest_v10_companies_company_id_recycle_bin_checklist_list_templates_get(procore_company_id, company_id, page=page, per_page=per_page)

List Recycled Company Checklist Templates

Returns a list of all Recycled Checklist Templates for a given Company.

### Example


```python
import procore_sdk
from procore_sdk.models.checklist_template3 import ChecklistTemplate3
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
    api_instance = procore_sdk.QualitySafetyInspectionsCompanyChecklistTemplatesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Recycled Company Checklist Templates
        api_response = api_instance.rest_v10_companies_company_id_recycle_bin_checklist_list_templates_get(procore_company_id, company_id, page=page, per_page=per_page)
        print("The response of QualitySafetyInspectionsCompanyChecklistTemplatesApi->rest_v10_companies_company_id_recycle_bin_checklist_list_templates_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsCompanyChecklistTemplatesApi->rest_v10_companies_company_id_recycle_bin_checklist_list_templates_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[ChecklistTemplate3]**](ChecklistTemplate3.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_recycle_bin_checklist_list_templates_id_get**
> RestV10CompaniesCompanyIdChecklistListTemplatesIdGet200Response rest_v10_companies_company_id_recycle_bin_checklist_list_templates_id_get(procore_company_id, company_id, id)

Show Recycled Company Checklist Template

View the details of a Recycled Company Checklist Template

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_checklist_list_templates_id_get200_response import RestV10CompaniesCompanyIdChecklistListTemplatesIdGet200Response
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
    api_instance = procore_sdk.QualitySafetyInspectionsCompanyChecklistTemplatesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | Company Checklist Template ID

    try:
        # Show Recycled Company Checklist Template
        api_response = api_instance.rest_v10_companies_company_id_recycle_bin_checklist_list_templates_id_get(procore_company_id, company_id, id)
        print("The response of QualitySafetyInspectionsCompanyChecklistTemplatesApi->rest_v10_companies_company_id_recycle_bin_checklist_list_templates_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsCompanyChecklistTemplatesApi->rest_v10_companies_company_id_recycle_bin_checklist_list_templates_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| Company Checklist Template ID | 

### Return type

[**RestV10CompaniesCompanyIdChecklistListTemplatesIdGet200Response**](RestV10CompaniesCompanyIdChecklistListTemplatesIdGet200Response.md)

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

# **rest_v10_companies_company_id_recycle_bin_checklist_list_templates_id_restore_patch**
> rest_v10_companies_company_id_recycle_bin_checklist_list_templates_id_restore_patch(procore_company_id, company_id, id)

Restore a Recycled Company Checklist Template

Restores the specified Recycled Company Checklist Template

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
    api_instance = procore_sdk.QualitySafetyInspectionsCompanyChecklistTemplatesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | Company Checklist Template ID

    try:
        # Restore a Recycled Company Checklist Template
        api_instance.rest_v10_companies_company_id_recycle_bin_checklist_list_templates_id_restore_patch(procore_company_id, company_id, id)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsCompanyChecklistTemplatesApi->rest_v10_companies_company_id_recycle_bin_checklist_list_templates_id_restore_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| Company Checklist Template ID | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

