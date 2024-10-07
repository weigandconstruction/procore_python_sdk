# procore_sdk.CoreCompanyConstructionVolumeApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_construction_volume_urgent_error_post**](CoreCompanyConstructionVolumeApi.md#rest_v10_companies_company_id_construction_volume_urgent_error_post) | **POST** /rest/v1.0/companies/{company_id}/construction_volume/urgent_error | Send Urgent Error


# **rest_v10_companies_company_id_construction_volume_urgent_error_post**
> object rest_v10_companies_company_id_construction_volume_urgent_error_post(procore_company_id, company_id, rest_v10_companies_company_id_construction_volume_urgent_error_post_request=rest_v10_companies_company_id_construction_volume_urgent_error_post_request)

Send Urgent Error

Send an urgent error to be recieved and delt with quickly.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_construction_volume_urgent_error_post_request import RestV10CompaniesCompanyIdConstructionVolumeUrgentErrorPostRequest
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
    api_instance = procore_sdk.CoreCompanyConstructionVolumeApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    rest_v10_companies_company_id_construction_volume_urgent_error_post_request = procore_sdk.RestV10CompaniesCompanyIdConstructionVolumeUrgentErrorPostRequest() # RestV10CompaniesCompanyIdConstructionVolumeUrgentErrorPostRequest |  (optional)

    try:
        # Send Urgent Error
        api_response = api_instance.rest_v10_companies_company_id_construction_volume_urgent_error_post(procore_company_id, company_id, rest_v10_companies_company_id_construction_volume_urgent_error_post_request=rest_v10_companies_company_id_construction_volume_urgent_error_post_request)
        print("The response of CoreCompanyConstructionVolumeApi->rest_v10_companies_company_id_construction_volume_urgent_error_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCompanyConstructionVolumeApi->rest_v10_companies_company_id_construction_volume_urgent_error_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **rest_v10_companies_company_id_construction_volume_urgent_error_post_request** | [**RestV10CompaniesCompanyIdConstructionVolumeUrgentErrorPostRequest**](RestV10CompaniesCompanyIdConstructionVolumeUrgentErrorPostRequest.md)|  | [optional] 

### Return type

**object**

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
**0** | Unexpected Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

