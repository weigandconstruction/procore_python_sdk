# procore_sdk.QualitySafetyInspectionsCompanyChecklistTemplateSectionsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_checklist_list_templates_list_template_id_sections_get**](QualitySafetyInspectionsCompanyChecklistTemplateSectionsApi.md#rest_v10_companies_company_id_checklist_list_templates_list_template_id_sections_get) | **GET** /rest/v1.0/companies/{company_id}/checklist/list_templates/{list_template_id}/sections | List Company Checklist Template Sections
[**rest_v10_companies_company_id_checklist_list_templates_list_template_id_sections_post**](QualitySafetyInspectionsCompanyChecklistTemplateSectionsApi.md#rest_v10_companies_company_id_checklist_list_templates_list_template_id_sections_post) | **POST** /rest/v1.0/companies/{company_id}/checklist/list_templates/{list_template_id}/sections | Create Company Checklist Template Section


# **rest_v10_companies_company_id_checklist_list_templates_list_template_id_sections_get**
> List[CompanyChecklistSection] rest_v10_companies_company_id_checklist_list_templates_list_template_id_sections_get(procore_company_id, company_id, list_template_id)

List Company Checklist Template Sections

Returns a collection of Checklist Sections for a specified Checklist Template.

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
    api_instance = procore_sdk.QualitySafetyInspectionsCompanyChecklistTemplateSectionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    list_template_id = 56 # int | The ID of the Checklist Template

    try:
        # List Company Checklist Template Sections
        api_response = api_instance.rest_v10_companies_company_id_checklist_list_templates_list_template_id_sections_get(procore_company_id, company_id, list_template_id)
        print("The response of QualitySafetyInspectionsCompanyChecklistTemplateSectionsApi->rest_v10_companies_company_id_checklist_list_templates_list_template_id_sections_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsCompanyChecklistTemplateSectionsApi->rest_v10_companies_company_id_checklist_list_templates_list_template_id_sections_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **list_template_id** | **int**| The ID of the Checklist Template | 

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_checklist_list_templates_list_template_id_sections_post**
> CompanyChecklistSection rest_v10_companies_company_id_checklist_list_templates_list_template_id_sections_post(procore_company_id, company_id, list_template_id, company_checklist_section_create_body)

Create Company Checklist Template Section

Creates a Company Checklist Section for a specified Checklist Template.

### Example


```python
import procore_sdk
from procore_sdk.models.company_checklist_section import CompanyChecklistSection
from procore_sdk.models.company_checklist_section_create_body import CompanyChecklistSectionCreateBody
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
    api_instance = procore_sdk.QualitySafetyInspectionsCompanyChecklistTemplateSectionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    list_template_id = 56 # int | The ID of the Checklist Template
    company_checklist_section_create_body = procore_sdk.CompanyChecklistSectionCreateBody() # CompanyChecklistSectionCreateBody | 

    try:
        # Create Company Checklist Template Section
        api_response = api_instance.rest_v10_companies_company_id_checklist_list_templates_list_template_id_sections_post(procore_company_id, company_id, list_template_id, company_checklist_section_create_body)
        print("The response of QualitySafetyInspectionsCompanyChecklistTemplateSectionsApi->rest_v10_companies_company_id_checklist_list_templates_list_template_id_sections_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsCompanyChecklistTemplateSectionsApi->rest_v10_companies_company_id_checklist_list_templates_list_template_id_sections_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **list_template_id** | **int**| The ID of the Checklist Template | 
 **company_checklist_section_create_body** | [**CompanyChecklistSectionCreateBody**](CompanyChecklistSectionCreateBody.md)|  | 

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
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

