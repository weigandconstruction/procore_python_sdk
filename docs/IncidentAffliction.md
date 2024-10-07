# IncidentAffliction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Affliction ID | [optional] 
**affliction_type** | [**AfflictionType**](AfflictionType.md) |  | [optional] 
**affected_body_part** | **str** | The body part affected by the affliction | [optional] 

## Example

```python
from procore_sdk.models.incident_affliction import IncidentAffliction

# TODO update the JSON string below
json = "{}"
# create an instance of IncidentAffliction from a JSON string
incident_affliction_instance = IncidentAffliction.from_json(json)
# print the JSON string representation of the object
print(IncidentAffliction.to_json())

# convert the object into a dict
incident_affliction_dict = incident_affliction_instance.to_dict()
# create an instance of IncidentAffliction from a dict
incident_affliction_from_dict = IncidentAffliction.from_dict(incident_affliction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


