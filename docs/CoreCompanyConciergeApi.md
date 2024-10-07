# procore_sdk.CoreCompanyConciergeApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_concierge_patch**](CoreCompanyConciergeApi.md#rest_v10_companies_company_id_concierge_patch) | **PATCH** /rest/v1.0/companies/{company_id}/concierge | Update Concierge parameters


# **rest_v10_companies_company_id_concierge_patch**
> RestV10CompaniesCompanyIdConciergePatch200Response rest_v10_companies_company_id_concierge_patch(procore_company_id, company_id, rest_v10_companies_company_id_concierge_patch_request)

Update Concierge parameters

Upload Notification

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_concierge_patch200_response import RestV10CompaniesCompanyIdConciergePatch200Response
from procore_sdk.models.rest_v10_companies_company_id_concierge_patch_request import RestV10CompaniesCompanyIdConciergePatchRequest
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
    api_instance = procore_sdk.CoreCompanyConciergeApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    rest_v10_companies_company_id_concierge_patch_request = procore_sdk.RestV10CompaniesCompanyIdConciergePatchRequest() # RestV10CompaniesCompanyIdConciergePatchRequest | 

    try:
        # Update Concierge parameters
        api_response = api_instance.rest_v10_companies_company_id_concierge_patch(procore_company_id, company_id, rest_v10_companies_company_id_concierge_patch_request)
        print("The response of CoreCompanyConciergeApi->rest_v10_companies_company_id_concierge_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCompanyConciergeApi->rest_v10_companies_company_id_concierge_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **rest_v10_companies_company_id_concierge_patch_request** | [**RestV10CompaniesCompanyIdConciergePatchRequest**](RestV10CompaniesCompanyIdConciergePatchRequest.md)|  | 

### Return type

[**RestV10CompaniesCompanyIdConciergePatch200Response**](RestV10CompaniesCompanyIdConciergePatch200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

