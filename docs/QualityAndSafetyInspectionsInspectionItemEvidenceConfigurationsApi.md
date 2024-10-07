# procore_sdk.QualityAndSafetyInspectionsInspectionItemEvidenceConfigurationsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_evidence_configuration_get**](QualityAndSafetyInspectionsInspectionItemEvidenceConfigurationsApi.md#rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_evidence_configuration_get) | **GET** /rest/v2.0/companies/{company_id}/projects/{project_id}/inspection_items/{item_id}/evidence_configuration | Get a list of Inspection Item Evidence Configurations


# **rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_evidence_configuration_get**
> RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdEvidenceConfigurationGet200Response rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_evidence_configuration_get(procore_company_id, company_id, project_id, item_id, page=page, per_page=per_page, filters_id=filters_id)

Get a list of Inspection Item Evidence Configurations

Get a list of Inspection Item Evidence Configurations for a specified Inspection Item.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_evidence_configuration_get200_response import RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdEvidenceConfigurationGet200Response
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
    api_instance = procore_sdk.QualityAndSafetyInspectionsInspectionItemEvidenceConfigurationsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 'company_id_example' # str | Unique identifier for the company.
    project_id = 'project_id_example' # str | Unique identifier for the project.
    item_id = 'item_id_example' # str | Unique identifier for the inspection item.
    page = 56 # int | Page (optional)
    per_page = 10 # int | Elements per page (optional) (default to 10)
    filters_id = ['filters_id_example'] # List[str] | Return Item Evidence Configuration(s) with the specified IDs (optional)

    try:
        # Get a list of Inspection Item Evidence Configurations
        api_response = api_instance.rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_evidence_configuration_get(procore_company_id, company_id, project_id, item_id, page=page, per_page=per_page, filters_id=filters_id)
        print("The response of QualityAndSafetyInspectionsInspectionItemEvidenceConfigurationsApi->rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_evidence_configuration_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualityAndSafetyInspectionsInspectionItemEvidenceConfigurationsApi->rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_evidence_configuration_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **str**| Unique identifier for the company. | 
 **project_id** | **str**| Unique identifier for the project. | 
 **item_id** | **str**| Unique identifier for the inspection item. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] [default to 10]
 **filters_id** | [**List[str]**](str.md)| Return Item Evidence Configuration(s) with the specified IDs | [optional] 

### Return type

[**RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdEvidenceConfigurationGet200Response**](RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdEvidenceConfigurationGet200Response.md)

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

