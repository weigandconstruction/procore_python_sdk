# procore_sdk.QualityAndSafetyInspectionsProjectInspectionTemplateItemEvidenceConfigurationsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v20_companies_company_id_projects_project_id_inspection_template_items_template_item_id_evidence_configuration_get**](QualityAndSafetyInspectionsProjectInspectionTemplateItemEvidenceConfigurationsApi.md#rest_v20_companies_company_id_projects_project_id_inspection_template_items_template_item_id_evidence_configuration_get) | **GET** /rest/v2.0/companies/{company_id}/projects/{project_id}/inspection_template_items/{template_item_id}/evidence_configuration | Show a Project Inspection Template Item Evidence Configuration
[**rest_v20_companies_company_id_projects_project_id_inspection_template_items_template_item_id_evidence_configuration_patch**](QualityAndSafetyInspectionsProjectInspectionTemplateItemEvidenceConfigurationsApi.md#rest_v20_companies_company_id_projects_project_id_inspection_template_items_template_item_id_evidence_configuration_patch) | **PATCH** /rest/v2.0/companies/{company_id}/projects/{project_id}/inspection_template_items/{template_item_id}/evidence_configuration | Updates a Project Inspection Template Item Evidence Configuration


# **rest_v20_companies_company_id_projects_project_id_inspection_template_items_template_item_id_evidence_configuration_get**
> RestV20CompaniesCompanyIdProjectsProjectIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationGet200Response rest_v20_companies_company_id_projects_project_id_inspection_template_items_template_item_id_evidence_configuration_get(procore_company_id, company_id, project_id, template_item_id)

Show a Project Inspection Template Item Evidence Configuration

Show the specified Project Inspection Template Item Evidence Configuration.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v20_companies_company_id_projects_project_id_inspection_template_items_template_item_id_evidence_configuration_get200_response import RestV20CompaniesCompanyIdProjectsProjectIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationGet200Response
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
    api_instance = procore_sdk.QualityAndSafetyInspectionsProjectInspectionTemplateItemEvidenceConfigurationsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 'company_id_example' # str | Unique identifier for the company.
    project_id = 'project_id_example' # str | Unique identifier for the project.
    template_item_id = 'template_item_id_example' # str | Unique identifier for the inspection template item.

    try:
        # Show a Project Inspection Template Item Evidence Configuration
        api_response = api_instance.rest_v20_companies_company_id_projects_project_id_inspection_template_items_template_item_id_evidence_configuration_get(procore_company_id, company_id, project_id, template_item_id)
        print("The response of QualityAndSafetyInspectionsProjectInspectionTemplateItemEvidenceConfigurationsApi->rest_v20_companies_company_id_projects_project_id_inspection_template_items_template_item_id_evidence_configuration_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualityAndSafetyInspectionsProjectInspectionTemplateItemEvidenceConfigurationsApi->rest_v20_companies_company_id_projects_project_id_inspection_template_items_template_item_id_evidence_configuration_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **str**| Unique identifier for the company. | 
 **project_id** | **str**| Unique identifier for the project. | 
 **template_item_id** | **str**| Unique identifier for the inspection template item. | 

### Return type

[**RestV20CompaniesCompanyIdProjectsProjectIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationGet200Response**](RestV20CompaniesCompanyIdProjectsProjectIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationGet200Response.md)

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

# **rest_v20_companies_company_id_projects_project_id_inspection_template_items_template_item_id_evidence_configuration_patch**
> RestV20CompaniesCompanyIdProjectsProjectIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationGet200Response rest_v20_companies_company_id_projects_project_id_inspection_template_items_template_item_id_evidence_configuration_patch(procore_company_id, company_id, project_id, template_item_id, rest_v20_companies_company_id_projects_project_id_inspection_template_items_template_item_id_evidence_configuration_patch_request=rest_v20_companies_company_id_projects_project_id_inspection_template_items_template_item_id_evidence_configuration_patch_request)

Updates a Project Inspection Template Item Evidence Configuration

Updates the specified Project Inspection Template Item Evidence Configuration

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v20_companies_company_id_projects_project_id_inspection_template_items_template_item_id_evidence_configuration_get200_response import RestV20CompaniesCompanyIdProjectsProjectIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationGet200Response
from procore_sdk.models.rest_v20_companies_company_id_projects_project_id_inspection_template_items_template_item_id_evidence_configuration_patch_request import RestV20CompaniesCompanyIdProjectsProjectIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationPatchRequest
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
    api_instance = procore_sdk.QualityAndSafetyInspectionsProjectInspectionTemplateItemEvidenceConfigurationsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 'company_id_example' # str | Unique identifier for the company.
    project_id = 'project_id_example' # str | Unique identifier for the project.
    template_item_id = 'template_item_id_example' # str | Unique identifier for the inspection template item.
    rest_v20_companies_company_id_projects_project_id_inspection_template_items_template_item_id_evidence_configuration_patch_request = procore_sdk.RestV20CompaniesCompanyIdProjectsProjectIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationPatchRequest() # RestV20CompaniesCompanyIdProjectsProjectIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationPatchRequest |  (optional)

    try:
        # Updates a Project Inspection Template Item Evidence Configuration
        api_response = api_instance.rest_v20_companies_company_id_projects_project_id_inspection_template_items_template_item_id_evidence_configuration_patch(procore_company_id, company_id, project_id, template_item_id, rest_v20_companies_company_id_projects_project_id_inspection_template_items_template_item_id_evidence_configuration_patch_request=rest_v20_companies_company_id_projects_project_id_inspection_template_items_template_item_id_evidence_configuration_patch_request)
        print("The response of QualityAndSafetyInspectionsProjectInspectionTemplateItemEvidenceConfigurationsApi->rest_v20_companies_company_id_projects_project_id_inspection_template_items_template_item_id_evidence_configuration_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualityAndSafetyInspectionsProjectInspectionTemplateItemEvidenceConfigurationsApi->rest_v20_companies_company_id_projects_project_id_inspection_template_items_template_item_id_evidence_configuration_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **str**| Unique identifier for the company. | 
 **project_id** | **str**| Unique identifier for the project. | 
 **template_item_id** | **str**| Unique identifier for the inspection template item. | 
 **rest_v20_companies_company_id_projects_project_id_inspection_template_items_template_item_id_evidence_configuration_patch_request** | [**RestV20CompaniesCompanyIdProjectsProjectIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationPatchRequest**](RestV20CompaniesCompanyIdProjectsProjectIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationPatchRequest.md)|  | [optional] 

### Return type

[**RestV20CompaniesCompanyIdProjectsProjectIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationGet200Response**](RestV20CompaniesCompanyIdProjectsProjectIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationGet200Response.md)

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

