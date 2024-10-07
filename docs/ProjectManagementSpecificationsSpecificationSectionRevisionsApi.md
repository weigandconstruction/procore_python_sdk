# procore_sdk.ProjectManagementSpecificationsSpecificationSectionRevisionsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_specification_section_revisions_get**](ProjectManagementSpecificationsSpecificationSectionRevisionsApi.md#rest_v10_specification_section_revisions_get) | **GET** /rest/v1.0/specification_section_revisions | List Specification Section Revisions for a Specification Section Division
[**rest_v10_specification_section_revisions_id_get**](ProjectManagementSpecificationsSpecificationSectionRevisionsApi.md#rest_v10_specification_section_revisions_id_get) | **GET** /rest/v1.0/specification_section_revisions/{id} | Show Specification Section Revision


# **rest_v10_specification_section_revisions_get**
> List[SpecificationSectionRevision] rest_v10_specification_section_revisions_get(procore_company_id, project_id, specification_section_division_id, all_revisions=all_revisions, page=page, per_page=per_page)

List Specification Section Revisions for a Specification Section Division

### Example


```python
import procore_sdk
from procore_sdk.models.specification_section_revision import SpecificationSectionRevision
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
    api_instance = procore_sdk.ProjectManagementSpecificationsSpecificationSectionRevisionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    specification_section_division_id = 56 # int | 
    all_revisions = 'all_revisions_example' # str | By default, only current specification section revisions are returned. Set this parameter to \"true\" to return all specification section revisions. (optional)
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Specification Section Revisions for a Specification Section Division
        api_response = api_instance.rest_v10_specification_section_revisions_get(procore_company_id, project_id, specification_section_division_id, all_revisions=all_revisions, page=page, per_page=per_page)
        print("The response of ProjectManagementSpecificationsSpecificationSectionRevisionsApi->rest_v10_specification_section_revisions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementSpecificationsSpecificationSectionRevisionsApi->rest_v10_specification_section_revisions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **specification_section_division_id** | **int**|  | 
 **all_revisions** | **str**| By default, only current specification section revisions are returned. Set this parameter to \&quot;true\&quot; to return all specification section revisions. | [optional] 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[SpecificationSectionRevision]**](SpecificationSectionRevision.md)

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

# **rest_v10_specification_section_revisions_id_get**
> RestV10SpecificationSectionRevisionsIdGet200Response rest_v10_specification_section_revisions_id_get(procore_company_id, id, project_id)

Show Specification Section Revision

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_specification_section_revisions_id_get200_response import RestV10SpecificationSectionRevisionsIdGet200Response
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
    api_instance = procore_sdk.ProjectManagementSpecificationsSpecificationSectionRevisionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | Specification section revision ID
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Show Specification Section Revision
        api_response = api_instance.rest_v10_specification_section_revisions_id_get(procore_company_id, id, project_id)
        print("The response of ProjectManagementSpecificationsSpecificationSectionRevisionsApi->rest_v10_specification_section_revisions_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementSpecificationsSpecificationSectionRevisionsApi->rest_v10_specification_section_revisions_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| Specification section revision ID | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**RestV10SpecificationSectionRevisionsIdGet200Response**](RestV10SpecificationSectionRevisionsIdGet200Response.md)

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

