# procore_sdk.QualitySafetyInspectionsChecklistListFilterOptionsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_checklist_lists_filter_options_closed_by_contacts_get**](QualitySafetyInspectionsChecklistListFilterOptionsApi.md#rest_v10_projects_project_id_checklist_lists_filter_options_closed_by_contacts_get) | **GET** /rest/v1.0/projects/{project_id}/checklist/lists/filter_options/closed_by_contacts | List Checklist List Closed By Contact Filter Options
[**rest_v10_projects_project_id_checklist_lists_filter_options_inspectors_get**](QualitySafetyInspectionsChecklistListFilterOptionsApi.md#rest_v10_projects_project_id_checklist_lists_filter_options_inspectors_get) | **GET** /rest/v1.0/projects/{project_id}/checklist/lists/filter_options/inspectors | List Checklist List Inspector Filter Options
[**rest_v10_projects_project_id_checklist_lists_filter_options_list_templates_get**](QualitySafetyInspectionsChecklistListFilterOptionsApi.md#rest_v10_projects_project_id_checklist_lists_filter_options_list_templates_get) | **GET** /rest/v1.0/projects/{project_id}/checklist/lists/filter_options/list_templates | List Checklist List Template Filter Options
[**rest_v10_projects_project_id_checklist_lists_filter_options_locations_get**](QualitySafetyInspectionsChecklistListFilterOptionsApi.md#rest_v10_projects_project_id_checklist_lists_filter_options_locations_get) | **GET** /rest/v1.0/projects/{project_id}/checklist/lists/filter_options/locations | List Checklist List Location Filter Options
[**rest_v10_projects_project_id_checklist_lists_filter_options_points_of_contact_get**](QualitySafetyInspectionsChecklistListFilterOptionsApi.md#rest_v10_projects_project_id_checklist_lists_filter_options_points_of_contact_get) | **GET** /rest/v1.0/projects/{project_id}/checklist/lists/filter_options/points_of_contact | List Checklist List Point of Contact Filter Options
[**rest_v10_projects_project_id_checklist_lists_filter_options_responsible_contractors_get**](QualitySafetyInspectionsChecklistListFilterOptionsApi.md#rest_v10_projects_project_id_checklist_lists_filter_options_responsible_contractors_get) | **GET** /rest/v1.0/projects/{project_id}/checklist/lists/filter_options/responsible_contractors | List Checklist List Responsible Contractor Filter Options
[**rest_v10_projects_project_id_checklist_lists_filter_options_spec_sections_get**](QualitySafetyInspectionsChecklistListFilterOptionsApi.md#rest_v10_projects_project_id_checklist_lists_filter_options_spec_sections_get) | **GET** /rest/v1.0/projects/{project_id}/checklist/lists/filter_options/spec_sections | List Checklist List Specification Section Filter Options
[**rest_v10_projects_project_id_checklist_lists_filter_options_statuses_get**](QualitySafetyInspectionsChecklistListFilterOptionsApi.md#rest_v10_projects_project_id_checklist_lists_filter_options_statuses_get) | **GET** /rest/v1.0/projects/{project_id}/checklist/lists/filter_options/statuses | List Checklist List Status Filter Options
[**rest_v10_projects_project_id_checklist_lists_filter_options_trades_get**](QualitySafetyInspectionsChecklistListFilterOptionsApi.md#rest_v10_projects_project_id_checklist_lists_filter_options_trades_get) | **GET** /rest/v1.0/projects/{project_id}/checklist/lists/filter_options/trades | List Checklist List Trade Filter Options
[**rest_v10_projects_project_id_checklist_lists_filter_options_types_get**](QualitySafetyInspectionsChecklistListFilterOptionsApi.md#rest_v10_projects_project_id_checklist_lists_filter_options_types_get) | **GET** /rest/v1.0/projects/{project_id}/checklist/lists/filter_options/types | List Checklist List Inspection Type Filter Options


# **rest_v10_projects_project_id_checklist_lists_filter_options_closed_by_contacts_get**
> List[RestV10ProjectsProjectIdChecklistListsFilterOptionsClosedByContactsGet200ResponseInner] rest_v10_projects_project_id_checklist_lists_filter_options_closed_by_contacts_get(procore_company_id, project_id)

List Checklist List Closed By Contact Filter Options

Returns contacts that have closed inspections

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_checklist_lists_filter_options_closed_by_contacts_get200_response_inner import RestV10ProjectsProjectIdChecklistListsFilterOptionsClosedByContactsGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistListFilterOptionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.

    try:
        # List Checklist List Closed By Contact Filter Options
        api_response = api_instance.rest_v10_projects_project_id_checklist_lists_filter_options_closed_by_contacts_get(procore_company_id, project_id)
        print("The response of QualitySafetyInspectionsChecklistListFilterOptionsApi->rest_v10_projects_project_id_checklist_lists_filter_options_closed_by_contacts_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistListFilterOptionsApi->rest_v10_projects_project_id_checklist_lists_filter_options_closed_by_contacts_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**List[RestV10ProjectsProjectIdChecklistListsFilterOptionsClosedByContactsGet200ResponseInner]**](RestV10ProjectsProjectIdChecklistListsFilterOptionsClosedByContactsGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_checklist_lists_filter_options_inspectors_get**
> List[RestV10ProjectsProjectIdChecklistListsFilterOptionsClosedByContactsGet200ResponseInner] rest_v10_projects_project_id_checklist_lists_filter_options_inspectors_get(procore_company_id, project_id)

List Checklist List Inspector Filter Options

Returns inspectors associated to inspections

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_checklist_lists_filter_options_closed_by_contacts_get200_response_inner import RestV10ProjectsProjectIdChecklistListsFilterOptionsClosedByContactsGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistListFilterOptionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.

    try:
        # List Checklist List Inspector Filter Options
        api_response = api_instance.rest_v10_projects_project_id_checklist_lists_filter_options_inspectors_get(procore_company_id, project_id)
        print("The response of QualitySafetyInspectionsChecklistListFilterOptionsApi->rest_v10_projects_project_id_checklist_lists_filter_options_inspectors_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistListFilterOptionsApi->rest_v10_projects_project_id_checklist_lists_filter_options_inspectors_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**List[RestV10ProjectsProjectIdChecklistListsFilterOptionsClosedByContactsGet200ResponseInner]**](RestV10ProjectsProjectIdChecklistListsFilterOptionsClosedByContactsGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_checklist_lists_filter_options_list_templates_get**
> List[RestV10ProjectsProjectIdChecklistListsFilterOptionsClosedByContactsGet200ResponseInner] rest_v10_projects_project_id_checklist_lists_filter_options_list_templates_get(procore_company_id, project_id)

List Checklist List Template Filter Options

Returns list templates associated to inspections

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_checklist_lists_filter_options_closed_by_contacts_get200_response_inner import RestV10ProjectsProjectIdChecklistListsFilterOptionsClosedByContactsGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistListFilterOptionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.

    try:
        # List Checklist List Template Filter Options
        api_response = api_instance.rest_v10_projects_project_id_checklist_lists_filter_options_list_templates_get(procore_company_id, project_id)
        print("The response of QualitySafetyInspectionsChecklistListFilterOptionsApi->rest_v10_projects_project_id_checklist_lists_filter_options_list_templates_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistListFilterOptionsApi->rest_v10_projects_project_id_checklist_lists_filter_options_list_templates_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**List[RestV10ProjectsProjectIdChecklistListsFilterOptionsClosedByContactsGet200ResponseInner]**](RestV10ProjectsProjectIdChecklistListsFilterOptionsClosedByContactsGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_checklist_lists_filter_options_locations_get**
> List[RestV10ProjectsProjectIdChecklistListsFilterOptionsClosedByContactsGet200ResponseInner] rest_v10_projects_project_id_checklist_lists_filter_options_locations_get(procore_company_id, project_id)

List Checklist List Location Filter Options

Returns locations associated to inspections

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_checklist_lists_filter_options_closed_by_contacts_get200_response_inner import RestV10ProjectsProjectIdChecklistListsFilterOptionsClosedByContactsGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistListFilterOptionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.

    try:
        # List Checklist List Location Filter Options
        api_response = api_instance.rest_v10_projects_project_id_checklist_lists_filter_options_locations_get(procore_company_id, project_id)
        print("The response of QualitySafetyInspectionsChecklistListFilterOptionsApi->rest_v10_projects_project_id_checklist_lists_filter_options_locations_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistListFilterOptionsApi->rest_v10_projects_project_id_checklist_lists_filter_options_locations_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**List[RestV10ProjectsProjectIdChecklistListsFilterOptionsClosedByContactsGet200ResponseInner]**](RestV10ProjectsProjectIdChecklistListsFilterOptionsClosedByContactsGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_checklist_lists_filter_options_points_of_contact_get**
> List[RestV10ProjectsProjectIdChecklistListsFilterOptionsClosedByContactsGet200ResponseInner] rest_v10_projects_project_id_checklist_lists_filter_options_points_of_contact_get(procore_company_id, project_id)

List Checklist List Point of Contact Filter Options

Returns points of contact associated to inspections

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_checklist_lists_filter_options_closed_by_contacts_get200_response_inner import RestV10ProjectsProjectIdChecklistListsFilterOptionsClosedByContactsGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistListFilterOptionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.

    try:
        # List Checklist List Point of Contact Filter Options
        api_response = api_instance.rest_v10_projects_project_id_checklist_lists_filter_options_points_of_contact_get(procore_company_id, project_id)
        print("The response of QualitySafetyInspectionsChecklistListFilterOptionsApi->rest_v10_projects_project_id_checklist_lists_filter_options_points_of_contact_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistListFilterOptionsApi->rest_v10_projects_project_id_checklist_lists_filter_options_points_of_contact_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**List[RestV10ProjectsProjectIdChecklistListsFilterOptionsClosedByContactsGet200ResponseInner]**](RestV10ProjectsProjectIdChecklistListsFilterOptionsClosedByContactsGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_checklist_lists_filter_options_responsible_contractors_get**
> List[RestV10ProjectsProjectIdChecklistListsFilterOptionsClosedByContactsGet200ResponseInner] rest_v10_projects_project_id_checklist_lists_filter_options_responsible_contractors_get(procore_company_id, project_id)

List Checklist List Responsible Contractor Filter Options

Returns responsible contractors associated to inspections

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_checklist_lists_filter_options_closed_by_contacts_get200_response_inner import RestV10ProjectsProjectIdChecklistListsFilterOptionsClosedByContactsGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistListFilterOptionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.

    try:
        # List Checklist List Responsible Contractor Filter Options
        api_response = api_instance.rest_v10_projects_project_id_checklist_lists_filter_options_responsible_contractors_get(procore_company_id, project_id)
        print("The response of QualitySafetyInspectionsChecklistListFilterOptionsApi->rest_v10_projects_project_id_checklist_lists_filter_options_responsible_contractors_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistListFilterOptionsApi->rest_v10_projects_project_id_checklist_lists_filter_options_responsible_contractors_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**List[RestV10ProjectsProjectIdChecklistListsFilterOptionsClosedByContactsGet200ResponseInner]**](RestV10ProjectsProjectIdChecklistListsFilterOptionsClosedByContactsGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_checklist_lists_filter_options_spec_sections_get**
> List[RestV10ProjectsProjectIdChecklistListsFilterOptionsClosedByContactsGet200ResponseInner] rest_v10_projects_project_id_checklist_lists_filter_options_spec_sections_get(procore_company_id, project_id)

List Checklist List Specification Section Filter Options

Returns specification sections associated to inspections

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_checklist_lists_filter_options_closed_by_contacts_get200_response_inner import RestV10ProjectsProjectIdChecklistListsFilterOptionsClosedByContactsGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistListFilterOptionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.

    try:
        # List Checklist List Specification Section Filter Options
        api_response = api_instance.rest_v10_projects_project_id_checklist_lists_filter_options_spec_sections_get(procore_company_id, project_id)
        print("The response of QualitySafetyInspectionsChecklistListFilterOptionsApi->rest_v10_projects_project_id_checklist_lists_filter_options_spec_sections_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistListFilterOptionsApi->rest_v10_projects_project_id_checklist_lists_filter_options_spec_sections_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**List[RestV10ProjectsProjectIdChecklistListsFilterOptionsClosedByContactsGet200ResponseInner]**](RestV10ProjectsProjectIdChecklistListsFilterOptionsClosedByContactsGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_checklist_lists_filter_options_statuses_get**
> List[RestV10ProjectsProjectIdChecklistListsFilterOptionsClosedByContactsGet200ResponseInner] rest_v10_projects_project_id_checklist_lists_filter_options_statuses_get(procore_company_id, project_id)

List Checklist List Status Filter Options

Returns possible statuses of an inspection

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_checklist_lists_filter_options_closed_by_contacts_get200_response_inner import RestV10ProjectsProjectIdChecklistListsFilterOptionsClosedByContactsGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistListFilterOptionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.

    try:
        # List Checklist List Status Filter Options
        api_response = api_instance.rest_v10_projects_project_id_checklist_lists_filter_options_statuses_get(procore_company_id, project_id)
        print("The response of QualitySafetyInspectionsChecklistListFilterOptionsApi->rest_v10_projects_project_id_checklist_lists_filter_options_statuses_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistListFilterOptionsApi->rest_v10_projects_project_id_checklist_lists_filter_options_statuses_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**List[RestV10ProjectsProjectIdChecklistListsFilterOptionsClosedByContactsGet200ResponseInner]**](RestV10ProjectsProjectIdChecklistListsFilterOptionsClosedByContactsGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_checklist_lists_filter_options_trades_get**
> List[RestV10ProjectsProjectIdChecklistListsFilterOptionsClosedByContactsGet200ResponseInner] rest_v10_projects_project_id_checklist_lists_filter_options_trades_get(procore_company_id, project_id)

List Checklist List Trade Filter Options

Returns trades associated to inspections

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_checklist_lists_filter_options_closed_by_contacts_get200_response_inner import RestV10ProjectsProjectIdChecklistListsFilterOptionsClosedByContactsGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistListFilterOptionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.

    try:
        # List Checklist List Trade Filter Options
        api_response = api_instance.rest_v10_projects_project_id_checklist_lists_filter_options_trades_get(procore_company_id, project_id)
        print("The response of QualitySafetyInspectionsChecklistListFilterOptionsApi->rest_v10_projects_project_id_checklist_lists_filter_options_trades_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistListFilterOptionsApi->rest_v10_projects_project_id_checklist_lists_filter_options_trades_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**List[RestV10ProjectsProjectIdChecklistListsFilterOptionsClosedByContactsGet200ResponseInner]**](RestV10ProjectsProjectIdChecklistListsFilterOptionsClosedByContactsGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_checklist_lists_filter_options_types_get**
> List[RestV10ProjectsProjectIdChecklistListsFilterOptionsClosedByContactsGet200ResponseInner] rest_v10_projects_project_id_checklist_lists_filter_options_types_get(procore_company_id, project_id)

List Checklist List Inspection Type Filter Options

Returns inspection types associated to inspections

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_checklist_lists_filter_options_closed_by_contacts_get200_response_inner import RestV10ProjectsProjectIdChecklistListsFilterOptionsClosedByContactsGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistListFilterOptionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.

    try:
        # List Checklist List Inspection Type Filter Options
        api_response = api_instance.rest_v10_projects_project_id_checklist_lists_filter_options_types_get(procore_company_id, project_id)
        print("The response of QualitySafetyInspectionsChecklistListFilterOptionsApi->rest_v10_projects_project_id_checklist_lists_filter_options_types_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistListFilterOptionsApi->rest_v10_projects_project_id_checklist_lists_filter_options_types_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**List[RestV10ProjectsProjectIdChecklistListsFilterOptionsClosedByContactsGet200ResponseInner]**](RestV10ProjectsProjectIdChecklistListsFilterOptionsClosedByContactsGet200ResponseInner.md)

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

