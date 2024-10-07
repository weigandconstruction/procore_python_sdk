# procore_sdk.ProjectManagementSubmittalsSubmittalApproversApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_submittal_approvers_id_patch**](ProjectManagementSubmittalsSubmittalApproversApi.md#rest_v10_submittal_approvers_id_patch) | **PATCH** /rest/v1.0/submittal_approvers/{id} | Update Submittal Approver


# **rest_v10_submittal_approvers_id_patch**
> List[RestV10SubmittalApproversIdPatch200ResponseInner] rest_v10_submittal_approvers_id_patch(procore_company_id, id, project_id, submittal_id, rest_v10_submittal_approvers_id_patch_request, send_emails=send_emails)

Update Submittal Approver

Update Submittal Approver for the specified Submittal

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_submittal_approvers_id_patch200_response_inner import RestV10SubmittalApproversIdPatch200ResponseInner
from procore_sdk.models.rest_v10_submittal_approvers_id_patch_request import RestV10SubmittalApproversIdPatchRequest
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
    api_instance = procore_sdk.ProjectManagementSubmittalsSubmittalApproversApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | Submittal Approver ID
    project_id = 56 # int | Unique identifier for the project.
    submittal_id = 56 # int | Submittal ID
    rest_v10_submittal_approvers_id_patch_request = procore_sdk.RestV10SubmittalApproversIdPatchRequest() # RestV10SubmittalApproversIdPatchRequest | 
    send_emails = True # bool | Designates whether or not emails will be sent (default false) (optional)

    try:
        # Update Submittal Approver
        api_response = api_instance.rest_v10_submittal_approvers_id_patch(procore_company_id, id, project_id, submittal_id, rest_v10_submittal_approvers_id_patch_request, send_emails=send_emails)
        print("The response of ProjectManagementSubmittalsSubmittalApproversApi->rest_v10_submittal_approvers_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementSubmittalsSubmittalApproversApi->rest_v10_submittal_approvers_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| Submittal Approver ID | 
 **project_id** | **int**| Unique identifier for the project. | 
 **submittal_id** | **int**| Submittal ID | 
 **rest_v10_submittal_approvers_id_patch_request** | [**RestV10SubmittalApproversIdPatchRequest**](RestV10SubmittalApproversIdPatchRequest.md)|  | 
 **send_emails** | **bool**| Designates whether or not emails will be sent (default false) | [optional] 

### Return type

[**List[RestV10SubmittalApproversIdPatch200ResponseInner]**](RestV10SubmittalApproversIdPatch200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Submittal Approver updated successfully |  -  |
**400** | Invalid Submittal Response for the specified Submittal Approver |  -  |
**403** | User does not have permission to update Submittal Approver |  -  |
**404** | Submittal Approver not found |  -  |
**422** | Error updating Submittal Approver |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

