# procore_sdk.QualitySafetyActionPlansActionPlanApproverSignatureApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_action_plans_plan_approvers_plan_approver_id_signature_delete**](QualitySafetyActionPlansActionPlanApproverSignatureApi.md#rest_v10_projects_project_id_action_plans_plan_approvers_plan_approver_id_signature_delete) | **DELETE** /rest/v1.0/projects/{project_id}/action_plans/plan_approvers/{plan_approver_id}/signature | Delete Action Plan Approver Signature
[**rest_v10_projects_project_id_action_plans_plan_approvers_plan_approver_id_signature_get**](QualitySafetyActionPlansActionPlanApproverSignatureApi.md#rest_v10_projects_project_id_action_plans_plan_approvers_plan_approver_id_signature_get) | **GET** /rest/v1.0/projects/{project_id}/action_plans/plan_approvers/{plan_approver_id}/signature | Show Action Plan Approver Signature
[**rest_v10_projects_project_id_action_plans_plan_approvers_plan_approver_id_signature_post**](QualitySafetyActionPlansActionPlanApproverSignatureApi.md#rest_v10_projects_project_id_action_plans_plan_approvers_plan_approver_id_signature_post) | **POST** /rest/v1.0/projects/{project_id}/action_plans/plan_approvers/{plan_approver_id}/signature | Create Action Plan Approver Signature


# **rest_v10_projects_project_id_action_plans_plan_approvers_plan_approver_id_signature_delete**
> rest_v10_projects_project_id_action_plans_plan_approvers_plan_approver_id_signature_delete(procore_company_id, project_id, plan_approver_id)

Delete Action Plan Approver Signature

Delete an Action Plan Approver Signature

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
    api_instance = procore_sdk.QualitySafetyActionPlansActionPlanApproverSignatureApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    plan_approver_id = 56 # int | Action Plan Approver ID

    try:
        # Delete Action Plan Approver Signature
        api_instance.rest_v10_projects_project_id_action_plans_plan_approvers_plan_approver_id_signature_delete(procore_company_id, project_id, plan_approver_id)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansActionPlanApproverSignatureApi->rest_v10_projects_project_id_action_plans_plan_approvers_plan_approver_id_signature_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **plan_approver_id** | **int**| Action Plan Approver ID | 

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
**204** | No Content |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_action_plans_plan_approvers_plan_approver_id_signature_get**
> RestV10ProjectsProjectIdActionPlansPlanReceiversPlanReceiverIdSignatureGet200Response rest_v10_projects_project_id_action_plans_plan_approvers_plan_approver_id_signature_get(procore_company_id, project_id, plan_approver_id)

Show Action Plan Approver Signature

Get the details of an Action Plan Approver Signature

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_receivers_plan_receiver_id_signature_get200_response import RestV10ProjectsProjectIdActionPlansPlanReceiversPlanReceiverIdSignatureGet200Response
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
    api_instance = procore_sdk.QualitySafetyActionPlansActionPlanApproverSignatureApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    plan_approver_id = 56 # int | Action Plan Approver ID

    try:
        # Show Action Plan Approver Signature
        api_response = api_instance.rest_v10_projects_project_id_action_plans_plan_approvers_plan_approver_id_signature_get(procore_company_id, project_id, plan_approver_id)
        print("The response of QualitySafetyActionPlansActionPlanApproverSignatureApi->rest_v10_projects_project_id_action_plans_plan_approvers_plan_approver_id_signature_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansActionPlanApproverSignatureApi->rest_v10_projects_project_id_action_plans_plan_approvers_plan_approver_id_signature_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **plan_approver_id** | **int**| Action Plan Approver ID | 

### Return type

[**RestV10ProjectsProjectIdActionPlansPlanReceiversPlanReceiverIdSignatureGet200Response**](RestV10ProjectsProjectIdActionPlansPlanReceiversPlanReceiverIdSignatureGet200Response.md)

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_action_plans_plan_approvers_plan_approver_id_signature_post**
> RestV10ProjectsProjectIdActionPlansPlanReceiversPlanReceiverIdSignatureGet200Response rest_v10_projects_project_id_action_plans_plan_approvers_plan_approver_id_signature_post(procore_company_id, project_id, plan_approver_id, signature=signature)

Create Action Plan Approver Signature

Create a single Action Plan Approver Signature. Note that only one of `attachment` or `attachment_string` may be passed when creating a signature, not both.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_receivers_plan_receiver_id_signature_get200_response import RestV10ProjectsProjectIdActionPlansPlanReceiversPlanReceiverIdSignatureGet200Response
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_receivers_plan_receiver_id_signature_post_request_signature import RestV10ProjectsProjectIdActionPlansPlanReceiversPlanReceiverIdSignaturePostRequestSignature
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
    api_instance = procore_sdk.QualitySafetyActionPlansActionPlanApproverSignatureApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    plan_approver_id = 56 # int | Action Plan Approver ID
    signature = procore_sdk.RestV10ProjectsProjectIdActionPlansPlanReceiversPlanReceiverIdSignaturePostRequestSignature() # RestV10ProjectsProjectIdActionPlansPlanReceiversPlanReceiverIdSignaturePostRequestSignature |  (optional)

    try:
        # Create Action Plan Approver Signature
        api_response = api_instance.rest_v10_projects_project_id_action_plans_plan_approvers_plan_approver_id_signature_post(procore_company_id, project_id, plan_approver_id, signature=signature)
        print("The response of QualitySafetyActionPlansActionPlanApproverSignatureApi->rest_v10_projects_project_id_action_plans_plan_approvers_plan_approver_id_signature_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansActionPlanApproverSignatureApi->rest_v10_projects_project_id_action_plans_plan_approvers_plan_approver_id_signature_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **plan_approver_id** | **int**| Action Plan Approver ID | 
 **signature** | [**RestV10ProjectsProjectIdActionPlansPlanReceiversPlanReceiverIdSignaturePostRequestSignature**](RestV10ProjectsProjectIdActionPlansPlanReceiversPlanReceiverIdSignaturePostRequestSignature.md)|  | [optional] 

### Return type

[**RestV10ProjectsProjectIdActionPlansPlanReceiversPlanReceiverIdSignatureGet200Response**](RestV10ProjectsProjectIdActionPlansPlanReceiversPlanReceiverIdSignatureGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

