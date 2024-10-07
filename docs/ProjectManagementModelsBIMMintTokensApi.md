# procore_sdk.ProjectManagementModelsBIMMintTokensApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_bim_mint_tokens_post**](ProjectManagementModelsBIMMintTokensApi.md#rest_v10_bim_mint_tokens_post) | **POST** /rest/v1.0/bim_mint_tokens | Create BIM Mint Tokens


# **rest_v10_bim_mint_tokens_post**
> BIMMintTokens rest_v10_bim_mint_tokens_post(procore_company_id, body135)

Create BIM Mint Tokens

Create BIM mint tokens in a Project

### Example


```python
import procore_sdk
from procore_sdk.models.bim_mint_tokens import BIMMintTokens
from procore_sdk.models.body135 import Body135
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
    api_instance = procore_sdk.ProjectManagementModelsBIMMintTokensApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    body135 = procore_sdk.Body135() # Body135 | 

    try:
        # Create BIM Mint Tokens
        api_response = api_instance.rest_v10_bim_mint_tokens_post(procore_company_id, body135)
        print("The response of ProjectManagementModelsBIMMintTokensApi->rest_v10_bim_mint_tokens_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementModelsBIMMintTokensApi->rest_v10_bim_mint_tokens_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **body135** | [**Body135**](Body135.md)|  | 

### Return type

[**BIMMintTokens**](BIMMintTokens.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

