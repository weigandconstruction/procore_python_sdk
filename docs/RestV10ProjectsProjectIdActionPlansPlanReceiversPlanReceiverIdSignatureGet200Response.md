# RestV10ProjectsProjectIdActionPlansPlanReceiversPlanReceiverIdSignatureGet200Response

Action Plan Party Signature (Show)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**attachment** | [**RestV10ProjectsProjectIdActionPlansPlanReceiversPlanReceiverIdSignatureGet200ResponseAttachment**](RestV10ProjectsProjectIdActionPlansPlanReceiversPlanReceiverIdSignatureGet200ResponseAttachment.md) |  | [optional] 
**captured_at** | **datetime** | Captured At | [optional] 
**captured_by** | [**RestV10ProjectsProjectIdActionPlansPlanTemplatesGet200ResponseInnerManager**](RestV10ProjectsProjectIdActionPlansPlanTemplatesGet200ResponseInnerManager.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_receivers_plan_receiver_id_signature_get200_response import RestV10ProjectsProjectIdActionPlansPlanReceiversPlanReceiverIdSignatureGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdActionPlansPlanReceiversPlanReceiverIdSignatureGet200Response from a JSON string
rest_v10_projects_project_id_action_plans_plan_receivers_plan_receiver_id_signature_get200_response_instance = RestV10ProjectsProjectIdActionPlansPlanReceiversPlanReceiverIdSignatureGet200Response.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdActionPlansPlanReceiversPlanReceiverIdSignatureGet200Response.to_json())

# convert the object into a dict
rest_v10_projects_project_id_action_plans_plan_receivers_plan_receiver_id_signature_get200_response_dict = rest_v10_projects_project_id_action_plans_plan_receivers_plan_receiver_id_signature_get200_response_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdActionPlansPlanReceiversPlanReceiverIdSignatureGet200Response from a dict
rest_v10_projects_project_id_action_plans_plan_receivers_plan_receiver_id_signature_get200_response_from_dict = RestV10ProjectsProjectIdActionPlansPlanReceiversPlanReceiverIdSignatureGet200Response.from_dict(rest_v10_projects_project_id_action_plans_plan_receivers_plan_receiver_id_signature_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


