# procore_sdk.CoreConfigurationsCustomFieldsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_custom_field_definitions_custom_field_definition_id_configurable_field_sets_get**](CoreConfigurationsCustomFieldsApi.md#rest_v10_companies_company_id_custom_field_definitions_custom_field_definition_id_configurable_field_sets_get) | **GET** /rest/v1.0/companies/{company_id}/custom_field_definitions/{custom_field_definition_id}/configurable_field_sets | List Custom Field Definition&#39;s Configurable Field Sets
[**rest_v10_custom_field_definitions_custom_field_definition_id_custom_field_lov_entries_get**](CoreConfigurationsCustomFieldsApi.md#rest_v10_custom_field_definitions_custom_field_definition_id_custom_field_lov_entries_get) | **GET** /rest/v1.0/custom_field_definitions/{custom_field_definition_id}/custom_field_lov_entries | List Custom Field Lov Entries
[**rest_v10_custom_field_definitions_custom_field_definition_id_custom_field_lov_entries_id_get**](CoreConfigurationsCustomFieldsApi.md#rest_v10_custom_field_definitions_custom_field_definition_id_custom_field_lov_entries_id_get) | **GET** /rest/v1.0/custom_field_definitions/{custom_field_definition_id}/custom_field_lov_entries/{id} | Show Custom Field Lov Entry
[**rest_v10_custom_field_definitions_get**](CoreConfigurationsCustomFieldsApi.md#rest_v10_custom_field_definitions_get) | **GET** /rest/v1.0/custom_field_definitions | List Custom Field Definitions
[**rest_v10_custom_field_definitions_id_get**](CoreConfigurationsCustomFieldsApi.md#rest_v10_custom_field_definitions_id_get) | **GET** /rest/v1.0/custom_field_definitions/{id} | Show Custom Field Definition
[**rest_v10_custom_field_metadata_get**](CoreConfigurationsCustomFieldsApi.md#rest_v10_custom_field_metadata_get) | **GET** /rest/v1.0/custom_field_metadata | List Custom Field Metadata
[**rest_v10_custom_field_metadata_id_get**](CoreConfigurationsCustomFieldsApi.md#rest_v10_custom_field_metadata_id_get) | **GET** /rest/v1.0/custom_field_metadata/{id} | Show Custom Field Metadatum
[**rest_v10_custom_fields_sections_get**](CoreConfigurationsCustomFieldsApi.md#rest_v10_custom_fields_sections_get) | **GET** /rest/v1.0/custom_fields_sections | List Custom Field Sections
[**rest_v10_custom_fields_sections_id_get**](CoreConfigurationsCustomFieldsApi.md#rest_v10_custom_fields_sections_id_get) | **GET** /rest/v1.0/custom_fields_sections/{id} | Show Custom Fields Section
[**rest_v11_companies_company_id_custom_field_definitions_get**](CoreConfigurationsCustomFieldsApi.md#rest_v11_companies_company_id_custom_field_definitions_get) | **GET** /rest/v1.1/companies/{company_id}/custom_field_definitions | List Custom Field Definitions


# **rest_v10_companies_company_id_custom_field_definitions_custom_field_definition_id_configurable_field_sets_get**
> List[ConfigurableFieldSet2] rest_v10_companies_company_id_custom_field_definitions_custom_field_definition_id_configurable_field_sets_get(procore_company_id, company_id, custom_field_definition_id)

List Custom Field Definition's Configurable Field Sets

Return a list of all Configurable Field Sets for a given Custom Field Definition associated with the Current Company.

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
    api_instance = procore_sdk.CoreConfigurationsCustomFieldsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    custom_field_definition_id = 56 # int | Custom Field Definition ID

    try:
        # List Custom Field Definition's Configurable Field Sets
        api_response = api_instance.rest_v10_companies_company_id_custom_field_definitions_custom_field_definition_id_configurable_field_sets_get(procore_company_id, company_id, custom_field_definition_id)
        print("The response of CoreConfigurationsCustomFieldsApi->rest_v10_companies_company_id_custom_field_definitions_custom_field_definition_id_configurable_field_sets_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreConfigurationsCustomFieldsApi->rest_v10_companies_company_id_custom_field_definitions_custom_field_definition_id_configurable_field_sets_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **custom_field_definition_id** | **int**| Custom Field Definition ID | 

### Return type

[**List[ConfigurableFieldSet2]**](ConfigurableFieldSet2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Per-Page - Number of items retrieved per page <br>  * Total - Total number of items to be retrieved <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_custom_field_definitions_custom_field_definition_id_custom_field_lov_entries_get**
> RestV10CustomFieldDefinitionsCustomFieldDefinitionIdCustomFieldLovEntriesGet200Response rest_v10_custom_field_definitions_custom_field_definition_id_custom_field_lov_entries_get(procore_company_id, company_id, custom_field_definition_id, page=page, per_page=per_page, filters_start_with=filters_start_with, filters_active=filters_active, filters_label_with=filters_label_with)

List Custom Field Lov Entries

Return a list of all Custom Field Lov Entries associated with the Current Company and the Custom Field Definition passed by path param.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_custom_field_definitions_custom_field_definition_id_custom_field_lov_entries_get200_response import RestV10CustomFieldDefinitionsCustomFieldDefinitionIdCustomFieldLovEntriesGet200Response
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
    api_instance = procore_sdk.CoreConfigurationsCustomFieldsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    custom_field_definition_id = 56 # int | Unique identifier for the Custom Field Definition.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_start_with = 'filters_start_with_example' # str | return lov entries that label start with letters (optional)
    filters_active = True # bool | return lov entries that active status is (true or false) (optional)
    filters_label_with = 'filters_label_with_example' # str | return lov entries that contains the label with the text (optional)

    try:
        # List Custom Field Lov Entries
        api_response = api_instance.rest_v10_custom_field_definitions_custom_field_definition_id_custom_field_lov_entries_get(procore_company_id, company_id, custom_field_definition_id, page=page, per_page=per_page, filters_start_with=filters_start_with, filters_active=filters_active, filters_label_with=filters_label_with)
        print("The response of CoreConfigurationsCustomFieldsApi->rest_v10_custom_field_definitions_custom_field_definition_id_custom_field_lov_entries_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreConfigurationsCustomFieldsApi->rest_v10_custom_field_definitions_custom_field_definition_id_custom_field_lov_entries_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **custom_field_definition_id** | **int**| Unique identifier for the Custom Field Definition. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_start_with** | **str**| return lov entries that label start with letters | [optional] 
 **filters_active** | **bool**| return lov entries that active status is (true or false) | [optional] 
 **filters_label_with** | **str**| return lov entries that contains the label with the text | [optional] 

### Return type

[**RestV10CustomFieldDefinitionsCustomFieldDefinitionIdCustomFieldLovEntriesGet200Response**](RestV10CustomFieldDefinitionsCustomFieldDefinitionIdCustomFieldLovEntriesGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Per-Page - Number of items retrieved per page <br>  * Total - Total number of items to be retrieved <br>  * Link - Link headers for the first, prev, next, and last link <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_custom_field_definitions_custom_field_definition_id_custom_field_lov_entries_id_get**
> CustomFieldLovEntry rest_v10_custom_field_definitions_custom_field_definition_id_custom_field_lov_entries_id_get(procore_company_id, custom_field_definition_id, id, company_id)

Show Custom Field Lov Entry

Returns the details for a specified Custom Field Lov Entry

### Example


```python
import procore_sdk
from procore_sdk.models.custom_field_lov_entry import CustomFieldLovEntry
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
    api_instance = procore_sdk.CoreConfigurationsCustomFieldsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    custom_field_definition_id = 56 # int | Unique identifier for the Custom Field Definition.
    id = 56 # int | Unique identifier for the Custom Field List of Values (LOV) Entry.
    company_id = 56 # int | Unique identifier for the company.

    try:
        # Show Custom Field Lov Entry
        api_response = api_instance.rest_v10_custom_field_definitions_custom_field_definition_id_custom_field_lov_entries_id_get(procore_company_id, custom_field_definition_id, id, company_id)
        print("The response of CoreConfigurationsCustomFieldsApi->rest_v10_custom_field_definitions_custom_field_definition_id_custom_field_lov_entries_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreConfigurationsCustomFieldsApi->rest_v10_custom_field_definitions_custom_field_definition_id_custom_field_lov_entries_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **custom_field_definition_id** | **int**| Unique identifier for the Custom Field Definition. | 
 **id** | **int**| Unique identifier for the Custom Field List of Values (LOV) Entry. | 
 **company_id** | **int**| Unique identifier for the company. | 

### Return type

[**CustomFieldLovEntry**](CustomFieldLovEntry.md)

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

# **rest_v10_custom_field_definitions_get**
> RestV10CustomFieldDefinitionsGet200Response rest_v10_custom_field_definitions_get(procore_company_id, company_id, page=page, per_page=per_page, view=view, tool_name=tool_name, includes_configurable_field_sets_count=includes_configurable_field_sets_count, filters_with_label=filters_with_label, scope_type=scope_type, scope_category=scope_category, scope_inspection_type_id=scope_inspection_type_id, scope_generic_tool_id=scope_generic_tool_id, scope_action_plan_type_id=scope_action_plan_type_id, sort=sort)

List Custom Field Definitions

DEPRECATED This endpoint has been deprecated, it will be sunset at 9/1/2024. Instead, please use rest/v1.1/companies/{company_id}/custom_field_definitions

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_custom_field_definitions_get200_response import RestV10CustomFieldDefinitionsGet200Response
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
    api_instance = procore_sdk.CoreConfigurationsCustomFieldsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    view = 'view_example' # str | The extended view provides what is shown below. The default view returns the same as the extended view but excludes the attribute custom_field_lov_entries. The with_lov_entries view is the same as extended. (optional)
    tool_name = 'tool_name_example' # str | The name of the company/project level tool that is allowed read permissions to custom field definitions. (optional)
    includes_configurable_field_sets_count = False # bool | If true, response will include the number of field sets using item (custom field). (optional) (default to False)
    filters_with_label = 'filters_with_label_example' # str | Return custom field definitions that label contains text (optional)
    scope_type = 'scope_type_example' # str | Return custom field definitions that contains fieldset type (optional)
    scope_category = 'scope_category_example' # str | Return custom field definitions that contains category (optional)
    scope_inspection_type_id = 56 # int | Return custom field definitions that contains inspection_type_id (optional)
    scope_generic_tool_id = 56 # int | Return custom field definitions that contains generic_tool_id (optional)
    scope_action_plan_type_id = 56 # int | Return custom field definitions that contains action_plan_type_id (optional)
    sort = 'sort_example' # str | Direction (asc/desc) can be controlled by the presence or absence of '-' before the sort parameter. (optional)

    try:
        # List Custom Field Definitions
        api_response = api_instance.rest_v10_custom_field_definitions_get(procore_company_id, company_id, page=page, per_page=per_page, view=view, tool_name=tool_name, includes_configurable_field_sets_count=includes_configurable_field_sets_count, filters_with_label=filters_with_label, scope_type=scope_type, scope_category=scope_category, scope_inspection_type_id=scope_inspection_type_id, scope_generic_tool_id=scope_generic_tool_id, scope_action_plan_type_id=scope_action_plan_type_id, sort=sort)
        print("The response of CoreConfigurationsCustomFieldsApi->rest_v10_custom_field_definitions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreConfigurationsCustomFieldsApi->rest_v10_custom_field_definitions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **view** | **str**| The extended view provides what is shown below. The default view returns the same as the extended view but excludes the attribute custom_field_lov_entries. The with_lov_entries view is the same as extended. | [optional] 
 **tool_name** | **str**| The name of the company/project level tool that is allowed read permissions to custom field definitions. | [optional] 
 **includes_configurable_field_sets_count** | **bool**| If true, response will include the number of field sets using item (custom field). | [optional] [default to False]
 **filters_with_label** | **str**| Return custom field definitions that label contains text | [optional] 
 **scope_type** | **str**| Return custom field definitions that contains fieldset type | [optional] 
 **scope_category** | **str**| Return custom field definitions that contains category | [optional] 
 **scope_inspection_type_id** | **int**| Return custom field definitions that contains inspection_type_id | [optional] 
 **scope_generic_tool_id** | **int**| Return custom field definitions that contains generic_tool_id | [optional] 
 **scope_action_plan_type_id** | **int**| Return custom field definitions that contains action_plan_type_id | [optional] 
 **sort** | **str**| Direction (asc/desc) can be controlled by the presence or absence of &#39;-&#39; before the sort parameter. | [optional] 

### Return type

[**RestV10CustomFieldDefinitionsGet200Response**](RestV10CustomFieldDefinitionsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Per-Page - Number of items retrieved per page <br>  * Total - Total number of items to be retrieved <br>  * Link - Link headers for the first, prev, next, and last link <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_custom_field_definitions_id_get**
> CustomFieldDefinition1 rest_v10_custom_field_definitions_id_get(procore_company_id, id, company_id, view=view, includes_configurable_field_sets_count=includes_configurable_field_sets_count)

Show Custom Field Definition

Returns the details for a specified Custom Field Definition

### Example


```python
import procore_sdk
from procore_sdk.models.custom_field_definition1 import CustomFieldDefinition1
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
    api_instance = procore_sdk.CoreConfigurationsCustomFieldsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | Custom Field Definition ID
    company_id = 56 # int | Unique identifier for the company.
    view = 'view_example' # str | The extended view provides what is shown below. The default view returns the same as the extended view but excludes the attribute custom_field_lov_entries. The with_lov_entries view is the same as extended. (optional)
    includes_configurable_field_sets_count = False # bool | If true, response will include the number of field sets using item (custom field). (optional) (default to False)

    try:
        # Show Custom Field Definition
        api_response = api_instance.rest_v10_custom_field_definitions_id_get(procore_company_id, id, company_id, view=view, includes_configurable_field_sets_count=includes_configurable_field_sets_count)
        print("The response of CoreConfigurationsCustomFieldsApi->rest_v10_custom_field_definitions_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreConfigurationsCustomFieldsApi->rest_v10_custom_field_definitions_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| Custom Field Definition ID | 
 **company_id** | **int**| Unique identifier for the company. | 
 **view** | **str**| The extended view provides what is shown below. The default view returns the same as the extended view but excludes the attribute custom_field_lov_entries. The with_lov_entries view is the same as extended. | [optional] 
 **includes_configurable_field_sets_count** | **bool**| If true, response will include the number of field sets using item (custom field). | [optional] [default to False]

### Return type

[**CustomFieldDefinition1**](CustomFieldDefinition1.md)

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

# **rest_v10_custom_field_metadata_get**
> List[CustomFieldMetadatum] rest_v10_custom_field_metadata_get(procore_company_id, company_id, page=page, per_page=per_page, view=view, filters_field_set_type=filters_field_set_type, filters_field_set_id=filters_field_set_id, filters_custom_field_definitions_id=filters_custom_field_definitions_id)

List Custom Field Metadata

Return a list of all Custom Field Metadata associated with the Current Company.

### Example


```python
import procore_sdk
from procore_sdk.models.custom_field_metadatum import CustomFieldMetadatum
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
    api_instance = procore_sdk.CoreConfigurationsCustomFieldsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    view = 'view_example' # str | The extended view provides what is shown below. The default view returns the same as the extended view but excludes the attributes company_id, host_type, source_type, source_id, label, data_type. The with_lov_entries returns the default attributes but adding lov_entries. (optional)
    filters_field_set_type = ['filters_field_set_type_example'] # List[str] | Return a list of all Custom Field Metadata associated with the Current Company and source_type provided. (optional)
    filters_field_set_id = [56] # List[int] | Return a list of all Custom Field Metadata associated with the Current Company and source_id provided. (optional)
    filters_custom_field_definitions_id = 56 # int | Return a list of all Custom Field Metadata associated with the Current Company and custom_field_definition_id provided. (optional)

    try:
        # List Custom Field Metadata
        api_response = api_instance.rest_v10_custom_field_metadata_get(procore_company_id, company_id, page=page, per_page=per_page, view=view, filters_field_set_type=filters_field_set_type, filters_field_set_id=filters_field_set_id, filters_custom_field_definitions_id=filters_custom_field_definitions_id)
        print("The response of CoreConfigurationsCustomFieldsApi->rest_v10_custom_field_metadata_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreConfigurationsCustomFieldsApi->rest_v10_custom_field_metadata_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **view** | **str**| The extended view provides what is shown below. The default view returns the same as the extended view but excludes the attributes company_id, host_type, source_type, source_id, label, data_type. The with_lov_entries returns the default attributes but adding lov_entries. | [optional] 
 **filters_field_set_type** | [**List[str]**](str.md)| Return a list of all Custom Field Metadata associated with the Current Company and source_type provided. | [optional] 
 **filters_field_set_id** | [**List[int]**](int.md)| Return a list of all Custom Field Metadata associated with the Current Company and source_id provided. | [optional] 
 **filters_custom_field_definitions_id** | **int**| Return a list of all Custom Field Metadata associated with the Current Company and custom_field_definition_id provided. | [optional] 

### Return type

[**List[CustomFieldMetadatum]**](CustomFieldMetadatum.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Per-Page - Number of items retrieved per page <br>  * Total - Total number of items to be retrieved <br>  * Link - Link headers for the first, prev, next, and last link <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_custom_field_metadata_id_get**
> CustomFieldMetadatum rest_v10_custom_field_metadata_id_get(procore_company_id, id, company_id, view=view)

Show Custom Field Metadatum

Returns the details for a specified Custom Field Metadatum

### Example


```python
import procore_sdk
from procore_sdk.models.custom_field_metadatum import CustomFieldMetadatum
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
    api_instance = procore_sdk.CoreConfigurationsCustomFieldsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | Custom Field Metadatum ID
    company_id = 56 # int | Unique identifier for the company.
    view = 'view_example' # str | The extended view provides what is shown below. The default view returns the same as the extended view but excludes the attributes company_id, host_type, source_type, source_id, label, data_type. The with_lov_entries returns the default attributes but adding lov_entries. (optional)

    try:
        # Show Custom Field Metadatum
        api_response = api_instance.rest_v10_custom_field_metadata_id_get(procore_company_id, id, company_id, view=view)
        print("The response of CoreConfigurationsCustomFieldsApi->rest_v10_custom_field_metadata_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreConfigurationsCustomFieldsApi->rest_v10_custom_field_metadata_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| Custom Field Metadatum ID | 
 **company_id** | **int**| Unique identifier for the company. | 
 **view** | **str**| The extended view provides what is shown below. The default view returns the same as the extended view but excludes the attributes company_id, host_type, source_type, source_id, label, data_type. The with_lov_entries returns the default attributes but adding lov_entries. | [optional] 

### Return type

[**CustomFieldMetadatum**](CustomFieldMetadatum.md)

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

# **rest_v10_custom_fields_sections_get**
> List[CustomFieldsSection] rest_v10_custom_fields_sections_get(procore_company_id, company_id, page=page, per_page=per_page)

List Custom Field Sections

Return a list of all Custom Field Sections associated with the Current Company.

### Example


```python
import procore_sdk
from procore_sdk.models.custom_fields_section import CustomFieldsSection
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
    api_instance = procore_sdk.CoreConfigurationsCustomFieldsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Custom Field Sections
        api_response = api_instance.rest_v10_custom_fields_sections_get(procore_company_id, company_id, page=page, per_page=per_page)
        print("The response of CoreConfigurationsCustomFieldsApi->rest_v10_custom_fields_sections_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreConfigurationsCustomFieldsApi->rest_v10_custom_fields_sections_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[CustomFieldsSection]**](CustomFieldsSection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Per-Page - Number of items retrieved per page <br>  * Total - Total number of items to be retrieved <br>  * Link - Link headers for the first, prev, next, and last link <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_custom_fields_sections_id_get**
> CustomFieldsSection rest_v10_custom_fields_sections_id_get(procore_company_id, company_id, id)

Show Custom Fields Section

Returns the details for a specified Custom Field Section

### Example


```python
import procore_sdk
from procore_sdk.models.custom_fields_section import CustomFieldsSection
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
    api_instance = procore_sdk.CoreConfigurationsCustomFieldsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | Custom Fields Section ID

    try:
        # Show Custom Fields Section
        api_response = api_instance.rest_v10_custom_fields_sections_id_get(procore_company_id, company_id, id)
        print("The response of CoreConfigurationsCustomFieldsApi->rest_v10_custom_fields_sections_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreConfigurationsCustomFieldsApi->rest_v10_custom_fields_sections_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| Custom Fields Section ID | 

### Return type

[**CustomFieldsSection**](CustomFieldsSection.md)

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

# **rest_v11_companies_company_id_custom_field_definitions_get**
> List[CustomFieldDefinition] rest_v11_companies_company_id_custom_field_definitions_get(procore_company_id, company_id, page=page, per_page=per_page, tool_name=tool_name, includes_configurable_field_sets_count=includes_configurable_field_sets_count, filters_with_label=filters_with_label, sort=sort)

List Custom Field Definitions

Return a list of Custom Field Definitions for a given company.

### Example


```python
import procore_sdk
from procore_sdk.models.custom_field_definition import CustomFieldDefinition
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
    api_instance = procore_sdk.CoreConfigurationsCustomFieldsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Items per page, default: 100, max: 100 (optional)
    tool_name = 'tool_name_example' # str | The name of the company/project level tool that is allowed read permissions to custom field definitions. (optional)
    includes_configurable_field_sets_count = False # bool | If true, response will include the number of field sets using item (custom field). (optional) (default to False)
    filters_with_label = 'filters_with_label_example' # str | Return custom field definitions that label contains text (optional)
    sort = 'sort_example' # str | Direction (asc/desc) can be controlled by the presence or absence of '-' before the sort parameter. (optional)

    try:
        # List Custom Field Definitions
        api_response = api_instance.rest_v11_companies_company_id_custom_field_definitions_get(procore_company_id, company_id, page=page, per_page=per_page, tool_name=tool_name, includes_configurable_field_sets_count=includes_configurable_field_sets_count, filters_with_label=filters_with_label, sort=sort)
        print("The response of CoreConfigurationsCustomFieldsApi->rest_v11_companies_company_id_custom_field_definitions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreConfigurationsCustomFieldsApi->rest_v11_companies_company_id_custom_field_definitions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Items per page, default: 100, max: 100 | [optional] 
 **tool_name** | **str**| The name of the company/project level tool that is allowed read permissions to custom field definitions. | [optional] 
 **includes_configurable_field_sets_count** | **bool**| If true, response will include the number of field sets using item (custom field). | [optional] [default to False]
 **filters_with_label** | **str**| Return custom field definitions that label contains text | [optional] 
 **sort** | **str**| Direction (asc/desc) can be controlled by the presence or absence of &#39;-&#39; before the sort parameter. | [optional] 

### Return type

[**List[CustomFieldDefinition]**](CustomFieldDefinition.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Per-Page - Number of items retrieved per page <br>  * Total - Total number of items to be retrieved <br>  * Link - Link headers for the first, prev, next, and last link <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

