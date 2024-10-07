# OriginPayload

Payload Keys change depending on origin.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checklist_item_id** | **int** | Checklist Item ID | [optional] 
**checklist_list_id** | **int** | Checklist List ID | [optional] 
**coordination_issue_id** | **int** | Coordination Issue ID the Observation Item belongs to | [optional] 
**coordination_issue_number** | **int** | Coordination Issue Number the Observation Item belongs to | [optional] 
**incident_action_id** | **int** | Incident action Id the Observation Item belongs to | [optional] 
**incident_id** | **int** | Incident Id the Observation Item belongs to | [optional] 
**bim_model_id** | **int** | Bim model Id the Observation Item belongs to | [optional] 
**bim_model_name** | **str** | Bim model name the Observation Item belongs to | [optional] 

## Example

```python
from procore_sdk.models.origin_payload import OriginPayload

# TODO update the JSON string below
json = "{}"
# create an instance of OriginPayload from a JSON string
origin_payload_instance = OriginPayload.from_json(json)
# print the JSON string representation of the object
print(OriginPayload.to_json())

# convert the object into a dict
origin_payload_dict = origin_payload_instance.to_dict()
# create an instance of OriginPayload from a dict
origin_payload_from_dict = OriginPayload.from_dict(origin_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


