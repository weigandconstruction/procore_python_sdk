# procore_sdk.CoreConfigurationsCustomFieldLovEntriesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_custom_field_definitions_custom_field_definition_id_custom_field_lov_entries_bulk_create_post**](CoreConfigurationsCustomFieldLovEntriesApi.md#rest_v10_custom_field_definitions_custom_field_definition_id_custom_field_lov_entries_bulk_create_post) | **POST** /rest/v1.0/custom_field_definitions/{custom_field_definition_id}/custom_field_lov_entries/bulk_create | Bulk Create Custom Field Lov Entries


# **rest_v10_custom_field_definitions_custom_field_definition_id_custom_field_lov_entries_bulk_create_post**
> List[CustomFieldLovEntry] rest_v10_custom_field_definitions_custom_field_definition_id_custom_field_lov_entries_bulk_create_post(procore_company_id, custom_field_definition_id, rest_v10_custom_field_definitions_custom_field_definition_id_custom_field_lov_entries_bulk_create_post_request=rest_v10_custom_field_definitions_custom_field_definition_id_custom_field_lov_entries_bulk_create_post_request)

Bulk Create Custom Field Lov Entries

Bulk Creates a Custom Field Lov Entries. Position is sorted descending, highest position is visually the top of the list.

### Example


```python
import procore_sdk
from procore_sdk.models.custom_field_lov_entry import CustomFieldLovEntry
from procore_sdk.models.rest_v10_custom_field_definitions_custom_field_definition_id_custom_field_lov_entries_bulk_create_post_request import RestV10CustomFieldDefinitionsCustomFieldDefinitionIdCustomFieldLovEntriesBulkCreatePostRequest
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
    api_instance = procore_sdk.CoreConfigurationsCustomFieldLovEntriesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    custom_field_definition_id = 56 # int | Unique identifier for the Custom Field Definition.
    rest_v10_custom_field_definitions_custom_field_definition_id_custom_field_lov_entries_bulk_create_post_request = procore_sdk.RestV10CustomFieldDefinitionsCustomFieldDefinitionIdCustomFieldLovEntriesBulkCreatePostRequest() # RestV10CustomFieldDefinitionsCustomFieldDefinitionIdCustomFieldLovEntriesBulkCreatePostRequest |  (optional)

    try:
        # Bulk Create Custom Field Lov Entries
        api_response = api_instance.rest_v10_custom_field_definitions_custom_field_definition_id_custom_field_lov_entries_bulk_create_post(procore_company_id, custom_field_definition_id, rest_v10_custom_field_definitions_custom_field_definition_id_custom_field_lov_entries_bulk_create_post_request=rest_v10_custom_field_definitions_custom_field_definition_id_custom_field_lov_entries_bulk_create_post_request)
        print("The response of CoreConfigurationsCustomFieldLovEntriesApi->rest_v10_custom_field_definitions_custom_field_definition_id_custom_field_lov_entries_bulk_create_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreConfigurationsCustomFieldLovEntriesApi->rest_v10_custom_field_definitions_custom_field_definition_id_custom_field_lov_entries_bulk_create_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **custom_field_definition_id** | **int**| Unique identifier for the Custom Field Definition. | 
 **rest_v10_custom_field_definitions_custom_field_definition_id_custom_field_lov_entries_bulk_create_post_request** | [**RestV10CustomFieldDefinitionsCustomFieldDefinitionIdCustomFieldLovEntriesBulkCreatePostRequest**](RestV10CustomFieldDefinitionsCustomFieldDefinitionIdCustomFieldLovEntriesBulkCreatePostRequest.md)|  | [optional] 

### Return type

[**List[CustomFieldLovEntry]**](CustomFieldLovEntry.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

