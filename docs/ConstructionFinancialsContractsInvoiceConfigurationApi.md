# procore_sdk.ConstructionFinancialsContractsInvoiceConfigurationApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_contracts_contract_id_invoice_configuration_get**](ConstructionFinancialsContractsInvoiceConfigurationApi.md#rest_v10_projects_project_id_contracts_contract_id_invoice_configuration_get) | **GET** /rest/v1.0/projects/{project_id}/contracts/{contract_id}/invoice_configuration | Get Contract&#39;s Invoice Configuration
[**rest_v10_projects_project_id_contracts_contract_id_invoice_configuration_patch**](ConstructionFinancialsContractsInvoiceConfigurationApi.md#rest_v10_projects_project_id_contracts_contract_id_invoice_configuration_patch) | **PATCH** /rest/v1.0/projects/{project_id}/contracts/{contract_id}/invoice_configuration | Update Contract&#39;s Invoice Configuration


# **rest_v10_projects_project_id_contracts_contract_id_invoice_configuration_get**
> RestV10ProjectsProjectIdContractsContractIdInvoiceConfigurationGet200Response rest_v10_projects_project_id_contracts_contract_id_invoice_configuration_get(procore_company_id, project_id, contract_id)

Get Contract's Invoice Configuration

Get the details of a specific Contract's Invoice Configuration

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_contracts_contract_id_invoice_configuration_get200_response import RestV10ProjectsProjectIdContractsContractIdInvoiceConfigurationGet200Response
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
    api_instance = procore_sdk.ConstructionFinancialsContractsInvoiceConfigurationApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    contract_id = 56 # int | ID of the Contract

    try:
        # Get Contract's Invoice Configuration
        api_response = api_instance.rest_v10_projects_project_id_contracts_contract_id_invoice_configuration_get(procore_company_id, project_id, contract_id)
        print("The response of ConstructionFinancialsContractsInvoiceConfigurationApi->rest_v10_projects_project_id_contracts_contract_id_invoice_configuration_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsContractsInvoiceConfigurationApi->rest_v10_projects_project_id_contracts_contract_id_invoice_configuration_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **contract_id** | **int**| ID of the Contract | 

### Return type

[**RestV10ProjectsProjectIdContractsContractIdInvoiceConfigurationGet200Response**](RestV10ProjectsProjectIdContractsContractIdInvoiceConfigurationGet200Response.md)

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
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_contracts_contract_id_invoice_configuration_patch**
> RestV10ProjectsProjectIdContractsContractIdInvoiceConfigurationGet200Response rest_v10_projects_project_id_contracts_contract_id_invoice_configuration_patch(procore_company_id, project_id, contract_id, rest_v10_projects_project_id_contracts_contract_id_invoice_configuration_patch_request)

Update Contract's Invoice Configuration

Update a specific Contract's Invoice Configuration

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_contracts_contract_id_invoice_configuration_get200_response import RestV10ProjectsProjectIdContractsContractIdInvoiceConfigurationGet200Response
from procore_sdk.models.rest_v10_projects_project_id_contracts_contract_id_invoice_configuration_patch_request import RestV10ProjectsProjectIdContractsContractIdInvoiceConfigurationPatchRequest
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
    api_instance = procore_sdk.ConstructionFinancialsContractsInvoiceConfigurationApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    contract_id = 56 # int | ID of the Contract
    rest_v10_projects_project_id_contracts_contract_id_invoice_configuration_patch_request = procore_sdk.RestV10ProjectsProjectIdContractsContractIdInvoiceConfigurationPatchRequest() # RestV10ProjectsProjectIdContractsContractIdInvoiceConfigurationPatchRequest | 

    try:
        # Update Contract's Invoice Configuration
        api_response = api_instance.rest_v10_projects_project_id_contracts_contract_id_invoice_configuration_patch(procore_company_id, project_id, contract_id, rest_v10_projects_project_id_contracts_contract_id_invoice_configuration_patch_request)
        print("The response of ConstructionFinancialsContractsInvoiceConfigurationApi->rest_v10_projects_project_id_contracts_contract_id_invoice_configuration_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsContractsInvoiceConfigurationApi->rest_v10_projects_project_id_contracts_contract_id_invoice_configuration_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **contract_id** | **int**| ID of the Contract | 
 **rest_v10_projects_project_id_contracts_contract_id_invoice_configuration_patch_request** | [**RestV10ProjectsProjectIdContractsContractIdInvoiceConfigurationPatchRequest**](RestV10ProjectsProjectIdContractsContractIdInvoiceConfigurationPatchRequest.md)|  | 

### Return type

[**RestV10ProjectsProjectIdContractsContractIdInvoiceConfigurationGet200Response**](RestV10ProjectsProjectIdContractsContractIdInvoiceConfigurationGet200Response.md)

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
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

