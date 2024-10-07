# procore_sdk.QualitySafetyInspectionsChecklistSectionsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_checklist_lists_list_id_sections_id_delete**](QualitySafetyInspectionsChecklistSectionsApi.md#rest_v10_checklist_lists_list_id_sections_id_delete) | **DELETE** /rest/v1.0/checklist/lists/{list_id}/sections/{id} | Delete Checklist Section
[**rest_v10_checklist_lists_list_id_sections_id_get**](QualitySafetyInspectionsChecklistSectionsApi.md#rest_v10_checklist_lists_list_id_sections_id_get) | **GET** /rest/v1.0/checklist/lists/{list_id}/sections/{id} | Show Checklist Section
[**rest_v10_checklist_lists_list_id_sections_id_patch**](QualitySafetyInspectionsChecklistSectionsApi.md#rest_v10_checklist_lists_list_id_sections_id_patch) | **PATCH** /rest/v1.0/checklist/lists/{list_id}/sections/{id} | Update Checklist Section
[**rest_v10_checklist_lists_list_id_sections_post**](QualitySafetyInspectionsChecklistSectionsApi.md#rest_v10_checklist_lists_list_id_sections_post) | **POST** /rest/v1.0/checklist/lists/{list_id}/sections | Create Checklist Section
[**rest_v10_checklist_lists_list_id_sections_section_id_toggle_not_applicable_patch**](QualitySafetyInspectionsChecklistSectionsApi.md#rest_v10_checklist_lists_list_id_sections_section_id_toggle_not_applicable_patch) | **PATCH** /rest/v1.0/checklist/lists/{list_id}/sections/{section_id}/toggle_not_applicable | Toggle Checklist Section Not Applicable status
[**rest_v10_checklist_lists_list_id_sections_section_id_toggle_not_applicable_put**](QualitySafetyInspectionsChecklistSectionsApi.md#rest_v10_checklist_lists_list_id_sections_section_id_toggle_not_applicable_put) | **PUT** /rest/v1.0/checklist/lists/{list_id}/sections/{section_id}/toggle_not_applicable | Toggle Checklist Section Not Applicable status
[**rest_v10_projects_project_id_checklist_list_sections_get**](QualitySafetyInspectionsChecklistSectionsApi.md#rest_v10_projects_project_id_checklist_list_sections_get) | **GET** /rest/v1.0/projects/{project_id}/checklist/list_sections | List Checklist (Inspection) Sections
[**rest_v11_projects_project_id_recycle_bin_checklist_list_sections_get**](QualitySafetyInspectionsChecklistSectionsApi.md#rest_v11_projects_project_id_recycle_bin_checklist_list_sections_get) | **GET** /rest/v1.1/projects/{project_id}/recycle_bin/checklist/list_sections | List Recycled Checklist (Inspection) Sections


# **rest_v10_checklist_lists_list_id_sections_id_delete**
> rest_v10_checklist_lists_list_id_sections_id_delete(procore_company_id, list_id, id, project_id)

Delete Checklist Section

This is a deprecated endpoint.

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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistSectionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    list_id = 56 # int | Checklist ID
    id = 56 # int | Checklist Section ID
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Delete Checklist Section
        api_instance.rest_v10_checklist_lists_list_id_sections_id_delete(procore_company_id, list_id, id, project_id)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistSectionsApi->rest_v10_checklist_lists_list_id_sections_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **list_id** | **int**| Checklist ID | 
 **id** | **int**| Checklist Section ID | 
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
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_checklist_lists_list_id_sections_id_get**
> ChecklistSection2 rest_v10_checklist_lists_list_id_sections_id_get(procore_company_id, list_id, id, project_id)

Show Checklist Section

Retrieves Checklist Section in a specified Checklist.

### Example


```python
import procore_sdk
from procore_sdk.models.checklist_section2 import ChecklistSection2
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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistSectionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    list_id = 56 # int | Checklist ID
    id = 56 # int | Checklist Section ID
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Show Checklist Section
        api_response = api_instance.rest_v10_checklist_lists_list_id_sections_id_get(procore_company_id, list_id, id, project_id)
        print("The response of QualitySafetyInspectionsChecklistSectionsApi->rest_v10_checklist_lists_list_id_sections_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistSectionsApi->rest_v10_checklist_lists_list_id_sections_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **list_id** | **int**| Checklist ID | 
 **id** | **int**| Checklist Section ID | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**ChecklistSection2**](ChecklistSection2.md)

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

# **rest_v10_checklist_lists_list_id_sections_id_patch**
> ChecklistSection2 rest_v10_checklist_lists_list_id_sections_id_patch(procore_company_id, list_id, id, checklist_section_body)

Update Checklist Section

This is a deprecated endpoint.

### Example


```python
import procore_sdk
from procore_sdk.models.checklist_section2 import ChecklistSection2
from procore_sdk.models.checklist_section_body import ChecklistSectionBody
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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistSectionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    list_id = 56 # int | Checklist ID
    id = 56 # int | Checklist Section ID
    checklist_section_body = procore_sdk.ChecklistSectionBody() # ChecklistSectionBody | 

    try:
        # Update Checklist Section
        api_response = api_instance.rest_v10_checklist_lists_list_id_sections_id_patch(procore_company_id, list_id, id, checklist_section_body)
        print("The response of QualitySafetyInspectionsChecklistSectionsApi->rest_v10_checklist_lists_list_id_sections_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistSectionsApi->rest_v10_checklist_lists_list_id_sections_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **list_id** | **int**| Checklist ID | 
 **id** | **int**| Checklist Section ID | 
 **checklist_section_body** | [**ChecklistSectionBody**](ChecklistSectionBody.md)|  | 

### Return type

[**ChecklistSection2**](ChecklistSection2.md)

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
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_checklist_lists_list_id_sections_post**
> ChecklistSection2 rest_v10_checklist_lists_list_id_sections_post(procore_company_id, list_id, checklist_section_body)

Create Checklist Section

This is a deprecated endpoint.

### Example


```python
import procore_sdk
from procore_sdk.models.checklist_section2 import ChecklistSection2
from procore_sdk.models.checklist_section_body import ChecklistSectionBody
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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistSectionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    list_id = 56 # int | Checklist ID
    checklist_section_body = procore_sdk.ChecklistSectionBody() # ChecklistSectionBody | 

    try:
        # Create Checklist Section
        api_response = api_instance.rest_v10_checklist_lists_list_id_sections_post(procore_company_id, list_id, checklist_section_body)
        print("The response of QualitySafetyInspectionsChecklistSectionsApi->rest_v10_checklist_lists_list_id_sections_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistSectionsApi->rest_v10_checklist_lists_list_id_sections_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **list_id** | **int**| Checklist ID | 
 **checklist_section_body** | [**ChecklistSectionBody**](ChecklistSectionBody.md)|  | 

### Return type

[**ChecklistSection2**](ChecklistSection2.md)

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
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_checklist_lists_list_id_sections_section_id_toggle_not_applicable_patch**
> ChecklistSection2 rest_v10_checklist_lists_list_id_sections_section_id_toggle_not_applicable_patch(procore_company_id, list_id, section_id, rest_v10_checklist_lists_list_id_sections_section_id_toggle_not_applicable_put_request)

Toggle Checklist Section Not Applicable status

Toggles Checklist Section Not Applicable status in a specified Checklist and Checklist Section.

### Example


```python
import procore_sdk
from procore_sdk.models.checklist_section2 import ChecklistSection2
from procore_sdk.models.rest_v10_checklist_lists_list_id_sections_section_id_toggle_not_applicable_put_request import RestV10ChecklistListsListIdSectionsSectionIdToggleNotApplicablePutRequest
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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistSectionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    list_id = 56 # int | Checklist ID
    section_id = 56 # int | Checklist Section ID
    rest_v10_checklist_lists_list_id_sections_section_id_toggle_not_applicable_put_request = procore_sdk.RestV10ChecklistListsListIdSectionsSectionIdToggleNotApplicablePutRequest() # RestV10ChecklistListsListIdSectionsSectionIdToggleNotApplicablePutRequest | 

    try:
        # Toggle Checklist Section Not Applicable status
        api_response = api_instance.rest_v10_checklist_lists_list_id_sections_section_id_toggle_not_applicable_patch(procore_company_id, list_id, section_id, rest_v10_checklist_lists_list_id_sections_section_id_toggle_not_applicable_put_request)
        print("The response of QualitySafetyInspectionsChecklistSectionsApi->rest_v10_checklist_lists_list_id_sections_section_id_toggle_not_applicable_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistSectionsApi->rest_v10_checklist_lists_list_id_sections_section_id_toggle_not_applicable_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **list_id** | **int**| Checklist ID | 
 **section_id** | **int**| Checklist Section ID | 
 **rest_v10_checklist_lists_list_id_sections_section_id_toggle_not_applicable_put_request** | [**RestV10ChecklistListsListIdSectionsSectionIdToggleNotApplicablePutRequest**](RestV10ChecklistListsListIdSectionsSectionIdToggleNotApplicablePutRequest.md)|  | 

### Return type

[**ChecklistSection2**](ChecklistSection2.md)

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
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_checklist_lists_list_id_sections_section_id_toggle_not_applicable_put**
> ChecklistSection2 rest_v10_checklist_lists_list_id_sections_section_id_toggle_not_applicable_put(procore_company_id, list_id, section_id, rest_v10_checklist_lists_list_id_sections_section_id_toggle_not_applicable_put_request)

Toggle Checklist Section Not Applicable status

Toggles Checklist Section Not Applicable status in a specified Checklist and Checklist Section.

### Example


```python
import procore_sdk
from procore_sdk.models.checklist_section2 import ChecklistSection2
from procore_sdk.models.rest_v10_checklist_lists_list_id_sections_section_id_toggle_not_applicable_put_request import RestV10ChecklistListsListIdSectionsSectionIdToggleNotApplicablePutRequest
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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistSectionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    list_id = 56 # int | Checklist ID
    section_id = 56 # int | Checklist Section ID
    rest_v10_checklist_lists_list_id_sections_section_id_toggle_not_applicable_put_request = procore_sdk.RestV10ChecklistListsListIdSectionsSectionIdToggleNotApplicablePutRequest() # RestV10ChecklistListsListIdSectionsSectionIdToggleNotApplicablePutRequest | 

    try:
        # Toggle Checklist Section Not Applicable status
        api_response = api_instance.rest_v10_checklist_lists_list_id_sections_section_id_toggle_not_applicable_put(procore_company_id, list_id, section_id, rest_v10_checklist_lists_list_id_sections_section_id_toggle_not_applicable_put_request)
        print("The response of QualitySafetyInspectionsChecklistSectionsApi->rest_v10_checklist_lists_list_id_sections_section_id_toggle_not_applicable_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistSectionsApi->rest_v10_checklist_lists_list_id_sections_section_id_toggle_not_applicable_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **list_id** | **int**| Checklist ID | 
 **section_id** | **int**| Checklist Section ID | 
 **rest_v10_checklist_lists_list_id_sections_section_id_toggle_not_applicable_put_request** | [**RestV10ChecklistListsListIdSectionsSectionIdToggleNotApplicablePutRequest**](RestV10ChecklistListsListIdSectionsSectionIdToggleNotApplicablePutRequest.md)|  | 

### Return type

[**ChecklistSection2**](ChecklistSection2.md)

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
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_checklist_list_sections_get**
> List[ChecklistSection1] rest_v10_projects_project_id_checklist_list_sections_get(procore_company_id, project_id, page=page, per_page=per_page, filters_id=filters_id, filters_updated_at=filters_updated_at, filters_list_id=filters_list_id, sort=sort)

List Checklist (Inspection) Sections

Returns the Checklist Sections from Checklists (Inspections) on the Project

### Example


```python
import procore_sdk
from procore_sdk.models.checklist_section1 import ChecklistSection1
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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistSectionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_list_id = [56] # List[int] | Return section(s) with the specified Checklist List IDs (optional)
    sort = 'sort_example' # str | Sort item(s) by the chosen param; check below for a list of options. The direction of sorting is ascending by default; for descending sort, insert the - symbol before the param. (optional)

    try:
        # List Checklist (Inspection) Sections
        api_response = api_instance.rest_v10_projects_project_id_checklist_list_sections_get(procore_company_id, project_id, page=page, per_page=per_page, filters_id=filters_id, filters_updated_at=filters_updated_at, filters_list_id=filters_list_id, sort=sort)
        print("The response of QualitySafetyInspectionsChecklistSectionsApi->rest_v10_projects_project_id_checklist_list_sections_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistSectionsApi->rest_v10_projects_project_id_checklist_list_sections_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_id** | [**List[int]**](int.md)| Return item(s) with the specified IDs. | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_list_id** | [**List[int]**](int.md)| Return section(s) with the specified Checklist List IDs | [optional] 
 **sort** | **str**| Sort item(s) by the chosen param; check below for a list of options. The direction of sorting is ascending by default; for descending sort, insert the - symbol before the param. | [optional] 

### Return type

[**List[ChecklistSection1]**](ChecklistSection1.md)

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

# **rest_v11_projects_project_id_recycle_bin_checklist_list_sections_get**
> List[ChecklistSection1] rest_v11_projects_project_id_recycle_bin_checklist_list_sections_get(procore_company_id, project_id, page=page, per_page=per_page, filters_id=filters_id, filters_updated_at=filters_updated_at, filters_list_id=filters_list_id, sort=sort)

List Recycled Checklist (Inspection) Sections

Returns the Recycled Checklist Sections from Checklists (Inspections) on the Project

### Example


```python
import procore_sdk
from procore_sdk.models.checklist_section1 import ChecklistSection1
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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistSectionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_list_id = [56] # List[int] | Return section(s) with the specified Checklist List IDs (optional)
    sort = 'sort_example' # str | Sort item(s) by the chosen param; check below for a list of options. The direction of sorting is ascending by default; for descending sort, insert the - symbol before the param. (optional)

    try:
        # List Recycled Checklist (Inspection) Sections
        api_response = api_instance.rest_v11_projects_project_id_recycle_bin_checklist_list_sections_get(procore_company_id, project_id, page=page, per_page=per_page, filters_id=filters_id, filters_updated_at=filters_updated_at, filters_list_id=filters_list_id, sort=sort)
        print("The response of QualitySafetyInspectionsChecklistSectionsApi->rest_v11_projects_project_id_recycle_bin_checklist_list_sections_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistSectionsApi->rest_v11_projects_project_id_recycle_bin_checklist_list_sections_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_id** | [**List[int]**](int.md)| Return item(s) with the specified IDs. | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_list_id** | [**List[int]**](int.md)| Return section(s) with the specified Checklist List IDs | [optional] 
 **sort** | **str**| Sort item(s) by the chosen param; check below for a list of options. The direction of sorting is ascending by default; for descending sort, insert the - symbol before the param. | [optional] 

### Return type

[**List[ChecklistSection1]**](ChecklistSection1.md)

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

