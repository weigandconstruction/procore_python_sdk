# procore_sdk.ProjectManagementModelsBIMModelRevisionPlanBatchApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_bim_model_revision_plans_batch_post**](ProjectManagementModelsBIMModelRevisionPlanBatchApi.md#rest_v10_bim_model_revision_plans_batch_post) | **POST** /rest/v1.0/bim_model_revision_plans/batch | Create a batch of BIM Model Revision Plans


# **rest_v10_bim_model_revision_plans_batch_post**
> BIMModelRevisionPlanBatchCreateResponse rest_v10_bim_model_revision_plans_batch_post(procore_company_id, body134)

Create a batch of BIM Model Revision Plans

Create relationships between several BIM Model Revisions and BIM Plans.

### Example


```python
import procore_sdk
from procore_sdk.models.bim_model_revision_plan_batch_create_response import BIMModelRevisionPlanBatchCreateResponse
from procore_sdk.models.body134 import Body134
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
    api_instance = procore_sdk.ProjectManagementModelsBIMModelRevisionPlanBatchApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    body134 = procore_sdk.Body134() # Body134 | 

    try:
        # Create a batch of BIM Model Revision Plans
        api_response = api_instance.rest_v10_bim_model_revision_plans_batch_post(procore_company_id, body134)
        print("The response of ProjectManagementModelsBIMModelRevisionPlanBatchApi->rest_v10_bim_model_revision_plans_batch_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementModelsBIMModelRevisionPlanBatchApi->rest_v10_bim_model_revision_plans_batch_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **body134** | [**Body134**](Body134.md)|  | 

### Return type

[**BIMModelRevisionPlanBatchCreateResponse**](BIMModelRevisionPlanBatchCreateResponse.md)

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

