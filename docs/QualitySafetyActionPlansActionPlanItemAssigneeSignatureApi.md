# procore_sdk.QualitySafetyActionPlansActionPlanItemAssigneeSignatureApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_action_plans_plan_item_assignees_plan_item_assignee_id_signature_delete**](QualitySafetyActionPlansActionPlanItemAssigneeSignatureApi.md#rest_v10_projects_project_id_action_plans_plan_item_assignees_plan_item_assignee_id_signature_delete) | **DELETE** /rest/v1.0/projects/{project_id}/action_plans/plan_item_assignees/{plan_item_assignee_id}/signature | Delete Action Plan Item Assignee Signature
[**rest_v10_projects_project_id_action_plans_plan_item_assignees_plan_item_assignee_id_signature_get**](QualitySafetyActionPlansActionPlanItemAssigneeSignatureApi.md#rest_v10_projects_project_id_action_plans_plan_item_assignees_plan_item_assignee_id_signature_get) | **GET** /rest/v1.0/projects/{project_id}/action_plans/plan_item_assignees/{plan_item_assignee_id}/signature | Show Action Plan Item Assignee Signature
[**rest_v10_projects_project_id_action_plans_plan_item_assignees_plan_item_assignee_id_signature_post**](QualitySafetyActionPlansActionPlanItemAssigneeSignatureApi.md#rest_v10_projects_project_id_action_plans_plan_item_assignees_plan_item_assignee_id_signature_post) | **POST** /rest/v1.0/projects/{project_id}/action_plans/plan_item_assignees/{plan_item_assignee_id}/signature | Create Action Plan Item Assignee Signature


# **rest_v10_projects_project_id_action_plans_plan_item_assignees_plan_item_assignee_id_signature_delete**
> rest_v10_projects_project_id_action_plans_plan_item_assignees_plan_item_assignee_id_signature_delete(procore_company_id, project_id, plan_item_assignee_id)

Delete Action Plan Item Assignee Signature

Delete an Action Plan Item Assignee Signature

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
    api_instance = procore_sdk.QualitySafetyActionPlansActionPlanItemAssigneeSignatureApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    plan_item_assignee_id = 56 # int | Action Plan Item Assignee ID

    try:
        # Delete Action Plan Item Assignee Signature
        api_instance.rest_v10_projects_project_id_action_plans_plan_item_assignees_plan_item_assignee_id_signature_delete(procore_company_id, project_id, plan_item_assignee_id)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansActionPlanItemAssigneeSignatureApi->rest_v10_projects_project_id_action_plans_plan_item_assignees_plan_item_assignee_id_signature_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **plan_item_assignee_id** | **int**| Action Plan Item Assignee ID | 

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

# **rest_v10_projects_project_id_action_plans_plan_item_assignees_plan_item_assignee_id_signature_get**
> RestV10ProjectsProjectIdActionPlansPlanReceiversPlanReceiverIdSignatureGet200Response rest_v10_projects_project_id_action_plans_plan_item_assignees_plan_item_assignee_id_signature_get(procore_company_id, project_id, plan_item_assignee_id)

Show Action Plan Item Assignee Signature

Get the details of an Action Plan Item Assignee Signature

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
    api_instance = procore_sdk.QualitySafetyActionPlansActionPlanItemAssigneeSignatureApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    plan_item_assignee_id = 56 # int | Action Plan Item Assignee ID

    try:
        # Show Action Plan Item Assignee Signature
        api_response = api_instance.rest_v10_projects_project_id_action_plans_plan_item_assignees_plan_item_assignee_id_signature_get(procore_company_id, project_id, plan_item_assignee_id)
        print("The response of QualitySafetyActionPlansActionPlanItemAssigneeSignatureApi->rest_v10_projects_project_id_action_plans_plan_item_assignees_plan_item_assignee_id_signature_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansActionPlanItemAssigneeSignatureApi->rest_v10_projects_project_id_action_plans_plan_item_assignees_plan_item_assignee_id_signature_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **plan_item_assignee_id** | **int**| Action Plan Item Assignee ID | 

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

# **rest_v10_projects_project_id_action_plans_plan_item_assignees_plan_item_assignee_id_signature_post**
> RestV10ProjectsProjectIdActionPlansPlanReceiversPlanReceiverIdSignatureGet200Response rest_v10_projects_project_id_action_plans_plan_item_assignees_plan_item_assignee_id_signature_post(procore_company_id, project_id, plan_item_assignee_id, signature=signature)

Create Action Plan Item Assignee Signature

Create a single Action Plan Item Assignee Signature. Note that only one of `attachment` or `attachment_string` may be passed when creating a signature, not both.

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
    api_instance = procore_sdk.QualitySafetyActionPlansActionPlanItemAssigneeSignatureApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    plan_item_assignee_id = 56 # int | Action Plan Item Assignee ID
    signature = procore_sdk.RestV10ProjectsProjectIdActionPlansPlanReceiversPlanReceiverIdSignaturePostRequestSignature() # RestV10ProjectsProjectIdActionPlansPlanReceiversPlanReceiverIdSignaturePostRequestSignature |  (optional)

    try:
        # Create Action Plan Item Assignee Signature
        api_response = api_instance.rest_v10_projects_project_id_action_plans_plan_item_assignees_plan_item_assignee_id_signature_post(procore_company_id, project_id, plan_item_assignee_id, signature=signature)
        print("The response of QualitySafetyActionPlansActionPlanItemAssigneeSignatureApi->rest_v10_projects_project_id_action_plans_plan_item_assignees_plan_item_assignee_id_signature_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansActionPlanItemAssigneeSignatureApi->rest_v10_projects_project_id_action_plans_plan_item_assignees_plan_item_assignee_id_signature_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **plan_item_assignee_id** | **int**| Action Plan Item Assignee ID | 
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
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

