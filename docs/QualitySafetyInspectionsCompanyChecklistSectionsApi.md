# procore_sdk.QualitySafetyInspectionsCompanyChecklistSectionsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_checklist_sections_get**](QualitySafetyInspectionsCompanyChecklistSectionsApi.md#rest_v10_companies_company_id_checklist_sections_get) | **GET** /rest/v1.0/companies/{company_id}/checklist/sections | List Company Checklist Sections
[**rest_v10_companies_company_id_checklist_sections_id_delete**](QualitySafetyInspectionsCompanyChecklistSectionsApi.md#rest_v10_companies_company_id_checklist_sections_id_delete) | **DELETE** /rest/v1.0/companies/{company_id}/checklist/sections/{id} | Delete Company Checklist Section
[**rest_v10_companies_company_id_checklist_sections_id_get**](QualitySafetyInspectionsCompanyChecklistSectionsApi.md#rest_v10_companies_company_id_checklist_sections_id_get) | **GET** /rest/v1.0/companies/{company_id}/checklist/sections/{id} | Show Company Checklist Section
[**rest_v10_companies_company_id_checklist_sections_id_patch**](QualitySafetyInspectionsCompanyChecklistSectionsApi.md#rest_v10_companies_company_id_checklist_sections_id_patch) | **PATCH** /rest/v1.0/companies/{company_id}/checklist/sections/{id} | Update Company Checklist Section


# **rest_v10_companies_company_id_checklist_sections_get**
> List[CompanyChecklistSection] rest_v10_companies_company_id_checklist_sections_get(procore_company_id, company_id, list_template_id)

List Company Checklist Sections

Returns a list of Checklist Sections for a given Company List Template.

### Example


```python
import procore_sdk
from procore_sdk.models.company_checklist_section import CompanyChecklistSection
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
    api_instance = procore_sdk.QualitySafetyInspectionsCompanyChecklistSectionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    list_template_id = 56 # int | Checklist Template ID

    try:
        # List Company Checklist Sections
        api_response = api_instance.rest_v10_companies_company_id_checklist_sections_get(procore_company_id, company_id, list_template_id)
        print("The response of QualitySafetyInspectionsCompanyChecklistSectionsApi->rest_v10_companies_company_id_checklist_sections_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsCompanyChecklistSectionsApi->rest_v10_companies_company_id_checklist_sections_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **list_template_id** | **int**| Checklist Template ID | 

### Return type

[**List[CompanyChecklistSection]**](CompanyChecklistSection.md)

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

# **rest_v10_companies_company_id_checklist_sections_id_delete**
> rest_v10_companies_company_id_checklist_sections_id_delete(procore_company_id, company_id, id)

Delete Company Checklist Section

Deletes a Checklist Section for a specified Company.

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
    api_instance = procore_sdk.QualitySafetyInspectionsCompanyChecklistSectionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | Company Checklist Section ID

    try:
        # Delete Company Checklist Section
        api_instance.rest_v10_companies_company_id_checklist_sections_id_delete(procore_company_id, company_id, id)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsCompanyChecklistSectionsApi->rest_v10_companies_company_id_checklist_sections_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| Company Checklist Section ID | 

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

# **rest_v10_companies_company_id_checklist_sections_id_get**
> CompanyChecklistSection rest_v10_companies_company_id_checklist_sections_id_get(procore_company_id, company_id, id)

Show Company Checklist Section

Returns the details for a specified Company Checklist Section

### Example


```python
import procore_sdk
from procore_sdk.models.company_checklist_section import CompanyChecklistSection
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
    api_instance = procore_sdk.QualitySafetyInspectionsCompanyChecklistSectionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | Company Checklist Section ID

    try:
        # Show Company Checklist Section
        api_response = api_instance.rest_v10_companies_company_id_checklist_sections_id_get(procore_company_id, company_id, id)
        print("The response of QualitySafetyInspectionsCompanyChecklistSectionsApi->rest_v10_companies_company_id_checklist_sections_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsCompanyChecklistSectionsApi->rest_v10_companies_company_id_checklist_sections_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| Company Checklist Section ID | 

### Return type

[**CompanyChecklistSection**](CompanyChecklistSection.md)

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

# **rest_v10_companies_company_id_checklist_sections_id_patch**
> CompanyChecklistSection rest_v10_companies_company_id_checklist_sections_id_patch(procore_company_id, company_id, id, company_checklist_section_update_body)

Update Company Checklist Section

Updates a Checklist Section for a specified Company.

### Example


```python
import procore_sdk
from procore_sdk.models.company_checklist_section import CompanyChecklistSection
from procore_sdk.models.company_checklist_section_update_body import CompanyChecklistSectionUpdateBody
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
    api_instance = procore_sdk.QualitySafetyInspectionsCompanyChecklistSectionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | Company Checklist Section ID
    company_checklist_section_update_body = procore_sdk.CompanyChecklistSectionUpdateBody() # CompanyChecklistSectionUpdateBody | 

    try:
        # Update Company Checklist Section
        api_response = api_instance.rest_v10_companies_company_id_checklist_sections_id_patch(procore_company_id, company_id, id, company_checklist_section_update_body)
        print("The response of QualitySafetyInspectionsCompanyChecklistSectionsApi->rest_v10_companies_company_id_checklist_sections_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsCompanyChecklistSectionsApi->rest_v10_companies_company_id_checklist_sections_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| Company Checklist Section ID | 
 **company_checklist_section_update_body** | [**CompanyChecklistSectionUpdateBody**](CompanyChecklistSectionUpdateBody.md)|  | 

### Return type

[**CompanyChecklistSection**](CompanyChecklistSection.md)

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

