# procore_sdk.ConstructionFinancialsCommitmentsCommitmentChangeOrderExportPDFApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v20_companies_company_id_projects_project_id_commitment_change_orders_commitment_change_order_id_pdf_get**](ConstructionFinancialsCommitmentsCommitmentChangeOrderExportPDFApi.md#rest_v20_companies_company_id_projects_project_id_commitment_change_orders_commitment_change_order_id_pdf_get) | **GET** /rest/v2.0/companies/{company_id}/projects/{project_id}/commitment_change_orders/{commitment_change_order_id}/pdf | Check PDF generation status
[**rest_v20_companies_company_id_projects_project_id_commitment_change_orders_commitment_change_order_id_pdf_post**](ConstructionFinancialsCommitmentsCommitmentChangeOrderExportPDFApi.md#rest_v20_companies_company_id_projects_project_id_commitment_change_orders_commitment_change_order_id_pdf_post) | **POST** /rest/v2.0/companies/{company_id}/projects/{project_id}/commitment_change_orders/{commitment_change_order_id}/pdf | Create PDF export for a Commitment Change Order


# **rest_v20_companies_company_id_projects_project_id_commitment_change_orders_commitment_change_order_id_pdf_get**
> rest_v20_companies_company_id_projects_project_id_commitment_change_orders_commitment_change_order_id_pdf_get(procore_company_id, company_id, project_id, commitment_change_order_id)

Check PDF generation status

Check the status of a PDF document generation for a Commitment Change Order. Note: This endpoint is currently only supported in Procore Zones US01 && US02.

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
    api_instance = procore_sdk.ConstructionFinancialsCommitmentsCommitmentChangeOrderExportPDFApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 'company_id_example' # str | Unique identifier for the company.
    project_id = 'project_id_example' # str | Unique identifier for the project.
    commitment_change_order_id = 'commitment_change_order_id_example' # str | Unique identifier for the Commitment Change Order.

    try:
        # Check PDF generation status
        api_instance.rest_v20_companies_company_id_projects_project_id_commitment_change_orders_commitment_change_order_id_pdf_get(procore_company_id, company_id, project_id, commitment_change_order_id)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsCommitmentsCommitmentChangeOrderExportPDFApi->rest_v20_companies_company_id_projects_project_id_commitment_change_orders_commitment_change_order_id_pdf_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **str**| Unique identifier for the company. | 
 **project_id** | **str**| Unique identifier for the project. | 
 **commitment_change_order_id** | **str**| Unique identifier for the Commitment Change Order. | 

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
**202** | Accepted |  -  |
**302** | See other |  * Location - URL to check the status of the PDF export <br>  |
**400** | Bad Request, indicates that the generation was unsuccessful |  -  |
**404** | Not Found, job not found (PDF generation has expired, or never started). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v20_companies_company_id_projects_project_id_commitment_change_orders_commitment_change_order_id_pdf_post**
> rest_v20_companies_company_id_projects_project_id_commitment_change_orders_commitment_change_order_id_pdf_post(procore_company_id, company_id, project_id, commitment_change_order_id)

Create PDF export for a Commitment Change Order

Creates a PDF export for a given Commitment Change Order. Note: This endpoint is currently only supported in Procore Zones US01 && US02.

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
    api_instance = procore_sdk.ConstructionFinancialsCommitmentsCommitmentChangeOrderExportPDFApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 'company_id_example' # str | Unique identifier for the company.
    project_id = 'project_id_example' # str | Unique identifier for the project.
    commitment_change_order_id = 'commitment_change_order_id_example' # str | Unique identifier for the Commitment Change Order.

    try:
        # Create PDF export for a Commitment Change Order
        api_instance.rest_v20_companies_company_id_projects_project_id_commitment_change_orders_commitment_change_order_id_pdf_post(procore_company_id, company_id, project_id, commitment_change_order_id)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsCommitmentsCommitmentChangeOrderExportPDFApi->rest_v20_companies_company_id_projects_project_id_commitment_change_orders_commitment_change_order_id_pdf_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **str**| Unique identifier for the company. | 
 **project_id** | **str**| Unique identifier for the project. | 
 **commitment_change_order_id** | **str**| Unique identifier for the Commitment Change Order. | 

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
**202** | Accepted, returns back location to PDF export job which can be queried for progress. |  * Location - URL to check the status of the PDF export <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

