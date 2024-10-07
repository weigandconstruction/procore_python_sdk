# IncidentAffliction1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Affliction ID | [optional] 
**affliction_type** | [**AfflictionType1**](AfflictionType1.md) |  | [optional] 
**affected_body_part** | **str** | The body part affected by the affliction | [optional] 

## Example

```python
from procore_sdk.models.incident_affliction1 import IncidentAffliction1

# TODO update the JSON string below
json = "{}"
# create an instance of IncidentAffliction1 from a JSON string
incident_affliction1_instance = IncidentAffliction1.from_json(json)
# print the JSON string representation of the object
print(IncidentAffliction1.to_json())

# convert the object into a dict
incident_affliction1_dict = incident_affliction1_instance.to_dict()
# create an instance of IncidentAffliction1 from a dict
incident_affliction1_from_dict = IncidentAffliction1.from_dict(incident_affliction1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


