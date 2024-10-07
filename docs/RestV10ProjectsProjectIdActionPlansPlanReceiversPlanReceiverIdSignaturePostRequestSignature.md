# RestV10ProjectsProjectIdActionPlansPlanReceiversPlanReceiverIdSignaturePostRequestSignature


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachment** | **bytearray** | Attachment representing the Signature. To upload an attachment you must upload the entire payload as &#x60;multipart/form-data&#x60; content-type with the &#x60;attachment&#x60; file. | 
**attachment_string** | **str** | Base64 encoded string representing PNG image of signature | 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_receivers_plan_receiver_id_signature_post_request_signature import RestV10ProjectsProjectIdActionPlansPlanReceiversPlanReceiverIdSignaturePostRequestSignature

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdActionPlansPlanReceiversPlanReceiverIdSignaturePostRequestSignature from a JSON string
rest_v10_projects_project_id_action_plans_plan_receivers_plan_receiver_id_signature_post_request_signature_instance = RestV10ProjectsProjectIdActionPlansPlanReceiversPlanReceiverIdSignaturePostRequestSignature.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdActionPlansPlanReceiversPlanReceiverIdSignaturePostRequestSignature.to_json())

# convert the object into a dict
rest_v10_projects_project_id_action_plans_plan_receivers_plan_receiver_id_signature_post_request_signature_dict = rest_v10_projects_project_id_action_plans_plan_receivers_plan_receiver_id_signature_post_request_signature_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdActionPlansPlanReceiversPlanReceiverIdSignaturePostRequestSignature from a dict
rest_v10_projects_project_id_action_plans_plan_receivers_plan_receiver_id_signature_post_request_signature_from_dict = RestV10ProjectsProjectIdActionPlansPlanReceiversPlanReceiverIdSignaturePostRequestSignature.from_dict(rest_v10_projects_project_id_action_plans_plan_receivers_plan_receiver_id_signature_post_request_signature_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


