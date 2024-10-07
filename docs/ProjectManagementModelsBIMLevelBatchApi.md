# procore_sdk.ProjectManagementModelsBIMLevelBatchApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_bim_levels_batch_post**](ProjectManagementModelsBIMLevelBatchApi.md#rest_v10_bim_levels_batch_post) | **POST** /rest/v1.0/bim_levels/batch | Create a batch of BIM Levels


# **rest_v10_bim_levels_batch_post**
> BIMLevelBatchCreateResponse rest_v10_bim_levels_batch_post(procore_company_id, body138)

Create a batch of BIM Levels

Create a batch of BIM Levels

### Example


```python
import procore_sdk
from procore_sdk.models.bim_level_batch_create_response import BIMLevelBatchCreateResponse
from procore_sdk.models.body138 import Body138
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
    api_instance = procore_sdk.ProjectManagementModelsBIMLevelBatchApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    body138 = procore_sdk.Body138() # Body138 | 

    try:
        # Create a batch of BIM Levels
        api_response = api_instance.rest_v10_bim_levels_batch_post(procore_company_id, body138)
        print("The response of ProjectManagementModelsBIMLevelBatchApi->rest_v10_bim_levels_batch_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementModelsBIMLevelBatchApi->rest_v10_bim_levels_batch_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **body138** | [**Body138**](Body138.md)|  | 

### Return type

[**BIMLevelBatchCreateResponse**](BIMLevelBatchCreateResponse.md)

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
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

