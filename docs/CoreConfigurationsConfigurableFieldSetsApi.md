# procore_sdk.CoreConfigurationsConfigurableFieldSetsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_configurable_field_sets_find_by_index_get**](CoreConfigurationsConfigurableFieldSetsApi.md#rest_v10_companies_company_id_configurable_field_sets_find_by_index_get) | **GET** /rest/v1.0/companies/{company_id}/configurable_field_sets/find_by_index | Find Configurable Field Set by Index
[**rest_v10_companies_company_id_configurable_field_sets_get**](CoreConfigurationsConfigurableFieldSetsApi.md#rest_v10_companies_company_id_configurable_field_sets_get) | **GET** /rest/v1.0/companies/{company_id}/configurable_field_sets | List Configurable Field Sets
[**rest_v10_companies_company_id_configurable_field_sets_id_delete**](CoreConfigurationsConfigurableFieldSetsApi.md#rest_v10_companies_company_id_configurable_field_sets_id_delete) | **DELETE** /rest/v1.0/companies/{company_id}/configurable_field_sets/{id} | Delete Configurable Field Set
[**rest_v10_companies_company_id_configurable_field_sets_id_duplicate_post**](CoreConfigurationsConfigurableFieldSetsApi.md#rest_v10_companies_company_id_configurable_field_sets_id_duplicate_post) | **POST** /rest/v1.0/companies/{company_id}/configurable_field_sets/{id}/duplicate | Duplicate a Configurable Field Set and its custom fields
[**rest_v10_companies_company_id_configurable_field_sets_id_get**](CoreConfigurationsConfigurableFieldSetsApi.md#rest_v10_companies_company_id_configurable_field_sets_id_get) | **GET** /rest/v1.0/companies/{company_id}/configurable_field_sets/{id} | Show Configurable Field Set
[**rest_v10_companies_company_id_configurable_field_sets_id_patch**](CoreConfigurationsConfigurableFieldSetsApi.md#rest_v10_companies_company_id_configurable_field_sets_id_patch) | **PATCH** /rest/v1.0/companies/{company_id}/configurable_field_sets/{id} | Update Configurable Field Set
[**rest_v10_companies_company_id_configurable_field_sets_id_project_options_get**](CoreConfigurationsConfigurableFieldSetsApi.md#rest_v10_companies_company_id_configurable_field_sets_id_project_options_get) | **GET** /rest/v1.0/companies/{company_id}/configurable_field_sets/{id}/project_options | List Configurable Field Set Project options
[**rest_v10_companies_company_id_configurable_field_sets_id_validations_post**](CoreConfigurationsConfigurableFieldSetsApi.md#rest_v10_companies_company_id_configurable_field_sets_id_validations_post) | **POST** /rest/v1.0/companies/{company_id}/configurable_field_sets/{id}/validations | Validate Custom Fields Values With Configurable Field Set
[**rest_v10_companies_company_id_configurable_field_sets_post**](CoreConfigurationsConfigurableFieldSetsApi.md#rest_v10_companies_company_id_configurable_field_sets_post) | **POST** /rest/v1.0/companies/{company_id}/configurable_field_sets | Create Configurable Field Sets
[**rest_v10_projects_project_id_configurable_field_sets_get**](CoreConfigurationsConfigurableFieldSetsApi.md#rest_v10_projects_project_id_configurable_field_sets_get) | **GET** /rest/v1.0/projects/{project_id}/configurable_field_sets | List Project Configurable Field Sets
[**rest_v10_projects_project_id_custom_fields_tool_name_user_options_get**](CoreConfigurationsConfigurableFieldSetsApi.md#rest_v10_projects_project_id_custom_fields_tool_name_user_options_get) | **GET** /rest/v1.0/projects/{project_id}/custom_fields/{tool_name}/user_options | List Custom Fields User options


# **rest_v10_companies_company_id_configurable_field_sets_find_by_index_get**
> ConfigurableFieldSet2 rest_v10_companies_company_id_configurable_field_sets_find_by_index_get(procore_company_id, company_id, type, project_id=project_id, scope_category=scope_category, scope_inspection_type_id=scope_inspection_type_id, scope_generic_tool_id=scope_generic_tool_id, scope_action_plan_type_id=scope_action_plan_type_id)

Find Configurable Field Set by Index

Returns the details for a specified Configurable Field Set if found. If not, template of type Field Set will be returned with ID null.

### Example


```python
import procore_sdk
from procore_sdk.models.configurable_field_set2 import ConfigurableFieldSet2
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
    api_instance = procore_sdk.CoreConfigurationsConfigurableFieldSetsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    type = 'type_example' # str | The type of Configurable Field Set
    project_id = 56 # int | Project ID that is associated to the Configurable Field Set, if applicable (optional)
    scope_category = 56 # int | Required for an Observations Configurable Field Set (0 = quality, 1 = safety, 2 = commissioning, 3 = warranty, 4 = work to complete) (optional)
    scope_inspection_type_id = 56 # int | Required for an Inspection Configurable Field Set. If a value is provided, only field set of the specific Inspection type is returned. If no value is provided, only field set of unassociated Inspections (Inspections with no type) is returned. (optional)
    scope_generic_tool_id = 56 # int | Required for a Generic Tool Item Configurable Field Set (type of ConfigurableFieldSet::GenericToolItem) (optional)
    scope_action_plan_type_id = 56 # int | Required for an Action Plans Plan Configurable Field Set (type of ConfigurableFieldSet::ActionPlans::Plan) (optional)

    try:
        # Find Configurable Field Set by Index
        api_response = api_instance.rest_v10_companies_company_id_configurable_field_sets_find_by_index_get(procore_company_id, company_id, type, project_id=project_id, scope_category=scope_category, scope_inspection_type_id=scope_inspection_type_id, scope_generic_tool_id=scope_generic_tool_id, scope_action_plan_type_id=scope_action_plan_type_id)
        print("The response of CoreConfigurationsConfigurableFieldSetsApi->rest_v10_companies_company_id_configurable_field_sets_find_by_index_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreConfigurationsConfigurableFieldSetsApi->rest_v10_companies_company_id_configurable_field_sets_find_by_index_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **type** | **str**| The type of Configurable Field Set | 
 **project_id** | **int**| Project ID that is associated to the Configurable Field Set, if applicable | [optional] 
 **scope_category** | **int**| Required for an Observations Configurable Field Set (0 &#x3D; quality, 1 &#x3D; safety, 2 &#x3D; commissioning, 3 &#x3D; warranty, 4 &#x3D; work to complete) | [optional] 
 **scope_inspection_type_id** | **int**| Required for an Inspection Configurable Field Set. If a value is provided, only field set of the specific Inspection type is returned. If no value is provided, only field set of unassociated Inspections (Inspections with no type) is returned. | [optional] 
 **scope_generic_tool_id** | **int**| Required for a Generic Tool Item Configurable Field Set (type of ConfigurableFieldSet::GenericToolItem) | [optional] 
 **scope_action_plan_type_id** | **int**| Required for an Action Plans Plan Configurable Field Set (type of ConfigurableFieldSet::ActionPlans::Plan) | [optional] 

### Return type

[**ConfigurableFieldSet2**](ConfigurableFieldSet2.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_configurable_field_sets_get**
> List[ConfigurableFieldSet] rest_v10_companies_company_id_configurable_field_sets_get(procore_company_id, company_id, include_lov_entries=include_lov_entries, page=page, per_page=per_page, filters_type=filters_type, filters_generic_tool_id=filters_generic_tool_id, view=view)

List Configurable Field Sets

Return a list of all Configurable Field Sets associated with a Company.

### Example


```python
import procore_sdk
from procore_sdk.models.configurable_field_set import ConfigurableFieldSet
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
    api_instance = procore_sdk.CoreConfigurationsConfigurableFieldSetsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    include_lov_entries = True # bool | whether or not to include LOV entries in the response (defaults to true) (optional)
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_type = ['filters_type_example'] # List[str] | Filter by field set type(s). Could be a string or an array of string. (optional)
    filters_generic_tool_id = [56] # List[int] | Filter by generic tool id(s). Could be a integer or an array of integer. (optional)
    view = 'view_example' # str | Specify which view to render. Options are extended, mobile, or with_project_ids (optional)

    try:
        # List Configurable Field Sets
        api_response = api_instance.rest_v10_companies_company_id_configurable_field_sets_get(procore_company_id, company_id, include_lov_entries=include_lov_entries, page=page, per_page=per_page, filters_type=filters_type, filters_generic_tool_id=filters_generic_tool_id, view=view)
        print("The response of CoreConfigurationsConfigurableFieldSetsApi->rest_v10_companies_company_id_configurable_field_sets_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreConfigurationsConfigurableFieldSetsApi->rest_v10_companies_company_id_configurable_field_sets_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **include_lov_entries** | **bool**| whether or not to include LOV entries in the response (defaults to true) | [optional] 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_type** | [**List[str]**](str.md)| Filter by field set type(s). Could be a string or an array of string. | [optional] 
 **filters_generic_tool_id** | [**List[int]**](int.md)| Filter by generic tool id(s). Could be a integer or an array of integer. | [optional] 
 **view** | **str**| Specify which view to render. Options are extended, mobile, or with_project_ids | [optional] 

### Return type

[**List[ConfigurableFieldSet]**](ConfigurableFieldSet.md)

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

# **rest_v10_companies_company_id_configurable_field_sets_id_delete**
> rest_v10_companies_company_id_configurable_field_sets_id_delete(procore_company_id, company_id, id)

Delete Configurable Field Set

Deletes a Configurable Field Set.

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
    api_instance = procore_sdk.CoreConfigurationsConfigurableFieldSetsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | Configurable Field Set ID

    try:
        # Delete Configurable Field Set
        api_instance.rest_v10_companies_company_id_configurable_field_sets_id_delete(procore_company_id, company_id, id)
    except Exception as e:
        print("Exception when calling CoreConfigurationsConfigurableFieldSetsApi->rest_v10_companies_company_id_configurable_field_sets_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| Configurable Field Set ID | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_configurable_field_sets_id_duplicate_post**
> ConfigurableFieldSet rest_v10_companies_company_id_configurable_field_sets_id_duplicate_post(procore_company_id, company_id, id, name, include_custom_fields=include_custom_fields)

Duplicate a Configurable Field Set and its custom fields

Returns the newly duplicated configurable field set.

### Example


```python
import procore_sdk
from procore_sdk.models.configurable_field_set import ConfigurableFieldSet
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
    api_instance = procore_sdk.CoreConfigurationsConfigurableFieldSetsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | Configurable Field Set ID
    name = 'name_example' # str | Name for new fieldset
    include_custom_fields = True # bool | Boolean to dictate if the custom fields are duplicated (optional)

    try:
        # Duplicate a Configurable Field Set and its custom fields
        api_response = api_instance.rest_v10_companies_company_id_configurable_field_sets_id_duplicate_post(procore_company_id, company_id, id, name, include_custom_fields=include_custom_fields)
        print("The response of CoreConfigurationsConfigurableFieldSetsApi->rest_v10_companies_company_id_configurable_field_sets_id_duplicate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreConfigurationsConfigurableFieldSetsApi->rest_v10_companies_company_id_configurable_field_sets_id_duplicate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| Configurable Field Set ID | 
 **name** | **str**| Name for new fieldset | 
 **include_custom_fields** | **bool**| Boolean to dictate if the custom fields are duplicated | [optional] 

### Return type

[**ConfigurableFieldSet**](ConfigurableFieldSet.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_configurable_field_sets_id_get**
> ConfigurableFieldSet2 rest_v10_companies_company_id_configurable_field_sets_id_get(procore_company_id, company_id, id)

Show Configurable Field Set

Returns the details for a specified Configurable Field Set

### Example


```python
import procore_sdk
from procore_sdk.models.configurable_field_set2 import ConfigurableFieldSet2
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
    api_instance = procore_sdk.CoreConfigurationsConfigurableFieldSetsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | Configurable Field Set ID

    try:
        # Show Configurable Field Set
        api_response = api_instance.rest_v10_companies_company_id_configurable_field_sets_id_get(procore_company_id, company_id, id)
        print("The response of CoreConfigurationsConfigurableFieldSetsApi->rest_v10_companies_company_id_configurable_field_sets_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreConfigurationsConfigurableFieldSetsApi->rest_v10_companies_company_id_configurable_field_sets_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| Configurable Field Set ID | 

### Return type

[**ConfigurableFieldSet2**](ConfigurableFieldSet2.md)

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

# **rest_v10_companies_company_id_configurable_field_sets_id_patch**
> ConfigurableFieldSet2 rest_v10_companies_company_id_configurable_field_sets_id_patch(procore_company_id, company_id, id, rest_v10_companies_company_id_configurable_field_sets_id_patch_request)

Update Configurable Field Set

Updates a Configurable Field Set.

### Example


```python
import procore_sdk
from procore_sdk.models.configurable_field_set2 import ConfigurableFieldSet2
from procore_sdk.models.rest_v10_companies_company_id_configurable_field_sets_id_patch_request import RestV10CompaniesCompanyIdConfigurableFieldSetsIdPatchRequest
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
    api_instance = procore_sdk.CoreConfigurationsConfigurableFieldSetsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | Configurable Field Set ID
    rest_v10_companies_company_id_configurable_field_sets_id_patch_request = procore_sdk.RestV10CompaniesCompanyIdConfigurableFieldSetsIdPatchRequest() # RestV10CompaniesCompanyIdConfigurableFieldSetsIdPatchRequest | 

    try:
        # Update Configurable Field Set
        api_response = api_instance.rest_v10_companies_company_id_configurable_field_sets_id_patch(procore_company_id, company_id, id, rest_v10_companies_company_id_configurable_field_sets_id_patch_request)
        print("The response of CoreConfigurationsConfigurableFieldSetsApi->rest_v10_companies_company_id_configurable_field_sets_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreConfigurationsConfigurableFieldSetsApi->rest_v10_companies_company_id_configurable_field_sets_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| Configurable Field Set ID | 
 **rest_v10_companies_company_id_configurable_field_sets_id_patch_request** | [**RestV10CompaniesCompanyIdConfigurableFieldSetsIdPatchRequest**](RestV10CompaniesCompanyIdConfigurableFieldSetsIdPatchRequest.md)|  | 

### Return type

[**ConfigurableFieldSet2**](ConfigurableFieldSet2.md)

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

# **rest_v10_companies_company_id_configurable_field_sets_id_project_options_get**
> List[RestV10CompaniesCompanyIdConfigurableFieldSetsIdProjectOptionsGet200ResponseInner] rest_v10_companies_company_id_configurable_field_sets_id_project_options_get(procore_company_id, company_id, id, page=page, per_page=per_page, with_name=with_name, starts_with=starts_with)

List Configurable Field Set Project options

Returns projects available for the specified configurable field set

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_configurable_field_sets_id_project_options_get200_response_inner import RestV10CompaniesCompanyIdConfigurableFieldSetsIdProjectOptionsGet200ResponseInner
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
    api_instance = procore_sdk.CoreConfigurationsConfigurableFieldSetsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | Configurable Field Set ID
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    with_name = 'A value, 0001 - Document, 0001' # str | Filter by project name, project number or display name which contains the given text. (optional)
    starts_with = 'A value, 0001 - Document, 0001' # str | Filter by project name, project number or display name starts with the given text. (optional)

    try:
        # List Configurable Field Set Project options
        api_response = api_instance.rest_v10_companies_company_id_configurable_field_sets_id_project_options_get(procore_company_id, company_id, id, page=page, per_page=per_page, with_name=with_name, starts_with=starts_with)
        print("The response of CoreConfigurationsConfigurableFieldSetsApi->rest_v10_companies_company_id_configurable_field_sets_id_project_options_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreConfigurationsConfigurableFieldSetsApi->rest_v10_companies_company_id_configurable_field_sets_id_project_options_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| Configurable Field Set ID | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **with_name** | **str**| Filter by project name, project number or display name which contains the given text. | [optional] 
 **starts_with** | **str**| Filter by project name, project number or display name starts with the given text. | [optional] 

### Return type

[**List[RestV10CompaniesCompanyIdConfigurableFieldSetsIdProjectOptionsGet200ResponseInner]**](RestV10CompaniesCompanyIdConfigurableFieldSetsIdProjectOptionsGet200ResponseInner.md)

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

# **rest_v10_companies_company_id_configurable_field_sets_id_validations_post**
> RestV10CompaniesCompanyIdConfigurableFieldSetsIdValidationsPost200Response rest_v10_companies_company_id_configurable_field_sets_id_validations_post(procore_company_id, company_id, id, project_id=project_id, rest_v10_companies_company_id_configurable_field_sets_id_validations_post_request=rest_v10_companies_company_id_configurable_field_sets_id_validations_post_request)

Validate Custom Fields Values With Configurable Field Set

Returns validation failure/success messages for values supplied to custom fields within the configurable field set.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_configurable_field_sets_id_validations_post200_response import RestV10CompaniesCompanyIdConfigurableFieldSetsIdValidationsPost200Response
from procore_sdk.models.rest_v10_companies_company_id_configurable_field_sets_id_validations_post_request import RestV10CompaniesCompanyIdConfigurableFieldSetsIdValidationsPostRequest
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
    api_instance = procore_sdk.CoreConfigurationsConfigurableFieldSetsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | Configurable Field Set ID
    project_id = 56 # int | Project ID (optional)
    rest_v10_companies_company_id_configurable_field_sets_id_validations_post_request = procore_sdk.RestV10CompaniesCompanyIdConfigurableFieldSetsIdValidationsPostRequest() # RestV10CompaniesCompanyIdConfigurableFieldSetsIdValidationsPostRequest |  (optional)

    try:
        # Validate Custom Fields Values With Configurable Field Set
        api_response = api_instance.rest_v10_companies_company_id_configurable_field_sets_id_validations_post(procore_company_id, company_id, id, project_id=project_id, rest_v10_companies_company_id_configurable_field_sets_id_validations_post_request=rest_v10_companies_company_id_configurable_field_sets_id_validations_post_request)
        print("The response of CoreConfigurationsConfigurableFieldSetsApi->rest_v10_companies_company_id_configurable_field_sets_id_validations_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreConfigurationsConfigurableFieldSetsApi->rest_v10_companies_company_id_configurable_field_sets_id_validations_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| Configurable Field Set ID | 
 **project_id** | **int**| Project ID | [optional] 
 **rest_v10_companies_company_id_configurable_field_sets_id_validations_post_request** | [**RestV10CompaniesCompanyIdConfigurableFieldSetsIdValidationsPostRequest**](RestV10CompaniesCompanyIdConfigurableFieldSetsIdValidationsPostRequest.md)|  | [optional] 

### Return type

[**RestV10CompaniesCompanyIdConfigurableFieldSetsIdValidationsPost200Response**](RestV10CompaniesCompanyIdConfigurableFieldSetsIdValidationsPost200Response.md)

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

# **rest_v10_companies_company_id_configurable_field_sets_post**
> ConfigurableFieldSet2 rest_v10_companies_company_id_configurable_field_sets_post(procore_company_id, company_id, rest_v10_companies_company_id_configurable_field_sets_post_request, include_lov_entries=include_lov_entries)

Create Configurable Field Sets

Creates a Configurable Field Set

### Example


```python
import procore_sdk
from procore_sdk.models.configurable_field_set2 import ConfigurableFieldSet2
from procore_sdk.models.rest_v10_companies_company_id_configurable_field_sets_post_request import RestV10CompaniesCompanyIdConfigurableFieldSetsPostRequest
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
    api_instance = procore_sdk.CoreConfigurationsConfigurableFieldSetsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    rest_v10_companies_company_id_configurable_field_sets_post_request = procore_sdk.RestV10CompaniesCompanyIdConfigurableFieldSetsPostRequest() # RestV10CompaniesCompanyIdConfigurableFieldSetsPostRequest | 
    include_lov_entries = True # bool | whether or not to include LOV entries in the response (defaults to true) (optional)

    try:
        # Create Configurable Field Sets
        api_response = api_instance.rest_v10_companies_company_id_configurable_field_sets_post(procore_company_id, company_id, rest_v10_companies_company_id_configurable_field_sets_post_request, include_lov_entries=include_lov_entries)
        print("The response of CoreConfigurationsConfigurableFieldSetsApi->rest_v10_companies_company_id_configurable_field_sets_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreConfigurationsConfigurableFieldSetsApi->rest_v10_companies_company_id_configurable_field_sets_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **rest_v10_companies_company_id_configurable_field_sets_post_request** | [**RestV10CompaniesCompanyIdConfigurableFieldSetsPostRequest**](RestV10CompaniesCompanyIdConfigurableFieldSetsPostRequest.md)|  | 
 **include_lov_entries** | **bool**| whether or not to include LOV entries in the response (defaults to true) | [optional] 

### Return type

[**ConfigurableFieldSet2**](ConfigurableFieldSet2.md)

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

# **rest_v10_projects_project_id_configurable_field_sets_get**
> List[ConfigurableFieldSet] rest_v10_projects_project_id_configurable_field_sets_get(procore_company_id, project_id, page=page, per_page=per_page, include_lov_entries=include_lov_entries, types=types, include_default_configurable_field_sets=include_default_configurable_field_sets, generic_tool_id=generic_tool_id, action_plan_type_id=action_plan_type_id, inspection_type_id=inspection_type_id, category=category)

List Project Configurable Field Sets

Return a list of all Configurable Field Sets associated with a Project.

### Example


```python
import procore_sdk
from procore_sdk.models.configurable_field_set import ConfigurableFieldSet
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
    api_instance = procore_sdk.CoreConfigurationsConfigurableFieldSetsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    include_lov_entries = True # bool | whether or not to include LOV entries in the response (defaults to true) (optional)
    types = ['[\"ConfigurableFieldSet::PurchaeOrderContract\",\"ConfigurableFieldSet::Observations::Item\"]'] # List[str] | Filter by of configurable field set types (optional)
    include_default_configurable_field_sets = True # bool | Flag to include the default values for each type of Configurable Field Set if one has not been created. (optional)
    generic_tool_id = 1 # int | Filter by generic tool id(s). Could be a integer or an array of integer. (optional)
    action_plan_type_id = 1 # int | Filter by Action Plan type id. (optional)
    inspection_type_id = 1 # int | Filter by inspection type id. (optional)
    category = '1' # str | Filter by category. (optional)

    try:
        # List Project Configurable Field Sets
        api_response = api_instance.rest_v10_projects_project_id_configurable_field_sets_get(procore_company_id, project_id, page=page, per_page=per_page, include_lov_entries=include_lov_entries, types=types, include_default_configurable_field_sets=include_default_configurable_field_sets, generic_tool_id=generic_tool_id, action_plan_type_id=action_plan_type_id, inspection_type_id=inspection_type_id, category=category)
        print("The response of CoreConfigurationsConfigurableFieldSetsApi->rest_v10_projects_project_id_configurable_field_sets_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreConfigurationsConfigurableFieldSetsApi->rest_v10_projects_project_id_configurable_field_sets_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **include_lov_entries** | **bool**| whether or not to include LOV entries in the response (defaults to true) | [optional] 
 **types** | [**List[str]**](str.md)| Filter by of configurable field set types | [optional] 
 **include_default_configurable_field_sets** | **bool**| Flag to include the default values for each type of Configurable Field Set if one has not been created. | [optional] 
 **generic_tool_id** | **int**| Filter by generic tool id(s). Could be a integer or an array of integer. | [optional] 
 **action_plan_type_id** | **int**| Filter by Action Plan type id. | [optional] 
 **inspection_type_id** | **int**| Filter by inspection type id. | [optional] 
 **category** | **str**| Filter by category. | [optional] 

### Return type

[**List[ConfigurableFieldSet]**](ConfigurableFieldSet.md)

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

# **rest_v10_projects_project_id_custom_fields_tool_name_user_options_get**
> List[RestV10ProjectsProjectIdRfisDefaultDistributionGet200ResponseInner] rest_v10_projects_project_id_custom_fields_tool_name_user_options_get(procore_company_id, project_id, tool_name, page=page, per_page=per_page)

List Custom Fields User options

Returns login informations that have access to the specified tool.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_rfis_default_distribution_get200_response_inner import RestV10ProjectsProjectIdRfisDefaultDistributionGet200ResponseInner
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
    api_instance = procore_sdk.CoreConfigurationsConfigurableFieldSetsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    tool_name = 'tool_name_example' # str | Tool name identifier
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Custom Fields User options
        api_response = api_instance.rest_v10_projects_project_id_custom_fields_tool_name_user_options_get(procore_company_id, project_id, tool_name, page=page, per_page=per_page)
        print("The response of CoreConfigurationsConfigurableFieldSetsApi->rest_v10_projects_project_id_custom_fields_tool_name_user_options_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreConfigurationsConfigurableFieldSetsApi->rest_v10_projects_project_id_custom_fields_tool_name_user_options_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **tool_name** | **str**| Tool name identifier | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[RestV10ProjectsProjectIdRfisDefaultDistributionGet200ResponseInner]**](RestV10ProjectsProjectIdRfisDefaultDistributionGet200ResponseInner.md)

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

