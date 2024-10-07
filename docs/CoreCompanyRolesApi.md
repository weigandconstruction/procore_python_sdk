# procore_sdk.CoreCompanyRolesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_roles_get**](CoreCompanyRolesApi.md#rest_v10_companies_company_id_roles_get) | **GET** /rest/v1.0/companies/{company_id}/roles | List Company Roles


# **rest_v10_companies_company_id_roles_get**
> List[Role] rest_v10_companies_company_id_roles_get(procore_company_id, company_id, filters_users_only=filters_users_only)

List Company Roles

Return a list of roles for a company.

### Example


```python
import procore_sdk
from procore_sdk.models.role import Role
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
    api_instance = procore_sdk.CoreCompanyRolesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    filters_users_only = False # bool | If true, returns only project roles of type user. (optional) (default to False)

    try:
        # List Company Roles
        api_response = api_instance.rest_v10_companies_company_id_roles_get(procore_company_id, company_id, filters_users_only=filters_users_only)
        print("The response of CoreCompanyRolesApi->rest_v10_companies_company_id_roles_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCompanyRolesApi->rest_v10_companies_company_id_roles_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **filters_users_only** | **bool**| If true, returns only project roles of type user. | [optional] [default to False]

### Return type

[**List[Role]**](Role.md)

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

